# EE192 Course Site
To build, run 'python build/scons.py'. This creates a new directory, site (ignored by .gitignore) which contains the entire website.
Repository structure:
slides/, docs/: for LaTeX .tex documents. These are automatically compiled to .pdf files and put into site/slides or site/docs, respectively. There are currently no build rules in place to compile other formats, like .docx. Please try to keep the build cross-platform compatible.
files/: for miscellaneous files, these are directly copied to site/files.
src/: jemdoc files, which are automatically compiled to .html and put into site.