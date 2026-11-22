#!/usr/bin/env python3
"""Standalone verification of a five-step extinction clock and a motif law on fan graphs.
All arithmetic is exact, and no external Python packages are required.
"""
from itertools import product
from collections import defaultdict

MOTIFS = {(1,0,0,0,1), (1,0,2,0,1)}

def update(s):
    n=len(s)-1
    e=[v==1 for v in s]
    hub = ((s[0]+1)%3 if s[0] else int(sum(e[1:])>=2))
    rim=[]
    for i in range(1,n+1):
        neighbors=int(e[0])+(int(e[i-1]) if i>1 else 0)+(int(e[i+1]) if i<n else 0)
        rim.append((s[i]+1)%3 if s[i] else int(neighbors>=2))
    return (hub,*rim)

def occur(word):
    return sum(tuple(word[i:i+5]) in MOTIFS for i in range(len(word)-4))

def exhaustive(n):
    hist=[0]*6
    for s in product(range(3), repeat=n+1):
        x=s
        t=0
        while any(x) and t<=5:
            x=update(x)
            t+=1
        assert not any(x), (n,s)
        hist[t]+=1
        assert (t==5)==(s[0]==1 and occur(s[1:])>=2),(n,s,t)
    return hist

def motif_dp(n):
    # Keep the last four colors and the number of motif hits, truncated at two.
    dp={((),0):1}
    for _ in range(n):
        nxt=defaultdict(int)
        for (suffix,hits),count in dp.items():
            for c in range(3):
                new=suffix+(c,)
                hit=int(len(new)==5 and new in MOTIFS)
                nxt[(new[-4:], min(2,hits+hit))]+=count
        dp=nxt
    return [sum(cnt for (s,h),cnt in dp.items() if h==k) for k in range(3)]

def gf_coeffs(limit):
    # Rational GF: 4 z^9 (1-2z)/((1-3z)*(1-3z+2z^4-4z^5)^2).
    def mult(a,b):
        r=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):r[i+j]+=x*y
        return r
    d=mult(mult([1,-3],[1,-3,0,0,2,-4]),[1,-3,0,0,2,-4])
    ns=[0]*(limit+1)
    for k in range(limit+1):
        rhs=4 if k==9 else (-8 if k==10 else 0)
        ns[k]=rhs-sum(d[j]*ns[k-j] for j in range(1,min(k,len(d)-1)+1))
    return ns

def local_exclusion():
    # Any graph boundary is weaker than an interior path; all allowable hub
    # initial triples are checked for every length-seven neighborhood.
    hub_triples=[(0,0,0),(0,0,1),(0,1,2),(1,2,0),(2,0,0),(2,0,1)]
    for hs in hub_triples:
        for v in product(range(3),repeat=7):
            a=list(v)
            for t in range(3):
                b=[0]*7
                for i in range(1,6):
                    k=int(hs[t]==1)+int(a[i-1]==1)+int(a[i+1]==1)
                    b[i]=(a[i]+1)%3 if a[i] else int(k>=2)
                a=b
            assert a[3]!=1,(hs,v)
    return 6*3**7

if __name__=='__main__':
    checked=local_exclusion()
    print('LOCAL_WINDOWS_OK',checked)
    seq=gf_coeffs(65)
    for n in range(0,66):
        a,b,c=motif_dp(n)
        assert a+b+c==3**n
        assert c==seq[n],(n,c,seq[n])
    print('GENERATING_FUNCTION_OK', [(n,seq[n]) for n in range(9,16)])
    for n in range(1,11):
        hist=exhaustive(n)
        assert hist[5]==seq[n]
        print('EXHAUSTIVE',n,'states',3**(n+1),'first_hit',hist)
    print('VERIFY_OK')
