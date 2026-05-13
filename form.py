# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(756, 509)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QVBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u"assets/icons/voices.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Roboto Thin"])
        font.setPointSize(37)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.aboutButton = QPushButton(self.centralwidget)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setMaximumSize(QSize(40, 40))
        self.aboutButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.aboutButton.setStyleSheet(u"border: none;\n"
"")
        self.aboutButton.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        icon = QIcon()
        icon.addFile(u"assets/icons/about.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.aboutButton.setIcon(icon)
        self.aboutButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.aboutButton)


        self.horizontalLayout.addLayout(self.horizontalLayout_11)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cmbBoxIdiomas = QComboBox(self.centralwidget)
        self.cmbBoxIdiomas.setObjectName(u"cmbBoxIdiomas")

        self.horizontalLayout_4.addWidget(self.cmbBoxIdiomas)

        self.cmbBoxGenero = QComboBox(self.centralwidget)
        self.cmbBoxGenero.setObjectName(u"cmbBoxGenero")

        self.horizontalLayout_4.addWidget(self.cmbBoxGenero)

        self.cmbBoxVoz = QComboBox(self.centralwidget)
        self.cmbBoxVoz.setObjectName(u"cmbBoxVoz")

        self.horizontalLayout_4.addWidget(self.cmbBoxVoz)

        self.spin_speed = QDoubleSpinBox(self.centralwidget)
        self.spin_speed.setObjectName(u"spin_speed")
        self.spin_speed.setStyleSheet(u"selection-background-color: transparent;\n"
"selection-color: rgb(0, 0, 0);")
        self.spin_speed.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.spin_speed.setSingleStep(0.010000000000000)
        self.spin_speed.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.spin_speed)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)

        self.text_edit = QTextEdit(self.centralwidget)
        self.text_edit.setObjectName(u"text_edit")
        self.text_edit.setStyleSheet(u"border-radius: 6px;\n"
"border: 1px solid #c0c0c0;\n"
"padding: 4px;\n"
"background-color: white;")

        self.horizontalLayout.addWidget(self.text_edit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_load = QPushButton(self.centralwidget)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setStyleSheet(u"background-color: #2196F3;\n"
"color: white; font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.btn_load)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setStyleSheet(u"background-color: #4CAF50;\n"
"color: white; font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.btn_generate)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setStyleSheet(u"background-color: #F44336;\n"
"color: white; font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.exitButton)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.status_label)

        self.downloadonnx = QPushButton(self.centralwidget)
        self.downloadonnx.setObjectName(u"downloadonnx")
        self.downloadonnx.setEnabled(True)
        self.downloadonnx.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_7.addWidget(self.downloadonnx)

        self.versionlabel = QLabel(self.centralwidget)
        self.versionlabel.setObjectName(u"versionlabel")
        font1 = QFont()
        font1.setPointSize(9)
        self.versionlabel.setFont(font1)
        self.versionlabel.setStyleSheet(u"color: rgb(100, 100, 100);")
        self.versionlabel.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.versionlabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.versionlabel)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Voices :: Uma interface gr\u00e1fica para Kokoro ONNX", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"VOICES", None))
#if QT_CONFIG(tooltip)
        self.aboutButton.setToolTip(QCoreApplication.translate("MainWindow", u"Sobre", None))
#endif // QT_CONFIG(tooltip)
        self.aboutButton.setText("")
        self.cmbBoxIdiomas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escolha um idioma...", None))
        self.cmbBoxGenero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escolha um g\u00eanero...", None))
        self.cmbBoxVoz.setCurrentText("")
        self.cmbBoxVoz.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione uma voz...", None))
        self.spin_speed.setPrefix(QCoreApplication.translate("MainWindow", u"Velocidade da fala:    ", None))
        self.text_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escreva, cole  ou carregue um arquivo .txt aqui.", None))
        self.btn_load.setText(QCoreApplication.translate("MainWindow", u"Carregar arquivo", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"Gerar \u00e1udio", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Encerrar programa", None))
        self.status_label.setText("")
        self.downloadonnx.setText(QCoreApplication.translate("MainWindow", u"Fazer download!", None))
        self.versionlabel.setText(QCoreApplication.translate("MainWindow", u"Vers\u00e3o 0.1.0, 64bits", None))
    # retranslateUi

