from fabric.api import *
from fabric.contrib.files import exists
import time

env.user = 'bender'
env.shell = '/bin/bash -c'

# Checkout updated code
def sync(source, destination, time):
  print "===> Ensuring that backup directory exists"
  if not exists('/usr/share/nginx/backups', use_sudo=False, verbose=True):
    print "===> Creating backup directory"
    run("mkdir -p /usr/share/nginx/backups")
  print "===> Backing up destination database"
  run("drush @%s sql-dump --gzip --result-file=../backups/%s.%s.sql --debug" %(destination, destination, time))
  print("===> Syncing FROM %s TO %s" %(source, destination))
  run("drush -y sql-sync @%s @%s --no-ordered-dump --debug" %(source, destination))
