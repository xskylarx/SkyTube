#!/bin/bash
 
echo " Moviendo SkyTube a /usr/share "
if [ -d /usr/share/skytube ];
then
   echo " Actualizando Carpeta SkyTube"
   sudo rm -r -f /usr/share/skytube
   sudo mv skytube /usr/share
else
   echo " Creando Carpeta SkyTube"
   sudo mv skytube /usr/share
fi

echo " Creando Vinculo Skytube "
if [ -f /usr/bin/skytube ];
then
   echo "Vinculo Existente ...."
else
   sudo ln -s /usr/share/skytube/skytube /usr/bin/skytube
fi

echo "Creando vinculo Skytubec "
if [ -f /usr/bin/skytubec ];
then
   echo " Vinculo Existente ..."
else
   sudo ln -s /usr/share/skytube/skytubec /usr/bin/skytubec
fi

echo "Copiando Skytube a menu aplicaciones "
if [ -f /usr/share/applications/skytube.desktop ];
then
   echo "Aplicacion Skytube  existe... Actualizando"
   sudo rm /usr/share/applications/skytube.desktop
   sudo mv skytube.desktop /usr/share/applications
else
   echo "Moviendo Aplicacion Skytube "
   sudo mv skytube.desktop /usr/share/applications
fi




