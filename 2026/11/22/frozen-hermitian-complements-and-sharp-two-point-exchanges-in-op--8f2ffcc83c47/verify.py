"""Exact projective-plane double-blocking reconfiguration certificate.
Pure Python 3, no third-party packages. Executable with python3 verify.py.
"""
from itertools import product, combinations
from collections import Counter

# GF(4)=GF(2)[w]/(w*w+w+1), encoded 0,1,w,w+1.
def mul(a,b):
    if not a or not b: return 0
    if a==1: return b
    if b==1: return a
    return {(2,2):3,(2,3):1,(3,2):1,(3,3):2}[(a,b)]
inv=(0,1,3,2)
def norm(v):
    pivot=next(x for x in v if x)
    return tuple(mul(x,inv[pivot]) for x in v)
P=sorted({norm(v) for v in product(range(4),repeat=3) if any(v)})
assert len(P)==21
L=[sum(1<<i for i,p in enumerate(P) if not (mul(ell[0],p[0])^mul(ell[1],p[1])^mul(ell[2],p[2]))) for ell in P]
assert len(set(L))==21 and all(l.bit_count()==5 for l in L)
full=(1<<21)-1

def good(s): return all((s&ell).bit_count()>=2 for ell in L)
# Exhausts all 2^21 labelled subsets, including every cardinality below 12.
S={s for s in range(1<<21) if s.bit_count()<=12 and good(s)}
assert len(S)==11480 and all(s.bit_count()==12 for s in S)

def profile(s):
    cnt=Counter((s&ell).bit_count() for ell in L)
    return tuple(cnt[i] for i in range(6))
profiles={p:{s for s in S if profile(s)==p} for p in {profile(s) for s in S}}
A=(0,0,9,9,0,3); B=(0,0,10,6,3,2); C=(0,0,12,0,9,0)
assert {p:len(v) for p,v in profiles.items()}=={A:1120,B:10080,C:280}

# Five explicit incidence-preserving generators of PΓL(3,4).
def transform(v,j):
    a,b,c=v
    return norm(((b,a,c),(a^b,b,c),(mul(a,2),b,c),
                 (mul(a,a),mul(b,b),mul(c,c)),(a,c,b))[j])
perms=[]
for k in range(5):
    pi=tuple(P.index(transform(v,k)) for v in P)
    assert {sum(1<<pi[i] for i in range(21) if l&(1<<i)) for l in L}==set(L)
    perms.append(pi)
def act(s,pi): return sum(1<<pi[i] for i in range(21) if s&(1<<i))
reps={p:min(v) for p,v in profiles.items()}
for p,start in reps.items():
    seen={start};queue=[start]
    for x in queue:
        for pi in perms:
            y=act(x,pi)
            if y not in seen:seen.add(y);queue.append(y)
    assert seen==profiles[p], (p,len(seen))

def neighbors(s,max_exchange):
    inside=[1<<i for i in range(21) if s&(1<<i)]
    outside=[1<<i for i in range(21) if not s&(1<<i)]
    for r in range(1,max_exchange+1):
        for drop in combinations(inside,r):
            base=s
            for bit in drop:base^=bit
            for add in combinations(outside,r):
                t=base
                for bit in add:t|=bit
                if t in S:yield t

def bfs(start,r):
    d={start:0};q=[start]
    for x in q:
        for y in neighbors(x,r):
            if y not in d:d[y]=d[x]+1;q.append(y)
    layers=Counter(d.values())
    return len(q),max(d.values()),tuple(layers[j] for j in range(max(d.values())+1))

assert {p:Counter(profile(t) for t in neighbors(reps[p],1)) for p in reps} == {
    A:Counter({B:27}),B:Counter({A:3,B:12}),C:Counter()}
assert {p:Counter(profile(t) for t in neighbors(reps[p],2)) for p in reps} == {
    A:Counter({B:135,A:27}),B:Counter({A:15,B:141,C:3}),C:Counter({B:108})}
one={p:bfs(start,1) for p,start in reps.items()}
two={p:bfs(start,2) for p,start in reps.items()}
assert one[A]==(11200,8,(1,27,135,711,1863,3972,3249,1188,54))
assert one[B]==(11200,8,(1,15,132,619,1979,3759,3465,1146,84))
assert one[C]==(1,0,(1,))
assert two[A]==(11480,5,(1,162,2817,7230,1269,1))
assert two[B]==(11480,4,(1,159,2901,7159,1260))
assert two[C]==(11480,5,(1,108,3078,6984,1305,4))
# Orbit transitivity turns these representative eccentricities into exact diameters.
assert 1120*27==10080*3
assert (1120*27+10080*15)//2==90720
print('PASS: 11480 extrema in three transitive geometry classes (1120,10080,280).')
print('One-exchange: 280 isolated + connected 11200-state core, 90720 edges, core diameter 8.')
print('Up-to-two exchange: connected 11480-state graph, radius 4, diameter 5.')
for name,p in [('triangle',A),('mixed',B),('unital complement',C)]:
    print(name,'1-exchange',one[p],'2-exchange',two[p])
