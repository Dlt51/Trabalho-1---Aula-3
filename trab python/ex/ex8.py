f = open("8.txt", "w+")

text = ["i'm", "so", "alive"]

for l in text:
    f.write(l)
    f.write("\n")
f.close()






# lendo novamente para só ver o texto 
with open('8.txt', 'r') as f:
    print(f.read())