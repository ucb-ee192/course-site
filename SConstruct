from subprocess import call
import os
import shutil

VariantDir('site/docs', 'docs', duplicate=0)
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
    call('cd %(source_dir)s && python ../build/jemdoc.py -o %(target_dir)s %(source_file)s' 
         % {'source_dir': source_dir, 'target_dir': target_dir, 'source_file': source_file}, shell=True)
	
jemdoc_build = Builder(action = jemdoc_build_fn,
                       suffix = '.html',
	                     src_suffix = '.jemdoc')
                       
def copy_fn(target, source, env):
  target_dir = os.path.abspath(os.path.dirname(str(target[0]))) + os.sep
  for source_node in source:
    shutil.copy(str(source_node), target_dir)
    
copy_build = Builder(action = copy_fn)

env = Environment(ENV = {'PATH' : os.environ['PATH']})
env.Append(BUILDERS = {'Jemdoc' : jemdoc_build})
env.Append(BUILDERS = {'Copy' : copy_build})

env.PDF(Glob('site/docs/*.tex'))

env.Copy(Glob('site/files/*'))
env.Copy(Glob('site/images/cp1/*'))

env.Jemdoc(Glob('site/*.jemdoc'))
env.Copy(Glob('site/jemdoc.css'))
