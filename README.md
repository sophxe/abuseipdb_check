# abuseipdb_check

A simple Python script which uses the AbuseIPDB API to check if an IP address is suspected to be malicious, and returns the number of times the IP has been reported. The script is based off the [AbuseIPDB API documentation](https://docs.abuseipdb.com/?python#check-endpoint) and amended for my own lazy requirements. 

The script takes an input of a file of a list of IP addresses for checking against the AbuseIPDB database. The file must be formatted with each IP address separated by a carriage return and must be in the same directory as the script. An AbuseIPDB API key is required for it to work, which you can place inside the api_key variable. The script makes a simple HTTP GET request to obtain information on previous known reports to AbuseIPDB.

The script is very simple and was just thrown together with the purpose of making my mornings a bit easier.

Sample output:

`IP address 123.123.123.123 has 618 reports  
IP address 123.123.123.124 has 127 reports  
IP address 123.123.123.125 has 450 reports`

The script can easily be amended to return whichever JSON fields you like from the query made to AbuseIPDB, as the script returns the whole JSON object for a given IP address, and then just parses the output to what I needed to see.


# abuseipdb_report

Another simple script to bulk report IP addresses to AbuseIPDB. The script is based off [AbuseIPDB API documentation](https://docs.abuseipdb.com/?python#report-endpoint)

Like abuseipdb_check, it takes an input file of a list of IPs formatted with a carriage return which you have confirmed are malicious. Again it is a very lazy script and just made things easier for me when bulk reporting IPs An AbuseIPDB API key is required for it to work, which you can place inside the api_key variable. The script makes a HTTP POST request to AbuseIPDB to report the malicious IPs.

In the script you are required to input a category in numerical format from the list printed out. Multiple categories can be entered, separate by a comma as instructed

Sample output - successful:

`IP address 123.123.123.123 reported for Web App Attack to AbuseIPDB`

Sample output - error:

`You can only report the same IP address (123.123.123.123) once in 15 minutes.`

Again, script is easily modifiable to return whichever JSON fields are needed from the JSON response.
