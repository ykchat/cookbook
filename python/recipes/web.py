#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import urllib.request
import json
import requests

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def title():

    logger.info('# Http')

def cook():

    def log(report):

        forcast = report['timeSeries'][0]
        point = forcast['timeDefines']

        logger.info(f"天気予報 by {report['publishingOffice']} at {report['reportDatetime']}")
        for area in forcast['areas']:
            logger.info(f"[{area['area']['name']}]")
            for point, whether in zip(forcast['timeDefines'], area['weathers']):
                logger.info(f'{point}: {whether}')

    url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/140000.json'

    ## HTTPリクエスト

    with urllib.request.urlopen(url) as res:

        ## HTTPレスポンス解析

        data = json.loads(res.read().decode('utf-8'))

        log(data[0])

    ## HTTPリクエスト

    res = requests.get(url)

    ## HTTPレスポンス解析

    data = res.json()
    log(data[0])

if __name__ == '__main__':

    title()
    cook()
