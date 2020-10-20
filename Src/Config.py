# BiliBiliHelper Python Version
# Copy right (c) 2019-2020 TheWanderingCoel

import os
import sys
import json

from configobj import ConfigObj

account = json.loads(os.environ['ACCOUNT'])
config = json.loads(os.environ['CONFIG'])
notification = ConfigObj(sys.path[0] + "/Conf/Notification.conf", encoding = "UTF8")
