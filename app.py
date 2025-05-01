import subprocess
from alicebot import Bot
import shutil
import os
from pypdl import Pypdl
import tarfile

run_lagrange = not (os.environ.get('QQBOT') == 'external')

os.chdir('/app')

LAGRANGE = os.path.join(os.getcwd(),'lagrange','config','lagrange')
WEBAPI = ['python','-m','fastapi','run']

shutil.copy('lagrange/appsettings.json','lagrange/config/appsettings.json')

if run_lagrange and not os.path.exists(LAGRANGE):
    dl = Pypdl()
    dl.start('https://github.com/LagrangeDev/Lagrange.Core/releases/download/nightly/Lagrange.OneBot_linux-x64_net9.0_SelfContained.tar.gz','lagrange/config/lagrange.tar.gz')
    with tarfile.open('lagrange/config/lagrange.tar.gz') as tar:
        member = tar.getmember('./Lagrange.OneBot/bin/Release/net9.0/linux-x64/publish/Lagrange.OneBot')
        member.name = 'lagrange'
        tar.extract(member,'lagrange/config')
    os.remove('lagrange/config/lagrange.tar.gz')

subprocess.Popen(LAGRANGE,cwd='lagrange/config') if run_lagrange else None
subprocess.Popen(WEBAPI,cwd='webapi')
bot = Bot()

if __name__ == '__main__':
    bot.run()