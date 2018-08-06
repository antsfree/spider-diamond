# /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from multiprocessing import cpu_count, Pool


def run_process(url):
    print(url)


if __name__ == '__main__':
    pool = Pool(cpu_count())
    for i in range(1, cpu_count() + 1):
        pool.apply_async(run_process, args=(i,))
    pool.close()
    pool.join()
    print('end.')
