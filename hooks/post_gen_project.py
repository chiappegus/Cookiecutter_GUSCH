import subprocess

from datetime import datetime 

now = datetime.now()

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR:_>100}Almost done!")
print(f"{MESSAGE_COLOR:#<100}Almost done!")
print(f"{MESSAGE_COLOR:|^100}Almost done!")
print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")


project_slug = "{{ cookiecutter.project_slug }}"

print(f"{MESSAGE_COLOR}Se esta terminó  el proyecto {project_slug} , siendo las {now:%c}  ")
#
