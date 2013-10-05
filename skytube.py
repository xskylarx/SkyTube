__author__ = 'xskylarx'
 #!/usr/bi/python3
# -*- coding: utf8 -*-
# Python + PyQt4 By Skylar
#
# Creado: 29 - sep - 2013
#      Por: xskylarx
# xskyofx@gmail.com
#V1.2 ->
# Se agrega Directorio de videos, con la cual se puede dar doble clic y abrir el video en VLC.
#
# Por favor si modificas algo haz referencia al autor.
from pafy import Pafy
from PyQt4 import QtGui, QtCore
from inicio import Ui_Form
import urllib.request
import os
import sys
import subprocess
import webbrowser


class v_skytube(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.vskytube = Ui_Form()
        self.vskytube.setupUi(self)
        self.connect(self.vskytube.btn_valida,QtCore.SIGNAL('clicked()'), self.valida)
        self.resize(579,106)
        self.vskytube.label_7.setStyleSheet("color:grey;")
        self.setWindowTitle('SkyTube Download v.1.3')
        self.setMaximumSize(869,288)
        self.setMinimumSize(579,106)
        self.vskytube.groupBox.setVisible(False)
        self.connect(self.vskytube.btn_valida_2,QtCore.SIGNAL('clicked()'), self.descarga)
        self.connect(self.vskytube.btn_vlc,QtCore.SIGNAL('clicked()'), self.AbreVLC)
        self.connect(self.vskytube.btn_otro,QtCore.SIGNAL('clicked()'), self.muestra)
        self.vskytube.lbl_desc.setVisible(False)
        self.vskytube.btn_vlc.setVisible(False)
        self.vskytube.btn_otro.setVisible(False)
        self.vskytube.ck_lst_auto.setEnabled(False)
        self.connect(self.vskytube.btn_folder,QtCore.SIGNAL('clicked()'), self.crea_directorio)
        self.vskytube.treeView.doubleClicked.connect(self.directorio)
        #self.vskytube.la.doubleClicked.connect(self.directorio)
        self.vskytube.treeView.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)
        self.setStyleSheet("background-image: url('imagenes/skylogo.png');")
        self.connect(self.vskytube.btn_folder_2,QtCore.SIGNAL('clicked()'), self.folder)

        self.connect(self.vskytube.btn_add_video, QtCore.SIGNAL('clicked()'), self.add)
        self.connect(self.vskytube.btn_add, QtCore.SIGNAL('clicked()'), self.crea_lista)
        self.connect(self.vskytube.btn_paypal, QtCore.SIGNAL('clicked()'), self.donapaypal)
        self.connect(self.vskytube.ck_captura, QtCore.SIGNAL('stateChanged(int)'), self.CapturaClip)
        self.connect(self.vskytube.lst_encola, QtCore.SIGNAL('itemClicked(QListWidgetItem*)'), self.valida_lista)
        self.connect(self.vskytube.lst_encola, QtCore.SIGNAL('itemDoubleClicked(QListWidgetItem*)'), self.elimina_item)
        self.connect(self.vskytube.btn_de_item, QtCore.SIGNAL('clicked()'), self.elimina_item)
        self.connect(self.vskytube.btn_add_lista, QtCore.SIGNAL('clicked()'), self.valida_descarga)


        self.setclipboard()


    def setclipboard(self):
        global data
        data = QtGui.QApplication.clipboard()
        data = data.setText('skylar')





    def elimina_item(self):
        try:
            for index in range(self.vskytube.lst_encola.count()):
                if self.vskytube.lst_encola.currentItem().text() == self.vskytube.lst_encola.item(index).text():

                    respuesta = QtGui.QMessageBox.question(self, 'Elimina Link ', 'Estas seguro de Eliminar el Link \n' + self.vskytube.lst_encola.item(index).text() + ' ?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if respuesta == QtGui.QMessageBox.Yes:
                        item = self.vskytube.lst_encola.takeItem(index)
                        del item
                        self.vskytube.groupBox.setVisible(False)

        except:
            QtGui.QMessageBox.about(self,'Error Link','No hay Link Que eliminar')

    def descarga_lista(self):

        self.vskytube.ck_captura.setChecked(False)
        QtGui.QMessageBox.about(self,'Comenzando Descarga','Tu lista empezara a Descargarce, esto va a tardar varios minutos.')
        items=[]
        for index in range(self.vskytube.lst_encola.count()):
            items.append(self.vskytube.lst_encola.item(index).text())


        url = '"' + str(items) + '" ' + self.formato()
        #QtGui.QMessageBox.about(self,'t',url)

        os.system('skytubec.exe ' + url)

        QtGui.QMessageBox.about(self,'Descarga Completada', 'La Lista se Descargo Correctamente..')
        self.crea_directorio()
        self.vskytube.lst_encola.clear()


    def add(self):
        try:

            video_id = self.vskytube.lineEdit.text()
            if len(video_id) == 11:
                url= 'http://www.youtube.com/watch?v=' + video_id



            elif len(str(video_id).split('?v=')) == 2:
                video_id = video_id.split('?v=')
            else:
                self.setclipboard()
                self.vskytube.lineEdit.clear()
                QtGui.QMessageBox.about(self,'Alerta Link! ','Link No valido!' )
                return
            if len(video_id) == 2:
                url= 'http://www.youtube.com/watch?v=' + video_id[1]
            else:
                url= 'http://www.youtube.com/watch?v=' + video_id



            items=[]
            for index in range(self.vskytube.lst_encola.count()):
                items.append(self.vskytube.lst_encola.item(index).text())

            existe = 'No'
            for i in items:
                 if url == i:
                     existe = 'Si'


            if existe == 'No':
                self.setclipboard()
                if Pafy(url):
                    self.vskytube.lst_encola.addItem(url)
                    self.vskytube.lineEdit.clear()
            else:
                self.vskytube.lineEdit.clear()
                self.setclipboard()
                QtGui.QMessageBox.about(self,'Alerta Link! ','Este Link ya fue agregado a la lista!' )
        except:
             self.vskytube.lineEdit.setText('Link No Valido')
             self.setclipboard()




    def clipboard(self):
        global data
        data = QtGui.QApplication.clipboard()
        data = data.text()


        if len(data) == 11:
            item = ('http://www.youtube.com/watch?v=' + data)
            self.vskytube.lineEdit.setText(item)
            if self.vskytube.ck_lst_auto.isChecked():
                    self.add()
            timer = QtCore.QTimer()
            timer.stop()
            self.CapturaClip()

        if len(str(data).split('?v=')) == 2:
            data = str(data).split('?v=')

            if len(data) == 2:

                item = ('http://www.youtube.com/watch?v=' + data[1])
                self.vskytube.lineEdit.setText(item)
                if self.vskytube.ck_lst_auto.isChecked():
                    self.add()

                timer = QtCore.QTimer()
                timer.stop()
                self.CapturaClip()

        else:
            timer = QtCore.QTimer()
            timer.stop()
            self.CapturaClip()




    def CapturaClip(self):
        #QtCore.QTimer.singleShot(3000, self.clipboard)
        if self.vskytube.ck_captura.isChecked():
            global timer
            timer = QtCore.QTimer()
            timer.start(3000)
            timer.connect(timer,QtCore.SIGNAL("timeout()"), self.clipboard)
            self.vskytube.ck_lst_auto.setEnabled(True)


        else:
            self.vskytube.ck_lst_auto.setEnabled(False)
            self.vskytube.ck_lst_auto.setChecked(False)
            timer = QtCore.QTimer()
            self.setclipboard()
            timer.stop()

    def crea_directorio(self):

        if self.vskytube.btn_folder.text() == '>':
            self.oculta()
            self.resize(869,288)
            self.vskytube.treeView.setVisible(True)
            self.vskytube.lbl_perfil.setVisible(True)
            self.vskytube.btn_folder_2.setVisible(True)
            self.vskytube.btn_folder.setText('<')
            self.vskytube.btn_folder.setToolTip('Motrar Videos')
            if sys.platform == 'win32':
                self.vskytube.lbl_perfil.setText((os.path.join (os.environ['USERPROFILE'],'videos')))
            if sys.platform == 'darwin':
                self.vskytube.lbl_perfil.setText((os.path.join (os.environ['HOME'],'Movies')))
        else:
            self.resize(579,106)
            self.vskytube.treeView.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            self.vskytube.btn_folder_2.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            self.vskytube.btn_folder.setText('>')
            self.vskytube.btn_folder.setToolTip('Ocultar Videos')
            self.vskytube.lbl_perfil.setVisible(False)



        fileSystemModel = QtGui.QFileSystemModel(self.vskytube.treeView)
        fileSystemModel.setReadOnly(True)
        if sys.platform == 'win32':
                root = fileSystemModel.setRootPath((os.path.join (os.environ['USERPROFILE'],'videos')))
        elif sys.platform == 'darwin':
            root = fileSystemModel.setRootPath((os.path.join (os.environ['HOME'],'Movies')))

        self.vskytube.treeView.setModel(fileSystemModel)
        self.vskytube.treeView.setRootIndex(root)
        self.vskytube.treeView.setColumnHidden(1,True)
        self.vskytube.treeView.setColumnHidden(2,True)
        self.vskytube.treeView.setColumnHidden(3,True)
        self.vskytube.treeView.setHeaderHidden(True)


    def crea_lista(self):

        if self.vskytube.btn_add.text() == '>':
            self.oculta()
            self.resize(869,288)
            self.vskytube.lst_encola.setVisible(True)
            self.vskytube.btn_add_lista.setVisible(True)
            self.vskytube.btn_add_video.setVisible(True)
            self.vskytube.btn_de_item.setVisible(True)
            self.vskytube.btn_add.setText('<')
            self.vskytube.btn_folder.setToolTip('Mostrar Lista')

        else:
            self.resize(579,106)
            self.vskytube.lst_encola.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            self.vskytube.btn_add_lista.setVisible(False)
            self.vskytube.btn_add_video.setVisible(False)
            self.vskytube.btn_de_item.setVisible(False)
            self.vskytube.btn_add.setText('>')
            self.vskytube.btn_folder.setToolTip('Ocultar Lista')


    def oculta(self):
        self.vskytube.lst_encola.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)
        self.vskytube.btn_add_lista.setVisible(False)
        self.vskytube.btn_add_video.setVisible(False)
        self.vskytube.btn_add.setText('>')
        self.vskytube.btn_folder.setToolTip('Ocultar Lista')
        self.vskytube.treeView.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)
        self.vskytube.btn_folder_2.setVisible(False)
        self.vskytube.btn_folder.setText('>')
        self.vskytube.btn_folder.setToolTip('Ocultar Videos')
        self.vskytube.lbl_perfil.setVisible(False)
        self.vskytube.btn_de_item.setVisible(False)



    def donapaypal(self):
        QtGui.QMessageBox.information(self,'Donacion PayPal','Gracias por conciderar  hacer una donacion al proyecto SkyTube \n Todo el dinero seran utilizado para el Hosting \
                                                             \n Muchas Gracias =)')
        webbrowser.open('https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2K6Y3B8AG39DQ')

    def directorio(self, mensaje):
        if sys.platform == 'win32':
            if os.path.isfile('c:\progra~1\VideoLAN\VLC\\vlc.exe'):
                subprocess.Popen('c:\progra~1\VideoLAN\VLC\\vlc.exe "' + str((os.path.join (os.environ['USERPROFILE'],'videos'))) + '\\' +str(mensaje.data()) + '"' )
            elif os.path.isfile('c:\progra~2\VideoLAN\VLC\\vlc.exe'):
                subprocess.Popen('c:\progra~2\VideoLAN\VLC\\vlc.exe "' + str((os.path.join (os.environ['USERPROFILE'],'videos'))) + '\\' +str(mensaje.data()) + '"')
            else:
                QtGui.QMessageBox.about(self,'\nError VlC','Para poder reproducir los videos desde SkyTube necesitas VLC \n tus videos estan en la  siguiente ruta:\n\n '\
                                                          + str((os.path.join (os.environ['USERPROFILE'],'videos'))))
        if sys.platform == 'darwin':
            subprocess.Popen('/Applications/VLC.app/Contents/MacOS/VLC ' + str((os.path.join (os.environ['HOME'],'Movies'))) + '\\' +str(mensaje.data()) + '')

    def folder(self):
        if sys.platform == 'win32':
            perfil = (os.path.join (os.environ['USERPROFILE'],'videos'))
            subprocess.Popen('explorer ' + str(perfil))
        if sys.platform == 'linux2':
            print('si')



    def descarga(self):
        try:


            self.vskytube.lineEdit.setVisible(False)
            self.vskytube.btn_valida.setVisible(False)
            self.vskytube.label_7.setVisible(False)
            self.vskytube.btn_folder.setVisible(False)
            self.vskytube.treeView.setVisible(False)
            self.vskytube.btn_folder_2.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            self.vskytube.groupBox.setVisible(False)
            self.vskytube.groupBox_2.setVisible(False)
            self.vskytube.btn_add.setVisible(False)
            self.vskytube.ck_lst_auto.setVisible(False)
            self.vskytube.ck_captura.setVisible(False)
            self.vskytube.lbl_desc.setStyleSheet("color:red;")
            self.vskytube.lbl_desc.setText('Tu video se esta descargado, puede tardar varios minutos ...')
            self.vskytube.lbl_desc.setVisible(True)
            self.resize(579,106)
            QtGui.QMessageBox.about(self,'Empezando Descarga ... ','La descarga puede tardar varios minutos, dependiendo de tu conexion ...')
            global url
            os.system('skytubec.exe ' + url + ' ' + self.formato())
            self.vskytube.lbl_desc.setStyleSheet("color:green;")
            self.vskytube.lbl_desc.setText('Tu video se descargo correctamente ...')
            self.vskytube.btn_vlc.setVisible(True)
            self.vskytube.btn_otro.setVisible(True)
            win32clipboard.OpenClipboard()
            global data
            win32clipboard.EmptyClipboard()
            data = win32clipboard.SetClipboardText('skytube')
            win32clipboard.CloseClipboard()
            self.vskytube.lineEdit.clear()
            if os.path.isfile('c:\progra~1\VideoLAN\VLC\\vlc.exe') or os.path.isfile('c:\progra~2\VideoLAN\VLC\\vlc.exe'):
                self.vskytube.btn_vlc.setEnabled(True)
            else:
                self.vskytube.btn_vlc.setEnabled(False)

        except Exception as e:
            QtGui.QMessageBox.about(self,'Error Descarga', str(e))



    def muestra(self):
        self.vskytube.lineEdit.setVisible(True)
        self.vskytube.btn_valida.setVisible(True)
        self.vskytube.label_7.setVisible(True)
        self.vskytube.btn_folder.setVisible(True)
        self.vskytube.groupBox_2.setVisible(True)
        self.vskytube.btn_add.setVisible(True)
        self.vskytube.ck_lst_auto.setVisible(True)
        self.vskytube.ck_captura.setVisible(True)
        self.vskytube.lbl_desc.setVisible(False)
        self.vskytube.btn_vlc.setVisible(False)
        self.vskytube.btn_otro.setVisible(False)
        self.vskytube.groupBox.setVisible(False)
        self.vskytube.lineEdit.clear()

    def AbreVLC(self):

        best = video.getbest(preftype=self.formato())
        titulo = best.title
        titulo = str(titulo).replace('.','')
        titulo = str(titulo).replace('"','')
        titulo = str(titulo).replace(':','')
        titulo = str(titulo).replace('_','')
        titulo = str(titulo).replace('-','')
        titulo = str(titulo).replace(';','')
        titulo = str(titulo).replace('|','')
        titulo = str(titulo).replace("'",'')
        titulo = str(titulo).replace("+",'')
        titulo = str(titulo).replace("!",'')
        titulo = str(titulo).replace("/",'')
        titulo = str(titulo).replace("\\",'')
        titulo = str(titulo).replace("*",'')
        titulo = str(titulo).replace("#",'')
        titulo = str(titulo).replace("%",'')
        titulo = str(titulo).replace("&",'')
        titulo = str(titulo).replace("(",'')
        titulo = str(titulo).replace(")",'')
        titulo = str(titulo).replace("[",'')
        titulo = str(titulo).replace("]",'')
        titulo = str(titulo).replace("{",'')
        titulo = str(titulo).replace("}",'')
        titulo = str(titulo).replace("=",'')
        titulo = str(titulo).replace("~",'')
        titulo = str(titulo).replace("<",'')
        titulo = str(titulo).replace(">",'')

        perfil = (os.path.join (os.environ['USERPROFILE'],'videos'))
        #QtGui.QMessageBox.about(self,'ff','"' + os.path.abspath(os.path.dirname(__file__)) + '\\videos\\' + best.title + '.' + best.extension + '"' )
        if os.path.isfile('c:\progra~1\VideoLAN\VLC\\vlc.exe'):
            subprocess.Popen('c:\progra~1\VideoLAN\VLC\\vlc.exe "' +str(perfil) + '\\' + titulo + '.' + best.extension + '"' )
        else:
             subprocess.Popen('c:\progra~2\VideoLAN\VLC\\vlc.exe "' + str(perfil) + '\\' + titulo + '.' + best.extension + '"' )

    def formato(self):

        if self.vskytube.r_3gp.isChecked():
            return '3gp'

        if self.vskytube.r_flv.isChecked():
            return 'flv'

        if self.vskytube.r_webm.isChecked():
           return 'webm'

        if self.vskytube.r_mp4.isChecked():
            return 'mp4'


    def valida_descarga(self):
        try:
            url = ''
            for index in range(self.vskytube.lst_encola.count()):
                url = self.vskytube.lst_encola.item(index).text()

            if  url == '':
                QtGui.QMessageBox.about(self,'Error Lista vacia','No hay Links para procesar')
            else:
                self.descarga_lista()
        except Exception as e:
            QtGui.QMessageBox.about(self,'Error en Link ','El Link : ' + url + ' No existe..\n Se eliminara de la lista..\n Por favor Vuelve a descargar la lista ')

    def valida_lista(self):
        try:
            self.vskytube.groupBox.setVisible(False)
            self.vskytube.lbl_imagen.setText('sin imagen')
            if os.path.isfile(os.path.dirname(sys.executable)+ '\\skytube.jpg'):
                os.remove(os.path.dirname(sys.executable) + '\\skytube.jpg')

            item = self.vskytube.lst_encola.currentItem()
            url = item.text()

            video = Pafy(url)
            best = video.getbest(preftype=self.formato())
            self.vskytube.lbl_calidad.setText(best.resolution + ' Extencion: ' + best.extension)

            self.vskytube.groupBox.setStyleSheet("color:green;")
            self.vskytube.groupBox.setTitle(video.title)
            self.vskytube.lbl_autor.setText(video.author)
            self.vskytube.lbl_duracion.setText(video.duration)
            self.vskytube.lbl_id.setText(video.videoid)
            self.vskytube.lbl_rating.setText(str(video.rating))
            self.vskytube.lbl_visto.setText(str(video.viewcount))
            self.vskytube.btn_valida_2.setVisible(False)

            url = video.thumb
            file = ('skytube.jpg')
            urllib.request.urlretrieve(url, file)
            img = (os.path.dirname(sys.executable) + '\skytube.jpg')
            self.vskytube.lbl_imagen.setPixmap(QtGui.QPixmap(img))
            self.vskytube.groupBox.setVisible(True)
        except Exception as e:
            self.vskytube.groupBox.setVisible(False)
            QtGui.QMessageBox.about(self,'Error en Link ','El Link : ' + item.text() + ' No existe..\n Se eliminara de la lista..' + str(e))
            self.elimina_item()


    def valida(self):
        try:
            self.oculta()

            self.vskytube.groupBox.setVisible(False)
            self.resize(579,106)
            self.vskytube.lbl_imagen.setText('sin imagen')
            if os.path.isfile(os.path.dirname(sys.executable)+ '\\skytube.jpg'):
                os.remove(os.path.dirname(sys.executable) + '\\skytube.jpg')

            self.vskytube.groupBox.setVisible(True)

            video_id = self.vskytube.lineEdit.text()

            if len(video_id) == 11:
                url= 'http://www.youtube.com/watch?v=' + video_id


            if video_id.split('?v=') == 1:
                video_id = video_id.split('?v=')

            if len(video_id) == 1:
                global url
                url= 'http://www.youtube.com/watch?v=' + video_id[1]
            else:
                global url
                url= 'http://www.youtube.com/watch?v=' + video_id



            global video

            video = Pafy(url)
            best = video.getbest(preftype=self.formato())
            self.vskytube.lbl_calidad.setText(best.resolution + ' Extencion: ' + best.extension)

            self.vskytube.groupBox.setStyleSheet("color:green;")
            self.vskytube.groupBox.setTitle(video.title)
            self.vskytube.lbl_autor.setText(video.author)
            self.vskytube.lbl_duracion.setText(video.duration)
            self.vskytube.lbl_id.setText(video.videoid)
            self.vskytube.lbl_rating.setText(str(video.rating))
            self.vskytube.lbl_visto.setText(str(video.viewcount))
            self.resize(579,288)
            self.vskytube.btn_valida_2.setVisible(True)


            #os.chdir(os.path.dirname(sys.executable))
            url_img = video.thumb
            file = ('skytube.jpg')
            urllib.request.urlretrieve(url_img, file)
            img = (os.path.dirname(sys.executable) + '\skytube.jpg')
            #img = (video.thumb)
            #self.vskytube.lbl_imagen.setText('<img src="'+ img +'" />')
            self.vskytube.lbl_imagen.setPixmap(QtGui.QPixmap(img))
        except Exception as e:
            QtGui.QMessageBox.about(self,'Error SkyTube ',' No existe el video favor de verificar.')
            QtGui.QMessageBox.about(self,'Error SkyTube ',str(e))

def main():
    app = QtGui.QApplication(sys.argv)
    vskytube = v_skytube()
    vskytube.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


