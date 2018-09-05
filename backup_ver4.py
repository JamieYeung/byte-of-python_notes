import time
import zipfile
import os

source = ['/home/jamieyeung/temp/notes']
target_dir = '/home/jamieyeung/temp/backup'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
comment = input('Enter a comment: --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

if not os.path.exists(today):
    os.mkdir(today)

zip_command = 'zipfile.Zipfile({0}, mode="r",compression=ZIP_STORED,allowZip64=True'.format(source)

print(zip_command)
print('Running:')




