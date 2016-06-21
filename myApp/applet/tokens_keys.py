"""The following keys and tokens are necessary to set up the links between
the mSurvey App Engine, the mSurvey Messenger Applet and the client facebook page"""
access_token = "EAAEADYGYYM4BALLYhwbV2ZAGkR1QF5C0TVJZBgFTg3wEWyCUSZALMt0WsanQ8kWWbwLi6GD5vT4WQX" \
                    "m1Q2c56lsd524oCQqFNtq5ERSre5Lavwcw5pbQcelEVnx66Dw2hqpnF7S3988GhYRoxyP7taAeVZCLA" \
                    "1Xufkz259KrbQZDZD"
verify_token = "2318934571"
outgoing_key = "7abdf718bf4f5c537a768d3ac4dfaee8b97818736485e161f82d8b48053df090d0428c83871eaf1b2f2" \
                      "acec582ddfa1107ae2537334fa78eddc601b5662319e7"
incoming_key = "1cab16f7fec92180933bfd4ab0886e98298ef410459c25e12839cc9828c3b37b0b000cb720e8784b8bd" \
               "4f88102529f3eba11a34ca2e6ff9e067a7007e2d5df17"
post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % access_token
