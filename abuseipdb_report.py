#!/usr/bin/env python

import requests
import json

url = 'https://api.abuseipdb.com/api/v2/report'
api_key = 'YOUR_API_KEY_HERE'


headers = {
        'Accept': 'application/json',
        'Key': api_key
}
s
categories = {'1': 'DNS Compromise', '2': 'DNS Poisoning', '3': 'Fraud Orders', '4': 'Ddos Attack', '5': 'FTP Brute Force', '6': 'Ping of Death', '7': 'Phishing', '8': 'Fraud Voip', '9': 'Open Proxy', '10': 'Web Spam', '11': 'Email Spam', '12': 'Blog Spam', '13': 'VPN IP', '14': 'Port Scan', '15': 'Hacking', '16': 'SQL Injection', '17': 'Spoofing', '18': 'Brute-Force', '19': 'Bad Web Bot', '20': 'Exploited Host', '21': 'Web App Attack', '22': 'SSH', '23': 'IoT Targeted' }

def readFile(file):
    with open(file,mode='r') as ip_list:
        suspect_ips = ip_list.read().splitlines()
        return suspect_ips
        
# this uses the input for categories to find the matching description in the categories dictionary
def getComment(categories, categories_list):
    input_list = []
    for key, value in categories.items():
        if key in categories_list:
            input_list.append(value)
        else:
            continue
    return ','.join(input_list)

def reportAbuseIPDB(suspect_ips):
    for ip in suspect_ips:
        comment = ''
        while comment == '':
            suspect_categories = input(f'Enter categories separated by comma for IP address {ip} e.g. 18,20: ')     
	# suspect_categories = input(f'Enter categories separated by comma for IP address {ip} e.g. 18,20: ')
	# need to convert to a list to iterate through with dictionary values.
            suspect_categories_list = suspect_categories.split(',')
	# commented is converted back to a string for the post_body in the function
            comment = getComment(categories, suspect_categories_list)
        # if comment is still blank after requesting input, caused by an out of range issue, print warning message
            if comment == '':
                print('Please enter a valid category from the list above')   
		
    
        post_string = {
		'ip': ip,
		'categories': suspect_categories,
		'comment': comment
        }
	
        
	
	# format the post response
        response = requests.request(method='POST', url=url, headers=headers, params=post_string)
	
	# format the output
        decodedResponse = json.loads(response.text)

        if 'data' in decodedResponse.keys():
            print('IP address', decodedResponse['data']['ipAddress'], 'reported for', post_string['comment'], 'to AbuseIPDB')
        else:
        # print the error message which is nested in a list within the decodedResponse dictionary
            print(decodedResponse['errors'][0]['detail'])
		
        	
# script logic
        
input_file = 'ips.txt'
suspect_ips = readFile(input_file)
print('_________________________________')
print('Report an IP address to AbuseIPDB')
print('_________________________________')
print('\nCategories of abuse:\n')
for key, value in categories.items():
   print(key, '-', value)
    
reportAbuseIPDB(suspect_ips)
