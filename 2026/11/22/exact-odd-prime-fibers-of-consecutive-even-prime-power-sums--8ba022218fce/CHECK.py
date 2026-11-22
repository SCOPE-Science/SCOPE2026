#!/usr/bin/env python3
"""Finite verification of local image/fibers of consecutive even prime-power sums.
Mathematical proof is separate; brute force checks only listed finite cases.
"""
from collections import Counter


def expected_fibers(p,s,k):
    d=2*(p**s)
    q=p**k
    center=pow(2,1-d,q) if d<=1 else pow(pow(2,d-1,q),-1,q)
    cc=(-pow(2,-1,p))%p
    counts=Counter()
    modulus_reg = p ** min(k,s+1)
    for a in range(p):
        if a==cc: continue
        v=(pow(a,d,modulus_reg)+pow(a+1,d,modulus_reg))%modulus_reg
        for y in range(v,q,modulus_reg):
            counts[y] += p**min(s,k-1)
    # each regular branch yields p^min(s,k-1) index values
    modulus_crit=p**min(s+2,k)
    A=(d-1)*pow(pow(2,d-3,q),-1,q)%q
    if k <= s+2:
        counts[center%q] += p**(k-1)
    else:
        n=k-s-2
        for u in range(p**n):
            y=(center + (p**(s+2))*A*u*u)%q
            counts[y] += p**(s+1)
    return counts


def q_squares(p,n):
    return 1+sum(((p-1)//2)*p**(n-2*j-1) for j in range((n+1)//2))


def verify(p,s,k):
    q=p**k
    d=2*(p**s)
    obs=Counter((pow(x,d,q)+pow(x+1,d,q))%q for x in range(q))
    ex=expected_fibers(p,s,k)
    assert obs==ex, (p,s,k,[(y,obs[y],ex[y]) for y in range(q) if obs[y]!=ex[y]][:10])
    assert sum(obs.values())==q
    formula=((p-1)//2)*p**max(0,k-s-1)+q_squares(p,max(0,k-s-2))
    assert len(obs)==formula, (p,s,k,len(obs),formula)
    return len(obs),max(obs.values())


if __name__ == '__main__':
    combos=[(3,1,6),(3,2,6),(5,1,5),(5,2,5),(7,1,4),(11,1,4)]
    checks=0
    for p,s,maxk in combos:
        for k in range(1,maxk+1):
            image,maximum=verify(p,s,k)
            checks+=1
            print(p,s,k,'image',image,'max_fiber',maximum)
    print('PASS',checks,'complete prime-power target histograms')
