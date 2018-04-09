#coding: utf-8
from _index import data
import json

fix_data={}

for item in data:
    if item['style'] not in fix_data:
        fix_data[item['style']]=[]

for item in data:
    new_item={}
    new_item['id']=item['id']
    new_item['filename']=item['filename']
    fix_data[item['style']].append(new_item)

for i in fix_data:
    print i,len(fix_data[i])
    print fix_data[i][0]

with open('_fix_index.py','w') as f:
    f.write(json.dumps(fix_data))
#print fix_data,len(fix_data)
