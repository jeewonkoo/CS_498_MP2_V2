import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

s1, s2 = '54.177.95.10:80', '13.57.3.17:80'
# print(s2)
payload = {
		'ip_address1':   s1, # <insert ip address:port of first EC2 instance>,
		'ip_address2':   s2, # <insert ip address:port of secong EC2 instance>,
        'load_balancer' : 'MP-V2-752084824.us-west-1.elb.amazonaws.com',
		# 'load_balancer' : 'SP23-CS498-MP2-617891044.us-west-1.elb.amazonaws.com', # <insert address of load balancer>,
		'submitterEmail':  'jeewonk2@illinois.edu',
		'secret': '6tG7X6i94OAmCjtd' # <insert your secret token from coursera>
		}
print(payload)
r = requests.post(url, data=json.dumps(payload))
print(r)
print(r.status_code, r.reason)
print(r.text)