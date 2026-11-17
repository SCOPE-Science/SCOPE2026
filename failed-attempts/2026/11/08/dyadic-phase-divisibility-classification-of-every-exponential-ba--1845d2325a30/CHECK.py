#!/usr/bin/env python3
"""Exact cyclotomic check of dyadic graph-spectrum multiplicities.
Finite tests are corroborative; the general proof is in RESULT.md.
"""
from itertools import product
from collections import Counter
from math import gcd

def coeffs_cyclo(p,q):
    # Phi_{p*q}(X)=Phi_p(-X^(q/2)), p an odd prime, q a power of two.
    step=q//2; degree=(p-1)*step
    z=[0]*(degree+1)
    for j in range(p): z[j*step]=(-1)**j
    assert z[degree]==1
    return z

def roots_of_unity_table(p,q):
    n=p*q;phi=coeffs_cyclo(p,q);d=len(phi)-1
    def shift(v):
        a=v[-1];ret=[0]+list(v[:-1])
        if a:
            for i in range(d):ret[i]-=a*phi[i]
        return tuple(ret)
    v=tuple([1]+[0]*(d-1));ans=[]
    for e in range(n):
        ans.append(v);v=shift(v)
    assert v==ans[0]
    return ans

def gcd_diffs(f,q):
    d=q
    for y in f[1:]:d=gcd(d,y-f[0])
    return d

def check(p,q):
    vals=roots_of_unity_table(p,q);dim=len(vals[0]);graphs=0;freq_check=0
    histogram=Counter();pred_hist=Counter();fibers=0
    # Independently evaluate all nontrivial Fourier coefficient zeros by exact
    # integer arithmetic modulo Phi_{p*q}, then enumerate EVERY candidate spectrum.
    for f in product(range(q),repeat=p):
        ftab={}
        for w in range(p):
            for v in range(q):
                arr=[0]*dim
                for x in range(p):
                    a=vals[(q*w*x + p*v*f[x])%(p*q)]
                    for j in range(dim): arr[j]+=a[j]
                ftab[w,v]=all(t==0 for t in arr)
        # Check mathematically independent fact that a frequency pair at fixed u
        # cannot be orthogonal: odd number of dyadic roots cannot sum to zero.
        assert all(not ftab[0,v] for v in range(1,q))
        count=0
        for vtuple in product(range(q),repeat=p):
            okay=True
            for u in range(p):
                for z in range(u+1,p):
                    if not ftab[(u-z)%p,(vtuple[u]-vtuple[z])%q]:
                        okay=False;break
                if not okay:break
            count+=okay
            freq_check+=1
        h=gcd_diffs(f,q)
        assert count==q*h**(p-1),(p,q,f,count,h)
        histogram[count]+=1;pred_hist[count]+=1;graphs+=1;fibers+=count
    assert graphs==q**p
    for r in range(q.bit_length()):
        h=1<<r
        if h>q:break
        expected=h*(q//h)**p - ((h*2)*(q//(h*2))**p if h<q else 0)
        assert histogram[q*h**(p-1)]==expected,(p,q,h,histogram,expected)
    print('CASE_OK p=%d q=%d functions=%d spectrum_tests=%d spectrum_pairs=%d histogram=%s'%(p,q,graphs,freq_check,fibers,dict(sorted(histogram.items()))))

if __name__=='__main__':
    for p,q in [(3,4),(3,8),(5,4)]:check(p,q)
    print('CHECK_OK exact_cyclotomic=True')
