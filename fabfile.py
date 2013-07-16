from fabric.api import local

def hello():
    print("Hello world")
def test():
    local("python manage.py test polls")
    
def commit():
    local("git add . && git commit")

def push():
    local("git push")

def prepare_deploy():
    test()
    commit()
    push


