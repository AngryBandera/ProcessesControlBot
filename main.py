from telegram.ext import Updater
import subprocess, time, sys

target = ["testingtests"]

targetProcesses = {}

TOKEN = "1714618330:AAEbU_syFg6qkaL4OwSGLQ1o-S5hKCxONRk"

updater = Updater(TOKEN, use_context=True)

processes = subprocess.getstatusoutput('ps -ef|grep python')[1].split("\n")

procCount = 0
def getProcesses():
    return subprocess.getstatusoutput('ps -ef|grep python')[1].split("\n")

def getPath(name):
    path = subprocess.getstatusoutput(f'ps -ef | grep "{name}" |grep -v grep| awk ''{print $2}'' | xargs pwdx')[1]

for process in processes:
    for target in target:
        if target in process:
            path = getPath(target)
            targetProcesses[target] = path
            procCount+=1
            continue

if procCount<len(target):
    print("Start target processes first")
    sys.exit()

while True:
    existedProc = targetProcesses
    processes = getProcesses()
    for process in processes:
        if process in existedProc.keys():
            del existedProc[process]
    for process in existedProc.keys():
        path = existedProc[process]
        cmd = f"python3 {path}"
        subprocess.Popen(cmd, shell=False)

    time.sleep(1)
