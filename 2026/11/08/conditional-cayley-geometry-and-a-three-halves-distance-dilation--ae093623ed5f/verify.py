"""Standalone exact checker for a conditional random bipartite tree law.
Run with Python 3: python verify.py. Standard library only.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, product
from math import comb, factorial

checks=0

def eq(a,b,context=''):
    global checks
    checks+=1
    assert a==b, f'{context}: got {a!r} expected {b!r}'

def edges_k(n):
    return [(i,n+j) for i in range(n) for j in range(n)]

def is_tree(E,n):
    parent=list(range(2*n))
    def find(u):
        while u!=parent[u]: u=parent[u]
        return u
    for u,v in E:
        u=find(u); v=find(v)
        if u==v:return False
        parent[v]=u
    return True

def matching(E,n):
    adj=[set() for _ in range(2*n)]
    for u,v in E:
        adj[u].add(v);adj[v].add(u)
    alive=set(range(2*n)); matched=[]
    while alive:
        leaf=next((x for x in alive if len(adj[x]&alive)==1),None)
        if leaf is None: return None
        y=next(iter(adj[leaf]&alive));matched.append((min(leaf,y),max(leaf,y)))
        alive.remove(leaf);alive.remove(y)
    return tuple(sorted(matched))

def distances(E,n,start):
    adj=[[] for _ in range(2*n)]
    for u,v in E: adj[u].append(v);adj[v].append(u)
    d=[-1]*(2*n);d[start]=0
    q=deque([start])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if d[v]<0:d[v]=d[u]+1;q.append(v)
    return d

def quotient(E,n,M):
    index={j:i for i,j in M}
    mset=set(M); C=[];bits=[]
    for e in E:
        if e in mset:continue
        u,v=e; i=u;j=index[v]
        lo,hi=sorted((i,j))
        C.append((lo,hi)); bits.append((lo,hi, int(i==lo)))
    return tuple(sorted(C)),tuple(sorted(bits))

def cdistance(C,n,i,j):
    adj=[[] for _ in range(n)]
    for u,v in C:adj[u].append(v);adj[v].append(u)
    q=deque([i]);d=[-1]*n;d[i]=0
    while q:
        u=q.popleft()
        for v in adj[u]:
            if d[v]<0:d[v]=d[u]+1;q.append(v)
    return d[j]

for n in range(2,5):
    dist=Counter(); grouped=defaultdict(Counter); total=0; matchable=0
    for E0 in combinations(edges_k(n),2*n-1):
        if not is_tree(E0,n):continue
        E=tuple(sorted(E0));total+=1
        M=matching(E,n)
        if M is None:continue
        matchable+=1
        C,bits=quotient(E,n,M)
        grouped[(M,C)][bits]+=1
    eq(total,n**(2*n-2),f'number of spanning trees n={n}')
    eq(matchable,factorial(n)*2**(n-1)*n**(n-2),f'matchable count n={n}')
    eq(len(grouped),factorial(n)*n**(n-2),f'(matching,quotient) pairs n={n}')
    for (M,C),orientations in grouped.items():
        eq(len(orientations),2**(n-1),f'all orientations n={n}')
        eq(set(orientations.values()),{1},'orientation multiplicity')
    # Enumerate all lifts of identity matching of each quotient Cayley tree.
    M=tuple((i,n+i) for i in range(n))
    cs={C for (mm,C) in grouped if mm==M}
    for C in cs:
        for i,j in combinations(range(n),2):
            ell=cdistance(C,n,i,j)
            observed=Counter()
            for orient in product([0,1],repeat=n-1):
                E=list(M)
                for (lo,hi),bit in zip(C,orient):
                    E.append((lo,n+hi) if bit else (hi,n+lo))
                observed[distances(E,n,i)[j]]+=1
            # 2^(ell-1) local configurations with multiplicity 2^(n-ell).
            predicted=Counter()
            for h in range(ell):
                count=comb(ell-1,h)*2**(n-1-ell)
                if h%2==0:
                    predicted[2*ell-h]+=count*2
                else:
                    predicted[2*ell-h-1]+=count
                    predicted[2*ell-h+1]+=count
            # Each h is weighted by 2^-ell local coin bits; total counts 2^(n-1)
            # The above expression uses 2^(n-ell) for the base + a factor 2 for even h.
            # Odd h has two endpoint parity choices, each with the same base multiplicity.
            eq(observed,predicted,f'distance law n={n}, ell={ell}')
    print('size',n,'total',total,'perfect_matchable',matchable,'quotients',len(cs))

# Independent check of the Cayley distance formula by Prüfer enumeration.
def tree_from_prufer(n,s):
    deg=[1]*n
    for x in s:deg[x]+=1
    E=[]
    for x in s:
        y=next(i for i in range(n) if deg[i]==1)
        E.append((min(x,y),max(x,y)));deg[x]-=1;deg[y]-=1
    rest=[i for i in range(n) if deg[i]==1]
    E.append(tuple(rest))
    return E
for n in range(2,7):
    observed=Counter()
    for code in product(range(n),repeat=n-2):
        E=tree_from_prufer(n,code)
        observed[cdistance(E,n,0,1)]+=1
    for ell in range(1,n):
        expected=(ell+1)*factorial(n-2)*n**(n-ell-1)//(factorial(n-ell-1)*n)
        # For ell=n-1 this equals n!, denominator n, so divisible by n.
        eq(observed[ell],expected, f'Cayley pair distance n={n}, ell={ell}')
    eq(sum(observed.values()),n**(n-2))
print('VERIFY_OK',checks,'exact assertions')
