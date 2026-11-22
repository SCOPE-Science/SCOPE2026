#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

def omega(a,b,n):
    return ((a&((1<<n)-1)) & (b>>n)).bit_count()%2 ^ ((b&((1<<n)-1))&(a>>n)).bit_count()%2

def span(basis):
    o={0}
    for b in basis:o|={x^b for x in tuple(o)}
    return frozenset(o)

def all_lags(n):
    N=1<<(2*n); lags=set()
    def rec(basis,sp):
        if len(basis)==n:
            lags.add(sp);return
        for v in range(1,N):
            if v in sp or any(omega(v,b,n) for b in basis):continue
            rec(basis+[v],span(basis+[v]))
    rec([],frozenset({0}));return sorted(lags,key=lambda t:tuple(sorted(t)))

def rank_f2(vs):
    piv={}
    for x in vs:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)

def run(n):
    npoints=(1<<(2*n))-1;points=list(range(1,npoints+1));lags=all_lags(n)
    print('n',n,'points',npoints,'lagrangians',len(lags))
    classmask=[]
    for l in lags:
        m=0
        for v in l:
            if v:m|=1<<(v-1)
        classmask.append(m)
    layers=[ [()] ]; pred=[1]
    for k in range(1,n+1):
        faces=[]
        for S in combinations(points,k):
            if not all(omega(x,y,n)==0 for x,y in combinations(S,2)):continue
            if len(span(S))!=1<<k:continue
            faces.append(S)
            patterns={sum(((m>>(v-1))&1)<<i for i,v in enumerate(S)) for m in classmask}
            if len(patterns)!=(1<<k):raise ValueError('bad trace '+str(S))
        layers.append(faces);pred.append(len(faces))
    print('f-vector',pred)
    if n<=3:
        all_rank=[0]
        for k in range(1,n+1):
            down={face:i for i,face in enumerate(layers[k-1])}
            cols=[]
            for face in layers[k]:
                t=sum(1<<down[sub] for sub in combinations(face,k-1));cols.append(t)
            r=rank_f2(cols);all_rank.append(r)
            print('boundary',k,'rank',r)
        bets=[]
        for i in range(n):bets.append(len(layers[i+1])-all_rank[i+1]- (all_rank[i+2] if i+2<=n else 0))
        print('reduced Betti degrees 0..',n-1, bets)
    # verify missed candidates are not shattered for n<=3 all candidates
    if n<=3:
        valid=set(layers[-1]);
        for k in range(1,n+1):
            valid=set(layers[k]); # for n3 checking k 1..3
            for S in combinations(points,k):
                if S in valid:continue
                patterns={sum(((m>>(v-1))&1)<<i for i,v in enumerate(S)) for m in classmask}
                if len(patterns)==1<<k:raise ValueError('spurious '+str(S))
        print('FULL SHATTERING CHECK PASS')
if __name__=='__main__':
    for n in (1,2,3):run(n)
