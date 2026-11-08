"""Exact finite-state certificate for paired-dominating matching counts of cycle prisms.
No optional dependencies; verifies transfer states, zero-defect cycles, rational functions,
and small graph instances by independent edge matching enumeration.
"""
from itertools import product, combinations
from math import comb
from collections import Counter, defaultdict

COLS=[(a,b) for a,b in product('0LR',repeat=2)]+[('V','V')]
assert len(COLS)==10

def compatible(a,b):
    return all((x=='R')==(y=='L') for x,y in zip(a,b))

def dominated(prev,cur,nxt):
    return all(v!='0' or cur[1-r]!='0' or prev[r]!='0' or nxt[r]!='0'
               for r,v in enumerate(cur))

def weight(cur):
    return (1 if cur==('V','V') else 0)+cur.count('R')

STATES=sorted((p,c) for p in range(10) for c in range(10)
              if compatible(COLS[p],COLS[c]))
INDEX={s:i for i,s in enumerate(STATES)}
EDGES=[]
for (p,c),i in INDEX.items():
    for q in range(10):
        if compatible(COLS[c],COLS[q]) and dominated(COLS[p],COLS[c],COLS[q]):
            EDGES.append((i,INDEX[(c,q)],3*weight(COLS[c])-1))
assert len(STATES)==34 and len(EDGES)==101

# Shortest-path difference constraints provide an explicit integer potential.
# A negative directed cycle would violate the certificate; this loop detects one.
h=[0]*len(STATES)
for _ in range(len(STATES)):
    changed=False
    for u,v,w in EDGES:
        if h[v]>h[u]+w:
            h[v]=h[u]+w
            changed=True
    if not changed:
        break
else:
    raise AssertionError('negative-defect cycle')
E=[(u,v,w+h[u]-h[v]) for u,v,w in EDGES]
assert all(0<=d<=4 for u,v,d in E)
assert Counter(d for _,_,d in E)==Counter({0:44,1:24,2:29,4:4})
print('TRANSFER_OK',len(COLS),'columns',len(STATES),'pair-states',len(E),'transitions')

# Strong components of the zero-defect subgraph: exactly two directed simple
# cycles, lengths 3 and 6, plus 25 singleton acyclic components.
graph=[[] for _ in STATES]
rev=[[] for _ in STATES]
for u,v,d in E:
    if d==0:
        graph[u].append(v)
        rev[v].append(u)
visited=set();order=[]
def dfs(v):
    visited.add(v)
    for q in graph[v]:
        if q not in visited:dfs(q)
    order.append(v)
for v in range(len(STATES)):
    if v not in visited:dfs(v)
visited.clear();components=[]
def rdfs(v, comp):
    visited.add(v);comp.append(v)
    for q in rev[v]:
        if q not in visited:rdfs(q,comp)
for v in reversed(order):
    if v not in visited:
        comp=[];rdfs(v,comp);components.append(comp)
nontriv=[]
for comp in components:
    cs=set(comp)
    if len(comp)==1:
        assert comp[0] not in graph[comp[0]]
    else:
        assert all(sum(w in cs for w in graph[v])==1 for v in cs)
        assert all(sum(w in cs for w in rev[v])==1 for v in cs)
        nontriv.append(len(comp))
assert sorted(nontriv)==[3,6] and len(components)==27
print('ZERO_DEFECT_DETERMINANT_OK (1-x^3)(1-x^6)')

# Trace of the reweighted transfer matrix, truncated to u-degree 2.
MAXN=103
trace=defaultdict(int)
OUT=[[] for _ in STATES]
for u,v,d in E:OUT[u].append((v,d))
for st in range(len(STATES)):
    dp={(st,0):1}
    for n in range(1,MAXN+1):
        nxt=defaultdict(int)
        for (u,defect),count in dp.items():
            for v,cost in OUT[u]:
                nd=defect+cost
                if nd<=2:nxt[(v,nd)]+=count
        dp=nxt
        for d in range(3): trace[n,d]+=dp.get((st,d),0)

# Coefficients of the three candidate rational generating functions.
# F0=3x^3(1+3x^3)/(1-x^6).
# F1=x^2(6+7x^3-x^6)/(1-x^3)^3.
# F2=x(1+39x^3+22x^6+41x^9-17x^12+15x^15-6x^18+x^21)
#       /((1-x^3)^5(1+x^3)^2).
def desired(n, d):
    if d==0:
        if n%3!=0 or n<3:return 0
        return 9 if n%6==0 else 3
    if d==1:
        if n%3!=2:return 0
        q=(n-2)//3
        return (3*q+2)*(2*q+3)
    if d==2:
        if n%3!=1:return 0
        if n==1:return 1
        if n%6==4:
            j=(n-4)//6
            return ((3*j+2)*(16*j**3+72*j*j+110*j+63))//3
        j=(n-1)//6
        return ((6*j+1)*(8*j**3+24*j*j+25*j+6))//3
    raise AssertionError(d)
