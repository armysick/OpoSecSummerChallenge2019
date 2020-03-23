## time curl -XPOST localhost:5000 -d '{"lol":"12341ab40xyzgh"}'

import time

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def hello():
    pwd_array = ['1','2','3','4','1','a','b','4','0','x','y','z','g','h']
    print request.get_json(force=True)
    try:
        jaysun = str(request.get_json(force=True)['lol'])
    except:
        return "NOT OK"

    for idx,o in enumerate(pwd_array):
        try:
            if o == jaysun[idx]:
                time.sleep(0.1)
            else:
                return "NOT OK"
        except IndexError:
            return "NOT OK"

    if len(jaysun)>len(pwd_array):
        return "NOT OK"
    return "OK! \n flag{ticking_away_the_moments_that_make_up_a_dull_day} \n "
