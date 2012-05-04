import sys
import plivo

arg_list = sys.argv
if len(arg_list) != 3:
	print " Not enough arguments "
	print " Should pass 2 phone numbers as argument "
	sys.exit(0)
else:
	arg_list.pop(0)

auth_id = 'XXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
from_number = 1212121212
ring_url = 'http://http://127.0.0.1:5002/ring_url'
answer_url= 'http://http://127.0.0.1:5002/answer_url'
hangup_url= 'http://http://127.0.0.1:5002/hangup_url'

p = plivo.RestAPI(auth_id, auth_token)


for i in arg_list:
	params = {'to': str(i),	
	'from': str(from_number),
	'ring_url': ring_url,
	'answer_url': answer_url,
	'hangup_url': hangup_url
	}

	response = p.make_call(params)

	if len(response) > 0:
		if response[0] == 200:
			print response[1]," form ",i
		else:
			print response[1]," form ",i
	print

	
	
#'To' : '>'.join(arg_list), for bulkcall
#plivo.bulk_call(call_params)
