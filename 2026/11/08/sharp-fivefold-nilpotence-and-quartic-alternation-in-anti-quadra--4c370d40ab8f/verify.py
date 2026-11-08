"""Exact verification for the sharp nilpotence bound of near/anti-L/R algebras.
No external packages required. Operations use integer structure constants.
"""
from functools import lru_cache
from itertools import permutations, combinations, product
from collections import defaultdict, deque

@lru_cache(None)
def bracket_trees(seq):
    if len(seq)==1:
        return (seq[0],)
    return tuple((left,right)
                 for k in range(1,len(seq))
                 for left in bracket_trees(seq[:k])
                 for right in bracket_trees(seq[k:]))

def elementary_relations(m):
    if type(m) is int:
        return []
    x,y=m
    out=[]
    if type(x) is tuple:
        a,b=x
        out += [((b,(y,a)),1), (((a,y),b),-1)]
    if type(y) is tuple:
        b,c=y
        out += [((b,(x,c)),-1)]
    out += [((t,y),s) for t,s in elementary_relations(x)]
    out += [((x,t),s) for t,s in elementary_relations(y)]
    return out

def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

cycle=[
    ((((0,1),2),3),4),
    ((((0,1),2),4),3),
    ((((0,2),1),4),3),
    ((1,(4,(0,2))),3),
    ((1,((2,4),0)),3),
    (((0,1),(2,4)),3),
    ((2,4),(3,(0,1))),
    ((2,(3,(0,1))),4),
    ((((0,1),2),3),4),
]
cycle_signs=[1,-1,1,1,1,1,1,-1,-1]
assert cycle[0]==cycle[-1] and cycle_signs[0]==-cycle_signs[-1]
for k in range(len(cycle)-1):
    sign=cycle_signs[k]*cycle_signs[k+1]
    assert ((cycle[k+1],sign) in elementary_relations(cycle[k]) or
            (cycle[k],sign) in elementary_relations(cycle[k+1]))
print('IDENTITY_CYCLE_OK steps=8')

for arity,expected in [(3,3),(4,1),(5,0)]:
    monomials=set()
    for p in permutations(range(arity)):
        monomials.update(bracket_trees(p))
    terms=list(monomials)
    lookup={m:i for i,m in enumerate(terms)}
    adjacency=[[] for _ in terms]
    for i,m in enumerate(terms):
        for nxt,s in elementary_relations(m):
            j=lookup[nxt]
            adjacency[i].append((j,s))
            adjacency[j].append((i,s))
    components=[]
    seen={}
    inconsistent=[]
    for start in range(len(terms)):
        if start in seen:continue
        comp=[];q=deque([start]);seen[start]=1;bad=False
        while q:
            i=q.popleft();comp.append(i)
            for j,s in adjacency[i]:
                implied=seen[i]*s
                if j not in seen:
                    seen[j]=implied;q.append(j)
                elif seen[j]!=implied:
                    bad=True
        components.append(comp)
        inconsistent.append(bad)
    nonzero=sum(not x for x in inconsistent)
    assert len(terms)=={3:12,4:120,5:1680}[arity]
    assert nonzero==expected,(arity,nonzero)
    if arity==4:
        assert len(components)==1 and not inconsistent[0]
        root=((((0,1),2),3))
        rel=seen[lookup[root]]
        for p in permutations(range(4)):
            left=(((p[0],p[1]),p[2]),p[3])
            assert seen[lookup[left]]==rel*parity(p)
    if arity==5:
        assert len(components)==1 and inconsistent[0]
    print(f'ARITY_OK arity={arity} monomials={len(terms)} components={len(components)} surviving={nonzero}')

V=[t for d in range(1,5) for t in combinations(range(4),d)]
I={a:i for i,a in enumerate(V)}
CO={(1,1):1,(1,2):1,(2,1):1,(2,2):1,(1,3):-1,(3,1):-1}

def wedge_product(x,y):
    if set(x)&set(y):return None,0
    inv=sum(a>b for a in x for b in y)
    return tuple(sorted(x+y)),(-1)**inv*CO.get((len(x),len(y)),0)

N=len(V)
for a,b,c in product(V,repeat=3):
    def left(a,b,c):
        x,t=wedge_product(a,b)
        if not t:return 0
        y,s=wedge_product(x,c)
        return t*s
    def right(a,b,c):
        x,t=wedge_product(b,c)
        if not t:return 0
        y,s=wedge_product(a,x)
        return t*s
    assert left(a,b,c)==right(b,c,a)
    assert left(a,b,c)==-left(a,c,b)
    assert right(a,b,c)==-right(b,a,c)
print('BASE_OK dimension=15 triple_tests=3375')

# The zero-cocycle cotangent extension B + B^*.
D={}
for i,j in product(range(2*N),repeat=2):
    out={}
    if i<N and j<N:
        w,c=wedge_product(V[i],V[j])
        if c:out[I[w]]=c
    elif i<N and j>=N:
        for h in range(N):
            w,c=wedge_product(V[h],V[i])
            if w==V[j-N] and c:out[N+h]=-c
    elif i>=N and j<N:
        for h in range(N):
            w,c=wedge_product(V[j],V[h])
            if w==V[i-N] and c:out[N+h]=-c
    D[i,j]=out

def multiply(X,Y):
    out=defaultdict(int)
    for i,a in X.items():
        for j,b in Y.items():
            for k,c in D[i,j].items():out[k]+=a*b*c
    return {i:x for i,x in out.items() if x}

def neg(X):return {i:-v for i,v in X.items()}
def omega(X,Y):
    return sum(c*Y.get(i-N,0) for i,c in X.items() if i>=N)-sum(c*Y.get(i+N,0) for i,c in X.items() if i<N)

E=[{i:1} for i in range(2*N)]
for i,j,k in product(range(2*N),repeat=3):
    x,y,z=E[i],E[j],E[k]
    assert multiply(multiply(x,y),z)==multiply(y,multiply(z,x))
    assert multiply(multiply(x,y),z)==neg(multiply(multiply(x,z),y))
    assert multiply(x,multiply(y,z))==neg(multiply(y,multiply(x,z)))
    assert omega(multiply(x,y),z)==-omega(x,multiply(y,z))

x=E[I[(0,)]]
for j in (1,2,3):x=multiply(x,E[I[(j,)]])
assert x=={I[(0,1,2,3)]:-1}
# The August 2026 symmetric-metric lemma (ab)c=-(ba)c is not universal here.
a,b,c=E[I[(0,1)]], E[I[(2,)]], E[I[(3,)]]
assert multiply(multiply(a,b),c)==multiply(multiply(b,a),c)
assert multiply(multiply(a,b),c)
print('EXTENSION_OK dimension=30 triple_tests=27000 fourfold_nonzero=-e0123')
print('VERIFY_OK')
