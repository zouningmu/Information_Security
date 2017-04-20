#!/usr/bin/python
import json, sys, hashlib
from fractions import gcd

def usage():
    print """Usage:
    python find_waldo.py student_id (i.e., qchenxiong3)"""
    sys.exit(1)

#TODO -- n1 and n2 share p or q?
def is_waldo(n1, n2):
    result = False

    #your code start here
    if gcd(n1,n2)>1:
	result = True

    #your code ends here

    return result

#TODO -- get private key of n1
def get_private_key(n1, n2, e):
    d = 0

    #your code starts here
    p=gcd(n1,n2);
    q1=n1/p;
    q2=n2/p;
    phi=(p-1)*(q1-1);

    k=1;
    while k<=e:
        if (phi*k+1)%e==0:
            d=(phi*k+1)/e;
            break;
        k=k+1;
    


    #your code ends here

    return d

def main():
    if len(sys.argv) != 2:
        usage()

    all_keys = None
    with open("keys.json", 'r') as f:
        all_keys = json.load(f)

    name = hashlib.sha224(sys.argv[1].strip()).hexdigest()
    if name not in all_keys:
        print sys.argv[1], "not in keylist"
        usage()

    pub_key = all_keys[name]
    n1 = int(pub_key['N'], 16)
    e = int(pub_key['e'], 16)
    d = 0
    waldo = "dolores"

    print "your public key: (", hex(n1).rstrip("L"), ",", hex(e).rstrip("L"), ")"

    for classmate in all_keys:
        if classmate == name:
            continue
        n2 = int(all_keys[classmate]['N'], 16)

        if is_waldo(n1, n2):
            waldo = classmate
            d = get_private_key(n1, n2, e)
            break
    
    print "your private key: ", hex(d).rstrip("L")
    print "your waldo: ", waldo


if __name__ == "__main__":
    main()
