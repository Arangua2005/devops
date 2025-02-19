#copia_archivos.sh

if [ -z "$1" ]; then
	echo "Uso: $0 <nombre_del_archivo>"
	exit 1
fi
cp ./eventos.txt "$1"
echo "Contenido copiado"

echo "José Carlos Arangua de Luna - t03096769 - $(date +%F)"

