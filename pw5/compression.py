import os
from zipfile import ZipFile

def get_all_file_paths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            if filename in ['courses.txt', 'students.txt', 'marks.txt']:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

    return file_paths

directory = '/home/vietah/Documents/AdvancedP/pw5'
file_paths = get_all_file_paths(directory)
print('Following files will be zipped:')
for file_name in file_paths:
    print(file_name)

with ZipFile('students.dat', 'w') as zip:
    for file in file_paths:
        zip.write(file)

print('All files zipped successfully!')

file_zip = 'students.dat'
with ZipFile(file_zip, 'r') as zip:
    zip.printdir()
    print('Extracting all files now ...')
    zip.extractall()
    print('Done!')