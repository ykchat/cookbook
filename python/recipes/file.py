#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import os

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def title():

    logger.info('# FIle')

def cook():

    name = os.path.abspath('file.py')

    # 基本情報

    logger.info(f'dir={os.path.dirname(name)}')
    logger.info(f'file={os.path.basename(name)}')
    logger.info(f'size={os.path.getsize(name)}')

    # 行数カウント

    lc = 0
    with open(name, 'r') as file:
        lc = sum(1 for line in file)
    logger.info(f'lc={lc}')

    lc = 0
    with open(name, 'r') as file:
        lc = len(file.readlines())
    logger.info(f'lc={lc}')

    lc = 0
    with open(name, 'r') as file:
        for line in file:
            lc += 1
    logger.info(f'lc={lc}')

if __name__ == '__main__':

    title()
    cook()
