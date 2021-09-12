import time

import requests
while True:
    i = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=df0fa438a8cdf3661bcd021419339dd4&symbols=USD,AUD,CAD,PLN,MXN")

    print()
    import json
    a=json.loads(i.text)
    print()
    del a["success"]
    del a["timestamp"]
    with (open("htyui.json","w")) as file:
        json.dump(a, file)
    file.close()
    time.sleep(3)
    print(a)