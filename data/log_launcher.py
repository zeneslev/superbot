import subprocess
from time import sleep

subprocess.Popen("python logger.py UST-USD", shell=False)
subprocess.Popen("python logger.py BTC-USD", shell=False)
print('done')

while(True):
    sleep(100)