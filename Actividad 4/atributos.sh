if [ -z "$1" ]; then
  echo "Uso: $0 <archivo>"
  exit 1
fi

archivo="$1"

if [ ! -f "$archivo" ]; then
  echo "Error: El archivo '$archivo' no existe."
  exit 1
fi

permisos=$(stat -c "%a" "$archivo")
usuario=$(stat -c "%U" "$archivo")
grupo=$(stat -c "%G" "$archivo")
tamano=$(stat -c "%s" "$archivo")
fecha=$(stat -c "%y" "$archivo")
nombre=$(basename "$archivo")

exec > atributosinfo.txt

echo "Permisos: $permisos"
echo "Usuario: $usuario"
echo "Grupo: $grupo"
echo "Tamaño: $tamano bytes"
echo "Fecha y Hora: $fecha"
echo "Nombre del Archivo: $nombre"
echo "Información guardada en atributosinfo.txt"

echo "José Carlos Arangua de Luna - t03096769 - $(date +%F)"
