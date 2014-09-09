Test DNS-Record Type Support
============================

Tests a DNS resolver for DNS record type support. Used to test DNS-Proxies in CPE devices.

This script will test a DNS Query toward the default resolver in
'/etc/resolv.conf' or a custom resolver that can be given on the
command line.

Be careful not to trigger response-rate limiting on the DNS-Server.

The list of record types to test has been taken from 
http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4

The script requires the python-wrapper around ldns from https://www.nlnetlabs.nl/projects/ldns/

New record types can be checked manually from the command-line using dig:

<code>
dig defaultroutes.org TYPE59 @127.0.0.1
</code>