from subprocess import call
import glob
import os
import shutil

VariantDir('site/docs', 'docs', duplicate=0)
VariantDir('site/slides', 'slides', duplicate=0)
VariantDir('site', 'src', duplicate=0)
VariantDir('site/files', 'files', duplicate=0)
VariantDir('site/images', 'images', duplicate=0)

def jemdoc_build_fn(target, source, env):
  assert len(target) == 1 # It seems there is a single target even using Glob()
  assert len(source) >= 1
  source_dir = os.path.abspath(os.path.dirname(str(source[0]))) + os.sep
  target_dir = os.path.abspath(os.path.dirname(str(target[0]))) + os.sep
  for source_node in source:
    source_file = os.path.basename(str(source_node))
    # TODO: restructure using Popen
    print("JEMDOC %s" % source_file)
    call('cd %(source_dir)s && python ../build/jemdoc.py -o %(target_dir)s %(source_file)s' 
         % {'source_dir': source_dir, 'target_dir': target_dir, 'source_file': source_file}, shell=True)

jemdoc_build = Builder(action = jemdoc_build_fn,
                       suffix = '.html',
                       src_suffix = '.jemdoc')
                       
def copy_fn(target, source, env):
  target_dir = os.path.abspath(os.path.dirname(str(target[0]))) + os.sep
  for source_node in source:
    print("COPY %s" % source_node)
    shutil.copy(str(source_node), target_dir)
    
copy_build = Builder(action = copy_fn)

def odg_build_fn(target, source, env):
  assert len(target) == 1 # It seems there is a single target even using Glob()
  assert len(source) >= 1
  
  for source_node in source:
    # TODO: restructure using Popen
    print("UNOCONV %s" % source_node)
    call('python unoconv/unoconv -f png %(source_file)s' 
         % {'source_file': str(source_node)}, shell=True)

odg_build = Builder(action = odg_build_fn,
                          suffix = '.png',
                          src_suffix = '.odg')

env = Environment(ENV = {'PATH' : os.environ['PATH']})
env.Append(BUILDERS = {'Jemdoc' : jemdoc_build})
env.Append(BUILDERS = {'ODGImage' : odg_build})
env.Append(BUILDERS = {'Copy' : copy_build})

def independent_glob(fn, glob_str, srcdir='', tardir=''):
  files = glob.glob(srcdir + glob_str)
  for file in files:
    fn('site/' + tardir + os.path.relpath(file, srcdir))

if ARGUMENTS.get('unoconv', 0):
  # usage: python build/scons.py unoconv=1
  # Most machines probably don't have OpenOffice Draw, which is that the
  # diagrams are drawn in. Therefore, this step to build the diagrams into
  # images is run only with a special flag.
  # The images should be checked in to the repository.
  # (yes, it's a dirty hack, but it gets stuff working)
  independent_glob(env.ODGImage, 'slides/images*/*.odg')

independent_glob(env.Jemdoc, '*.jemdoc', 'src/', '')
env.Copy(Glob('site/jemdoc.css'))

independent_glob(env.PDF, 'docs/*.tex')
independent_glob(env.PDF, 'slides/*.tex')

independent_glob(env.Copy, 'files/*')
independent_glob(env.Copy, 'images/**/*')
