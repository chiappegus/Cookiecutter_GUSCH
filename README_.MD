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

$ python -m cookiecutter https://github.com/platzi/curso-entorno-avanzado-ds --checkout cookiecutter-personal-platzi



¡Está genial! En caso de que alguien lo requiera, acá los pasos para hacerlo:

    Abre una terminal en Deepnote
    Ejecuta: pip install cookiecutter
    Ejecuta: cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science

Para más info: https://drivendata.github.io/cookiecutter-data-science/

requeriments :
arrow==1.3.0
binaryornot==0.4.4
certifi==2024.2.2
chardet==5.2.0
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
contourpy==1.2.0
cookiecutter==2.6.0
cycler==0.12.1
fonttools==4.49.0
idna==3.6
Jinja2==3.1.3
kiwisolver==1.4.5
markdown-it-py==3.0.0
MarkupSafe==2.1.5
matplotlib==3.8.3
mdurl==0.1.2
numpy==1.26.4
packaging==23.2
pillow==10.2.0
Pygments==2.17.2
pyparsing==3.1.1
python-dateutil==2.9.0.post0
python-slugify==8.0.4
PyYAML==6.0.1
requests==2.31.0
rich==13.7.1
six==1.16.0
text-unidecode==1.3
types-python-dateutil==2.8.19.20240106
urllib3==2.2.1




