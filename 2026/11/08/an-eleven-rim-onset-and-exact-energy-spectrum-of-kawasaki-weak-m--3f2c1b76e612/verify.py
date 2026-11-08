#!/usr/bin/env python3
"""Exact, finite cross-checks for wheel exchange-local-minimum enumeration.
No external dependencies; direct energy tests and independent cyclic transfer DP.
"""
from itertools import combinations, product
from math import comb
from collections import Counter, defaultdict

def formula(n):
    assert n >= 3 and n % 2
    q = (n+1)//2
    terms={0:2*n}
    for t in range(2,(q-2)//2+1):
        sum_st=0
        u=q-2*t
        for s in range(1,min(t,u-1)+1):
            nom=comb(u-1,s-1)*comb(t-1,s-1)*comb(q-t-s-2,u-s-1)
            assert (n*nom)%s==0  # single term is integral in this parametrization
            sum_st+=n*nom//s
        if sum_st: terms[t-1]=2*sum_st
    return terms

def energy(v, n, J, K, h):
    return J*sum(v[i]*v[i+1] if i<n else v[n]*v[1] for i in range(1,n+1)) + K*v[0]*sum(v[1:]) - h*sum(v)

def brute(n, J=3, K=7, h=11):
    # Zero total magnetization: N=n+1 even and N/2 positive spins.
    N=n+1; count=Counter()
    edges=[(0,i) for i in range(1,n+1)]+[(i,i%n+1) for i in range(1,n+1)]
    for pos in combinations(range(N),N//2):
        vv=[1 if i in pos else -1 for i in range(N)]
        e=energy(vv,n,J,K,h)
        for a,b in edges:
            if vv[a]==vv[b]: continue
            vv[a],vv[b]=vv[b],vv[a]
            ee=energy(vv,n,J,K,h)
            vv[a],vv[b]=vv[b],vv[a]
            if ee<e:break
        else:
            delta=e - (J*(2-n)-K)
            assert delta%(4*J)==0
            count[delta//(4*J)]+=1
    return dict(count)

def allowed(rim):
    n=len(rim)
    assert n>=3
    if sum(rim)!=-1:return False  # hub + 1
    return all(not (rim[i]==rim[(i+1)%n]==rim[(i+2)%n]==-1) for i in range(n)) and \
      all(not ((rim[i],rim[(i+1)%n],rim[(i+2)%n],rim[(i+3)%n]) in ((1,1,-1,-1),(-1,-1,1,1))) for i in range(n))

def transfer(n):
    # Independently enumerate 8-state binary paths; closing the path checks all patterns.
    q=(n+1)//2
    out=Counter()
    for first in product((-1,1), repeat=3):
        if first == (-1,-1,-1):continue
        dp={(first,first.count(-1),sum(first[i]*first[i+1] for i in range(2))):1}
        for length in range(3,n):
            nxt=defaultdict(int)
            for (last,m,e),v in dp.items():
                if m>q:continue
                for spin in (-1,1):
                    a,b,c=last
                    if b==c==spin==-1:continue
                    if (a,b,c,spin) in ((1,1,-1,-1),(-1,-1,1,1)):continue
                    nxt[((b,c,spin),m+(spin==-1),e+c*spin)]+=v
            dp=nxt
        for (last,m,e),v in dp.items():
            if m!=q:continue
            seq = last + first
            # boundary windows starting indices n-3, n-2, n-1
            # last3=(n-3,n-2,n-1), first3=(0,1,2)
            x=seq
            if any(x[j]==x[j+1]==x[j+2]==-1 for j in range(3)):continue
            if any(tuple(x[j:j+4]) in ((1,1,-1,-1),(-1,-1,1,1)) for j in range(3)):continue
            e_total=e+last[-1]*first[0]
            e_ground=2-n
            assert (e_total-e_ground)%4==0
            out[(e_total-e_ground)//4]+=v
    return {i:2*c for i,c in out.items()}

def exact_word_check(n):
    for rim in product((-1,1),repeat=n):
        if sum(rim)!=-1:continue
        vv=[1]+list(rim)
        if allowed(rim) != (not any(brute_one(vv,n))):
            raise AssertionError((n,rim))

def brute_one(v,n):
    ee=energy(v,n,2,5,7)
    for a,b in [(0,i) for i in range(1,n+1)]+[(i,i%n+1) for i in range(1,n+1)]:
        if v[a]==v[b]:continue
        w=v[:];w[a],w[b]=w[b],w[a]
        if energy(w,n,2,5,7)<ee:yield (a,b)

def run():
    checks=0
    for n in range(3,16,2):
        f=formula(n)
        b=brute(n)
        assert f==b,(n,f,b)
        checks+=sum(b.values())
        if n<=11:
            exact_word_check(n)
            checks+=2**n
        print('exact-spin',n,'histogram',dict(sorted(f.items())))
    for n in range(3,48,2):
        f=formula(n);t=transfer(n)
        assert f==t,(n,f,t)
        checks+=sum(f.values())%973+1
    for n in range(3,120,2):
        f=formula(n)
        assert f[0]==2*n
        if n<11:assert len(f)==1
        if n>=11:assert f.get(1,0)>0
        checks+=1
    print('VERIFY_OK',checks)
if __name__=='__main__':run()
