#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import datetime
import zoneinfo

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def title():

    logger.info('# Base')

def cook():

    ## 変数展開

    name = 'Recipe'

    hello = f'Hello {name}!'
    logger.info(hello)

    ## 現在時刻

    now = datetime.datetime.now(datetime.timezone.utc) 
    logger.info(now.isoformat())

    now = datetime.datetime.now(zoneinfo.ZoneInfo('Asia/Tokyo'))
    logger.info(now.isoformat())

if __name__ == '__main__':

    title()
    cook()
