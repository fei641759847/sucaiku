## 素材库API说明

## 图片分类

* url示例

http://47.92.145.29:8900/sucai_api/info


* 输出结果说明

<pre>
{
	"info": 0,            //查询信息正确为0，其它暂未定义
	"type": {             //所有的分类
		"img": {          //素材类型：图片 
			"sucai": [    //图片类型下的二级分类：素材
				{"count": 136, "name": "xiantiao_sc","ch":"\u7ebf\u6761"}, 
				...       //count：数量统计，name：详情接口中参数style对应的值,ch：中文名
			], 
			"background": [  //图片类型下的二级分类：背景
				{"count": 80, "name": "tuijian_bj", "ch": "\u63a8\u8350"}, 
				...
			], 
			"img": [   //图片类型下的二级分类：图片
				{"count": 159, "name": "canyin", "ch": "\u9910\u996e"}, 
				...
			]
		}
	}
}
</pre>



## 图片列表

* url示例

http://47.92.145.29:8900/sucai_api/api?style=canyin&page=1&length=20

* 输入数据字段说明：

参数名|类型|范围|说明
---|---|---|---
style|string||info接口中能查到的name的值，默认为推荐
page|int||数据的起始页，每页为20条，默认从第一页开始，可不加该参数
length|int||获取数据条数，默认为20条

* 输入数据举例

<pre>
[
	{
		"style": "canyin",   //类型，对应info查出来的name
		"url": "http://47.92.145.29:8900/sucai_api/down/2523",  //地址
		"filename": "5a05633ec013f.png",   //文件名
		"width": 80,         //图片宽度
		"purpose": "img",    //对应info输出中图片类型下的二级分类
		"height": 48,        //图片高度
		"id": 2523           //图片id
	},
	...
]                
</pre>

##其它

*缩略图地址

示例：http://47.92.145.29:8900/sucai_api/down_thumb/2523

说明：将详细图片信息中的url中/down/改成/down_thumb/即可
