#coding:utf-8

import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

from fabric.state import env

from essay.tasks import build
from essay.tasks import deploy
#from essay.tasks import nginx
#from essay.tasks import supervisor

env.GIT_SERVER = 'https://github.com/'  # ssh地址只需要填：github.com
env.PROJECT = 'essay_demo'
env.BUILD_PATH = '~/buildspace'
env.PROJECT_OWNER = 'EssayTech'
env.DEFAULT_BRANCH = 'master'
env.PYPI_INDEX = 'http://127.0.0.1:10110/simple'

######
# deploy settings:
env.PROCESS_COUNT = 2  #部署时启动的进程数目
env.roledefs = {
    'build': ['vagrant@127.0.0.1:2202'],  # 打包服务器配置
    'dev': ['vagrant@127.0.0.1:2201'],
}

env.VIRTUALENV_PREFIX = '/home/vagrant/essay_demo'
env.SUPERVISOR_CONF_TEMPLATE = os.path.join(PROJECT_ROOT, 'conf', 'supervisord.conf')

#根据工程确定项目编号, 不同环境保证监听不同的端口
PROJECT_NUM = 88
env.VENV_PORT_PREFIX_MAP = {
    'a': '%d0' % PROJECT_NUM,
    'b': '%d1' % PROJECT_NUM,
    'c': '%d2' % PROJECT_NUM,
    'd': '%d3' % PROJECT_NUM,
    'e': '%d4' % PROJECT_NUM,
    'f': '%d5' % PROJECT_NUM,
    'g': '%d6' % PROJECT_NUM,
    'h': '%d7' % PROJECT_NUM,
    'i': '%d8' % PROJECT_NUM,
}
# nginx配置
###########

# 切换nginx环境
env.NGINX_SWITCH_CONF = '/etc/nginx/extra/nginx.conf'
# nginx启动配置文件
env.NGINX_CONF = '/etc/nginx/extra/nginx.conf'
env.NGINX_BIN = '/usr/sbin/nginx'

env.SWITCH_VERSION_MAP = {
    'a': 'upstreamA',
    'b': 'upstreamB',
}

