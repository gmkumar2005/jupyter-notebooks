import os

port = int(os.environ.get('JUPYTER_NOTEBOOK_PORT', '8888'))

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = port
c.NotebookApp.open_browser = False
c.NotebookApp.quit_button = False
c.NotebookApp.allow_origin='*'
c.NotebookApp.password=''
c.NotebookApp.notebook_dir='/home/jovyan'
c.NotebookApp.token=''     
c.NotebookApp.allow_root=True

if os.environ.get('NB_PREFIX'):
    c.NotebookApp.base_url = os.environ.get('NB_PREFIX')
 
 

image_config_file = '/opt/app-root/src/.jupyter/jupyter_notebook_config.py'

if os.path.exists(image_config_file):
    with open(image_config_file) as fp:
        exec(compile(fp.read(), image_config_file, 'exec'), globals())
