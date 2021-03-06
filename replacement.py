import os

origin = 'https://www.sheldonl.com/'
replacement = 'https://sheldonldev.github.io/'
folder = './_posts'

fls = os.listdir(folder)

for file in fls:

    # print current files name
    print(file)
    
    path = folder + '/' + file
    with open (path, 'r') as old:
        lines = old.readlines()
        new_lines = []
        for line in lines:
            if line.find(origin) != -1:
                line = line.replace(origin, replacement)
                # print origin content will be replaced, then append to array 
                print(line)
            # store all the content should or should not be replaced
            new_lines.append(line)
    
    # save all the content of the file to a new file
    temp_path = './temp/' + file
    with open (temp_path, 'w') as new:
        for line in new_lines:
            new.write(line)
