#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import subprocess

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def title():

    logger.info('# Command')

def cook():

    command = 'ls'

    ## コマンド実行

    proc = subprocess.Popen(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    ## pid取得

    pid = proc.pid
    logger.info(f'{command}[#{pid}] started')

    ## 実行結果を取得

    out, err = proc.communicate()

    if proc.returncode:
        for line in err.splitlines():
            logger.error(line)
    else:
        for line in out.splitlines():
            logger.info(line)

    logger.info(f'{command}[#{pid}] exited')

if __name__ == '__main__':

    title()
    cook()
