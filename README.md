# EE192 Course Site
Sources for UC Berkeley's ee192 (Mechatronics Design Lab) course wbsite, including handouts and slides. See the live version [here](http://www-inst.eecs.berkeley.edu/~ee192).

## Quickstart
To build, run `python build/scons.py`. This creates a new directory, `site` (ignored by `.gitignore`) which contains the entire website.

## Repository structure
 - `slides/`, `docs/`: for LaTeX `.tex` documents.
   - These are automatically compiled to `.pdf` files and put into `site/slides` or `site/docs`, respectively. There are currently no build rules in place to compile other formats, like `.docx`. Please try to keep the build cross-platform compatible.
 - `files/`: for miscellaneous files, these are directly copied to `site/files`.
 - `src/`: jemdoc files, which are automatically compiled to `.html` and put into site.

## Copyright
This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). Note that this license only covers content created by the authors:

 - `.tex` files, including both documents and slides.
 - `.jemdoc` webpage sources.
 - `.odg` diagram sources.
 - Images created by the authors, including some photos and screenshots.

This license does not apply to resources pulled in from the Internet (which we do not claim copyright over), such as build scripts, some documents, and some images.
