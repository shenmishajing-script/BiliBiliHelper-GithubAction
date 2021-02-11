# BiliBiliHelper Python Version
# Copy right (c) 2019-2020 TheWanderingCoel

import os
import sys
import json

from configobj import ConfigObj

if os.path.exists(sys.path[0] + "/Conf/Account.json"):
    account = open(sys.path[0] + "/Conf/Account.json").read()
    config = open(sys.path[0] + "/Conf/BiliBiliHelper.json").read()
else:
    account = os.environ['ACCOUNT']
    config = os.environ['CONFIG']

account = json.loads(account)
config = json.loads(config)
notification = ConfigObj(sys.path[0] + "/Conf/Notification.conf", encoding = "UTF8")
