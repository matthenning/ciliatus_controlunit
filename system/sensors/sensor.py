#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser

import system.log as log


class Sensor(object):

    config = configparser.ConfigParser()
    logger = log.get_logger()
    name = ''
    id = ''

    def __init__(self):
        self.config.read('config.ini')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_sensorreading(self):
        pass
