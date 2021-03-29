import os

dir = r'C:\Users\khcho\Desktop\nutrients\parsing\moved\succesively'

# value들만 추려내는 과정

for file in os.listdir(dir):
    if f"final_{file}" not in os.listdir(dir):
        with open(f'{dir}\{file}', 'r') as fo:    
                    lines = fo.readlines()
                    line_length = len(lines)
                    headers = []
                    values = [] 
                    for num in range(len(lines)):
                        splited = lines[num].split(' ')
                        headers.append(splited[0])
                        values.append(splited[1])
 
                
    with open(f"final_{file}", 'a') as fw:
        for header in headers:
            fw.write(header + ' ')
        fw.write('\n')
        for value in values:
            fw.write(value + ' ')