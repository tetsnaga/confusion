'''
Downloads confusion datasets from Google Drive (datasets.zip)
'''

import gdown

file_id = '1LX1dEN2kubWVPTRXIkfOXVIs557LkDue'
url = f'https://drive.google.com/uc?id={file_id}'
output = 'datasets.zip'

gdown.download(url, output, quiet=False)