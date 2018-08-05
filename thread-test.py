# /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from multiprocessing import Process


def run_process(url):
    print(url)


if __name__ == '__main__':
    p = Process(target=run_process, args=('/api/diamonds',))
    print('Child Process will start')
    p.start()
    p.join()
    print('end.')
