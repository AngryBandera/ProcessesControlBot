from telegram.ext import Updater
import subprocess, time, sys

target = ["testingtests"]

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
    if getPath(tg)[0]!=0:
        print(getPath(tg))
        continue
    path = getPath(tg).split("\n")[0][5:]
    if "deleted" in path:
        path = path[0:-10]
    targetProcesses[tg] = path+f"{target}.py"
    print(path)


if __name__ == '__main__':
    while True:
        existedProc = targetProcesses
        processes = getProcesses()
        for process in processes:
            if process in existedProc.keys():
                del existedProc[process]
        for process in existedProc.keys():
            updater = Updater(TOKEN, use_context=True)
            text = f"Process {path} is down. Restarting."
            updater.bot.sendMessage(chat_id, text)
            path = existedProc[process]
            cmd = f"python3 {path}"
            subprocess.Popen(cmd, shell=False)
        time.sleep(1)
