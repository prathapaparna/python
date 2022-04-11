import os
#from pathlib import Path

WORKSPACE = os.environ.get('WORKSPACE')
print(WORKSPACE)
filename = '/var/lib/jenkins/workspace/python-job/shebang.sh'
    
directory = "temp"
parent_dir = os.environ.get('WORKSPACE')
path = os.path.join(parent_dir, directory) 
os.mkdir(path) 
print(directory)
print("Directory '% s' created" % directory) 

import requests

url = 'https://pypi.python.org/packages/source/x/xlrd-0.9.4.targz' 
target_path = directory + '/xlrd-0.9.4.tar.gz'
response = requests.get(url, stream=True)

with open(target_path,'wb') as f:
  f.write(response.raw.read())
  print(f)
  
import subprocess

p = subprocess.Popen('touch test.txt', shell=True, stdout=subprocess.PIPE)
stdout, stderr = p.communicate() 
print(stdout)

import os
import sys
my_path = parent_dir + "/test.txt"

if os.path.exists(my_path):
  print("build has failed with exit code")
  sys.exit(-1)



