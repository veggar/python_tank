#!/usr/bin/python
# -*- coding: utf-8-*-

from typing import Tuple
from collections import Counter
# import plotly 
# import plotly.graph_objs as go
import matplotlib
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify
import os

import updating_keyword

plt.switch_backend('Agg') 

app = Flask(__name__, static_folder='outputs')

font_path = 'NanumGothic.ttf'


@app.route("/outputs", methods=['GET', 'POST'])
def output():

    fig = updating_keyword.main()

    return fig.to_html()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)

    # curl -X POST -d '{"text": "안녕하세요? 저는 한국교원대학교 나동빈입니다. 여러분들과 함께 다양한 공부를 진행하면서 스터디에 참여하고 싶어요. 한 번 공부를 할 때 제대로 공부를 하는 것이 목표입니다. 공부는 쉽지 않지만 열심히 하다 보면 재미를 느끼고 참여할 수 있을 것 같아요. 이것은 10강 예제이고, 며칠만에 다시 하려니 기억도 안나네요",    "maxCount": 15, "minLength": 2, "words":{"1":{"weight":"7","word":"스터디"},"2":{"weight":"5","word":"참여"},"3":{"weight":"5","word":"분노"},"4":{"weight":"4","word":"치킨" }} "textID":"1"}' -H "Content-Type: application/json" http://10.10.113.22:5000/process
    # curl -X POST -d '{"text": "안녕하세요? 저는 한국교원대학교 나동빈입니다. 여러분들과 함께 다양한 공부를 진행하면서 스터디에 참여하고 싶 어요. 한 번 공부를 할 때 제대로 공부를 하는 것이 목표입니다. 공부는 쉽지 않지만 열심히 하다 보면 재미를 느끼고 참여할 수 있을 것 같아요. 지금 이것은 테스트이고, 며칠 만에 재개하는지 기억도 안나고 있음.",    "maxCount": 15, "minLength": 2, "words":{"1":{"weight":"7","word":"스터디"},"2":{"weight":"5","word":"참여"},"3":{"weight":"5","word":"분노"},"4":{"weight":"4","word":"치킨" }}}' -H "Content-Type: application/json" http://10.10.113.22:5000/process