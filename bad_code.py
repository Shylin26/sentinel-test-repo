import os
import subprocess

password = "admin123"
api_key = "sk-1234567890abcdef"

def execute_command(user_input):
    os.system(user_input)

def get_user(id):
    query = "SELECT * FROM users WHERE id = " + id
    return query

def process(data):
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            result.append(data[i] + data[j])
    return result

x = 1
y = 2
z = x+y
print(z)
