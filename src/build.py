import glob
import os


valid_files = set()
for fname in glob.glob('*.jemdoc'):
    print "Building: %s" % fname
    os.system('python jemdoc.py -o ../ %s' % fname)
    valid_files.add(fname[:-7])
for fname in glob.glob('*.css'):
    print "Copying: %s" % fname
    os.system('cp %s ../' % fname)
    
os.chdir('../')
for fname in glob.glob('*.html'):
    if fname[:-5] not in valid_files:
        print "Removing: %s" % fname
        os.system('rm %s' % fname)

print "Setting permissions..."
for fname in glob.glob('*.html'):
    os.system('chmod 0755 %s' % fname)
for fname in glob.glob('*.css'):
    os.system('chmod 0755 %s' % fname)
os.chdir('files')
for fname in glob.glob('*'):
    os.system('chmod 0755 %s' % fname)

print "All done!"
