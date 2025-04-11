with open('3.txt', 'w') as f:
    f.write('And it might not be wise\n')
    f.write('I d still have to try')

with open('3.txt', 'r') as f:
    print(f.read())




# lendo novamente para ver o texto 3
with open('3.txt', 'a') as f:
    f.write('\nWith all the love I have inside')

with open('3.txt', 'r') as f:
    print(f.read())