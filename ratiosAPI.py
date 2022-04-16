
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return data

url = ("https://financialmodelingprep.com/api/v3/income-statement/TMO?apikey=08bf349caa61264932e5ceb37ff6e7dc")

import pandas
a = get_jsonparsed_data(url)

o = pandas.read_json(a)
oh = o.iloc[0,:]
oh.head()