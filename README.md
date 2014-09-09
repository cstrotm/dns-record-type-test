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

Example usage:
==============

Good:

```
% ./dns-record-type-test.py defaultroutes.org 127.0.0.1
Checking URI: RCODE: NoError
Checking A: RCODE: NoError
Checking NS: RCODE: NoError
Checking MD: RCODE: NoError
Checking MF: RCODE: NoError
Checking CNAME: RCODE: NoError
Checking SOA: RCODE: NoError
Checking MB: RCODE: NoError
Checking MG: RCODE: NoError
Checking MR: RCODE: NoError
Checking NULL: RCODE: NoError
Checking WKS: RCODE: NoError
Checking PTR: RCODE: NoError
Checking HINFO: RCODE: NoError
Checking MINFO: RCODE: NoError
Checking MX: RCODE: NoError
Checking TXT: RCODE: NoError
Checking RP: RCODE: NoError
Checking AFSDB: RCODE: NoError
Checking X25: RCODE: NoError
Checking ISDN: RCODE: NoError
Checking RT: RCODE: NoError
Checking NSAP: RCODE: NoError
Checking NSAP-PTR: RCODE: NoError
Checking SIG: RCODE: ServFailServer
Checking KEY: RCODE: NoError
Checking PX: RCODE: NoError
Checking GPOS: RCODE: NoError
Checking AAAA: RCODE: NoError
Checking LOC: RCODE: NoError
Checking NXT: RCODE: NoError
Checking EID: RCODE: NoError
Checking NIMLOC: RCODE: NoError
Checking SRV: RCODE: NoError
Checking ARMA: RCODE: NoError
Checking NAPTR: RCODE: NoError
Checking KX: RCODE: NoError
Checking CERT: RCODE: NoError
Checking A6: RCODE: NoError
Checking DNAME: RCODE: NoError
Checking SINK: RCODE: NoError
Checking OPT: RCODE: ServFailServer
Checking APL: RCODE: NoError
Checking DS: RCODE: NoError
Checking SSHFP: RCODE: NoError
Checking IPSECKEY: RCODE: NoError
Checking RRSIG: RCODE: NoError
Checking NSEC: RCODE: NoError
Checking DNSKEY: RCODE: NoError
Checking DHCID: RCODE: NoError
Checking NSEC3: RCODE: NoError
Checking NSEC3PARAM: RCODE: NoError
Checking TLSA: RCODE: NoError
Checking HIP: RCODE: NoError
Checking NINFO: RCODE: NoError
Checking RKEY: RCODE: NoError
Checking TALINK: RCODE: NoError
Checking CDS: RCODE: ServFailServer
Checking CDNSKEY: RCODE: NoError
Checking OPENPGPKEY: RCODE: NoError
Checking TA: RCODE: NoError
Checking DLV: RCODE: NoError
Checking CAA: RCODE: NoError
Checking SPF: RCODE: NoError
Checking UINFO: RCODE: NoError
Checking UID: RCODE: NoError
Checking GID: RCODE: NoError
Checking UNSPEC: RCODE: NoError
Checking NID: RCODE: NoError
Checking L32: RCODE: NoError
Checking L64: RCODE: NoError
Checking LP: RCODE: NoError
Checking EUI48: RCODE: NoError
Checking EUI64: RCODE: NoError
Checking TKEY: RCODE: ServFailServer
Checking TSIG: RCODE: ServFailServer
Checking MAILB: RCODE: ServFailServer
Checking NAILA: RCODE: ServFailServer

Summary:


Supported RR-Types:
URI
A
NS
MD
MF
CNAME
SOA
MB
MG
MR
NULL
WKS
PTR
HINFO
MINFO
MX
TXT
RP
AFSDB
X25
ISDN
RT
NSAP
NSAP-PTR
KEY
PX
GPOS
AAAA
LOC
NXT
EID
NIMLOC
SRV
ARMA
NAPTR
KX
CERT
A6
DNAME
SINK
APL
DS
SSHFP
IPSECKEY
RRSIG
NSEC
DNSKEY
DHCID
NSEC3
NSEC3PARAM
TLSA
HIP
NINFO
RKEY
TALINK
CDNSKEY
OPENPGPKEY
TA
DLV
CAA
SPF
UINFO
UID
GID
UNSPEC
NID
L32
L64
LP
EUI48
EUI64
Failed (possibly unsupported) RR-Types:
SIG
OPT
CDS
TKEY
TSIG
MAILB
NAILA
```

