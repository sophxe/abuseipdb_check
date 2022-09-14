#!/usr/bin/env python

import requests
import json

# the API
url = 'https://api.abuseipdb.com/api/v2/check'
api_key = 'YOUR_API_KEY_HERE'

# http headers
headers = {
    'Accept': 'application/json',
    'Key': api_key
}

def readFile(file):
# read from file and put items into an array
    with open(file, mode='r') as ip_list:
        suspect_ips = ip_list.read().splitlines()
        return suspect_ips

def checkAbuseIPDB(suspect_ips):
# loop through suspect_ips and send a http request to abuseipdb, then capture the response inside of response variable
    for ip in suspect_ips:
        query_string = {
            'ipAddress': ip
        } 

        response = requests.request(method='GET', url=url, headers=headers, params=query_string)

        # format the output
        decodedResponse = json.loads(response.text)
        print('IP address',decodedResponse['data']['ipAddress'],'has', decodedResponse['data']['totalReports'], 'reports')


def main():
    input_file = input('Enter filename here (list of IPs split by carriage return): ')
    suspect_ips = readFile(input_file)
    checkAbuseIPDB(suspect_ips)

main()
