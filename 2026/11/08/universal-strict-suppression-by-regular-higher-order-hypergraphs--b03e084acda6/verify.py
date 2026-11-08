"""Exact rational checks for full-group birth-death fixation on regular hypergraphs.
Run: python3 verify.py (Python standard library only).
The proof is analytic; these finite checks test independent transition assembly and boundaries.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import defaultdict

checks=0

def chk(condition, reason):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(reason)

def hypergraph(n, kind):
    if kind=='single':
        return (tuple(range(n)),)
    if kind=='complete3':
        return tuple(combinations(range(n),3))
    if kind=='cyclic3':
        return tuple(sorted(set(tuple(sorted(((i+j)%n for j in range(3)))) for i in range(n))))
    if kind=='mixed34':
        return tuple(combinations(range(n),3))+tuple(combinations(range(n),4))
    if kind=='pairs':
        return tuple(sorted(set(tuple(sorted((i,(i+1)%n))) for i in range(n))))
    raise ValueError(kind)

def prepare(n, edges):
    ed=tuple(sum(1<<v for v in e) for e in edges)
    incident=[[] for _ in range(n)]
    for mask in ed:
        for v in range(n):
            if mask>>v&1:incident[v].append(mask)
    deg={len(x) for x in incident}
    chk(len(deg)==1 and next(iter(deg))>0, ('regular',n,edges))
    return ed,incident,next(iter(deg))

def transitions(n, incident, state, r):
    full=(1<<n)-1
    i=state.bit_count()
    z=r*i+n-i
    result=defaultdict(Q)
    for v in range(n):
        wt=r if state>>v&1 else Q(1)
        for e in incident[v]:
            nxt=(state|e) if state>>v&1 else (state & (full^e))
            result[nxt]+=wt/(z*len(incident[v]))
    chk(sum(result.values())==1, ('stochastic',n,state,r))
    return result

def predicted_drift(n,ed,d,state,r):
    i=state.bit_count()
    z=r*i+n-i
    y=r**(-i)
    total=Q(0)
    for e in ed:
        a=(e&state).bit_count()
        b=e.bit_count()-a
        total+=r*a*(r**(-b)-1)+b*(r**a-1)
    return y*total/(z*d)

def solve_linear(a,b):
    n=len(b)
    for j in range(n):
        pivot=next((k for k in range(j,n) if a[k][j]),None)
        chk(pivot is not None, ('noninvertible',j))
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
            b[j],b[pivot]=b[pivot],b[j]
        p=a[j][j]
        for k in range(j+1,n):
            if not a[k][j]: continue
            fac=a[k][j]/p
            for t in range(j+1,n):
                a[k][t]-=fac*a[j][t]
            a[k][j]=0
            b[k]-=fac*b[j]
    x=[Q(0)]*n
    for i in reversed(range(n)):
        x[i]=(b[i]-sum((a[i][j]*x[j] for j in range(i+1,n)),Q(0)))/a[i][i]
    return x

def fixation(n,inc,r):
    full=(1<<n)-1
    inner=list(range(1,full))
    lookup={s:i for i,s in enumerate(inner)}
    dim=len(inner)
    A=[[Q(int(i==j)) for j in range(dim)] for i in range(dim)]
    rhs=[Q(0) for _ in range(dim)]
    for idx,s in enumerate(inner):
        for to,p in transitions(n,inc,s,r).items():
            if to==full:rhs[idx]+=p
            elif to!=0:A[idx][lookup[to]]-=p
    return dict(zip(inner,solve_linear(A,rhs)))

for n,kind in [(3,'single'),(4,'complete3'),(5,'complete3'),(5,'cyclic3'),(5,'mixed34'),(6,'cyclic3'),(6,'complete3'),(5,'pairs'),(5,'single')]:
    ed,inc,d=prepare(n,hypergraph(n,kind))
    full=(1<<n)-1
    for r in (Q(1,2),Q(2,3),Q(1),Q(3,2),Q(2),Q(4)):
        for state in range(1,full):
            P=transitions(n,inc,state,r)
            i=state.bit_count()
            if r==1:
                diff=sum((p*to.bit_count() for to,p in P.items()),Q(0))-i
                chk(diff==0,('neutral drift',n,kind,state,r,diff))
            else:
                drift=sum((p*r**(-to.bit_count()) for to,p in P.items()),Q(0))-r**(-i)
                chk(drift==predicted_drift(n,ed,d,state,r),('drift identity',n,kind,state,r))
                if kind=='pairs':chk(drift==0,('pair equality',n,state,r))
                else:chk(drift>0,('positive high-order drift',n,kind,state,r))
        if n<=5:
            fx=fixation(n,inc,r)
            for state,p in fx.items():
                i=state.bit_count()
                mor=Q(i,n) if r==1 else (1-r**(-i))/(1-r**(-n))
                chk((p==mor if r==1 or kind=='pairs' else (p<mor if r>1 else p>mor)),('Moran comparison',n,kind,r,state,p,mor))
            if kind=='complete3' and n in (4,5) and r!=1:
                if n==4: source=r*r/(r*r+2*r+1)
                else:source=r*r*(8*r*r+12*r+1)/(8*r**4+28*r**3+33*r*r+28*r+8)
                for v in range(n):chk(fx[1<<v]==source,('source small formula',n,r,v,fx[1<<v],source))
print('PASS',checks,'exact rational assertions')
