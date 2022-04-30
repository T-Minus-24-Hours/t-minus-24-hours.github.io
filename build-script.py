from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from shutil import copy

env = Environment(
        loader = FileSystemLoader('.'),
        autoescape = select_autoescape()
)

files = 'about-us.html contact-us.html donate.html index.html updates.html'.split()
static = 'pradhyum.jpg rand.jfif templogo.png weblogo.png favicon.png athmik.png james.png liann.png nate.png'.split()
output_dir = Path('build')
if not output_dir.exists():
    output_dir.mkdir()

for filename in files:
    with open(output_dir / filename, 'w') as output:
        output.write(env.get_template(filename).render())

for filename in static:
    copy(filename, output_dir / filename)

print('\033[0;32mSuccess!\033[0m')