Bad:
```
% ./dns-record-type-test.py defaultroutes.org
Checking URI: No response
Checking A: RCODE: NoError
Checking NS: RCODE: NoError
Checking MD: RCODE: NoError
Checking MF: RCODE: NoError
Checking CNAME: RCODE: NoError
Checking SOA: RCODE: NoError
Checking MB: RCODE: NoError
Checking MG: RCODE: NoError
Checking MR: RCODE: NoError
Checking NULL: RCODE: NoError
Checking WKS: RCODE: NoError
Checking PTR: RCODE: NoError
Checking HINFO: RCODE: NoError
Checking MINFO: RCODE: NoError
Checking MX: RCODE: NoError
Checking TXT: RCODE: NoError
Checking RP: No response
Checking AFSDB: No response
Checking X25: No response
Checking ISDN: No response
Checking RT: No response
Checking NSAP: No response
Checking NSAP-PTR: No response
Checking SIG: No response
Checking KEY: No response
Checking PX: No response
Checking GPOS: No response
Checking AAAA: RCODE: NoError
Checking LOC: No response
Checking NXT: No response
Checking EID: No response
Checking NIMLOC: No response
Checking SRV: RCODE: NoError
Checking ARMA: No response
Checking NAPTR: RCODE: NoError
Checking KX: No response
Checking CERT: No response
Checking A6: No response
Checking DNAME: No response
Checking SINK: No response
Checking OPT: No response
Checking APL: No response
Checking DS: No response
Checking SSHFP: No response
Checking IPSECKEY: No response
Checking RRSIG: No response
Checking NSEC: No response
Checking DNSKEY: No response
Checking DHCID: No response
Checking NSEC3: No response
Checking NSEC3PARAM: No response
Checking TLSA: No response
Checking HIP: No response
Checking NINFO: No response
Checking RKEY: No response
Checking TALINK: No response
Checking CDS: No response
Checking CDNSKEY: No response
Checking OPENPGPKEY: No response
Checking TA: No response
Checking DLV: No response
Checking CAA: No response
Checking SPF: No response
Checking UINFO: No response
Checking UID: No response
Checking GID: No response
Checking UNSPEC: No response
Checking NID: No response
Checking L32: No response
Checking L64: No response
Checking LP: No response
Checking EUI48: No response
Checking EUI64: No response
Checking TKEY: No response
Checking TSIG: No response
Checking MAILB: No response
Checking NAILA: No response

Summary:

Supported RR-Types:
A
NS
MD
MF
CNAME
SOA
MB
MG
MR
NULL
WKS
PTR
HINFO
MINFO
MX
TXT
AAAA
SRV
NAPTR
Failed (possibly unsupported) RR-Types:
URI
RP
AFSDB
X25
ISDN
RT
NSAP
NSAP-PTR
SIG
KEY
PX
GPOS
LOC
NXT
EID
NIMLOC
ARMA
KX
CERT
A6
DNAME
SINK
OPT
APL
DS
SSHFP
IPSECKEY
RRSIG
NSEC
DNSKEY
DHCID
NSEC3
NSEC3PARAM
TLSA
HIP
NINFO
RKEY
TALINK
CDS
CDNSKEY
OPENPGPKEY
TA
DLV
CAA
SPF
UINFO
UID
GID
UNSPEC
NID
L32
L64
LP
EUI48
EUI64
TKEY
TSIG
MAILB
NAILA
```
