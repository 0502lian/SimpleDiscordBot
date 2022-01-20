"""
@Time ： 2022/1/03 
@Auth ： 28177408@qq.com

"""
import requests
import json
import random
import time
import re
import os


def gen_context():
    context_list = [
        "大家好",
        "我们冲呀",
        "我们学老外的  to the moon!",
        "不要问，就是肝，肝到干不动为止",
        "这是一个好项目，不要落空了",
        "有美女！",
        "一起成为家人，家人们好",
        "飞起",
        "起飞",
        "我也是",
        "嗯嗯",
        "测试性发言",
        "大家好友",
        "嗯啊",
        "酷酷",
        "哪里有美女",
        "当然好呀",
        "真是的",
        "哈哈",
        "嘻嘻",
        "什么呢?",
        "为什么不呢?",
        "不错",
        "肝肝",
        "非常好",
        "我回来去脱单去",
        "谢谢",
        "有大家一起，肝起来就有劲！",
        "感谢大家",
        "不不",
        "大家都来 这里",
        "有意思",
        "非常有趣！！",
        "有点累了",
    ]

    text = random.choice(context_list)
    return text


def chat():
    chanel_list = ["频道ID"]
    authorization_list = [
        "你的授权码",
    ]
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        }
        for chanel_id in chanel_list:

            msg = {
                "content": gen_context(),
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False,
            }
            url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
            try:
                print(url)
                print(header)
                print(json.dumps(msg))
                res = requests.post(url=url, headers=header, data=json.dumps(msg))
                print(res.text)

                time.sleep(1)
                # 删除消息
                result_obj = json.loads(res.text)
                print(result_obj)
                url2 = "https://discord.com/api/v9/channels/{}/messages/{}".format(
                    chanel_id, result_obj["id"]
                )
                requests.delete(url=url2, headers=header)

            except Exception as e:
                print(e)
                pass
            continue
        # time.sleep(random.randrange(1, 3))


if __name__ == "__main__":
    while True:
        try:
            chat()
            sleeptime = random.randrange(1, 5)
            time.sleep(sleeptime)
        except:
            pass
        continue
