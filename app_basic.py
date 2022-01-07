import requests  # this allows us to send http requests

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

response = requests.get(url)

print('response:', response)  # -> <Response [200]>
print('response status code:', response.status_code)

response_text = response.text
property_wanted = 'Previous Close'

# get the index of the string 'Previous Close', which is the property wanted
property_wanted_idx = response_text.index(property_wanted)
print('Index of string "Previous Close":', property_wanted_idx)  # -> 112322

# get reduced text around our target
# 200 is a guestimate
reduced_text_example = response_text[property_wanted_idx:property_wanted_idx+200]
print('Reduced response text:', reduced_text_example)

# extract the value wanted - we notice that it is located right before a </td> tag
reduced_text_list = response_text[property_wanted_idx:].split('</td>')
print('reduced_text_list[:3]:\n', reduced_text_list[:3])
value_wanted = reduced_text_list[1].split('>')[-1]
print('\nValue wanted: ', value_wanted)
