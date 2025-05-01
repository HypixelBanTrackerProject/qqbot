import subprocess
from alicebot import Bot
import shutil

LAGRANGE = './lagrange/lagrange'
WEBAPI = 'fastapi run'

shutil.copy('lagrange/appsettings.json','lagrange/config/appsettings.json')

subprocess.Popen(LAGRANGE,cwd='lagrange/config')
subprocess.Popen(WEBAPI,cwd='webapi')
bot = Bot()

if __name__ == '__main__':
    bot.run()