# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio.ui'
#
# Created: Sun Sep 29 11:28:04 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(579, 249)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.btn_valida = QtGui.QPushButton(Form)
        self.btn_valida.setGeometry(QtCore.QRect(490, 20, 41, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/buscar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_valida.setIcon(icon1)
        self.btn_valida.setObjectName(_fromUtf8("btn_valida"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 461, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(13, 60, 551, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(13, 80, 551, 161))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 62, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 83, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 104, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lbl_autor = QtGui.QLabel(self.groupBox)
        self.lbl_autor.setGeometry(QtCore.QRect(60, 18, 481, 16))
        self.lbl_autor.setObjectName(_fromUtf8("lbl_autor"))
        self.lbl_id = QtGui.QLabel(self.groupBox)
        self.lbl_id.setGeometry(QtCore.QRect(50, 38, 311, 16))
        self.lbl_id.setObjectName(_fromUtf8("lbl_id"))
        self.lbl_duracion = QtGui.QLabel(self.groupBox)
        self.lbl_duracion.setGeometry(QtCore.QRect(80, 60, 311, 16))
        self.lbl_duracion.setObjectName(_fromUtf8("lbl_duracion"))
        self.lbl_rating = QtGui.QLabel(self.groupBox)
        self.lbl_rating.setGeometry(QtCore.QRect(70, 80, 331, 16))
        self.lbl_rating.setObjectName(_fromUtf8("lbl_rating"))
        self.lbl_visto = QtGui.QLabel(self.groupBox)
        self.lbl_visto.setGeometry(QtCore.QRect(60, 101, 341, 16))
        self.lbl_visto.setObjectName(_fromUtf8("lbl_visto"))
        self.btn_valida_2 = QtGui.QPushButton(self.groupBox)
        self.btn_valida_2.setGeometry(QtCore.QRect(20, 130, 77, 24))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_valida_2.setIcon(icon2)
        self.btn_valida_2.setObjectName(_fromUtf8("btn_valida_2"))
        self.lbl_imagen = QtGui.QLabel(self.groupBox)
        self.lbl_imagen.setGeometry(QtCore.QRect(360, 40, 161, 91))
        self.lbl_imagen.setStyleSheet(_fromUtf8(""))
        self.lbl_imagen.setScaledContents(True)
        self.lbl_imagen.setObjectName(_fromUtf8("lbl_imagen"))
        self.lbl_calidad = QtGui.QLabel(self.groupBox)
        self.lbl_calidad.setGeometry(QtCore.QRect(364, 137, 171, 20))
        self.lbl_calidad.setObjectName(_fromUtf8("lbl_calidad"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(14, 43, 551, 21))
        self.label_7.setStyleSheet(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lbl_desc = QtGui.QLabel(Form)
        self.lbl_desc.setGeometry(QtCore.QRect(40, 20, 461, 20))
        self.lbl_desc.setObjectName(_fromUtf8("lbl_desc"))
        self.btn_vlc = QtGui.QPushButton(Form)
        self.btn_vlc.setGeometry(QtCore.QRect(185, 40, 75, 24))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/eye.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_vlc.setIcon(icon3)
        self.btn_vlc.setObjectName(_fromUtf8("btn_vlc"))
        self.btn_otro = QtGui.QPushButton(Form)
        self.btn_otro.setGeometry(QtCore.QRect(261, 40, 131, 24))
        self.btn_otro.setIcon(icon2)
        self.btn_otro.setObjectName(_fromUtf8("btn_otro"))
        self.btn_folder = QtGui.QPushButton(Form)
        self.btn_folder.setGeometry(QtCore.QRect(530, 20, 41, 24))
        self.btn_folder.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("imagenes/video.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_folder.setIcon(icon4)
        self.btn_folder.setObjectName(_fromUtf8("btn_folder"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btn_valida.setToolTip(_translate("Form", "Buscar Video", None))
        self.btn_valida.setText(_translate("Form", "...", None))
        self.label.setText(_translate("Form", "Autor:", None))
        self.label_2.setText(_translate("Form", "ID:", None))
        self.label_3.setText(_translate("Form", "Duracion:", None))
        self.label_4.setText(_translate("Form", "Rating:", None))
        self.label_5.setText(_translate("Form", "Visto: ", None))
        self.lbl_autor.setText(_translate("Form", "Autor:", None))
        self.lbl_id.setText(_translate("Form", "ID:", None))
        self.lbl_duracion.setText(_translate("Form", "Duracion:", None))
        self.lbl_rating.setText(_translate("Form", "Rating:", None))
        self.lbl_visto.setText(_translate("Form", "Visto: ", None))
        self.btn_valida_2.setToolTip(_translate("Form", "Descarga el Video en Mp4", None))
        self.btn_valida_2.setText(_translate("Form", "Descargar", None))
        self.lbl_imagen.setToolTip(_translate("Form", "Imagen Previa del Video", None))
        self.lbl_imagen.setText(_translate("Form", "https://i1.ytimg.com/vi/QJO3ROT-A4E/sddefault.jpg", None))
        self.lbl_calidad.setText(_translate("Form", "Calidad y Resolucion: ", None))
        self.label_7.setText(_translate("Form", "Ejemplo: http://www.youtube.com/watch?v=QJO3ROT-A4E ", None))
        self.lbl_desc.setToolTip(_translate("Form", "Introduce la URL de Youtube", None))
        self.lbl_desc.setText(_translate("Form", "TextLabel", None))
        self.btn_vlc.setToolTip(_translate("Form", "Abre  Video en Reproductor VLC", None))
        self.btn_vlc.setText(_translate("Form", "Abrir VLC", None))
        self.btn_otro.setToolTip(_translate("Form", "Regresar al Formulario de busqueda", None))
        self.btn_otro.setText(_translate("Form", "Descargar Otro Video", None))
        self.btn_folder.setToolTip(_translate("Form", "Abre la carpeta Videos", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

