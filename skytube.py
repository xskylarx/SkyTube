__author__ = 'xskylarx'
 #!/usr/bi/python3
# -*- coding: utf8 -*-
# Python + PyQt4 By Skylar
#
# Creado: 29 - sep - 2013
#      Por: xskylarx
# xskyofx@gmail.com
#v1.4 se añade compatibilidad con linux, mac, windows, se agrega funcion para abrir reproductor predeterminado, o vlc
#v1.3 se añade lista automatica, capturador de enlaces, lista de descarga
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
import webbrowser


class v_skytube(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.vskytube = Ui_Form()
        self.vskytube.setupUi(self)
        self.resize(585,121)
        self.vskytube.label_7.setStyleSheet("color:grey;")
        self.setWindowTitle('SkyTube Download v.1.4')
        self.setMaximumSize(880,321)
        self.setMinimumSize(489,48)
        self.vskytube.groupBox.setVisible(False)
        self.connect(self.vskytube.btn_valida_2,QtCore.SIGNAL('clicked()'), self.descarga)
        self.connect(self.vskytube.btn_valida,QtCore.SIGNAL('clicked()'), self.valida)
        self.vskytube.lbl_desc.setVisible(False)
        self.vskytube.ck_lst_auto.setEnabled(False)
        self.connect(self.vskytube.btn_folder,QtCore.SIGNAL('clicked()'), self.crea_directorio)
        self.vskytube.treeView.doubleClicked.connect(self.directorio)
        self.vskytube.lineEdit.returnPressed.connect(self.valida)
        self.vskytube.treeView.setVisible(False)
        self.vskytube.lbl_perfil.setVisible(False)
        self.setStyleSheet("background-image: url('imagenes/skylogo.png');")
        self.connect(self.vskytube.btn_folder_2,QtCore.SIGNAL('clicked()'), self.folder)

        self.connect(self.vskytube.btn_add_video, QtCore.SIGNAL('clicked()'), self.add)
        self.connect(self.vskytube.btn_add, QtCore.SIGNAL('clicked()'), self.crea_lista)
        self.connect(self.vskytube.btn_paypal, QtCore.SIGNAL('clicked()'), self.donapaypal)
        self.connect(self.vskytube.ck_captura, QtCore.SIGNAL('stateChanged(int)'), self.CapturaClip)
        self.connect(self.vskytube.ck_vlc, QtCore.SIGNAL('stateChanged(int)'), self.vlc_checked)
        self.connect(self.vskytube.lst_encola, QtCore.SIGNAL('itemClicked(QListWidgetItem*)'), self.valida_lista)
        self.connect(self.vskytube.lst_encola, QtCore.SIGNAL('itemDoubleClicked(QListWidgetItem*)'), self.elimina_item)
        self.connect(self.vskytube.btn_de_item, QtCore.SIGNAL('clicked()'), self.elimina_item)
        self.connect(self.vskytube.btn_add_lista, QtCore.SIGNAL('clicked()'), self.valida_descarga)
        self.connect(self.vskytube.btn_google, QtCore.SIGNAL('clicked()'), self.social_google)
        self.connect(self.vskytube.btn_twitter, QtCore.SIGNAL('clicked()'), self.social_twitter)
        self.connect(self.vskytube.btn_facebook, QtCore.SIGNAL('clicked()'), self.social_facebook)
        self.vskytube.lineEdit.setPlaceholderText('    Escribe o pega la direccion de tu video y da enter ..')
        self.oculta()
        self.process = QtCore.QProcess()



        self.setclipboard()
        self.vlc()

# revisado Linux, Windows
    def setclipboard(self):
        global data
        data = QtGui.QApplication.clipboard()
        data = data.setText('skylar')

#revisado Linux, Windows
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
        items = []
        for index in range(self.vskytube.lst_encola.count()):
            items.append(self.vskytube.lst_encola.item(index).text())


        url = str(items)
        url = url.replace('[','')
        url = url.replace(']','')
        url = url.replace("'","")
        url = url.replace(" ","")

        if 'win32' or 'win64' in self.sistema():
            os.system('skytubec.exe ' + url + ' ' + self.formato())

        if 'darwin' in self.sistema():
            os.system('skytubec.exe ' + url)

        if 'linux' in self.sistema():
            os.system('xterm -e "skytubec ' + url + ' ' + self.formato() + '"')

        QtGui.QMessageBox.about(self,'Descarga Completada', 'La Lista se Descargo Correctamente..')
        self.vskytube.groupBox.setVisible(False)

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



            items = []
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
            self.resize(880,321)
            self.vskytube.treeView.setVisible(True)
            self.vskytube.lbl_perfil.setVisible(True)
            self.vskytube.btn_folder_2.setVisible(True)
            self.vskytube.btn_folder.setText('<')
            self.vskytube.btn_folder.setToolTip('Motrar Videos')
            if 'win32' or 'win64' in self.sistema():
                self.vskytube.lbl_perfil.setText((os.path.join (os.environ['USERPROFILE'],'videos')))
            if 'darwin' in self.sistema():
                self.vskytube.lbl_perfil.setText((os.path.join (os.environ['HOME'],'Movies')))
            if 'linux' in self.sistema():
                if os.path.isdir(os.path.join (os.environ['HOME'],'Movies')):
                    self.vskytube.lbl_perfil.setText((os.path.join (os.environ['HOME'],'Movies')))
                else:
                    os.system('mkdir $HOME/Movies')
                    self.vskytube.lbl_perfil.setText((os.path.join (os.environ['HOME'],'Movies')))

        else:
            self.resize(585,121)
            self.vskytube.treeView.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            self.vskytube.btn_folder_2.setVisible(False)
            self.vskytube.lbl_perfil.setVisible(False)
            self.vskytube.btn_folder.setText('>')
            self.vskytube.btn_folder.setToolTip('Ocultar Videos')
            self.vskytube.lbl_perfil.setVisible(False)

        global fileSystemModel
        fileSystemModel = QtGui.QFileSystemModel(self.vskytube.treeView)
        fileSystemModel.setReadOnly(True)

        if 'win32' or 'win64' in self.sistema():
            fileSystemModel.setRootPath(str((os.path.join (os.environ['USERPROFILE'],'videos'))))
            indexRoot = fileSystemModel.index(fileSystemModel.rootPath())
            self.vskytube.treeView.setModel(fileSystemModel)
            self.vskytube.treeView.setRootIndex(indexRoot)
        elif 'darwin' or 'linux' in self.sistema():
            fileSystemModel.setRootPath(str((os.path.join (os.environ['HOME'],'Movies'))))
            indexRoot = fileSystemModel.index(fileSystemModel.rootPath())
            self.vskytube.treeView.setModel(fileSystemModel)
            self.vskytube.treeView.setRootIndex(indexRoot)


        self.vskytube.treeView.setColumnHidden(1,True)
        self.vskytube.treeView.setColumnHidden(2,True)
        self.vskytube.treeView.setColumnHidden(3,True)
        self.vskytube.treeView.setHeaderHidden(True)


    def crea_lista(self):

        if self.vskytube.btn_add.text() == '>':
            self.oculta()
            self.resize(880,321)
            self.vskytube.lst_encola.setVisible(True)
            self.vskytube.btn_add_lista.setVisible(True)
            self.vskytube.btn_add_video.setVisible(True)
            self.vskytube.btn_de_item.setVisible(True)
            self.vskytube.btn_add.setText('<')
            self.vskytube.btn_folder.setToolTip('Mostrar Lista')

        else:
            self.resize(585,121)
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

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def directorio(self, index):
        if self.vskytube.ck_vlc.isChecked():
            indexItem = fileSystemModel.index(index.row(), 0, index.parent())
            filePath = fileSystemModel.filePath(indexItem)
            self.directorio_vlc(filePath)
            return

        if 'win32' or 'win64' in self.sistema():
            indexItem = fileSystemModel.index(index.row(), 0, index.parent())
            filePath = fileSystemModel.filePath(indexItem)
            os.startfile(filePath)

        if 'darwin' in self.sistema():
            if os.path.isdir('/Applications/VLC.app'):
                indexItem = fileSystemModel.index(index.row(), 0, index.parent())
                filePath = fileSystemModel.filePath(indexItem)
                os.system('open -a /Applications/VLC.app/Contents/MacOS/VLC "' + filePath + '"')
            else:
                QtGui.QMessageBox.about(self,'\nError VlC','Para poder reproducir los videos desde SkyTube necesitas VLC \n tus videos estan en la  siguiente ruta:\n\n '\
                                                           + str((os.path.join (os.environ['HOME'],'Movies'))))

        if 'linux' in self.sistema():
            indexItem = fileSystemModel.index(index.row(), 0, index.parent())
            filePath = fileSystemModel.filePath(indexItem)
            self.process.start('xdg-open "' + filePath + '"')


    def directorio_vlc(self, video_vlc):
        if 'win32' or 'win64' in self.sistema():

            if os.path.isfile('c:\progra~1\VideoLAN\VLC\\vlc.exe'):
                 video_vlc = video_vlc.replace('/', '\\')
                 self.process.start('c:\progra~1\VideoLAN\VLC\\vlc.exe "' + video_vlc + '"')


            elif os.path.isfile('c:\progra~2\VideoLAN\VLC\\vlc.exe'):
                self.process.start('c:\progra~2\VideoLAN\VLC\\vlc.exe "' + video_vlc + '"')

        if 'darwin' in self.sistema():
            if os.path.isdir('/Applications/VLC.app'):
                self.process.start('open -a /Applications/VLC.app/Contents/MacOS/VLC "' + video_vlc + '"')

        if 'linux' in self.sistema():
            self.process.start('vlc "' + video_vlc + '"')

    def vlc(self):

        if os.path.isdir('/Applications/VLC.app') or os.path.isfile('/usr/bin/vlc') or os.path.isfile('c:\progra~1\VideoLAN\VLC\\vlc.exe') or os.path.isfile('c:\progra~2\VideoLAN\VLC\\vlc.exe'):
            self.vskytube.ck_vlc.setChecked(True)
            vlc_ok = QtGui.QIcon()
            vlc_ok.addPixmap(QtGui.QPixmap("imagenes/vlc_ok.png"))
            self.vskytube.ck_vlc.setIcon(vlc_ok)
        else:
            vlc_no = QtGui.QIcon()
            vlc_no.addPixmap(QtGui.QPixmap("imagenes/vlc.png"))
            self.vskytube.ck_vlc.setIcon(vlc_no)
            self.vskytube.ck_vlc.setEnabled(False)

    def vlc_checked(self):
        if self.vskytube.ck_vlc.isChecked():
            vlc_ok = QtGui.QIcon()
            vlc_ok.addPixmap(QtGui.QPixmap("imagenes/vlc_ok.png"))
            self.vskytube.ck_vlc.setIcon(vlc_ok)
        else:
            vlc_no = QtGui.QIcon()
            vlc_no.addPixmap(QtGui.QPixmap("imagenes/vlc.png"))
            self.vskytube.ck_vlc.setIcon(vlc_no)

    def social_google(self):
        webbrowser.open('https://plus.google.com/114802605768559072519')

    def social_facebook(self):
        webbrowser.open('https://www.facebook.com/xskylarx')

    def social_twitter(self):
        webbrowser.open('https://www.twitter.com/xskylarx')


    def folder(self):
        if 'win32' or 'win64' in self.sistema():
            perfil = (os.path.join (os.environ['USERPROFILE'],'videos'))
            self.process.start('explorer ' + str(perfil))
        if 'darwin' in self.sistema():
            perfil = (os.path.join (os.environ['HOME'],'Movies'))
            self.process.start('open ' + str(perfil))
        if 'linux' in self.sistema():
            perfil = (os.path.join (os.environ['HOME'],'Movies'))
            self.process.start('xdg-open "' + perfil + '"')




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
            self.resize(489,48)
            QtGui.QMessageBox.about(self,'Empezando Descarga ... ','La descarga puede tardar varios minutos, dependiendo de tu conexion ...')
            global url
            if 'win32' or 'win64' in self.sistema():
                os.system('skytubec.exe ' + url + ' ' + self.formato())
            if 'darwin' in self.sistema():
                os.system('python3 skytubec.py ' + url + ' ' + self.formato())
            if 'linux' in self.sistema():
                os.system('xterm -e "skytubec ' + url + ' ' + self.formato() + '"')
            self.setclipboard()
            self.vskytube.lineEdit.clear()
            QtGui.QMessageBox.about(self,'Descarga Finalizada', ' Tu descarga Finalizo')
            self.crea_directorio()
            self.resize(880,321)
            self.muestra()
        except Exception as e:
            QtGui.QMessageBox.about(self,'Error Descarga', str(e))


    def sistema(self):
        return sys.platform

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
        self.vskytube.groupBox.setVisible(False)
        self.vskytube.lineEdit.clear()


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

            if os.path.isfile('/tmp/skytube.jpg'):
                os.remove('/tmp/skytube.jpg')

            item = self.vskytube.lst_encola.currentItem()
            url = item.text()

            video = Pafy(url)
            best = video.getbest(preftype=self.formato())
            self.vskytube.lbl_calidad.setText(best.resolution + ' Extencion: ' + best.extension)

            self.vskytube.groupBox.setTitle(video.title)
            self.vskytube.lbl_autor.setText(video.author)
            self.vskytube.lbl_duracion.setText(video.duration)
            self.vskytube.lbl_id.setText(video.videoid)
            self.vskytube.lbl_rating.setText(str(video.rating))
            self.vskytube.lbl_visto.setText(str(video.viewcount))
            self.vskytube.btn_valida_2.setVisible(False)

            url = video.thumb
            if 'win32' or 'win64' in self.sistema():
                file = ('skytube.jpg')
            if 'linux' in self.sistema():
                file = ('/tmp/skytube.jpg')

            urllib.request.urlretrieve(url, file)

            if 'win32' or 'win64' in self.sistema():
                img = (os.path.dirname(sys.executable) + '\skytube.jpg')
            if 'linux' in self.sistema():
                img = ('/tmp/skytube.jpg')

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
            self.resize(585,121)
            self.vskytube.lbl_imagen.setText('sin imagen')
            if os.path.isfile(os.path.dirname(sys.executable)+ '\\skytube.jpg'):
                os.remove(os.path.dirname(sys.executable) + '\\skytube.jpg')

            if os.path.isfile('/tmp/skytube.jpg'):
                os.remove('/tmp/skytube.jpg')

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

            self.vskytube.groupBox.setTitle(video.title)
            self.vskytube.lbl_autor.setText(video.author)
            self.vskytube.lbl_duracion.setText(video.duration)
            self.vskytube.lbl_id.setText(video.videoid)
            self.vskytube.lbl_rating.setText(str(video.rating))
            self.vskytube.lbl_visto.setText(str(video.viewcount))
            self.resize(579,288)
            self.vskytube.btn_valida_2.setVisible(True)



            url_img = video.thumb
            if 'win32' or 'win64' in self.sistema():
                file = ('skytube.jpg')
            if 'linux' in self.sistema():
                file = ('/tmp/skytube.jpg')
            urllib.request.urlretrieve(url_img, file)
            if 'win32' or 'win64' in self.sistema():
                img = (os.path.dirname(sys.executable) + '\skytube.jpg')
            if 'linux' in self.sistema():
                img = ('/tmp/skytube.jpg')


            self.vskytube.lbl_imagen.setPixmap(QtGui.QPixmap(img))
        except Exception as e:
            QtGui.QMessageBox.about(self,'Error SkyTube ', ' No existe el video favor de verificar.')
            QtGui.QMessageBox.about(self,'Error SkyTube ', str(e))

def main():
    app = QtGui.QApplication(sys.argv)
    vskytube = v_skytube()
    vskytube.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


