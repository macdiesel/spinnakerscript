#!/usr/bin/env python

import json

build_info = {'imageId':'ami-bc223sdfd'}
with open('createdami.json', 'w') as outfile:
    json.dump(build_info, outfile)



