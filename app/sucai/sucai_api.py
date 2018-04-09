#coding: utf-8
#zhanghongfei 2018-04-03

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import logging
from flask import Flask,Blueprint,render_template,send_from_directory,request,send_file
import json,time
from . import sucai_api
import os
from app import app
from _index import data
from _fix_index import _fixdata
from _total_info import _total_info

#logging.basicConfig(level=logging.DEBUG,
#        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#        datefmt='%a,%d %b %Y %H:%M:%S',
#        filename='./house.log',
#        filemod='a')

@sucai_api.route('/',methods=['GET','POST'])
def allinfo():
    style=request.args.get('style','tuijian')
    page=int(request.args.get('page','0'))
    total=len(_fixdata[style])
    p=total/20 + 1
    f_page = 0 if page==0 else page-1
    n_page = page if page==p-1 else page+1
    return render_template('/sucai/index.html',f_page=f_page,n_page=n_page,page=page+1,p=p,imglist=_fixdata[style][page*20:page*20+20],dirname=style)

@sucai_api.route('/down/<id>')
def down_img(id):
    print id
    for style in _fixdata:
        for item in _fixdata[style]:
            if str(item['id'])==id:
                dirpath=os.path.join(app.root_path,'static/sucai/img/'+style)
                if item['filename'].split('.')[-1]=='svg' or item['filename'].split('.')[-1]=='SVG':
                    mimetype='image/svg+xml'
                else:
                    mimetype=None
                return send_file(dirpath+'/'+item['filename'],mimetype=mimetype)
    return 'not found'

@sucai_api.route('/down_thumb/<id>')
def down_thumb_img(id):
    print id
    for style in _fixdata:
        for item in _fixdata[style]:
            if str(item['id'])==id:
                dirpath=os.path.join(app.root_path,'static/sucai/img/'+style)
                if item['filename'].split('.')[-1]=='svg' or item['filename'].split('.')[-1]=='SVG':
                    mimetype='image/svg+xml'
                else:
                    mimetype=None
                return send_file(dirpath+'/thumb_'+item['filename'],mimetype=mimetype)
    return 'not found'

@sucai_api.route('/api',methods=['GET','POST'])
def api():
    style=request.args.get('style','tuijian')
    length=int(request.args.get('length','20'))
    page=int(request.args.get('page','1'))-1
    d=_fixdata[style][page*20:page*20+length]
    return_data=[]
    for i in d:
        new_i={}
        for item in data:
            if i['id']==item['id']:
                new_i['id']=i['id']
                new_i['url']='http://47.92.145.29:8900/sucai_api/down/'+str(i['id'])
                new_i['height']=item['height']
                new_i['width']=item['width']
                new_i['filename']=item['filename']
                new_i['style']=item['style']
                new_i['purpose']=item['purpose']
                return_data.append(new_i)
    return json.dumps(return_data)

@sucai_api.route('/info',methods=['GET','POST'])
def info():
    return json.dumps(_total_info)
