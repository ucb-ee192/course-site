from subprocess import call
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

if ARGUMENTS.get('unoconv', 0):
  # usage: python build/scons.py unoconv=1
  # Most machines probably don't have OpenOffice Draw, which is that the
  # diagrams are drawn in. Therefore, this step to build the diagrams into
  # images is run only with a special flag.
  # The images should be checked in to the repository.
  # (yes, it's a dirty hack, but it gets stuff working)
  for x in os.listdir('slides'):
    if os.path.isfile(os.path.join('slides', x)): continue
    if not x.startswith('images'): continue
    images_dir = os.path.join('slides', x)
    for x in os.listdir(images_dir):
      if os.path.splitext(x)[1] == '.odg':
        env.ODGImage(os.path.join(images_dir, x))

env.Jemdoc(Glob('site/*.jemdoc'))
env.Copy(Glob('site/jemdoc.css'))

env.PDF(Glob('site/docs/*.tex'))
env.PDF(Glob('site/slides/*.tex'))

env.Copy(Glob('site/files/*'))
env.Copy(Glob('site/images/cp1/*'))
