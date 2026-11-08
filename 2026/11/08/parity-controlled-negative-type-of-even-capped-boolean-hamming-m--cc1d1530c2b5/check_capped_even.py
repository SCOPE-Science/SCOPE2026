#!/usr/bin/env python3
"""Independent finite Walsh checks for capped Hamming metrics.
No third-party modules are required. Purely finite tests; proof is in RESULT.md.
"""
from math import comb, log, exp, expm1, factorial

def kraw(n, j, s):
    return sum((-1)**i*comb(s, i)*comb(n-s, j-i)
               for i in range(max(0, j-(n-s)), min(j, s)+1))

def direct_walsh(n, cap, p, s):
    # Uses the literal distance kernel and the original Krawtchouk definition.
    return sum(min(w, cap)**p * kraw(n, w, s) for w in range(1, n+1))

def telescoped_walsh(n, cap, p, s):
    return -(1+sum((exp(p*log(t-1))*expm1(p*log(t/(t-1))))*kraw(n-1,t-1,s-1)
                   for t in range(2,cap+1)))

def parity_q(n,p):
    m=n-1
    return (1 -m*(2**p-1) +comb(m,2)*(3**p-2**p)
            -comb(m,3)*(4**p-3**p))

def bisect_root(n):
    lo,hi=0.,1.
    assert parity_q(n,lo)>0 and parity_q(n,hi)<0
    for _ in range(90):
        mid=(lo+hi)/2
        if parity_q(n,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def check():
    for n in range(8,14):
        b=bisect_root(n)
        for p in (0.001,0.5*b,b,0.8,1.0):
            vals=[]
            for s in range(1,n+1):
                direct=direct_walsh(n,4,p,s)
                tele=telescoped_walsh(n,4,p,s)
                assert abs(direct-tele)<2e-9, ('formula',n,p,s,direct,tele)
                vals.append(tele)
            assert vals[n-1] >= max(vals)-1e-10, ('parity dominance',n,p)
            if p < b-1e-6: assert max(vals) < -1e-7,('before threshold',n,p)
            if p > b+1e-6: assert vals[-1] > 1e-7,('after threshold',n,p)
            if abs(p-b)<1e-10:
                assert abs(vals[-1])<1e-8
                assert max(vals[:-1]) < -1e-6
        print('n',n,'beta',format(b,'.12g'), 'n^3 beta',format(n**3*b,'.6g'))
    # Verify the general even-cap leading upper and lower bounds in sample dimensions.
    for cap in (2,4,6,8):
        j=cap-1
        c0=factorial(j)/log(cap/(cap-1))
        for n in (250,500):
            below=.5*c0/n**j
            above=2*c0/n**j
            for s in range(1,n+1):
                assert telescoped_walsh(n,cap,below,s) < 0,('even lower',cap,n,s)
            assert telescoped_walsh(n,cap,above,n)>0,('even upper',cap,n)
        print('cap',cap,'leading coefficient',format(c0,'.10g'))
    print('EVEN_CAPPED_HAMMING_WALSH_CHECKS_OK')
if __name__=='__main__': check()
