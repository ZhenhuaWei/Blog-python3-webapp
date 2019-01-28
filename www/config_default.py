#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
开发环境的默认标准配置
需要修改时，修改config_override.py来覆盖某些默认配置
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'password',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
