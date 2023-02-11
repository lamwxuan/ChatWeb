# encoding:utf-8

import json
import os
from chatgpt.utils.log import logger
from pathlib import Path

config = {}


def load_config():
    global config
    config_path = "F:\CodeProgram\PYTHON\Django\FinancialWeb\conf.json"
    try:
        config_str = read_file(config_path)
        # 将json字符串反序列化为dict类型
        config = json.loads(config_str)
        logger.info("[INIT] load config: {}".format(config))
    except IOError:
        raise Exception('配置文件不存在，请根据config-template.json模板创建config.json文件')

def get_root():
    return os.path.dirname(os.path.abspath( __file__ ))


def read_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()

# 能帮我写出保持websocket连接的JS代码吗
 
def conf():
    return config