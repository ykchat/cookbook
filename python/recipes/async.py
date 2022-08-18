#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import time
import threading
import asyncio

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def title():

    logger.info('# Async')

def cook():

    secs = [3, 2, 1]

    def sleep(sec):

        logger.info(f'sleep({sec}) started')
        time.sleep(sec)
        logger.info(f'sleep({sec}) exited')

    ## スレッド開始

    threads = list()
    for sec in secs:
        thread = threading.Thread(target=sleep, name='sleep({sec})', args=(sec,))
        thread.start()
        threads.append(thread)

    ## スレッド終了待ち

    for thread in threads: 
        thread.join()

    async def coro_sleep(sec):

        logger.info(f'sleep({sec}) started')
        await asyncio.sleep(sec)
        logger.info(f'sleep({sec}) exited')

    async def gather_coros(secs):

        coros = list()
        for sec in secs:
            coro = coro_sleep(sec)
            coros.append(coro)

        ## コルーチン並列実行/終了待ち

        await asyncio.gather(*coros)

    async def create_tasks(secs):

        ## コルーチン開始

        tasks = list()
        for sec in secs:
            task = asyncio.create_task(coro_sleep(sec))
            tasks.append(task)

        ## コルーチン終了待ち

        for task in tasks:
            await task

    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather_coros(secs))
    loop.run_until_complete(create_tasks(secs))


if __name__ == '__main__':

    title()
    cook()
