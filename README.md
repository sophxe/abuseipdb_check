# abuseipdb_check

A simple Python script which uses the AbuseIPDB API to check if an IP address is suspected to be malicious, and returns the number of times the IP has been reported.

The script takes an input of a file of a list of IP addresses for checking against the AbuseIPDB database. The file must be formatted with each IP address separated by a carriage return. An AbuseIPDB API key is required for it to work, which you can place inside the api_key variable.

The script is very simple and was just thrown together with the purpose of making my mornings a bit easier.

Sample output:

IP address 123.123.123.123 has 618 reports
IP address 123.123.123.124 has 127 reports
IP address 123.123.123.125 has 450 reports

The script can easily be amended to return whichever JSON fields you like from the query made to AbuseIPDB, as the script returns the whole JSON object for a given IP address, and then just parses the output to what I needed to see.
