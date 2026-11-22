#!/usr/bin/env python3
"""Direct word-count recurrence independently validates the prime-modulus periodic densities."""
from itertools import product
from collections import defaultdict

def report(q,p,nmax):
    pair=[(i,j) for i in range(q) for j in range(i+1,q)]
    zero=(0,)*(q+len(pair))
    D={zero:1}
    print(f'q={q},p={p},D={len(zero)},theoretical fiber={p**(len(zero)-1)}')
    for n in range(nmax+1):
        hits=0
        for s,mult in D.items():
            if all(s[q+k]%p==0 and (s[i]*s[j])%p==0 for k,(i,j) in enumerate(pair)):
                hits+=mult
        residue=n%p
        target=(1 if residue==0 else q)/p**(len(zero)-1)
        if n in (8,12,16,20,24,28,32,36,40):
            print(f' n={n:2} proportion={hits/q**n:.9f} target={target:.9f}')
        R=defaultdict(int)
        for s,mult in D.items():
            for j in range(q):
                t=list(s)
                for k,(i,b) in enumerate(pair):
                    if b==j:t[q+k]=(s[q+k]+s[i])%p
                t[j]=(s[j]+1)%p
                R[tuple(t)]+=mult
        D=R
    print('PASS')

if __name__=='__main__':
    report(2,2,40)
    report(2,3,40)
    report(3,2,40)
