import zipfile
import os
#test
def backuptozip()

folder = os.path.abspath('C:\Users\ecurt\OneDrive\Documents\Python\test')

number = 1
while True:
    zipfilename = os.path.basename(folder) + '_' + str (number) + '.zip'
    if not os.path.exists(zipfilename):
        break
    number = number + 1
backuptozip('C:\Users\ecurt\OneDrive\Documents\Python')    
