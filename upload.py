#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Upload error pages to CDN


import os

from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import QingStor


def upload():
    access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    config = Config(access_key_id, secret_access_key)
    bucket = QingStor(config).Bucket('datarc-cdn', 'sh1a')

    file_list = [
        '404.html',
        '500.html',
        '503.html',
    ]
    for filename in file_list:
        with open(filename, 'rb') as fi:
            output = bucket.put_object(filename, body=fi)
            print(output.status_code)


if __name__ == '__main__':
    upload()
