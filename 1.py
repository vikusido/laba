from random import choice

file = open("phrase.txt", "r")
data = file.readlines()
print(choice(data))
file.close
