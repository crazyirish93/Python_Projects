import zipfile
import os
folder = os.path.abspath('C:\\Users\\ecurt\\Documents\\ssh Keys')

def backuptozip(folder):
 folder = os.path.abspath('folder')   
    
number = 1
while True:
    zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zipfilename):
        break
    number = number + 1

print('creating zip %s...' % (zipfilename))

backupZip = zipfile.ZipFile(zipfilename, 'w')

for foldername,subfolders,filenames in os.walk(folder):
    print('adding files')
    backupZip.write(foldername)

    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
       
        backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
        print('done')
                                                              
backuptozip('C:\\Users\\ecurt\\Documents')
