#!/bin/bash
#
# Wrapper script for our fabfile to be called from Jenkins
#

# Where our fabfile is
FABFILE=/usr/local/bin/drush_sync/fabfile.py

HOST=$1
SOURCE=$2
DESTINATION=$3
TIME=`date +%Y%m%d%H%M%S`

if [ -z $HOST ] || [ -z $SOURCE ] || [ -z $DESTINATION ]
then
  echo "Missing arguments! Exiting"
  exit 1
fi

fab -f $FABFILE -H $HOST sync:source=$SOURCE,destination=$DESTINATION,time=$TIME || exit 1
