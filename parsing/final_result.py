import os

dir = r'C:\Users\khcho\Desktop\nutrients\parsing\final'

for file in os.listdir(dir):
    with open(f'{dir}\{file}','r') as fr:
        lines = fr.readlines()

    with open('final_result.txt','a') as fa:
        fa.write(lines[1] + '\n')
