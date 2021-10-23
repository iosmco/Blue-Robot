# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trackingKhRuHy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1000, 540))
        Form.setMaximumSize(QSize(1000, 540))
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: #101010;\n"
"}\n"
"QStackedWidget {\n"
"	background-color: #101010;\n"
"	background: #101010;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"QLabel {\n"
"	background-color: transparent;\n"
"	color: gray;\n"
"}\n"
"QToolButton {\n"
"	color: white;\n"
"}\n"
"QPushButton {\n"
"	border-radius: 10px;	\n"
"	background-color: #0055ff;\n"
"	color: white;\n"
"    text-align: center;\n"
"	outline: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #003db9;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"QPushButton:disabled {	\n"
"	border-radius: 10px;\n"
"    color: gray;\n"
"	background-color: black;\n"
"}\n"
"QLineEdit {\n"
"	background-color: black;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"    color: white;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #0055ff;\n"
"}\n"
"QProgressBar {\n"
"  background-color: black;\n"
"  color: white;\n"
"  border-radius: 10px;\n"
"}\n"
"QProgressBar:chunk {\n"
"  backgro"
                        "und-color: #0055ff;\n"
"  border-radius: 10px;\n"
"}\n"
"QGroupBox {\n"
"	border-radius: 10px;\n"
"	background-color: black;\n"
"	color: none;\n"
"	border: 2px solid white;\n"
"}\n"
"QTabWidget::pane {\n"
"	border: none;\n"
"	background: transparent;\n"
"	background-color: none;\n"
"}\n"
"QTabWidget::tab-bar:top {\n"
"	top: 1px;\n"
"}\n"
"QTabWidget::tab-bar:bottom {\n"
"	bottom: 1px;\n"
"}\n"
"QTabWidget::tab-bar:left {\n"
"	right: 1px;\n"
"}\n"
"QTabWidget::tab-bar:right {\n"
"	left: 1px;\n"
"}\n"
"QTabBar::tab {\n"
"	font: 57 8pt \"Roboto Medium\";\n"
"	background: transparent;\n"
"	border: none;\n"
"	padding: 8px;\n"
"}\n"
"QTabBar::tab:selected{\n"
"	font: 57 10pt \"Roboto Medium\";\n"
"	border: none;\n"
"	color: white;\n"
"	background: transparent;\n"
"	background-color: transparent;\n"
"}\n"
"QTabBar::tab:!selected{\n"
"	border: none;\n"
"	color: gray;\n"
"	background: transparent;\n"
"	background-color: transparent;\n"
"}\n"
"QComboBox{\n"
"	background-color: black;\n"
"	border: none;\n"
"	border-radiu"
                        "s: 10px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color: gray;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 2px;\n"
"	border-left-color: black;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image:url(:/icons/icons/chevron-down.svg);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color:white;	\n"
"	background-color:black;\n"
"	padding: 10px;\n"
"	selection-background-color: #202020;\n"
"	outline: none;\n"
"}\n"
"QCheckBox{\n"
"	color: white;\n"
"}\n"
"QCheckBox::indicator {\n"
"    border: 3px solid #202020;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: black;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid #303030;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #101010;\n"
"	border: 3p"
                        "x solid #101010;\n"
"	background-image: url(:/icons/icons/cil-check-alt.png);\n"
"}\n"
"QRadioButton{\n"
"	color: white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #202020;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: black;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid #303030;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #101010;\n"
"	border: 3px solid #202020;	\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #202020;\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #0055ff;\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #202020;\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #202020;\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: #202020;\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: #0055ff;\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"	background: #202020;\n"
"    height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
""
                        " QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background:#202020;\n"
"    height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(18, 27, 640, 480))
        self.label.setMinimumSize(QSize(640, 480))
        self.label.setMaximumSize(QSize(640, 480))
        font = QFont()
        font.setFamily(u"Roboto Medium")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	color: gray;\n"
"	border-radius: 0px;\n"
"	border: 2px solid #0055ff;\n"
"}")
        self.label.setFrameShape(QFrame.Panel)
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(0)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(669, 26, 326, 480))
        self.label_12.setMaximumSize(QSize(640, 480))
        self.label_12.setFont(font)
        self.label_12.setMouseTracking(True)
        self.label_12.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	color: gray;\n"
