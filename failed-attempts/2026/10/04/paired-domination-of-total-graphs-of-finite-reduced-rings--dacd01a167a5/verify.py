#!/usr/bin/env python3
from itertools import product, combinations

# A finite field is needed here only through its additive group: in a direct
# product of fields, x+y is a zero divisor iff one coordinate sum is zero.
# Represent F_{p^k} additively as (Z/pZ)^k.
def prime_power(q):
    for p in range(2,q+1):
        if any(p%d==0 for d in range(2,int(p**0.5)+1)):
            continue
        t=q; k=0
        while t%p==0:
            t//=p; k+=1
        if t==1 and k>=1:
            return p,k
    raise ValueError(q)

def field_elements(q):
    p,k=prime_power(q)
    return list(product(range(p), repeat=k)), p

def add(a,b,p):
    return tuple((x+y)%p for x,y in zip(a,b))

def zero(a):
    return all(x==0 for x in a)

def total_graph(qs):
    fields=[]; ps=[]
    for q in qs:
        E,p=field_elements(q); fields.append(E); ps.append(p)
    V=list(product(*fields))
    adj=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            if any(zero(add(x[c],y[c],ps[c])) for c in range(len(qs))):
                adj[i].add(j); adj[j].add(i)
    return V,adj

def dominates(S,adj,total=False):
    S=set(S)
    for v in range(len(adj)):
        if total:
            if not (adj[v] & S): return False
        else:
            if v not in S and not (adj[v] & S): return False
    return True

def has_perfect_matching(S,adj):
    S=frozenset(S)
    memo={}
    def rec(T):
        if not T: return True
        if T in memo: return memo[T]
        v=next(iter(T))
        for u in adj[v] & set(T):
            if rec(T-{v,u}):
                memo[T]=True; return True
        memo[T]=False; return False
    return len(S)%2==0 and rec(S)

def minima(qs):
    V,adj=total_graph(qs)
    n=len(V); q=min(qs)
    ordinary=total=paired=None
    # The theorem says all minima are <= q+1; search exactly through that bound.
    for k in range(1,q+2):
        if ordinary is None:
            for C in combinations(range(n),k):
                if dominates(C,adj,False): ordinary=k; break
        if total is None:
            for C in combinations(range(n),k):
                if dominates(C,adj,True): total=k; break
        if paired is None and k%2==0:
            for C in combinations(range(n),k):
                if dominates(C,adj,False) and has_perfect_matching(C,adj):
                    paired=k; break
        if ordinary is not None and total is not None and paired is not None:
            break
    return len(V),ordinary,total,paired

cases=[
    (2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(3,3,3),(5,5)
]
for qs in cases:
    N,g,gt,gp=minima(qs)
    q=min(qs)
    expected_gp=q if q%2==0 else q+1
    expected_gt=q
    expected_g=(q-1 if q%2==1 and all(x==q for x in qs) else q)
    assert (g,gt,gp)==(expected_g,expected_gt,expected_gp),(qs,N,g,gt,gp)
    print(f"profile={qs} vertices={N} gamma={g} gamma_t={gt} gamma_pr={gp}")

# Directly test the canonical witnesses used in the proof on more profiles,
# including larger prime powers where exhaustive subset search is unnecessary.
def witness_check(qs):
    V,adj=total_graph(qs)
    q=min(qs); i=qs.index(q)
    j=0 if i!=0 else 1
    # Build the q vertices having arbitrary i-coordinate and zero elsewhere.
    fields=[]; ps=[]
    for Q in qs:
        E,p=field_elements(Q); fields.append(E); ps.append(p)
    zeros=[tuple(0 for _ in fields[c][0]) for c in range(len(qs))]
    inds=[]
    for a in fields[i]:
        x=list(zeros); x[i]=a; x=tuple(x)
        inds.append(V.index(x))
    assert dominates(inds,adj,True)
    assert all(v in adj[u] for u,v in combinations(inds,2))
    if q%2==0:
        assert has_perfect_matching(inds,adj)
    else:
        c=next(a for a in fields[j] if not zero(a))
        e=list(zeros); e[j]=c; e=V.index(tuple(e))
        S=inds+[e]
        assert dominates(S,adj,False)
        assert has_perfect_matching(S,adj)

for qs in [(4,5),(4,8),(7,8),(8,9),(9,11),(4,4,5),(7,7,8)]:
    witness_check(qs)

print('VERIFY_OK')
print('exhaustive_profiles=9')
print('witness_only_profiles=7')
print('projection_lower_bound=proved_symbolically_in_RESULT')
