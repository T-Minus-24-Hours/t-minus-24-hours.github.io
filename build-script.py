#!/mnt/c/WINDOWS/py.exe
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from shutil import copy
import webbrowser as wb
import os
import sys

env = Environment(
        loader = FileSystemLoader('.'),
        autoescape = select_autoescape()
)

files = 'about-us.html contact-us.html donate.html index.html updates.html new.html'.split()
static = 'pradhyum.jpg rand.jfif templogo.png weblogo.png favicon.png athmik.png athmik-a.jpg james.jpg liann.jpg pradhyum_actual.jpg \
athmik-actual.JPG favicon.png sendmail.php features.css s.css'.split()
output_dir = Path('build')
if not output_dir.exists():
    output_dir.mkdir()

for filename in files:
    with open(output_dir / filename, 'w') as output:
        output.write(env.get_template(filename).render())

for filename in static:
    copy(filename, output_dir / filename)

print('\033[0;32mSuccess!\033[0m')
if sys.argv[1:] == ['-o']:
    wb.open('file://' + os.path.realpath('build/index.html'))
