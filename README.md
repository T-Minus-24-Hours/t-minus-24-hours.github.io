# T-24 Website

Available at [http://t-24hrs.ml/](http://t-24hrs.ml)

## Local development instructions

Setup:
 1. [Install Python](https://www.python.org/downloads/)
 2. Open terminal and run `python3 -m pip install Jinja2` (on Windows, you might have to replace `python3` with `py`)

Jinja is a templating engine. I've conveniently wrapped all necessary code into `build-script.py`, so when you want to see what the
website would look like with your changes, just run `python3 build-script.py -o` (this opens a new tab; if you don't want that to
happen, remove the `-o`). The output files are found in `build/`; if you're uploading everything to the actual website, just copy
everything in that directory over.

If you add a new html file, add the filename to the variable called `files` in `build-script.py`. This is necessary if you want the html
file to be copied over. If you add a new image/css/any other static file that doesn't need templating, add its filename to the variable called
`static`. **You must remember to do this or else you're not going to see any changes in the website**.

One last note: if you want to change the template (that is, the navbar styling, the footer, anything that is common to every page), you'll
need to edit `_template.html`. If you want to actually take advantage of the templating system, [RTFD](https://jinja.palletsprojects.com/en/3.1.x/)
(honestly, I need to do that as well).
