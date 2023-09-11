from twilio.rest import Client

account_sid = 'ACebebce47d93406a3a4012b895e9d8c7f'
auth_token = 'd60d7dd526abedd263221ceaf2741f26'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+447403938912',
  body='I cant believe this works',
  to='+447707265178'
)

print(message.sid)
