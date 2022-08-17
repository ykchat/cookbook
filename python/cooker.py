#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import importlib

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(levelname)s\t%(asctime)s\t%(process)s\t%(name)s\t%(message)s'   
))

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def cook(names):

    for name in names:

        logger.debug(f'START {name}')

        recipe = importlib.import_module(name)

        recipe.title()
        recipe.cook()

        logger.debug(f'END {name}')

if __name__ == '__main__':

    names = [
        'recipes.base',
    ]

    cook(names)

