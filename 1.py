from random import choice

file = open("phrase ch.txt", "r")
file1 = open("phrase m.txt", "r")
data = file.readlines()
print(choice(data))
file.close
data1 = file1.readlines()
print(choice(data1))
file1.close
