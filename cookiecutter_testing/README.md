# cookiecutter testing 

By: gusSoft.

Version: 0.1.0

do somethings cool

## Prerequisites

- [Anaconda](https://www.anaconda.com/download/) >=4.x
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
activate cookiecutter_testing
```

or 

```bash
mamba env create -f environment.yml
activate cookiecutter_testing
```

## Project organization

    cookiecutter_testing
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-jvelezmagic-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---
Project created for demonstration purposes for the course "[Personalización Avanzada de Entorno para ciencia de Datos]()" by [Platzi](https://platzi.com/) - [@jvelezmagic](https://jvelezmagic.com/).


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



pip freeze > ../requeriments.txt


¡Está genial! En caso de que alguien lo requiera, acá los pasos para hacerlo:

    Abre una terminal en Deepnote
    Ejecuta: pip install cookiecutter
    Ejecuta: cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science

Para más info: https://drivendata.github.io/cookiecutter-data-science/