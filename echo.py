#!/usr/bin/env python

import json

build_info = {'ami_id':'ami-123456'}
with open('build_info.json', 'w') as outfile:
    json.dump(build_info, outfile)



