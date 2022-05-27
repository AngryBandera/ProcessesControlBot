from telegram.ext import Updater
import subprocess, time, sys, os

f = open('data.txt', 'r')
target, TOKEN, chat_id = f.read().split("|&|")

target = target.split("/")
targets = ""
for t in target:targets+=t+" "

print("Monitoring processes: " + targets)

targetProcesses = {}

errText = "display this help and exit"

try:
    updater = Updater(TOKEN, use_context=True)
except:
    print("Valid token")
    sys.exit()

def getProcesses():
    return subprocess.getstatusoutput('ps -ef|grep python')[1].split("\n")

def getPath(name):
    path = subprocess.getstatusoutput(f'ps -ef | grep "{name}"'+"|grep -v grep| awk '{print $2}' | xargs pwdx")
    return path

for tg in target:
    path = getPath(tg)
    if path[0]!=0 or errText in path[1]:
        print("Enter valid process or start it")
        sys.exit()

    path = path[1].split("\n")[0][7:]

    if "deleted" in path:
        path = path[0:-10]

    targetProcesses[tg] = path

print()
if __name__ == '__main__':
    while True:
        existedProc = targetProcesses.copy()
        processes = getProcesses()
        for process in processes:
            for name in targetProcesses.keys():
                if name in process:
                    if name in existedProc:
                        del existedProc[name]

        for process in existedProc.keys():
            updater = Updater(TOKEN, use_context=True)
            path = existedProc[process]
            text = f"Process {process} is down. Restarting."
            updater.bot.sendMessage(chat_id, text)
            print(text)
            os.system(f"cd /{path} && python3 {process}.py")
        time.sleep(1)
