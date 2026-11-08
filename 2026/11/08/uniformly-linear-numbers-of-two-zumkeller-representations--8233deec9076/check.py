"""Exact finite premises for a theorem on the two-Zumkeller representation function.

Uses only integer arithmetic and exhaustive subset sums of actual divisors.
Run: python3 zum_check.py
"""
from math import isqrt

UV = [
(5985,61425),(17955,29835),(2205,29925),(14175,41895),
(26145,44625),(6435,10395),(22365,50085),(6615,80535),
(18585,46305),(2835,30555),(14805,42525),
(26775,82215),(38745,94185),(22995,50715),(7245,34965),
(19215,74655),(3465,7425),(15435,33915),(8925,27405),
(11655,39375),(23625,69825),(7875,63315),
(19845,84525),(4095,31815),(6825,16065),(9555,28035),
(12285,67725),(5775,8415),(8505,36225),(20475,48195),
(4725,23205),(16695,25935),(945,28665),
(12915,31395),(24885,34125),(9135,36855),(21105,39585),
(5355,33075),(8085,17325),(1575,29295),(13545,33345),
(25515,53235),(9765,37485),(21735,58695)]
A=(6,12,20,28,40,80)
# For the nine residues 0,2,...,16 modulo 18: (base seed, partner residue).
EVEN={0:(12,6),2:(80,12),4:(28,12),6:(12,12),
      8:(20,6),10:(40,6),12:(6,6),14:(20,12),16:(40,12)}

def divisors(n):
    low=[]; high=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            low.append(d)
            if d*d!=n:high.append(n//d)
    return low+high[::-1]

def zumkeller(n):
    ds=divisors(n)
    sigma=sum(ds)
    if sigma%2 or sigma<2*n:return False
    target=sigma//2-n
    bits=1
    for d in ds[:-1]:
        if d<=target:bits|=bits<<d
    return bool((bits>>target)&1)

def even_witness(n):
    a,b=EVEN[n%18]
    assert n>=90 and (n-a-b)%18==0
    m=(n-a-b)//18
    assert m>=0
    return [(a*(1+18*a*t),n-a*(1+18*a*t)) for t in range(m//(a*a)+1)]

def odd_witness(n):
    assert n>94185 and n&1
    idx=((n%88)+1)//2-1
    u,v=UV[idx]
    for s in (u,v):
        if n>s and (n-s)%88==0 and ((n-s)//88)%11!=0:
            m=(n-s)//88
            return [(s*(1+88*s*t),88*(m-s*s*t)) for t in range((m-1)//(s*s)+1)
                    if (m-s*s*t)%11!=0]
    raise AssertionError(('no starting seed',n))

def main():
    assert len(UV)==44
    for i,(u,v) in enumerate(UV,1):
        assert u%88==v%88==(2*i-1), (i,u,v)
        assert 0<u<=94185 and 0<v<=94185
        assert ((v-u)//88)%11!=0 and (v-u)%88==0
        assert zumkeller(u) and zumkeller(v), (i,u,v)
    for s in A:assert zumkeller(s),s
    print('44 residue-pairs: 88 source seeds certified by exact proper-divisor subset sums')
    print('all 44 residue/congruence safeguards and six even seeds checked')
    for n in list(range(90,2000,2)) + [2*10**6+2*i for i in range(9)]:
        ws=even_witness(n)
        for z,w in (ws[0],ws[-1]):
            assert z+w==n and z>0 and w>0
            a=EVEN[n%18][0]
            assert z%a==0 and (z//a-1)%(18*a)==0
            assert w%18 in (6,12)
            if n<2000:
                assert zumkeller(z) and zumkeller(w)
    print('even residue construction and endpoints checked: 964 sample totals')
    for n in list(range(94187,100000,2))+[100000001+2*i for i in range(44)]:
        ws=odd_witness(n)
        for z,w in (ws[:1]+ws[-1:]):
            assert z+w==n and w>0 and w%88==0 and (w//88)%11!=0
            assert z>0
            if n<95000:
                assert zumkeller(z) and zumkeller(w)
    print('odd residue construction and endpoints checked: 2951 sample totals')
    print('PASS: all finite premises verified; unbounded asymptotic from symbolic progression count')
if __name__=='__main__':main()
