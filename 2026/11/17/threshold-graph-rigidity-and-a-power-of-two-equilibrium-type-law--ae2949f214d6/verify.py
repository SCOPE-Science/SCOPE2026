#!/usr/bin/env python3
"""Independent threshold-word and recursive-family checks of majority equilibria on L(K_n)."""
from collections import Counter
from math import factorial

def threshold_word(n, bits):
    assert len(bits)==n and bits[0]==0
    degrees=[i*bits[i]+sum(bits[i+1:]) for i in range(n)]
    return all((degrees[i]+degrees[j]>=n if bits[j] else degrees[i]+degrees[j]<=n-2)
               for i in range(n) for j in range(i+1,n))

def word_profile(n):
    by_k=Counter(); fixed=0; orbit_polynomial=Counter()
    for mask in range(1<<(n-1)):
        bits=(0,)+tuple((mask>>(i-1))&1 for i in range(1,n))
        if not threshold_word(n,bits):continue
        d=[i*bits[i]+sum(bits[i+1:]) for i in range(n)]
        c=Counter(d)
        denom=1
        for z in c.values():denom*=factorial(z)
        w=factorial(n)//denom
        by_k[sum(bits)]+=1;fixed+=w
        orbit_polynomial[sum(d)//2]+=w
    return by_k,fixed,orbit_polynomial

def grow(word):
    assert word[0]==0 and 1 in word
    a=list(word)
    last=max(i for i,x in enumerate(a) if x==1)
    A=tuple(a[:last+1]+[1]+a[last+1:]+[0])
    if a[-1]==0:
        B=tuple(a+[0,1])
    else:
        begin=last
        while begin>0 and a[begin-1]==1:begin-=1
        B=tuple(a[:begin]+[0]+a[begin:]+[1])
    return A,B

def padding(w,p):return (0,)*p+tuple(w)

if __name__=='__main__':
    base={(0,0,0,1)}
    for k in range(1,9):
        n=2*k+2
        direct={ (0,)+tuple((mask>>(i-1))&1 for i in range(1,n))
                 for mask in range(1<<(n-1))
                 if threshold_word(n,(0,)+tuple((mask>>(i-1))&1 for i in range(1,n)))
                 and (mask.bit_count()==k)}
        assert base==direct,(k,len(base),len(direct))
        assert len(base)==2**(k-1)
        for h in range(0,4):
            n2=n+h
            assert {padding(w,h) for w in base}=={
                (0,)+tuple((mask>>(i-1))&1 for i in range(1,n2))
                for mask in range(1<<(n2-1))
                if mask.bit_count()==k and threshold_word(n2,(0,)+tuple((mask>>(i-1))&1 for i in range(1,n2)))}
        base={child for w in base for child in grow(w)}
        print('recursive k',k,'types',len(direct),'passed')
    expected={3:2,4:10,5:12,6:164,7:268,8:5562,9:11852,10:300952,11:785534,12:23769244,13:73294834,14:2588266802,15:9207892208}
    for n,val in expected.items():
        ks,count,poly=word_profile(n)
        assert count==val,(n,count,val)
        assert sum(ks.values())==2**(n//2)
        assert all(poly[e]==poly[n*(n-1)//2-e] for e in poly)
        print('labelled n',n,'fixed',count,'types',sum(ks.values()),'terms',len(poly))
    print('PASS')
