import subprocess
from alicebot import Bot

LAGRANGE = './lagrange/lagrange.exe'
WEBAPI = 'fastapi run'

subprocess.Popen(LAGRANGE,cwd='lagrange/config')
subprocess.Popen(WEBAPI,cwd='webapi')
bot = Bot()

if __name__ == '__main__':
    bot.run()