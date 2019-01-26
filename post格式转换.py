import os

file_path = os.getcwd()
file_path = r'{}/POST参数转换.txt'.format(file_path)
with open(file_path, 'r', encoding='utf-8-sig') as f:
    for line in f:
        line = '\'' + line.replace(': ', '\': \'').strip() + '\','
        print(line)
