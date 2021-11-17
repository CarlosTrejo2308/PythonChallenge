import requests

def getNext(nothing):
    number = nothing.split(' ')[-1]
    return number

req = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
resp = req.text
resp = getNext(resp)

while True:
    try:
        req = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + resp)
        resp = req.text
        resp = getNext(resp)
        print(resp)
    except:
        print(resp)
        break


