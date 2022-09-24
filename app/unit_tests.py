import pytest
import os
import subprocess


hashset = {0:'parent', 1:'owner', 2:'size',3:'month',4:'day',5:'stamp',6:'child', 7: 'permissions'}

def split_response(strings):
        temp = strings.splitlines()
        temp.pop(0)
        temp = [strings.replace('  ',' ') for strings in temp]
        lists=[strings.split(' ') for strings in temp]
        lists = [[level[i] for i in range(3, len(level)) if level[i] != ''] + [level[0]] for level in lists if len(level)>0]
        result = [{hashset[i]: level[i] for i in range(0, len(level)) if len(level)==8 } for level in lists if len(level)==8]
        return result


def test_size():
	strings = subprocess.check_output(['ls', '-lhaf']).decode('utf-8')
	assert len(os.listdir()) <= len(split_response(strings)), "size wrong"


def test_children():
	strings = subprocess.check_output(['ls', '-lhaf']).decode('utf-8')
	test = split_response(strings)
	print(test)
	test = set(level['child'] for level in test if len(level)>0)
	for tester in os.listdir():
		print(tester)
		assert tester in test, "missing children"



def test_hashset():
	strings = subprocess.check_output(['ls', '-lhaf']).decode('utf-8')
	test = split_response(strings)
	for level in test:
		print(len(level))
		assert len(level) == len(hashset), "hashset mismatch"
