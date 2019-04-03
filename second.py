import os
import sys

import requests

if len(sys.argv) < 2:
    print('No folder selected.\nUse command line argument: python second.py <DIR_PATH>')
    sys.exit(0)

dir = sys.argv[1]
if not os.path.isdir(dir):
    print(dir, 'folder does not exist')
    sys.exit(0)

for filename in os.listdir(dir):
    with open(os.path.join(dir, filename), 'rb') as f:
        img_data = f.read()
        requests.post('http://example.com/img', data={'filename': filename, 'data': img_data})



