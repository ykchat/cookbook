#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def title():

    logger.info('# Loop')

def cook():

    pow = lambda x: x**2

    nums = range(5)

    ## for文

    results = list()
    for num in nums:
        results.append(pow(num))
    logger.info(results)

    ## 内包表記

    results = [pow(num) for num in nums]
    logger.info(results)

    ## map関数

    results = list(map(pow, nums))
    logger.info(results)

if __name__ == '__main__':

    title()
    cook()