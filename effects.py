from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QGraphicsOpacityEffect


class PulsingEffect:
    def __init__(self, widget):
        self.widget = widget

        self.effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1600)  # mais lento = mais suave

        # Fade suave
        self.animation.setKeyValueAt(0.0, 1.0)
        self.animation.setKeyValueAt(0.5, 0.35)
        self.animation.setKeyValueAt(1.0, 1.0)

        # Curva mais natural
        self.animation.setEasingCurve(QEasingCurve.InOutSine)

        self.animation.setLoopCount(-1)

    def start(self, text=None):
        if text:
            self.widget.setText(text)

        self.animation.start()

    def stop(self, finaltext=None):
        self.animation.stop()

        self.effect.setOpacity(1.0)

        if finaltext:
            self.widget.setText(finaltext)
