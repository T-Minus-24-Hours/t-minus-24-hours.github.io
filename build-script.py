#!/mnt/c/WINDOWS/py.exe

###############################################################
### PARAMETERS ################################################
###############################################################

files = 'about-us.html contact-us.html donate.html index.html updates.html'.split()
static = 'pradhyum.jpg weblogo.png favicon.png athmik-a.jpg james.jpg liann.jpg nick.jpg blank-profile.png quill2.jpg kennen.jpg'.split()
stylesheet = 'style.scss'    # Currently only using a unified stylesheet
manual_copy = {
    'node_modules/bootstrap/dist/js/bootstrap.bundle.min.js': 'bootstrap.bundle.min.js'
}

###############################################################
### LOGIC #####################################################
###############################################################

FAILURE = lambda s: print(f'\033[0;31m{s}\033[0m')
SUCCESS = lambda s: print(f'\033[0;32m{s}\033[0m')

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    FAILURE("Jinja is not installed.")
    exit(1)
from pathlib import Path
from shutil import copy, which
import webbrowser as wb
import os     # subprocess doesn't work on my system for some reason
import sys

if not which("sass"):
    FAILURE('Sass is not installed. See https://sass-lang.com/install for more details.')

env = Environment(
        loader = FileSystemLoader('.'),
        autoescape = select_autoescape()
)

output_dir = Path('build')
if not output_dir.exists():
    output_dir.mkdir()

error_count = 0

for filename in files:
    try:
        with open(output_dir / filename, 'w') as output:
            output.write(env.get_template(filename).render())
        SUCCESS(f'Template success at {filename}')
    except Exception as e:
        FAILURE(f'Template failure at {filename}')
        error_count += 1

for filename in static:
    try:
        copy(filename, output_dir / filename)
        SUCCESS(f'Copy success at {filename}')
    except Exception as e:
        FAILURE(f'Copy failure at {filename}')
        error_count += 1

for from_, to_ in manual_copy.items():
    try:
        copy(from_, output_dir / to_)
        SUCCESS(f'Manual copy success at {from_}')
    except Exception as e:
        FAILURE(f'Manual copy failure at {from_}')
        error_count += 1

if '-ns' not in sys.argv:
    print('Compiling stylesheets...', end='\r')
    error_count += bool(os.system(f'sass {stylesheet} build/styles.css'))
    SUCCESS("Stylesheets compiled        ")

print()
if error_count == 0:
    SUCCESS('Success!')
else:
    FAILURE(f'{error_count} mistake(s) recorded. Don\'t trust the build files.')

if '-o' in sys.argv:
    wb.open('file://' + os.path.realpath('build/index.html'))
    print('Opened index.html')
