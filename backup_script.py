import os
import time

source = ['/Users/ananth/Desktop/']
target_dir = '/Users/ananth/Desktop/Backup_Desktop'

target_file_name = target_dir + os.sep + \
		time.strftime('%Y%m%d%S%M%H') + '.zip'


if not (os.path.exists(target_dir)):
	os.mkdir(target_dir)

zip_command = "zip -r {0} {1}".format(target_file_name,''.join(source))

print("The command is: ",zip_command)

if(os.system(zip_command) == 0):
	print("Executed successfully")
else:
	print("Script failed")
