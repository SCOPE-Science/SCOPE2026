#!/usr/bin/env python3
"""Independent complete S_n-orbit certificate by sorting parking words.
Only Python's standard library is required. Run: python3 check_orbits.py
"""
from itertools import combinations_with_replacement, permutations
from collections import Counter
from math import factorial
from pathlib import Path
PHI = {2:(1,1),3:(1,1,1),4:(1,0,1),5:(1,1,1,1,1),6:(1,-1,1)}

def divisible(poly, phi):
    c=list(poly); d=len(phi)-1
    for i in range(len(c)-1,d-1,-1):
        m=c[i]
        if m:
            for j in range(d+1): c[i-d+j]-=m*phi[j]
    return all(v==0 for v in c)

def sorted_parking_words(n):
    return [b for b in combinations_with_replacement(range(n),n)
            if all(x<=i for i,x in enumerate(b))]

def words(n):
    return [w for b in sorted_parking_words(n) for w in set(permutations(b))]

def multiorbit_size(freq):
    cs=Counter(freq)
    divisor=1
    for v in cs.values(): divisor*=factorial(v)
    return factorial(len(freq))//divisor

def verify(n):
    q=n+1; F=words(n); phi=PHI[q]
    expected={(1,2,3,4,5),(1,2,3,3,4),(1,2,3,3,5),
              (1,3,3,4,5),(2,3,3,4,5)} if n==5 else set()
    vanished=[]; extras=[]
    cert=[]
    for k in combinations_with_replacement(range(q),n):
        cnt=[0]*q
        for a in F:
            cnt[sum(x*y for x,y in zip(k,a))%q]+=1
        if n==5:
            A=cnt[0]-cnt[2]-cnt[3]+cnt[5]
            B=cnt[1]+cnt[2]-cnt[4]-cnt[5]
            cert.append((k,A,B))
            assert divisible(cnt,phi)==(A==0 and B==0)
        if divisible(cnt,phi):
            vanished.append(k)
            if sum(k)%q: extras.append(k)
    assert set(extras)==expected
    extra_total=sum(multiorbit_size(k) for k in extras)
    forced_total=sum(multiorbit_size(k) for k in vanished if sum(k)%q==0)
    assert extra_total==(360 if n==5 else 0)
    assert forced_total==q**(n-1)-1
    assert len(F)==q**(n-1)
    if n==5:
        certpath=Path(__file__).with_name("ORBIT_CERTIFICATE.tsv")
        if certpath.exists():
            expected_rows=["".join(map(str,k))+"\t"+str(a)+"\t"+str(b) for k,a,b in cert]
            assert certpath.read_text(encoding="utf-8").splitlines()==["frequency\tA\tB"]+expected_rows
    print('n=%d sorted PF=%d frequency orbits=%d exceptional orbits=%d extra frequencies=%d'%(
        n,len(sorted_parking_words(n)),len(list(combinations_with_replacement(range(q),n))),len(extras),extra_total))
    if n==5: print('Exception representatives:', extras)

if __name__=='__main__':
    for n in range(1,6): verify(n)
    print('PASS: independent sorted-preference / cyclotomic-divisibility certificate')
