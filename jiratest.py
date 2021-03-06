import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		# print(request.get_data())
		params = json.loads(request.get_data(), encoding='utf-8')

		if len(params) == 0:
			return 'No parameter'

		# params_str = ''
		# for key in params.keys():
		# 	params_str += 'key: {}, value: {}<br>'.format(key, params[key])
		print("Project Key: {}".format(params['issue']['fields']['project']['key']))
		print("id: {}".format(params['issue']['id']))
		print("status: {}".format(params['issue']['fields']['status']['name']))
		# print(params_str)
	return 'Hello Worlkd!'

if __name__ == '__main__':
	app.run()
