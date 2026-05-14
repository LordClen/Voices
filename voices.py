# This Python file uses the following encoding: utf-8
import sys
import os
import requests
import soundfile as sf
from kokoro_onnx import Kokoro
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QWidget, QVBoxLayout,
                             QHBoxLayout, QTextEdit, QComboBox, QPushButton,
                             QLabel, QFileDialog, QDoubleSpinBox, QMessageBox)
from PySide6.QtCore import QThread, Signal, Qt, QTimer

# Important:
# You need to run the following command to generate the form.py file
#     pyside6-uic form.ui -o form.py, or
#     pyside2-uic form.ui -o form.py
from form import Ui_MainWindow
from about import Ui_Dialog
from effects import PulsingEffect

VOZES_MAPA = {
    ("American English", "Voz feminina"): ["af_heart", "af_alloy", "af_aoede", "af_bella", "af_jessica", "af_kore", "af_nicole", "af_nova", "af_river", "af_sarah", "af_sky"],
    ("American English", "Voz masculina"): ["am_adam", "am_echo", "am_eric", "am_fenrir", "am_liam", "am_michael", "am_onyx", "am_puck", "am_santa"],
    ("British English", "Voz feminina"): ["bf_alice", "bf_emma", "bf_isabella", "bf_lily"],
    ("British English", "Voz masculina"): ["bm_daniel", "bm_fable", "bm_george", "bm_lewis"],
    ("Japanese", "Voz feminina"): ["jf_alpha", "jf_gongitsune", "jf_nezumi", "jf_tebukuro"],
    ("Japanese", "Voz masculina"): ["jm_kumo"],
    ("Mandarin Chinese", "Voz feminina"): ["zf_xiaobei", "zf_xiaoni", "zf_xiaoxiao", "zf_xiaoyi"],
    ("Mandarin Chinese", "Voz masculina"): ["zm_yunjian", "zm_yunxi", "zm_yunxia", "zm_yunyang"],
    ("Spanish", "Voz feminina"): ["ef_dora"],
    ("Spanish", "Voz masculina"): ["em_alex", "em_santa"],
    ("French", "Voz feminina"): ["ff_siwis"],
    ("French", "Voz masculina"): ["Não disponível"],
    ("Hindi", "Voz feminina"): ["hf_alpha", "hf_beta"],
    ("Hindi", "Voz masculina"): ["hm_omega", "hm_psi"],
    ("Italian", "Voz feminina"): ["if_sara"],
    ("Italian", "Voz masculina"): ["im_nicola"],
    ("Brazilian Portuguese", "Voz feminina"): ["pf_dora"],
    ("Brazilian Portuguese", "Voz masculina"): ["pm_alex", "pm_santa"],
}