# Independently expand the displayed rational functions by denominator recurrences,
# rather than trusting closed residue-class polynomials.
def rational_coefficients(numerator, factors, cutoff):
    den={0:1}
    for shift,coeff,power in factors:
        for _ in range(power):
            out=Counter()
            for e,c in den.items():
                out[e]+=c
                out[e+shift]+=c*coeff
            den=dict(out)
    seq=[]
    for n in range(cutoff+1):
        v=numerator.get(n,0)
        for e,c in den.items():
            if e and e<=n:v-=c*seq[n-e]
        seq.append(v)
    return seq,den
F0,D0=rational_coefficients({3:3,6:9},[(6,-1,1)],MAXN)
F1,D1=rational_coefficients({2:6,5:7,8:-1},[(3,-1,3)],MAXN)
F2,D2=rational_coefficients({1:1,4:39,7:22,10:41,13:-17,16:15,19:-6,22:1},[(3,-1,5),(3,1,2)],MAXN)
for n in range(MAXN+1):
    for d,seq in enumerate((F0,F1,F2)):
        assert seq[n]==(desired(n,d) if n else 0),(n,d,seq[n],desired(n,d))
print('RATIONAL_DENOMINATOR_EXPANSIONS_OK exact integer recurrence')

for n in range(1,MAXN+1):
    for d in range(3):
        assert trace[n,d]==desired(n,d),(n,d,trace[n,d],desired(n,d))
print('RATIONAL_CEFFICIENT_CERTIFICATE_OK n=1..103 defects=0,1,2')

# Independent brute force: select k disjoint actual graph edges, check graph
# domination with a separate bitset graph model. This does not reuse the
# symbolic column-state and transfer logic.
def brute(n, all_sizes=False):
    V=2*n
    edges=sorted({tuple(sorted((r*n+i,r*n+(i+1)%n)))
        for r in (0,1) for i in range(n)} |
        {(i,n+i) for i in range(n)})
    neigh=[1<<i for i in range(V)]
    for a,b in edges:
        neigh[a]|=1<<b
        neigh[b]|=1<<a
    covers=[neigh[a]|neigh[b] for a,b in edges]
    ep=[(1<<a)|(1<<b) for a,b in edges]
    full=(1<<V)-1
    ks=range(1,len(edges)+1) if all_sizes else [(n+2)//3]
    result=Counter()
    for k in ks:
        if k>(V//2):break
        for it in combinations(range(len(edges)),k):
            occupied=0;dom=0
            for i in it:
                if occupied&ep[i]:break
                occupied|=ep[i]
                dom|=covers[i]
            else:
                if dom==full:result[k]+=1
    return result
for n in range(3,13):
    k=(n+2)//3
    b=brute(n)
    assert b[k]==desired(n,(3*k-n)),(n,b,desired(n,3*k-n))
print('INDEPENDENT_BRUTE_MINIMUM_MATCHINGS_OK n=3..12')

# Full all-cardinality transfer check against independent graph matching enumeration.
def full_transfer(n):
    counts=Counter()
    out=defaultdict(list)
    for (p,c),u in INDEX.items():
        for q in range(10):
            if compatible(COLS[c],COLS[q]) and dominated(COLS[p],COLS[c],COLS[q]):
                out[u].append((INDEX[(c,q)],weight(COLS[c])))
    for st in range(len(STATES)):
        cur={(st,0):1}
        for _ in range(n):
            nxt=defaultdict(int)
            for (u,k),v in cur.items():
                for target,d in out[u]:nxt[(target,k+d)]+=v
            cur=nxt
        for k in range(1,n+1):counts[k]+=cur.get((st,k),0)
    return counts
for n in range(3,7):
    observed=brute(n,all_sizes=True)
    predicted=full_transfer(n)
    assert observed==predicted,(n,observed,predicted)
print('FULL_MATCHING_POLYNOMIAL_INDEPENDENT_OK n=3..6')

# General theorem uses the unconditional 6-vertex edge-neighbourhood bound:
# k >= ceil(n/3). A set of ceil(n/3) equally spaced rungs attains equality.
# A simple constructive domination check guards boundaries for n=3..120.
for n in range(3,121):
    k=(n+2)//3
    cyc=list(range(n))
    chosen=set(range(0,n,3))
    assert len(chosen)==k
    assert all(any(((j-i)%n in (0,1,n-1)) for i in chosen) for j in cyc)
print('RUNG_CONSTRUCTION_OK n=3..120')
print('VERIFY_OK')
