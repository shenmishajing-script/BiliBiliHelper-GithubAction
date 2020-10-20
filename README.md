
<p align="center"><img width="300px" src="https://i.loli.net/2018/04/20/5ad97bd395912.jpeg"></p>

[![codebeat][1]][2] [![Downloads][3]][4] [![Version][5]][6]
[![License][7]][8]

[1]: https://codebeat.co/badges/4171ff04-5cff-4bed-8213-b82944e130e6 "Codebeat badge"
[2]: https://codebeat.co/projects/github-com-thewanderingcoel-bilibilihelper-master "Codebeat"
[3]: https://img.shields.io/github/downloads/TheWanderingCoel/BiliBiliHelper/total.svg "All releases badge"
[4]: https://github.com/TheWanderingCoel/BiliBiliHelper/releases/ "All releases number"
[5]: https://img.shields.io/badge/version-v0.0.6-green.svg?longCache=true
[6]: https://github.com/TheWanderingCoel/BiliBiliHelper
[7]: https://img.shields.io/badge/license-GPL%20V3-blue.svg?longCache=true
[8]: https://github.com/TheWanderingCoel/BiliBiliHelper/blob/master/LICENSE

| OS | Windows | macOS | Linux |
| --- | --- | --- | --- |
| Build Status | [![Build Status Windows](http://badges.herokuapp.com/travis.com/TheWanderingCoel/BiliBiliHelper?style=flat-square&env=BADGE=windows&label=Windows&branch=master)](https://travis-ci.com/TheWanderingCoel/BiliBiliHelper) | [![Build Status macOS](http://badges.herokuapp.com/travis.com/TheWanderingCoel/BiliBiliHelper?style=flat-square&env=BADGE=osx&label=macOS&branch=master)](https://travis-ci.com/TheWanderingCoel/BiliBiliHelper) | [![Build Status Linux](http://badges.herokuapp.com/travis.com/TheWanderingCoel/BiliBiliHelper?style=flat-square&env=BADGE=linux&label=Linux&branch=master)](https://travis-ci.com/TheWanderingCoel/BiliBiliHelper) |

# BiliBiliHelper
B 站直播实用脚本Github Action版本

## 功能组件

|plugin              |version  |description   |
|--------------------|---------|--------------|
|AsyncioCurl         |19.03.07 |异步的网络请求组件|
|Auth                |19.03.07 |帐号登录组件    |
|Coin2Silver         |19.03.07 |硬币换银瓜子组件 |
|Curl                |19.03.17 |非异步的网络请求组件|
|Group               |19.03.07 |应援团签到      |
|Silver2Coin         |19.03.07 |银瓜子换硬币    |
|Task                |19.04.06 |每日任务       |


## 环境依赖
|Requirement|
|-------|
|Python 3.6+|
|aiohttp  |
|aiosocksy |
|  rsa    |
|requests[socks] |
|configobj|
| tailer  |

通常使用 `pip` 工具安装依赖。


## 使用指南

 1. Fork项目代码
 2. 根据 Conf/Account.sample.json 和 Conf/BiliBiliHelper.sample.json 为项目设置 ACCOUNT 和 CONFIG 两个 Sercet
 3. 手动运行一下试试是否可以正常运行
 
## 直播间 ID 问题
config 文件中有个 `ROOM_ID` 配置，填写此项可以清空临过期礼物给指定直播间。

通常可以在直播间页面的 url 获取到它
```
http://live.bilibili.com/23058
```

所有直播间号码小于 1000 的直播间为短号，该脚本在每次启动会自动修正，无需关心，


## 感谢
 - BilibiliHelper(php) https://github.com/metowolf/BilibiliHelper
 - blivedm             https://github.com/yjqiang/blivedm
 - bilibili-live-tools https://github.com/yjqiang/bilibili-live-tools
 - bili2.0             https://github.com/yjqiang/bili2.0
 - bilibili-raffle     https://github.com/Billyzou0741326/bilibili-raffle
 - bilibili-live-monitor-js https://github.com/Billyzou0741326/bilibili-live-monitor-js



## License 许可证

本项目基于 GPL V3 协议发布。

本项目的所有代码文件、配置项，除另有说明外，均基于上述介绍的协议发布，具体请看分支下的 LICENSE。

此处的文字仅用于说明，条款以 LICENSE 文件中的内容为准。
