import os
import subprocess
from flask import Flask, jsonify, request
import re

print("This API shows you the list of files within a particular directory.")

directory = None
while directory is None:
    try:
        directory = input("Please enter the directory you wish to query: ")
        os.chdir(directory)
    except ValueError:
        print("Oooooh... I couldn't change to that directory. Could you try again?")
        continue

hashset = {0:'parent', 1:'owner', 2:'size',3:'month',4:'day',5:'stamp',6:'child', 7: 'permissions'}

def split_response(strings):
        temp = strings.splitlines()
        temp.pop(0)
        temp = [strings.replace('  ',' ') for strings in temp]
        lists=[strings.split(' ') for strings in temp]
        lists = [[level[i] for i in range(3, len(level)) if level[i] != ''] + [level[0]] for level in lists if len(level)>0]
        result = [{hashset[i]: level[i] for i in range(0, len(level)) if len(level)==8 } for level in lists if len(level)==8]
        return result

def json_dict(directory,path, data):
	result = {}
	result[directory+path]=data
	return jsonify(result)


app = Flask(__name__)

@app.route('/')
def basicget():
	return jsonify(split_response(subprocess.check_output(['ls', '-lhaf']).decode('utf-8')))
@app.route('/<file>')
def get_files(file):
	os.chdir(file)
	data = split_response(subprocess.check_output(['ls', '-lhaf']).decode('utf-8'))
	os.chdir(directory)
	return json_dict(directory, file,data)
@app.route('/<file>/<subfile>')
def get_subfiles(file, subfile):
	path = f'{file}/{subfile}'
	os.chdir(path)
	data = split_response(subprocess.check_output(['ls', '-lhaf']).decode('utf-8'))
	os.chdir(directory)
	return json_dict(directory, path, data)

app.run(port=5000)

