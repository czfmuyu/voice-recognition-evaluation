# voice-recognition-evaluation

使用腾讯云https://cloud.tencent.com/进行语音识别和语音测评的编写。

## 上手指南
以下指南将帮助你在本地机器上安装和运行该项目，进行开发和测试。
1. 请在终端使用`git clone git@github.com:surgarman/voice-recognition-evaluation.git`下载到本地。
2. 或者直接下载zip。

## 目录
* examples
* 语音测评
* 语音识别

---
## examples
使用腾讯云 Python SDK 接入的例子汇总。

## Smart Oral Evaluation-English，SOE-E 腾讯云智聆口语评测（英文版）

腾讯云推出的语音评测产品。英语的口语练习，过去由于只能依赖专业教师听后进行主观评估，成本高，学习时间也难以保证。腾讯云针对此场景推出英文语音评测产品，支持从儿童到成人全年龄覆盖的语音评测，支持单词（词语），句子等多种模式，支持发音准确度（GOP），流利度，完整度，重音准确度等全方位打分机制，专家打分相似度95%以上。

本文件实现了部分测评的功能模块，未对返回参数进行分析和拆解。

## Automatic Speech Recognition，ASR 语音识别

为企业提供极具性价比的语音识别服务。被微信、王者荣耀、腾讯视频等大量内部业务使用，外部落地录音质检、会议实时转写、法庭/审讯记录、语音输入法等多个场景。

本文件实现了通过语音URL方式请求和通过本地语音文件上传方式请求。并且配备了GUI界面模块、录音功能模块和数据库存储模块。

---
## 接入流程

第 1 步： 登录注册
登录腾讯云官网https://cloud.tencent.com/。

第 2 步：实名认证
如果您的腾讯云账号未进行过实名认证，请首先在腾讯云账号中心的 账号信息页面，进行实名认证。

第 3 步：开通服务
实名认证后，进入 腾讯云控制台 ，开通服务。

第 4 步：新建密钥
进入 API 密钥管理页面，点击新建密钥，生成 AppID、SecretId 与 SecretKey，用于 API 调用时生成签名。

第 5 步：进行接入
根据您的需求，使用API/SDK进行接入，推荐使用SDK方式接入。

第 6 步：查看调用
接入后，您可以登录 腾讯云控制台，查看语音识别的各服务调用情况。
