import os
import socket

path = "/home/data"
file2 = open('/home/output/result.txt','w')
file2.write('\n Name: Uttasarga Singh')

files = []
dictionary={}

# a=root, b=directories, c = files
for a, b, c in os.walk(path):
    for file in c:
        if '.txt' in file:
            files.append(os.path.join(a, file))
            f1=os.path.join(a, file)
            num_words = 0
            with open(f1, 'r') as c:
                for line in c:
                    words= line.split()
                    num_words+= len(words)    
                dictionary.update({file:num_words})

for key, value in dictionary.items():
        file2.write("\nThe Document "+str(key)+" Contains "+str(value)+" words")

value = 0
for v in dictionary.values():
	value+=v
file2.write("\n Count of Words Present in All Files : "+str(value))

host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name)
file2.write("\n HOST NAME:  " + host_name)
file2.write("\n IP Address : "+ host_ip) 

file2 = open('/home/output/result.txt', 'r')

entries = file2.read()

print (entries)

file2.close()
