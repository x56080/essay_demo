#coding:utf-8

import settings

def main():
    print 'version:', settings.__version__
    print 'git version:', settings.__git_version__
    print 'release time', settings.__release_time__

    print 'hello world'

if __name__ == '__main__':
    main()
