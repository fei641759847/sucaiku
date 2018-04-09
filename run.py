#coding:utf-8
from app import app
from app.sucai import sucai_api

app.register_blueprint(sucai_api,url_prefix='/sucai_api')

if __name__=='__main__':
  app.run()
  #app.run(host='0.0.0.0',port=8900,debug=True)
