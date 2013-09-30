__author__ = 'xskylarx'
# -*- coding: utf-8 -*-

# Python + PyQt4 By Skylar 
#
# Creado: 29 - sep - 2013
#      Por: xskylarx
# xskyofx@gmail.com
#
#v1.2 -> se corrige Bug al recibir simbolos como " | ' <>-_:.,
# Por favor si modificas algo haz referencia al autor.
from pafy import Pafy
import os
import sys

try:
    if len(sys.argv) >= 2:

        url = sys.argv[1]
        video_id = url

        if video_id.split('?v=') == 1:
            video_id = video_id.split('?v=')

        if len(video_id) == 1:

            url= 'http://www.youtube.com/watch?v=' + video_id[1]
        else:

            url= 'http://www.youtube.com/watch?v=' + video_id

        video =Pafy(url)
        os.system('cls')
        print('')
        print('SkyTube Modo Consola =D ... V1.2')
        print('')
        print('')
        print('Tu video ' + video.title + ' se esta descargando ..')
        print('')
        print('')

        best = video.getbest(preftype="mp4")
        titulo = best.title
        titulo = str(titulo).replace('.','')
        titulo = str(titulo).replace('"','')
        titulo = str(titulo).replace(':','')
        titulo = str(titulo).replace('_','')
        titulo = str(titulo).replace('-','')
        titulo = str(titulo).replace(';','')
        titulo = str(titulo).replace('|','')
        titulo = str(titulo).replace("'",'')

        filename = os.path.join (os.environ['USERPROFILE'],'videos') + '\\' + titulo + '.' + best.extension
        best.download(quiet=False, filepath=filename)
        print('Tu video se Descargo Correctamente, lo encuentras en tu carpeta de Videos .. ')
        print('Esta ventana se cerrara en 5 segundos...')
        os.system('ping -n 5 localhost>nul')
        os.system('exit')
    else:
        os.system('cls')
        print('Error en SkyTubeC, no Hay URL de Youtube')
        print('')
        print('Modo de uso:  skytubec http://www.youtube.com/watch?v=QJO3ROT-A4E ')
        os.system('pause>nul')

except Exception as e:
    print('Url Invalida !' + '    ' + e)
    os.system('pause>nul')