class DownloadWorker(QThread):
    progresso = Signal(str)
    finalizado = Signal(bool)

    def __init__(self, urls, base_path):
        super().__init__()
        self.urls = urls
        self.base_path = base_path

    def run(self):
        try:
            for nome, url in self.urls.items():
                self.progresso.emit(f"Baixando {nome}...")
                caminho_arquivo = os.path.join(self.base_path, nome)
                
                response = requests.get(url, stream=True)
                response.raise_for_status()

                with open(caminho_arquivo, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
            self.finalizado.emit(True)
        except Exception as e:
            print(f"Erro: {e}")
            self.finalizado.emit(False)

class TTSWorker(QThread):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, text, voice, speed, model_path, voices_path):
        super().__init__()
        self.text = text
        self.voice = voice
        self.speed = speed
        self.model_path = model_path
        self.voices_path = voices_path

    def run(self):
        try:
            kokoro = Kokoro(self.model_path, self.voices_path)

            lang_map = {
                'a': 'en-us', # American English
                'b': 'en-gb', # British English
                'j': 'ja',    # Japanese
                'z': 'zh',    # Mandarin
                'e': 'es',    # Spanish
                'f': 'fr',    # French
                'h': 'hi',    # Hindi
                'i': 'it',    # Italian
                'p': 'pt-br'  # Brazilian Portuguese
            }

            voice_prefix = self.voice[0]
            target_lang = lang_map.get(voice_prefix, 'en-us')
            
            samples, sample_rate = kokoro.create(
                self.text, 
                voice=self.voice, 
                speed=self.speed,
                lang=target_lang
            )
            
            filename = "output.wav"
            sf.write(filename, samples, sample_rate)
            self.finished.emit(f"Áudio gerado: {filename}")
        except Exception as e:
            self.error.emit(str(e))

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(400, 300)
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.ui.okButton.clicked.connect(self.accept)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.downloadonnx.setVisible(False)
        self.ui.downloadonnx.clicked.connect(self.baixar_modelos)

        self.status_animator = PulsingEffect(self.ui.status_label)

        self.ui.exitButton.clicked.connect(self.close)
        self.ui.aboutButton.clicked.connect(self.showAbout)

        self.ui.cmbBoxIdiomas.addItems([
            "American English", "British English", "Japanese", "Mandarin Chinese",
            "Spanish", "French", "Hindi", "Italian", "Brazilian Portuguese"
        ])
        self.ui.cmbBoxGenero.addItems(["Voz feminina", "Voz masculina"])

        self.ui.cmbBoxIdiomas.currentTextChanged.connect(self.atualizar_vozes)
        self.ui.cmbBoxGenero.currentTextChanged.connect(self.atualizar_vozes)

        self.atualizar_vozes()

        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        self.model_path = os.path.join(base_path, "kokoro-v1.0.onnx")
        self.voices_path = os.path.join(base_path, "voices-v1.0.bin")

        self.checar_motor()

        self.ui.btn_load.clicked.connect(self.load_file)
        self.ui.btn_generate.clicked.connect(self.generate_audio)

    def atualizar_vozes(self):
        idioma = self.ui.cmbBoxIdiomas.currentText()
        genero = self.ui.cmbBoxGenero.currentText()

        self.ui.cmbBoxVoz.clear()

        vozes = VOZES_MAPA.get((idioma, genero), ["Não disponível"])
        self.ui.cmbBoxVoz.addItems(vozes)

    def checar_motor(self):
        if not os.path.exists(self.model_path) or not os.path.exists(self.voices_path):
            self.ui.status_label.setText("AVISO: Motor neural Kokoro ONNX não encontrado!")
            self.ui.downloadonnx.show()
        else:
            self.ui.status_label.setText("Kokoro ONNX carregado e pronto para uso!")
            self.ui.downloadonnx.hide()

    def baixar_modelos(self):
        self.ui.downloadonnx.setEnabled(False)

        if hasattr(self, 'status_animator'):
            self.status_animator.start()
            urls = {
                "kokoro-v1.0.onnx": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx", 
                "voices-v1.0.bin": "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin"
                }
            
        self.download_worker = DownloadWorker(urls, os.path.dirname(self.model_path))
        self.download_worker.progresso.connect(self.ui.status_label.setText)
        self.download_worker.finalizado.connect(self.finalizar_requisicao_download)
        self.download_worker.start()

    def finalizar_requisicao_download(self, sucesso):
        if hasattr(self, 'status_animator'):
            self.status_animator.stop()
        
        if sucesso:
            self.ui.status_label.setText("Kokoro ONNX carregado e pronto para uso!")
            self.ui.downloadonnx.hide()
        else:
            self.ui.status_label.setText("Falha no download. Tente novamente.")
            self.ui.downloadonnx.setEnabled(True)
            self.ui.downloadonnx.show()

    def showAbout(self):
        self.aboutWindow = AboutDialog(self)
        self.aboutWindow.exec()

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "", "Text Files (*.txt)")
        if path:
            with open(path, 'r', encoding='utf-8') as f:
                self.ui.text_edit.setText(f.read())

    def generate_audio(self):
        voice = self.ui.cmbBoxVoz.currentText()
        if voice == "Não disponível":
            self.ui.status_label.setText("Erro: Esta combinação de idioma/gênero não possui voz.")
            return
        text = self.ui.text_edit.toPlainText().strip()
        if not text: return

        self.ui.btn_generate.setEnabled(False)
        self.status_animator.start("Gerando áudio...")
        
        self.worker = TTSWorker(
            text, 
            self.ui.cmbBoxVoz.currentText(),
            self.ui.spin_speed.value(),
            self.model_path,
            self.voices_path
        )
        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.on_error)
        self.worker.start()

    def on_finished(self, msg):
        self.status_animator.stop(msg)
        self.ui.btn_generate.setEnabled(True)

    def on_error(self, err):
        self.status_animator.stop(f"Erro: {err}")
        self.ui.status_label.setStyleSheet("color: red;")
        self.ui.btn_generate.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
