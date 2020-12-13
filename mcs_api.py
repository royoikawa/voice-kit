import requests
import json
import time
import random

def get_mcs_word():
    url = "https://api.mediatek.com/mcs/v2/devices/D0GyA2Da/datachannels/words/datapoints"
    headers = {"Content-Type":"application/json", "deviceKey":"nOJM4aFkjC980deR"}
    r = requests.get(url,headers=headers)
    print(r.text)

def post_mcs_word(findWords):
    url = "https://api.mediatek.com/mcs/v2/devices/D0GyA2Da/datapoints"
    headers = {"Content-Type":"application/json", "deviceKey":"nOJM4aFkjC980deR"}
    body = {"datapoints":
            [
                {"values":{"value":findWords},"dataChnId":"words"}
                ]
            }
    r = requests.post(url,headers=headers,json=body)
    print(r.text)

def get_mcs_start():
    url = "https://api.mediatek.com/mcs/v2/devices/D0GyA2Da/datachannels/start/datapoints"
    headers = {"Content-Type":"application/json", "deviceKey":"nOJM4aFkjC980deR"}
    r = requests.get(url,headers=headers)
    j = json.loads(r.text)
    status = j["dataChannels"][0]["dataPoints"][0]["values"]["value"]
    return(status)

def post_mcs_start():
    url = "https://api.mediatek.com/mcs/v2/devices/D0GyA2Da/datapoints"
    headers = {"Content-Type":"application/json", "deviceKey":"nOJM4aFkjC980deR"}
    body = {"datapoints":
            [
                {"values":{"value":"off"},"dataChnId":"start"}
                ]
            }
    r = requests.post(url,headers=headers,json=body)
    print(r.text)

def post_mcs_done():
    url = "https://api.mediatek.com/mcs/v2/devices/D0GyA2Da/datapoints"
    headers = {"Content-Type":"application/json", "deviceKey":"nOJM4aFkjC980deR"}
    body = {"datapoints":
            [
                {"values":{"value":""},"dataChnId":"start"}
                ]
            }
    r = requests.post(url,headers=headers,json=body)
    print(r.text)
    
def get_mcs_id():
    url = "https://api.mediatek.com/mcs/v2/devices/D0GyA2Da/datachannels/project_id/datapoints"
    headers = {"Content-Type":"application/json", "deviceKey":"nOJM4aFkjC980deR"}
    r = requests.get(url,headers=headers)
    j = json.loads(r.text)
    pid = j["dataChannels"][0]["dataPoints"][0]["values"]["value"]        
    return(pid)
def clean_mcs_id():
    url = "https://api.mediatek.com/mcs/v2/devices/D0GyA2Da/datapoints"
    headers = {"Content-Type":"application/json", "deviceKey":"nOJM4aFkjC980deR"}
    body = {"datapoints":
            [
                {"values":{"value":""},"dataChnId":"project_id"}
                ]
            }
    r = requests.post(url,headers=headers,json=body)
    print(r.text)

#def main():
    #print(get_mcs_id())
    #post_mcs_start()
#if __name__ == '__main__':
    #main()