"	border-radius: 0px;\n"
"	border: 2px solid #0055ff;\n"
"}")
        self.label_12.setFrameShape(QFrame.Panel)
        self.label_12.setFrameShadow(QFrame.Sunken)
        self.label_12.setLineWidth(1)
        self.label_12.setMidLineWidth(0)
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setIndent(0)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(680, 50, 306, 424))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ConnectButton = QPushButton(self.layoutWidget)
        self.ConnectButton.setObjectName(u"ConnectButton")
        self.ConnectButton.setMinimumSize(QSize(80, 32))
        self.ConnectButton.setMaximumSize(QSize(80, 32))
        font1 = QFont()
        font1.setFamily(u"Roboto Medium")
        font1.setPointSize(9)
        self.ConnectButton.setFont(font1)

        self.gridLayout.addWidget(self.ConnectButton, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(100, 32))
        self.radioButton.setMaximumSize(QSize(100, 32))
        font2 = QFont()
        font2.setPointSize(8)
        self.radioButton.setFont(font2)

        self.gridLayout.addWidget(self.radioButton, 0, 1, 1, 1)

        self.LED_checkbox = QCheckBox(self.layoutWidget)
        self.LED_checkbox.setObjectName(u"LED_checkbox")
        self.LED_checkbox.setMinimumSize(QSize(100, 32))
        self.LED_checkbox.setMaximumSize(QSize(100, 32))
        font3 = QFont()
        font3.setFamily(u"Roboto Medium")
        font3.setPointSize(8)
        self.LED_checkbox.setFont(font3)
        self.LED_checkbox.setChecked(True)

        self.gridLayout.addWidget(self.LED_checkbox, 0, 2, 1, 1)

        self.UpdateButton = QPushButton(self.layoutWidget)
        self.UpdateButton.setObjectName(u"UpdateButton")
        self.UpdateButton.setMinimumSize(QSize(80, 32))
        self.UpdateButton.setMaximumSize(QSize(80, 32))
        self.UpdateButton.setFont(font1)

        self.gridLayout.addWidget(self.UpdateButton, 1, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(100, 32))
        self.radioButton_2.setMaximumSize(QSize(100, 32))
        self.radioButton_2.setFont(font2)

        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.LED_checkbox_3 = QCheckBox(self.layoutWidget)
        self.LED_checkbox_3.setObjectName(u"LED_checkbox_3")
        self.LED_checkbox_3.setMinimumSize(QSize(100, 32))
        self.LED_checkbox_3.setMaximumSize(QSize(100, 32))
        self.LED_checkbox_3.setFont(font3)
        self.LED_checkbox_3.setChecked(True)

        self.gridLayout.addWidget(self.LED_checkbox_3, 1, 2, 1, 1)

        self.PauseButton = QPushButton(self.layoutWidget)
        self.PauseButton.setObjectName(u"PauseButton")
        self.PauseButton.setMinimumSize(QSize(80, 32))
        self.PauseButton.setMaximumSize(QSize(80, 32))
        self.PauseButton.setFont(font1)

        self.gridLayout.addWidget(self.PauseButton, 2, 0, 1, 1)

        self.Manual_checkbox = QCheckBox(self.layoutWidget)
        self.Manual_checkbox.setObjectName(u"Manual_checkbox")
        self.Manual_checkbox.setMinimumSize(QSize(100, 32))
        self.Manual_checkbox.setMaximumSize(QSize(100, 32))
        self.Manual_checkbox.setFont(font3)

        self.gridLayout.addWidget(self.Manual_checkbox, 2, 1, 1, 1)

        self.InvertTilt_checkbox = QCheckBox(self.layoutWidget)
        self.InvertTilt_checkbox.setObjectName(u"InvertTilt_checkbox")
        self.InvertTilt_checkbox.setMinimumSize(QSize(100, 32))
        self.InvertTilt_checkbox.setMaximumSize(QSize(100, 32))
        self.InvertTilt_checkbox.setFont(font3)

        self.gridLayout.addWidget(self.InvertTilt_checkbox, 2, 2, 1, 1)

        self.QuitButton = QPushButton(self.layoutWidget)
        self.QuitButton.setObjectName(u"QuitButton")
        self.QuitButton.setMinimumSize(QSize(80, 32))
        self.QuitButton.setMaximumSize(QSize(80, 32))
        self.QuitButton.setFont(font1)

        self.gridLayout.addWidget(self.QuitButton, 3, 0, 1, 1)

        self.LED_checkbox_2 = QCheckBox(self.layoutWidget)
        self.LED_checkbox_2.setObjectName(u"LED_checkbox_2")
        self.LED_checkbox_2.setMinimumSize(QSize(100, 32))
        self.LED_checkbox_2.setMaximumSize(QSize(100, 32))
        self.LED_checkbox_2.setFont(font3)
        self.LED_checkbox_2.setChecked(True)

        self.gridLayout.addWidget(self.LED_checkbox_2, 3, 1, 1, 1)

        self.InvertPan_checkbox = QCheckBox(self.layoutWidget)
        self.InvertPan_checkbox.setObjectName(u"InvertPan_checkbox")
        self.InvertPan_checkbox.setMinimumSize(QSize(100, 32))
        self.InvertPan_checkbox.setMaximumSize(QSize(100, 32))
        self.InvertPan_checkbox.setFont(font3)

        self.gridLayout.addWidget(self.InvertPan_checkbox, 3, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.COMConnectLabel = QLabel(self.layoutWidget)
        self.COMConnectLabel.setObjectName(u"COMConnectLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.COMConnectLabel.sizePolicy().hasHeightForWidth())
        self.COMConnectLabel.setSizePolicy(sizePolicy1)
        self.COMConnectLabel.setMinimumSize(QSize(300, 32))
        self.COMConnectLabel.setMaximumSize(QSize(300, 32))
        self.COMConnectLabel.setFont(font1)
        self.COMConnectLabel.setStyleSheet(u"QLabel {\n"
"	background-color: transparent;\n"
"	color: gray;\n"
"	border-radius: 10px;\n"
"	border: 2px solid #0055ff;\n"
"}")
        self.COMConnectLabel.setAlignment(Qt.AlignCenter)
        self.COMConnectLabel.setWordWrap(False)
        self.COMConnectLabel.setMargin(0)
        self.COMConnectLabel.setIndent(-1)

        self.gridLayout_2.addWidget(self.COMConnectLabel, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(75, 32))
        self.label_4.setMaximumSize(QSize(75, 32))
        self.label_4.setFont(font1)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.COMlineEdit = QLineEdit(self.layoutWidget)
        self.COMlineEdit.setObjectName(u"COMlineEdit")
        self.COMlineEdit.setMinimumSize(QSize(60, 32))
        self.COMlineEdit.setMaximumSize(QSize(60, 32))
        self.COMlineEdit.setFont(font1)
        self.COMlineEdit.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.COMlineEdit)


        self.verticalLayout_2.addLayout(self.formLayout_6)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(75, 32))
        self.label_5.setMaximumSize(QSize(75, 32))
        self.label_5.setFont(font1)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.MinTiltlineEdit = QLineEdit(self.layoutWidget)
        self.MinTiltlineEdit.setObjectName(u"MinTiltlineEdit")
        self.MinTiltlineEdit.setMinimumSize(QSize(60, 32))
        self.MinTiltlineEdit.setMaximumSize(QSize(60, 32))
        self.MinTiltlineEdit.setFont(font1)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.MinTiltlineEdit)


        self.verticalLayout_2.addLayout(self.formLayout_7)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(75, 32))
        self.label_7.setMaximumSize(QSize(75, 32))
        self.label_7.setFont(font1)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.MinPanlineEdit = QLineEdit(self.layoutWidget)
        self.MinPanlineEdit.setObjectName(u"MinPanlineEdit")
        self.MinPanlineEdit.setMinimumSize(QSize(60, 32))
        self.MinPanlineEdit.setMaximumSize(QSize(60, 32))
        self.MinPanlineEdit.setFont(font1)
        self.MinPanlineEdit.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.MinPanlineEdit)


        self.verticalLayout_2.addLayout(self.formLayout_8)

        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(75, 32))
        self.label_6.setMaximumSize(QSize(75, 32))
        self.label_6.setFont(font1)

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.MaxTiltlineEdit = QLineEdit(self.layoutWidget)
        self.MaxTiltlineEdit.setObjectName(u"MaxTiltlineEdit")
        self.MaxTiltlineEdit.setMinimumSize(QSize(60, 32))
        self.MaxTiltlineEdit.setMaximumSize(QSize(60, 32))
        self.MaxTiltlineEdit.setFont(font1)
        self.MaxTiltlineEdit.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.MaxTiltlineEdit)


        self.verticalLayout_2.addLayout(self.formLayout_9)

        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(75, 32))
        self.label_8.setMaximumSize(QSize(75, 32))
        self.label_8.setFont(font1)

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.MaxPanlineEdit = QLineEdit(self.layoutWidget)
        self.MaxPanlineEdit.setObjectName(u"MaxPanlineEdit")
        self.MaxPanlineEdit.setMinimumSize(QSize(60, 32))
        self.MaxPanlineEdit.setMaximumSize(QSize(60, 32))
        self.MaxPanlineEdit.setFont(font1)
        self.MaxPanlineEdit.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.MaxPanlineEdit)


        self.verticalLayout_2.addLayout(self.formLayout_10)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(75, 32))
        self.label_11.setMaximumSize(QSize(75, 32))
        self.label_11.setFont(font1)
        self.label_11.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.CameraIDEdit = QLineEdit(self.layoutWidget)
        self.CameraIDEdit.setObjectName(u"CameraIDEdit")
        self.CameraIDEdit.setMinimumSize(QSize(60, 32))
        self.CameraIDEdit.setMaximumSize(QSize(60, 32))
        self.CameraIDEdit.setFont(font1)
        self.CameraIDEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.CameraIDEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(75, 32))
        self.label_9.setMaximumSize(QSize(75, 32))
        self.label_9.setFont(font1)
        self.label_9.setTextFormat(Qt.PlainText)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.TiltSensivityEdit = QLineEdit(self.layoutWidget)
        self.TiltSensivityEdit.setObjectName(u"TiltSensivityEdit")
        self.TiltSensivityEdit.setMinimumSize(QSize(60, 32))
        self.TiltSensivityEdit.setMaximumSize(QSize(60, 32))
        self.TiltSensivityEdit.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.TiltSensivityEdit)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(75, 32))
        self.label_10.setMaximumSize(QSize(75, 32))
        self.label_10.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.PanSensivityEdit = QLineEdit(self.layoutWidget)
        self.PanSensivityEdit.setObjectName(u"PanSensivityEdit")
        self.PanSensivityEdit.setMinimumSize(QSize(60, 32))
        self.PanSensivityEdit.setMaximumSize(QSize(60, 32))
        self.PanSensivityEdit.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.PanSensivityEdit)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(75, 32))
        self.label_3.setMaximumSize(QSize(75, 32))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.Tilt_LCD = QLCDNumber(self.layoutWidget)
        self.Tilt_LCD.setObjectName(u"Tilt_LCD")
        self.Tilt_LCD.setMinimumSize(QSize(60, 32))
        self.Tilt_LCD.setMaximumSize(QSize(60, 32))
        self.Tilt_LCD.setFont(font1)
        self.Tilt_LCD.setLayoutDirection(Qt.LeftToRight)
        self.Tilt_LCD.setStyleSheet(u"QLCDNumber{\n"
"	background-color: black;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"    color: white;\n"
"	text-align: left;\n"
"}")
        self.Tilt_LCD.setFrameShape(QFrame.StyledPanel)
        self.Tilt_LCD.setFrameShadow(QFrame.Sunken)
        self.Tilt_LCD.setLineWidth(1)
        self.Tilt_LCD.setSmallDecimalPoint(False)
        self.Tilt_LCD.setDigitCount(5)
        self.Tilt_LCD.setSegmentStyle(QLCDNumber.Flat)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.Tilt_LCD)


        self.verticalLayout.addLayout(self.formLayout_4)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(75, 32))
        self.label_2.setMaximumSize(QSize(75, 32))
        self.label_2.setFont(font1)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setLineWidth(1)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.Pan_LCD = QLCDNumber(self.layoutWidget)
        self.Pan_LCD.setObjectName(u"Pan_LCD")
        self.Pan_LCD.setMinimumSize(QSize(60, 32))
        self.Pan_LCD.setMaximumSize(QSize(60, 32))
        self.Pan_LCD.setFont(font1)
        self.Pan_LCD.setStyleSheet(u"QLCDNumber{\n"
"	background-color: black;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"    color: white;\n"
"}")
        self.Pan_LCD.setFrameShape(QFrame.StyledPanel)
        self.Pan_LCD.setFrameShadow(QFrame.Raised)
        self.Pan_LCD.setSmallDecimalPoint(False)
        self.Pan_LCD.setSegmentStyle(QLCDNumber.Flat)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.Pan_LCD)


        self.verticalLayout.addLayout(self.formLayout_5)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.label_12.raise_()
        self.label.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"No Signal !!", None))
        self.label_12.setText("")
        self.ConnectButton.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Face Mode", None))
        self.LED_checkbox.setText(QCoreApplication.translate("Form", u"LED's ON", None))
        self.UpdateButton.setText(QCoreApplication.translate("Form", u"Update", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Color Mode", None))
        self.LED_checkbox_3.setText(QCoreApplication.translate("Form", u"BUZ ON", None))
        self.PauseButton.setText(QCoreApplication.translate("Form", u"Pause", None))
        self.Manual_checkbox.setText(QCoreApplication.translate("Form", u"Manual control", None))
        self.InvertTilt_checkbox.setText(QCoreApplication.translate("Form", u"Invert tilt", None))
        self.QuitButton.setText(QCoreApplication.translate("Form", u"Quit", None))
        self.LED_checkbox_2.setText(QCoreApplication.translate("Form", u"LASER ON", None))
        self.InvertPan_checkbox.setText(QCoreApplication.translate("Form", u"Invert pan", None))
        self.COMConnectLabel.setText(QCoreApplication.translate("Form", u"Arduino Not Connected to Any Port !!", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"COM port", None))
        self.COMlineEdit.setText(QCoreApplication.translate("Form", u"COM3", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Min Tilt :", None))
        self.MinTiltlineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Min Pan :", None))
        self.MinPanlineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Max Tilt :", None))
        self.MaxTiltlineEdit.setText(QCoreApplication.translate("Form", u"90", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Max Pan :", None))
        self.MaxPanlineEdit.setText(QCoreApplication.translate("Form", u"180", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Camera ID :", None))
        self.CameraIDEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Tilt sensivity :", None))
        self.TiltSensivityEdit.setText(QCoreApplication.translate("Form", u"3", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Pan sensivity :", None))
        self.PanSensivityEdit.setText(QCoreApplication.translate("Form", u"5", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Tilt", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pan", None))
    # retranslateUi

