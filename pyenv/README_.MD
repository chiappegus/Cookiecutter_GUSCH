si estas en linux o wsl debes instalar

    sudo apt install -y python3-venv

Poner cada proyecto en su propio ambiente, entrar en cada carpeta.

    python3 -m venv env

Activar el ambiente

    source env/bin/activate

verifica lo que tengas instalado .

pip freeze 
pasa lo instalado a requeriments.txt

pip freeze >  requeriments.txt

para instalar :

pip install -r requeriments.txt

