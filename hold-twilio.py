# if knife detected send warning text using Twilio
"""NEED TO TEST THIS NOT SURE IT WORKS YET"""

if object_name == "knife":
    account_sid = 'enter_account_sid'
    auth_token = 'enter_auth_code'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Warning, Knife has been detected with " + label + " confidence",
        from_='+19032252880',
        to='+447954052087'
    )

    print(message.sid)