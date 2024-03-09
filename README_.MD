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

verificamos en donde esta instalado en este caso con
which pip 
which python 
which pip3
which python3
ejemplo
/mnt/d/Users/hpgus/Desktop/Platzi_Cookiecutter/env/bin/python3
y ahora vamos a instalar conda!!
y creamos otro en env dentro de este con los requeriments
pip freeze > requeriments.txt


