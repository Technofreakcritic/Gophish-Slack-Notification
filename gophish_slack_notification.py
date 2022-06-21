import requests
from distutils.command.config import config
from gophish import Gophish
from gophish.models import *
import random
import datetime

# GoPhish Config
api_key = '<GOPHISH API KEY>'
api = Gophish(api_key,host='<GOPHISH URL>',verify=True)

summary = api.campaigns.summary(campaign_id=397)
summary_breakdown = summary.stats.as_dict()

payload = '{"text":"*Total emails sent*: %s \n _Clicked_: %s \n *_Submitted data_*: %s"}' % (summary_breakdown['total'],summary_breakdown['clicked'],summary_breakdown['submitted_data'])


response = requests.post(
    '<SLACK WEBHOOK>',
    data = payload
)
print(response.text)
