#!/usr/bin/env python3
"""Check cardinality spectra for equal-sum divisor subsets of 3*2**(m-1)."""
from math import comb

def via_recurrence(max_m):
    a = [0, 0]  # polynomials as coefficient arrays for P_0 and P_1
    polys = {1: [0], 2: [0,1,0,1]}
    for m in range(3, max_m+1):
        p=polys[m-1];q=polys[m-2];res=[0]*(2*m+1)
        for i,v in enumerate(p):res[i+1]+=v
        for i,v in enumerate(q):res[i+1]+=v;res[i+3]+=v
        polys[m]=res
    return polys

def formula(m):
    if m<4:return 0
    return sum(comb(m-3-2*r,2*r+1)*comb(2*r+2,r+1)
               for r in range((m-4)//4+1))//2

def test():
    polys=via_recurrence(12)
    for m in range(1,13):
        M=2**m-1;weights=[0]*(2*m+1)
        for v in range(M+1):
            u=2*M-3*v
            if 0<=u<=M:
                weights[u.bit_count()+v.bit_count()]+=1
        rec=polys[m]+[0]*(len(weights)-len(polys[m]))
        assert rec==weights, ('full spectrum',m,rec,weights)
        assert weights[m]%2==0
        assert weights[m]//2==formula(m),('balanced count',m)
    print('PASS: 12 independent exhaustive full spectra and 12 closed central counts')
if __name__=='__main__':test()
