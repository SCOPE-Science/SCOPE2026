"""Independent finite rational diagnostics for stationary non-lazy walks on complete bipartite graphs."""
from fractions import Fraction
from itertools import product
from collections import defaultdict


def side_counts(lengths, bits):
    nA = nB = 0
    for t, side in zip(lengths, bits):
        nA += t//2 + (1 if t%2 else 0) + (1 if t%2==0 and side==0 else 0)
        nB += t//2 + (1 if t%2 else 0) + (1 if t%2==0 and side==1 else 0)
    return nA, nB


def single_counts(total, side):
    return (total//2+1, total//2) if total%2==0 and side==0 else \
        (total//2,total//2+1) if total%2==0 else ((total+1)//2,(total+1)//2)


def choose_side(Na,Nb,total):
    if total%2: return (0,1)
    if Na>Nb: return (0,)
    if Nb>Na: return (1,)
    return (0,1)


def dist(a,b,t):
    n=a+b
    adj={u:list(range(a,n)) if u<a else list(range(a)) for u in range(n)}
    d={(u,1<<u):Fraction(1,2*(a if u<a else b)) for u in range(n)}
    for _ in range(t):
        z=defaultdict(Fraction)
        for (u,mask),p in d.items():
            for v in adj[u]: z[(v,mask|1<<v)]+=p/Fraction(len(adj[u]))
        d=z
    out=defaultdict(Fraction)
    for (_,mask),p in d.items():out[mask]+=p
    assert sum(out.values())==1
    return out


def surv(d,n):
    return [sum((p for mask,p in d.items() if mask.bit_count()>=h),Fraction(0)) for h in range(n+1)]


checks=0
for k in range(1,5):
    for lengths in product(range(5),repeat=k):
        T=sum(lengths)
        for bits in product(range(2),repeat=k):
            Na,Nb=side_counts(lengths,bits)
            ss=choose_side(Na,Nb,T)
            for s in ss:
                na,nb=single_counts(T,s)
                assert Na>=na and Nb>=nb,(lengths,bits,Na,Nb,na,nb)
                checks+=1

for a,b in product(range(1,4),repeat=2):
    n=a+b
    for k in (2,3):
        for lengths in product(range(3),repeat=k):
            if sum(lengths)>5:continue
            target=dist(a,b,sum(lengths))
            d={0:Fraction(1)}
            for t in lengths:
                nxt=defaultdict(Fraction)
                for m,p in d.items():
                    for mask,q in dist(a,b,t).items():nxt[m|mask]+=p*q
                d=nxt
            x,y=surv(d,n),surv(target,n)
            assert all(p>=q for p,q in zip(x,y)),(a,b,lengths,x,y)
            checks+=n+1
print(f'{checks} independent finite checks passed')
