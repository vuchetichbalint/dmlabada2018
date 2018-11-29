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
    body = json.dumps( {'cities': ['Budapest', 'Szeged', 'Debrecen']} )
    conn.request(
    	'POST',
    	'/weather', 
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