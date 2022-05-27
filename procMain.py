from telegram.ext import Updater
import subprocess, time, sys, os

targets = ""
for t in target:targets+=t+" "

print("Monitoring processes: " + targets)

targetProcesses = {"botsHandler": "opt/feedback/feedbot/SimpleFeedbackBot/botsHandler.py"}

TOKEN = "5363787602:AAEkOHh1HFSXSWeL8wy5LH9cCKqrmSljpXA"
chat_id = 729560932

updater = Updater(TOKEN, use_context=True)

def getProcesses():
    return subprocess.getstatusoutput('ps -ef|grep python')[1].split("\n")

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
            text = f"Process {path} is down. Restarting."
            updater.bot.sendMessage(chat_id, text)
            print(text)
            os.system(f"cd / && python3 {path}")
        time.sleep(1)
