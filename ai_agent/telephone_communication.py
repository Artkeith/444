```python
import os
from twilio.rest import Client

# Import shared dependencies
from environment_setup import communication_details

# Your Account SID from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

def send_telephone_message(message_body):
    message = client.messages.create(
        to=communication_details['telephone_number'], 
        from_="+12345678901",
        body=message_body)

def receive_telephone_message():
    messages = client.messages.list()
    for record in messages:
        if record.to == communication_details['telephone_number']:
            return record.body
    return None
```