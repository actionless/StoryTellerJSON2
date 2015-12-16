#!/bin/env python

import pystache
import json
import os
import shutil


def main():

    try:
        os.mkdir('./output')
        shutil.copytree('./assets', './output/assets')
    except FileExistsError:
        pass

    with open('./index.mustache') as template_file:
        with open('./data.json') as data_file:
            with open('./output/index.html', 'w') as output_file:
                output_file.write(pystache.render(
                    template_file.read(),
                    json.load(data_file)
                ))


if __name__ == '__main__':
    main()
