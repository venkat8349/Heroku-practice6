# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:24:17 2020

@author: Venkateswara Rao
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())