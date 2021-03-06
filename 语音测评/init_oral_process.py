# -*- coding: utf-8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。

from tencentcloud.soe.v20180724 import soe_client, models

from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

from transmit_oral_process import transmit
'''
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("Your SecretId", "Your SecretKey")

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "soe.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile

    client = soe_client.SoeClient(cred, "", clientProfile)
    req = models.InitOralProcessRequest()
    req.SessionId = "stress_test_956938"
    req.RefText = "since"
    req.WorkMode = 0
    req.EvalMode = 1
    req.ScoreCoeff = 3.5

    resp = client.InitOralProcess(req)

    # 输出json格式的字符串回包
    print("%s" % resp.to_json_string())

except TencentCloudSDKException as err:
    print("%s" % err)
'''


def init_oral_process(SessionId,RefText,base64_data):
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDxe5GDPX6aonW1G78hyzmLglpeFagr9Vc", "A9uRkpfFZpqb6MQEm48xVaTs0ub3GDtK")

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "soe.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile

    client = soe_client.SoeClient(cred, "", clientProfile)
    req = models.InitOralProcessRequest()
    req.SessionId = SessionId
    req.RefText = RefText
    req.WorkMode = 1
    req.EvalMode = 0
    req.ScoreCoeff = 1.0

    resp = client.InitOralProcess(req)

    # 输出json格式的字符串回包
    print("初始化：%s" % resp.to_json_string())
    transmit(SessionId,base64_data)
