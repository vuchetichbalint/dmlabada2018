import http.client
import json

api_ip = '127.0.0.1'
api_port = '5000'

def get_response():
    conn = http.client.HTTPConnection(
    	f'{api_ip}:{api_port}'
    	)
    header = {
    'content-type': 'application/json',
    'token' : 'secret_key'
    }
    body = json.dumps( {'x': [[5.1, 3.4, 1.3, 0.2], [6.0, 3. , 5.1, 1.8], [6.9, 2.8, 4.8, 1.4] ]} )
    conn.request(
    	'POST',
    	'/predict', 
    	headers=header,
    	body=body
    )
    res = json.loads(
    	conn.getresponse() \
    	.read() \
    	.decode('utf-8')
    	)

    return res
if __name__ == '__main__':
	print(get_response())