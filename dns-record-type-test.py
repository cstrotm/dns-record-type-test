#!/usr/bin/env python
# Copyright (C) 2014 Carsten Strotmann
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND MEN & MICE DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL MEN & MICE BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
# OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
"""
this script tests the support for official IANA resource record types
http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4
"""

import ldns
import sys

rcodes = {0: "NoError",
          1: "FormErr",
          2: "ServFailServer",
          3: "NXDomain",
          4: "NotImp",
          5: "Refused",
          6: "YXDomain",
          7: "YXRRSet",
          8: "NXRRSet",
          9: "NotAuth",
          10: "NotZone",
          16: "BADVERS",
          16: "BADSIG",
          17: "BADKEY",
          18: "BADTIME",
          19: "BADMODE",
          20: "BADNAME",
          21: "BADALG",
          22: "BADTRUNC"}

rrtypes = {   1 : "A",
              2 : "NS",
              3 : "MD",
              4 : "MF",
              5 : "CNAME",
              6 : "SOA",
              7 : "MB",
              8 : "MG",
              9 : "MR",
             10 : "NULL",
             11 : "WKS",
             12 : "PTR",
             13 : "HINFO",
             14 : "MINFO",
             15 : "MX",
             16 : "TXT",
             17 : "RP",
             18 : "AFSDB",
             19 : "X25",
             20 : "ISDN",
             21 : "RT",
             22 : "NSAP",
             23 : "NSAP-PTR",
             24 : "SIG",
             25 : "KEY",
             26 : "PX",
             27 : "GPOS",
             28 : "AAAA",
             29 : "LOC",
             30 : "NXT",
             31 : "EID",
             32 : "NIMLOC",
             33 : "SRV",
             34 : "ARMA",
             35 : "NAPTR",
             36 : "KX",
             37 : "CERT",
             38 : "A6",
             39 : "DNAME",
             40 : "SINK",
             41 : "OPT",
             42 : "APL",
             43 : "DS",
             44 : "SSHFP",
             45 : "IPSECKEY",
             46 : "RRSIG",
             47 : "NSEC",
             48 : "DNSKEY",
             49 : "DHCID",
             50 : "NSEC3",
             51 : "NSEC3PARAM",
             52 : "TLSA",
             55 : "HIP",
             56 : "NINFO",
             57 : "RKEY",
             58 : "TALINK",
             59 : "CDS",
             60 : "CDNSKEY",
             61 : "OPENPGPKEY",
             99 : "SPF",
            100 : "UINFO",
            101 : "UID",
            102 : "GID",
            103 : "UNSPEC",
            104 : "NID",
            105 : "L32",
            106 : "L64",
            107 : "LP",
            108 : "EUI48",
            109 : "EUI64",
            249 : "TKEY",
            250 : "TSIG",
            253 : "MAILB",
            254 : "MAILA",
            256 : "URI",
            257 : "CAA",
          32768 : "TA",
          32769 : "DLV"
}

def check_record_type(name, rrtype):
    # Resolve IPv4 DNS name
    r = ldns.ldns_rr.new_frm_str(name + " A 1.2.3.4")
    r.set_type(rrtype)
    typestr = r.get_type_str()
    pkt = resolver.query(name, rrtype, ldns.LDNS_RR_CLASS_IN)
    if pkt and pkt.answer():


        # SERVFAIL indicated issue with server
        if pkt.get_rcode() is ldns.LDNS_RCODE_SERVFAIL:
            failed.append(rrtypes[rrtype])
        # NOERROR is the returncode we want to see
        if pkt.get_rcode() is ldns.LDNS_RCODE_NOERROR:
            success.append(rrtypes[rrtype])

        if debug:
            print name, "\t" + typestr + "-Record returned (" + str(pkt.ancount()) + " Records) RCODE:", rcodes[pkt.get_rcode()]
        else:
            print "RCODE:", rcodes[pkt.get_rcode()]
    else:
        failed.append(rrtypes[rrtype])
        if pkt:
            print "No " + typestr +"-Record found", pkt.get_rcode()
        else:
            print "No response"


# ---- (MAIN) ----

debug = False
success = []
failed = []

# Check args
argc = len(sys.argv)
name = "dnsworkshop.org"
if argc < 2:
    print "Usage:", sys.argv[0], "domain [resolver_addr]"
    sys.exit(1)
else:
    name = sys.argv[1]

for rrtype, rrtypename in rrtypes.iteritems():
    # Create resolver
    resolver = ldns.ldns_resolver.new_frm_file("/etc/resolv.conf")

    # Custom resolver
    if argc > 2:
        # Clear previous nameservers
        ns = resolver.pop_nameserver()
        while ns != None:
            ns = resolver.pop_nameserver()
        ip = ldns.ldns_rdf.new_frm_str(sys.argv[2], ldns.LDNS_RDF_TYPE_A)
        resolver.push_nameserver(ip)

    print "Checking {}:".format(rrtypename),
    check_record_type(name, rrtype)

print "Summary"
print "-------"

print "Supported RR-Types:"
for rrtype in success:
    print rrtype

print "Failed (possibly unsupported) RR-Types:"
for rrtype in failed:
    print rrtype


        
