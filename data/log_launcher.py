import subprocess
from time import sleep

subprocess.Popen('python logger.py UST-USD', shell=True)
subprocess.Popen('python logger.py BTC-USD', shell=True)
subprocess.Popen('python logger.py ETH-USD', shell=True)
print('done')

while(True):
    sleep(100)
