__author__ = 'xskylarx'
# -*- coding: utf-8 -*-
 
# Python + PyQt4 By Skylar 
#
# Creado: 29 - sep - 2013
#      Por: xskylarx
# xskyofx@gmail.com
#
#v1.4 se a単ade compatibilidad con Mac, Windows, Linux, a hora abre el reproductor predeterminado del sistema.
#v1.3 -> se a単ade lista automatica, capturador de enlaces, lista de descargas.
#v1.2 -> se corrige Bug al recibir simbolos como " | ' <>-_:.,
#
# Por favor si modificas algo haz referencia al autor.
from pafy import Pafy
import os
import sys
 
 
try:
    def sistema():
        return sys.platform
 
    if len(sys.argv) >= 1:
        u = sys.argv[1]
        u = str(u).replace('[','')
        u = str(u).replace(']','')
        u = str(u).replace("'",'')
 
 
        for i in u.split(','):
            url = i
            if len(sys.argv) <= 2:
                formato = 'mp4'
            else:
                formato = sys.argv[2]
 
            video_id = url
 
            if video_id.split('?v=') == 1:
                video_id = video_id.split('?v=')
 
            if len(video_id) == 1:
 
                url= 'http://www.youtube.com/watch?v=' + video_id[1]
            else:
 
                url= 'http://www.youtube.com/watch?v=' + video_id
 
 
 
            video =Pafy(url)
            if 'win32' in sistema() or 'win64' in sistema():
                os.system('cls')
            if 'darwin' in sistema():
                os.system('clear')
            if 'linux' in sistema():
                os.system('clear')
            stream = video.getbest(preftype=formato.lower())
            size = stream.get_filesize()
 
            print('           _____ _        _____     _')
            print('          /  ___| |      |_   _|   | |')
            print('          \  --.| | ___   _| |_   _| |__   ___ ')
            print("           `--. \ |/ / | | | | | | | |_ \\ / _ \\")
            print('          /\__/ /   <| |_| | | |_| | |_) |  __/')
            print('          \____/|_|\_\\__,  \_/\__,_|_.__/ \___|')
            print('                       __/ |                   ')
            print('                      |___/                V1.4')
 
            print(" Tu Video se esta descargando ... \n\n\n '{}' [{:,} Bytes]".format(stream.filename, size))
            print("-Resolucion %s; Formato: %s" % (stream.resolution, stream.extension))
            print('\n')
 
 
 
            titulo = stream.title
 
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
            titulo = str(titulo).replace("?",'')
            titulo = str(titulo).replace("多",'')
            titulo = str(titulo).replace("臓",'')
            titulo = str(titulo).replace("[",'')
            titulo = str(titulo).replace("]",'')
            titulo = str(titulo).replace("{",'')
            titulo = str(titulo).replace("}",'')
            titulo = str(titulo).replace("=",'')
            titulo = str(titulo).replace("~",'')
            titulo = str(titulo).replace("<",'')
            titulo = str(titulo).replace(">",'')
 
            if 'win32' in sistema() or 'win64' in sistema():
                filename = os.path.join (os.environ['USERPROFILE'],'videos') + '\\' + titulo + '.' + stream.extension
            else:
                filename = os.path.join (os.environ['HOME'],'Movies') + '/' + titulo + '.' + stream.extension
 
            stream.download(quiet=False, filepath=filename)
        print('Tu video se Descargo Correctamente, lo encuentras en tu carpeta de Videos .. ')
        print('Esta ventana se cerrara en 5 segundos...')
        if 'win32' in sistema() or 'win64' in sistema():
            os.system('ping -n 5 localhost>nul')
            os.system('exit')
        else:
            os.system('logout')
            os.system('sleep 5')
    else:
        if 'win32' in sistema() or 'win64' in sistema():
                os.system('cls')
        if 'darwin' in sistema():
                os.system('clear')
        if 'linux' in sistema():
                os.system('clear')
        print('Error en SkyTubeC, no Hay URL de Youtube')
        print('')
        print('Modo de uso:  skytubec http://www.youtube.com/watch?v=QJO3ROT-A4E ')
        if 'win32' in sistema() or 'win64' in sistema():
            os.system('pause>nul')
 
except Exception as e:
    print('           _____ _        _____     _')
    print('          /  ___| |      |_   _|   | |')
    print('          \  --.| | ___   _| |_   _| |__   ___ ')
    print("           `--. \ |/ / | | | | | | | |_ \\ / _ \\")
    print('          /\__/ /   <| |_| | | |_| | |_) |  __/')
    print('          \____/|_|\_\\__,  \_/\__,_|_.__/ \___|')
    print('                       __/ |                   ')
    print('                      |___/                V1.4')
    print('Hay un Error en la Direccion de Youtube:  \n ' + url + '\n      Por Favor Verifica..')
    print('')
    if 'win32' in sistema() or 'win64' in sistema():
                os.system('ping -n 5 localhost')
    if 'darwin' in sistema():
            os.system('sleep 5')
            os.system('logout')
    if 'linux' in sistema():
            os.system('clear')
    pass