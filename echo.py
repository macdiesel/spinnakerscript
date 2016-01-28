#!/usr/bin/env python

import json
import uuid

build_info = {'imageId':str(uuid.uuid4())[-9:]}
with open('createdami.json', 'w') as outfile:
    json.dump(build_info, outfile)



