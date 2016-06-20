# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Desarrollo\SkyTube\inicio.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(613, 477)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("/*\n"
" * The MIT License (MIT)\n"
" *\n"
" * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
" *\n"
" * Permission is hereby granted, free of charge, to any person obtaining a copy\n"
" * of this software and associated documentation files (the \"Software\"), to deal\n"
" * in the Software without restriction, including without limitation the rights\n"
" * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
" * copies of the Software, and to permit persons to whom the Software is\n"
" * furnished to do so, subject to the following conditions:\n"
"\n"
" * The above copyright notice and this permission notice shall be included in\n"
" * all copies or substantial portions of the Software.\n"
"\n"
" * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
" * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
" * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
" * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
" * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
" * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n"
" * THE SOFTWARE.\n"
" */\n"
"\n"
"QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#3d8ec9;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #3d8ec9;\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator\n"
"{\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator\n"
"{\n"
"    margin-left: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed\n"
"{\n"
"  border: none;\n"
"    image: url(:/qss_icons/rc/checkbox_checked_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:focus,\n"
"QGroupBox::indicator:indeterminate:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_indeterminate_focus.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:checked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"QRadioButton:disabled\n"
"{\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/qss_icons/rc/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed\n"
"{\n"
"  border: none;\n"
"  outline: none;\n"
"    image: url(:/qss_icons/rc/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed\n"
"{\n"
"        image: url(:/qss_icons/rc/radio_indeterminate.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  outline: none;\n"
"  image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:disabled\n"
"{\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #3d8ec9;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 5px 30px 5px 30px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"/* non-exclusive indicator = check box style indicator\n"
"   (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:non-exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked {\n"
"    image: url(:/qss_icons/rc/checkbox_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:non-exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);\n"
"}\n"
"\n"
"/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */\n"
"QMenu::indicator:exclusive:unchecked {\n"
"    image: url(:/qss_icons/rc/radio_unchecked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:unchecked:selected {\n"
"    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked {\n"
"    image: url(:/qss_icons/rc/radio_checked.png);\n"
"}\n"
"\n"
"QMenu::indicator:exclusive:checked:selected {\n"
"    image: url(:/qss_icons/rc/radio_checked_disabled.png);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    margin: 5px;\n"
"    image: url(:/qss_icons/rc/right_arrow.png)\n"
"}\n"
"\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 3px 15px 3px 15px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"    background-color: #2A2929;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #2A2929;\n"
"    width: 15px;\n"
"    margin: 15px 3px 15px 3px;\n"
"    border: 1px transparent #2A2929;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: #605F5F;\n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/qss_icons/rc/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"]\n"
"{\n"
"    border-radius: 2px;\n"
"    border: 1px transparent #444;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px transparent #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/qss_icons/rc/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/qss_icons/rc/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/qss_icons/rc/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    border-width: 1px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border-radius: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 1px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #454545;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #3d8ec9;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #3d8ec9;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #4A4949;\n"
"    border-color: #6A6969;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 2px;\n"
"    border: 1px solid #444;\n"
"    selection-background-color: #3d8ec9;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #484846;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    border-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/qss_icons/rc/close.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/close-hover.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    image: url(:/qss_icons/rc/close-pressed.png);\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* TOP TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-bottom: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"/* BOTTOM TABS */\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-top: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-bottom-left-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-top: 1px transparent #4A4949;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    background-color: #78879b;\n"
"}\n"
"\n"
"/* LEFT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-left: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-right-radius: 2px;\n"
"    border-bottom-right-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"\n"
"/* RIGHT TABS */\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #4A4949;\n"
"    border-right: 1px transparent black;\n"
"    background-color: #302F2F;\n"
"    padding: 5px;\n"
"    border-top-left-radius: 2px;\n"
"    border-bottom-left-radius: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #201F1F;\n"
"    border: 1px transparent #4A4949;\n"
"    border-right: 1px transparent #4A4949;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"    background-color: #48576b;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/qss_icons/rc/close.png);\n"
"    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    border: 1px solid #444;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover\n"
"{\n"
"    background: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/qss_icons/rc/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/qss_icons/rc/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/qss_icons/rc/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/qss_icons/rc/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: 1px transparent #4A4949;\n"
"    border-radius: 2px;\n"
"    margin: 3px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
" border: 1px transparent #4A4949;\n"
" border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
" border: 1px transparent #4A4949;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    background-color: transparent;\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed,\n"
"        QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"    top: -7px; left: -2px; /* shift it a bit */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 8px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: 1px solid #444;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #3d8ec9;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    border-radius: 2px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    border: 1px transparent black;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid #4A4949;\n"
"    border-bottom: 1px transparent #302F2F;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"    font: italic;\n"
"    background-color: #302F2F;\n"
"    border-color: #3d8ec9;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
" }\n"
"\n"
"\n"
"QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
"    background-color: #444;\n"
"}\n"
"\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #787876;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 1px;\n"
"}\n"
"")
        self.btn_valida = QtWidgets.QPushButton(Form)
        self.btn_valida.setGeometry(QtCore.QRect(359, 10, 21, 21))
        self.btn_valida.setAutoFillBackground(False)
        self.btn_valida.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagenes/buscar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_valida.setIcon(icon1)
        self.btn_valida.setFlat(True)
        self.btn_valida.setObjectName("btn_valida")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(95, 10, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.ck_captura = QtWidgets.QCheckBox(Form)
        self.ck_captura.setGeometry(QtCore.QRect(530, 10, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ck_captura.setFont(font)
        self.ck_captura.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imagenes/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ck_captura.setIcon(icon2)
        self.ck_captura.setObjectName("ck_captura")
        self.ck_lst_auto = QtWidgets.QCheckBox(Form)
        self.ck_lst_auto.setGeometry(QtCore.QRect(530, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ck_lst_auto.setFont(font)
        self.ck_lst_auto.setAutoFillBackground(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imagenes/lista.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ck_lst_auto.setIcon(icon3)
        self.ck_lst_auto.setObjectName("ck_lst_auto")
        self.ck_vlc = QtWidgets.QCheckBox(Form)
        self.ck_vlc.setGeometry(QtCore.QRect(430, 10, 58, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ck_vlc.setFont(font)
        self.ck_vlc.setAutoFillBackground(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imagenes/vlc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ck_vlc.setIcon(icon4)
        self.ck_vlc.setIconSize(QtCore.QSize(16, 16))
        self.ck_vlc.setObjectName("ck_vlc")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 591, 371))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.web = QtWebKitWidgets.QWebView(self.tab)
        self.web.setGeometry(QtCore.QRect(10, 4, 571, 291))
        self.web.setAutoFillBackground(False)
        self.web.setObjectName("web")
        self.lbl_descarga = QtWidgets.QLineEdit(self.tab)
        self.lbl_descarga.setGeometry(QtCore.QRect(120, 360, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lbl_descarga.setFont(font)
        self.lbl_descarga.setAutoFillBackground(False)
        self.lbl_descarga.setText("")
        self.lbl_descarga.setObjectName("lbl_descarga")
        self.lbl_desc = QtWidgets.QLabel(self.tab)
        self.lbl_desc.setGeometry(QtCore.QRect(10, 310, 571, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_desc.setFont(font)
        self.lbl_desc.setAutoFillBackground(False)
        self.lbl_desc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_desc.setObjectName("lbl_desc")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imagenes/loading.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lst_encola = QtWidgets.QListWidget(self.tab_2)
        self.lst_encola.setGeometry(QtCore.QRect(0, 2, 581, 291))
        self.lst_encola.setAutoFillBackground(True)
        self.lst_encola.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lst_encola.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.lst_encola.setAlternatingRowColors(True)
        self.lst_encola.setObjectName("lst_encola")
        self.btn_add_lista = QtWidgets.QPushButton(self.tab_2)
        self.btn_add_lista.setGeometry(QtCore.QRect(450, 300, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_add_lista.setFont(font)
        self.btn_add_lista.setAutoFillBackground(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("imagenes/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_lista.setIcon(icon6)
        self.btn_add_lista.setFlat(True)
        self.btn_add_lista.setObjectName("btn_add_lista")
        self.tabWidget.addTab(self.tab_2, icon3, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.treeView = QtWidgets.QTreeView(self.tab_3)
        self.treeView.setGeometry(QtCore.QRect(10, 2, 571, 291))
        self.treeView.setAutoFillBackground(True)
        self.treeView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setObjectName("treeView")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 420, 271, 21))
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lbl_autor_3 = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_autor_3.setGeometry(QtCore.QRect(10, 90, 241, 20))
        self.lbl_autor_3.setAutoFillBackground(False)
        self.lbl_autor_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_autor_3.setObjectName("lbl_autor_3")
        self.btn_play = QtWidgets.QPushButton(self.tab_3)
        self.btn_play.setGeometry(QtCore.QRect(10, 300, 41, 31))
        self.btn_play.setAutoFillBackground(False)
        self.btn_play.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("imagenes/reproduce.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon7)
        self.btn_play.setIconSize(QtCore.QSize(20, 20))
        self.btn_play.setFlat(True)
        self.btn_play.setObjectName("btn_play")
        self.lbl_autor_2 = QtWidgets.QLabel(self.tab_3)
        self.lbl_autor_2.setGeometry(QtCore.QRect(59, 305, 231, 20))
        self.lbl_autor_2.setAutoFillBackground(False)
        self.lbl_autor_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_autor_2.setObjectName("lbl_autor_2")
        self.btn_folder_2 = QtWidgets.QPushButton(self.tab_3)
        self.btn_folder_2.setGeometry(QtCore.QRect(556, 303, 21, 21))
        self.btn_folder_2.setAutoFillBackground(False)
        self.btn_folder_2.setFlat(True)
        self.btn_folder_2.setObjectName("btn_folder_2")
        self.lbl_perfil = QtWidgets.QLabel(self.tab_3)
        self.lbl_perfil.setGeometry(QtCore.QRect(300, 305, 241, 20))
        self.lbl_perfil.setAutoFillBackground(False)
        self.lbl_perfil.setObjectName("lbl_perfil")
        self.tabWidget.addTab(self.tab_3, icon7, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.btn_actualiza = QtWidgets.QPushButton(self.tab_4)
        self.btn_actualiza.setGeometry(QtCore.QRect(460, 300, 121, 31))
        self.btn_actualiza.setAutoFillBackground(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("imagenes/actualiza.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_actualiza.setIcon(icon8)
        self.btn_actualiza.setIconSize(QtCore.QSize(80, 20))
        self.btn_actualiza.setFlat(True)
        self.btn_actualiza.setObjectName("btn_actualiza")
        self.btn_ayuda = QtWidgets.QPushButton(self.tab_4)
        self.btn_ayuda.setGeometry(QtCore.QRect(530, 10, 41, 31))
        self.btn_ayuda.setAutoFillBackground(False)
        self.btn_ayuda.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("imagenes/ayuda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ayuda.setIcon(icon9)
        self.btn_ayuda.setIconSize(QtCore.QSize(24, 24))
        self.btn_ayuda.setFlat(True)
        self.btn_ayuda.setObjectName("btn_ayuda")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(110, 310, 291, 20))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.btn_paypal = QtWidgets.QPushButton(self.tab_4)
        self.btn_paypal.setGeometry(QtCore.QRect(360, 300, 31, 31))
        self.btn_paypal.setAutoFillBackground(False)
        self.btn_paypal.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("imagenes/paypal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_paypal.setIcon(icon10)
        self.btn_paypal.setIconSize(QtCore.QSize(30, 30))
        self.btn_paypal.setFlat(True)
        self.btn_paypal.setObjectName("btn_paypal")
        self.btn_google = QtWidgets.QPushButton(self.tab_4)
        self.btn_google.setGeometry(QtCore.QRect(36, 312, 31, 21))
        self.btn_google.setAutoFillBackground(False)
        self.btn_google.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("imagenes/googleplus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_google.setIcon(icon11)
        self.btn_google.setIconSize(QtCore.QSize(16, 16))
        self.btn_google.setFlat(True)
        self.btn_google.setObjectName("btn_google")
        self.btn_facebook = QtWidgets.QPushButton(self.tab_4)
        self.btn_facebook.setGeometry(QtCore.QRect(70, 312, 31, 21))
        self.btn_facebook.setAutoFillBackground(False)
        self.btn_facebook.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("imagenes/facebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_facebook.setIcon(icon12)
        self.btn_facebook.setIconSize(QtCore.QSize(16, 16))
        self.btn_facebook.setFlat(True)
        self.btn_facebook.setObjectName("btn_facebook")
        self.btn_twitter = QtWidgets.QPushButton(self.tab_4)
        self.btn_twitter.setGeometry(QtCore.QRect(2, 312, 31, 21))
        self.btn_twitter.setAutoFillBackground(False)
        self.btn_twitter.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("imagenes/twitter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_twitter.setIcon(icon13)
        self.btn_twitter.setIconSize(QtCore.QSize(16, 16))
        self.btn_twitter.setFlat(True)
        self.btn_twitter.setObjectName("btn_twitter")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(119, 65, 35, 35))
        self.label_8.setBaseSize(QtCore.QSize(45, 45))
        self.label_8.setAutoFillBackground(False)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("imagenes/python-3.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(10, 20, 281, 171))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(300, 190, 271, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imagenes/sky.png"))
        self.label_2.setObjectName("label_2")
        self.btn_actualiza.raise_()
        self.btn_ayuda.raise_()
        self.label_3.raise_()
        self.btn_paypal.raise_()
        self.btn_google.raise_()
        self.btn_facebook.raise_()
        self.btn_twitter.raise_()
        self.label.raise_()
        self.label_8.raise_()
        self.label_2.raise_()
        self.tabWidget.addTab(self.tab_4, icon, "")
        self.ck_play = QtWidgets.QCheckBox(Form)
        self.ck_play.setGeometry(QtCore.QRect(430, 30, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ck_play.setFont(font)
        self.ck_play.setAutoFillBackground(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("imagenes/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ck_play.setIcon(icon14)
        self.ck_play.setObjectName("ck_play")
        self.f_box = QtWidgets.QComboBox(Form)
        self.f_box.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.f_box.setFont(font)
        self.f_box.setAutoFillBackground(False)
        self.f_box.setObjectName("f_box")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("imagenes/mp4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.f_box.addItem(icon15, "")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("imagenes/mp3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.f_box.addItem(icon16, "")
        self.btn_add_video = QtWidgets.QPushButton(Form)
        self.btn_add_video.setGeometry(QtCore.QRect(382, 10, 21, 21))
        self.btn_add_video.setAutoFillBackground(False)
        self.btn_add_video.setFlat(True)
        self.btn_add_video.setObjectName("btn_add_video")
        self.btn_de_item = QtWidgets.QPushButton(Form)
        self.btn_de_item.setGeometry(QtCore.QRect(404, 10, 21, 21))
        self.btn_de_item.setAutoFillBackground(False)
        self.btn_de_item.setFlat(True)
        self.btn_de_item.setObjectName("btn_de_item")
        self.p_bar = QtWidgets.QProgressBar(Form)
        self.p_bar.setGeometry(QtCore.QRect(14, 413, 471, 23))
        self.p_bar.setProperty("value", 0)
        self.p_bar.setObjectName("p_bar")
        self.btn_valida_2 = QtWidgets.QPushButton(Form)
        self.btn_valida_2.setGeometry(QtCore.QRect(489, 413, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_valida_2.setFont(font)
        self.btn_valida_2.setAutoFillBackground(False)
        self.btn_valida_2.setIcon(icon6)
        self.btn_valida_2.setIconSize(QtCore.QSize(32, 32))
        self.btn_valida_2.setFlat(True)
        self.btn_valida_2.setObjectName("btn_valida_2")
        self.lbl_barr = QtWidgets.QLabel(Form)
        self.lbl_barr.setGeometry(QtCore.QRect(60, 440, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lbl_barr.setFont(font)
        self.lbl_barr.setAutoFillBackground(False)
        self.lbl_barr.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_barr.setObjectName("lbl_barr")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_valida.setToolTip(_translate("Form", "Buscar Video"))
        self.ck_captura.setToolTip(_translate("Form", "Capturar Enlaces de Youtube en Automatico"))
        self.ck_captura.setText(_translate("Form", "Clip"))
        self.ck_lst_auto.setToolTip(_translate("Form", "Lista Automatica"))
        self.ck_lst_auto.setText(_translate("Form", "Lista"))
        self.ck_vlc.setToolTip(_translate("Form", "Reproducir Videos en VLC"))
        self.ck_vlc.setText(_translate("Form", "vlc"))
        self.lbl_desc.setToolTip(_translate("Form", "Introduce la URL de Youtube"))
        self.lbl_desc.setText(_translate("Form", "SkyTube Play d(-_-)b"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", " Reproductor "))
        self.lst_encola.setToolTip(_translate("Form", "Lista de Descarga"))
        self.btn_add_lista.setToolTip(_translate("Form", "Descargar Lista de videos"))
        self.btn_add_lista.setText(_translate("Form", "Descargar Lista"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", " Lista "))
        self.treeView.setToolTip(_translate("Form", "Directorio Videos"))
        self.lbl_autor_3.setText(_translate("Form", "Reproducir en  -  SkyTube Play d(-_-)b"))
        self.btn_play.setToolTip(_translate("Form", "Roproducir Multimedia"))
        self.lbl_autor_2.setText(_translate("Form", "Reproducir en  -  SkyTube Play d(-_-)b"))
        self.btn_folder_2.setToolTip(_translate("Form", "<html><head/><body><p>Abrir Carpeta de Videos</p></body></html>"))
        self.btn_folder_2.setText(_translate("Form", "..."))
        self.lbl_perfil.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", " Descargas "))
        self.btn_actualiza.setToolTip(_translate("Form", "Actualiza Version"))
        self.btn_actualiza.setText(_translate("Form", "Actualiza v.0.0."))
        self.btn_ayuda.setToolTip(_translate("Form", "Como Usar SkyTube! Ayuda en Linea!"))
        self.label_3.setText(_translate("Form", "Por Favor Considera una Donacion al Proyecto -->"))
        self.btn_paypal.setToolTip(_translate("Form", "Donar en PayPal"))
        self.btn_google.setToolTip(_translate("Form", "Sigueme en G+"))
        self.btn_facebook.setToolTip(_translate("Form", "Sigueme en Facebook"))
        self.btn_twitter.setToolTip(_translate("Form", "Sigueme en Twitter"))
        self.label_8.setToolTip(_translate("Form", "<html><head/><body><p>Programado en Python! y PyQt4 ..  xskyofx@gmail.com</p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Autor</span><span style=\" font-size:10pt;\">: </span>Juan Antonio Sandoval Puente</p><p><span style=\" font-size:10pt; font-weight:600;\">Nombre del Software</span>: SkyTube Download Videos</p><p><span style=\" font-size:10pt; font-weight:600;\">Codigo</span>: Python 3.4</p><p><span style=\" font-size:10pt; font-weight:600;\">Interface</span>: Qt 5</p><p><span style=\" font-size:10pt; font-weight:600;\">URL Proyecto</span>: <a href=\"https://github.com/xskylarx/SkyTube\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a></p><p><br/></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", " Acerca de "))
        self.ck_play.setToolTip(_translate("Form", "AutoReproduccion de Videos Youtube y Videos Locales"))
        self.ck_play.setText(_translate("Form", "AutoPlay"))
        self.f_box.setToolTip(_translate("Form", "Formato"))
        self.f_box.setItemText(0, _translate("Form", "mp4"))
        self.f_box.setItemText(1, _translate("Form", "mp3"))
        self.btn_add_video.setToolTip(_translate("Form", "Añadir Link a la Lista de Descargas"))
        self.btn_add_video.setText(_translate("Form", "+"))
        self.btn_de_item.setToolTip(_translate("Form", "Eliminar Link"))
        self.btn_de_item.setText(_translate("Form", "-"))
        self.btn_valida_2.setToolTip(_translate("Form", "Descarga el Video"))
        self.btn_valida_2.setText(_translate("Form", "Descargar"))
        self.lbl_barr.setText(_translate("Form", "-----"))

from PyQt5 import QtWebKitWidgets
