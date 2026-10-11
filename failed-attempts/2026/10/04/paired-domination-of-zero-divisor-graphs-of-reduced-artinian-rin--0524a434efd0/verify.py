from itertools import product, combinations

def ring_vertices(qs):
    elems=list(product(*[range(q) for q in qs]))
    one=tuple(1 for _ in qs)
    zero=tuple(0 for _ in qs)
    def is_unit(x): return all(a!=0 for a in x)
    return [x for x in elems if x!=zero and not is_unit(x)]

def mul(a,b,qs): return tuple((x*y)%q for x,y,q in zip(a,b,qs))

def graph(qs):
    V=ring_vertices(qs)
    zero=tuple(0 for _ in qs)
    adj=[set() for _ in V]
    for i,a in enumerate(V):
        for j in range(i+1,len(V)):
            if mul(a,V[j],qs)==zero:
                adj[i].add(j); adj[j].add(i)
    return V,adj

def pm(S,adj):
    S=set(S)
    if not S:return True
    if len(S)%2:return False
    v=min(S)
    for u in sorted(adj[v]&S):
        if pm(S-{v,u},adj): return True
    return False

def paired_gamma(qs):
    V,adj=graph(qs)
    n=len(V)
    for k in range(2,n+1,2):
        for C in combinations(range(n),k):
            S=set(C)
            if all(v in S or bool(adj[v]&S) for v in range(n)) and pm(S,adj):
                return k,C,V,adj
    return None,None,V,adj

cases=[
    ((2,2),2),
    ((2,3),2),
    ((3,3),2),
    ((2,2,2),4),
    ((2,2,3),4),
    ((2,3,3),4),
    ((3,3,3),4),
    ((2,2,2,2),4),
    ((2,2,2,2,2),6),
]
print('VERIFY_OK')
for qs,exp in cases:
    got,C,V,adj=paired_gamma(qs)
    assert got==exp,(qs,got,exp)
    print('x'.join('F'+str(q) for q in qs), 'vertices='+str(len(V)), 'paired='+str(got))
