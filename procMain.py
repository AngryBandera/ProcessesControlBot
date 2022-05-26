from telegram.ext import Updater
import subprocess, time, sys, os

target = input("Enter your processes, separated with /: ").split("/")

targets = ""
for t in target:targets+=t+" "

print("Monitoring processes: " + targets)

targetProcesses = {}

TOKEN = "5363787602:AAEkOHh1HFSXSWeL8wy5LH9cCKqrmSljpXA"
chat_id = 729560932

updater = Updater(TOKEN, use_context=True)

def getProcesses():
    return subprocess.getstatusoutput('ps -ef|grep python')[1].split("\n")

def getPath(name):
    path = subprocess.getstatusoutput(f'ps -ef | grep "{name}"'+"|grep -v grep| awk '{print $2}' | xargs pwdx")
    return path

for tg in target:
    path = getPath(tg)
    if path[0]!=0:
        print(path[1])
        continue

    path = path[1].split("\n")[0][7:]

    if "deleted" in path:
        path = path[0:-10]

    targetProcesses[tg] = path+f"/{tg}.py"

print(targetProcesses)

if __name__ == '__main__':
    while True:
        existedProc = targetProcesses
        processes = getProcesses()
        print(processes)
        for process in processes:
            for name in existedProc.keys():
                if name in process:
                    print(process)
                    del existedProc[name]

        for process in existedProc.keys():
            updater = Updater(TOKEN, use_context=True)
            text = f"Process {path} is down. Restarting."
            updater.bot.sendMessage(chat_id, text)
            path = existedProc[process]
            os.system(f"python3 {path}")
        time.sleep(1)
