# wxcloudrun-flask
[![GitHub license](https://img.shields.io/github/license/WeixinCloud/wxcloudrun-express)](https://github.com/WeixinCloud/wxcloudrun-express)
![GitHub package.json dependency version (prod)](https://img.shields.io/badge/python-3.7.3-green)

微信云托管 python Flask 框架模版，实现简单的计数器读写接口，使用云托管 MySQL 读写、记录计数值。
用于原来是这样公众号后台，实现简单的自动回复功能。

![](https://qcloudimg.tencent-cloud.cn/raw/be22992d297d1b9a1a5365e606276781.png)


## 快速开始
前往 [微信云托管快速开始页面](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/basic/guide.html)，选择相应语言的模板，根据引导完成部署。

## 本地调试
下载代码在本地调试，请参考[微信云托管本地调试指南](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/guide/debug/)

## 实时开发
代码变动时，不需要重新构建和启动容器，即可查看变动后的效果。请参考[微信云托管实时开发指南](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/guide/debug/dev.html)

## Dockerfile最佳实践
请参考[如何提高项目构建效率](https://developers.weixin.qq.com/miniprogram/dev/wxcloudrun/src/scene/build/speed.html)




##  API 文档

POST `/`

请求示例：

```json
{
  "ToUserName": "gh_123abc456def", 
  "FromUserName": "oXabcdefghijklmnopqrstuvwxyz", 
  "CreateTime": 1672531200, 
  "MsgType": "text", 
  "Content": "注册", 
  "MsgId": 12345678901234567
}
```

响应示例：

```json
{
  "ToUserName": "oXabcdefghijklmnopqrstuvwxyz", 
  "FromUserName": "gh_123abc456def", 
  "CreateTime": 1672531200, 
  "MsgType": "text", 
  "Content": "428417fb93077e7772325c96a5813e5f5dfde22c82325a8407bdb496c7b0fa6f40256160e2d0e1f56a91cecf0223a4f4ef264def9e815b3dce49b42bcd45e01c", 
}

```