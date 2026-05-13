# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u"assets/icons/aboutBlack.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.leftSpacer)

        self.logoLabel = QLabel(Dialog)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(47, 47))
        self.logoLabel.setMaximumSize(QSize(47, 47))
        self.logoLabel.setPixmap(QPixmap(u":/assets/icons/voices.png"))
        self.logoLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logoLabel, 0, Qt.AlignmentFlag.AlignVCenter)

        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(0, 47))
        self.titleLabel.setMaximumSize(QSize(16777215, 47))
        font = QFont()
        font.setFamilies([u"Roboto Thin"])
        font.setPointSize(42)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setScaledContents(True)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.titleLabel, 0, Qt.AlignmentFlag.AlignVCenter)

        self.rightSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.rightSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.subtitleLabel = QLabel(Dialog)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        self.subtitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.subtitleLabel)

        self.versionLabel = QLabel(Dialog)
        self.versionLabel.setObjectName(u"versionLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionLabel.sizePolicy().hasHeightForWidth())
        self.versionLabel.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.versionLabel.setFont(font1)
        self.versionLabel.setStyleSheet(u"")
        self.versionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.versionLabel)

        self.pyside6Version = QLabel(Dialog)
        self.pyside6Version.setObjectName(u"pyside6Version")
        self.pyside6Version.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.pyside6Version)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(Dialog)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout_2.addWidget(self.okButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Sobre", None))
        self.logoLabel.setText("")
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"VOICES", None))
        self.subtitleLabel.setText(QCoreApplication.translate("Dialog", u"Uma interface gr\u00e1fica para Kokoro ONNX\n"
"", None))
        self.versionLabel.setText(QCoreApplication.translate("Dialog", u"Vers\u00e3o 0.1.0, 64bits", None))
        self.pyside6Version.setText(QCoreApplication.translate("Dialog", u"PySide6 version: 6.11.0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<p align=\"center\"><b>Voices</b> \u00e9 um projeto de c\u00f3digo aberto (Open Source) sob a <br> <span style='color: #2ecc71;'>Licen\u00e7a MIT</span>.</p>\n"
"<p align=\"center\"><a href=\"https://github.com/LordClen/Voices\">Ver c\u00f3digo fonte no GitHub</a></p>\n"
"<p align=\"center\"><small>Este software utiliza o modelo Kokoro-82M para s\u00edntese de voz.<br>\n"
"    Agradecimentos ao projeto original kokoro-onnx.</small></p>", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

