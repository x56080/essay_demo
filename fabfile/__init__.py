#coding:utf-8

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

from fabric.state import env

from essay.tasks import build
from essay.tasks import deploy
#from essay.tasks import nginx
#from essay.tasks import supervisor

env.PROJECT = 'essay_demo'
#env.DEPLOY_HOST = '127.0.0.1'
#env.DEPLOY_USER = 'username'
#env.DEPLOY_PATH = '/opt/deploy/'
#env.PROJECT_OWNER = 'EssayTech'
#env.DEFAULT_BRANCH = 'master'
#env.PYPI_INDEX = 'http://pypi.python.org/simple'
