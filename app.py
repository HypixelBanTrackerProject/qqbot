import subprocess
from alicebot import Bot
import shutil
import os

run_lagrange = not (os.environ.get('QQBOT') == 'external')

os.chdir('/app')

LAGRANGE = os.path.join(os.getcwd(),'lagrange','lagrange')
WEBAPI = ['python','-m','fastapi','run']

shutil.copy('lagrange/appsettings.json','lagrange/config/appsettings.json')

subprocess.Popen(LAGRANGE,cwd='lagrange/config') if run_lagrange else None
subprocess.Popen(WEBAPI,cwd='webapi')
bot = Bot()

if __name__ == '__main__':
    bot.run()