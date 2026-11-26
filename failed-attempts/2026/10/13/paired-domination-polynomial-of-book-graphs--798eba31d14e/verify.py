from itertools import combinations
from collections import Counter


def graph(n):
    # 0=a, 1=b, then x_i=2+2i and y_i=3+2i.
    N = 2 + 2*n
    adj = [set() for _ in range(N)]
    def edge(u,v):
        adj[u].add(v); adj[v].add(u)
    edge(0,1)
    for i in range(n):
        x, y = 2+2*i, 3+2*i
        edge(0,x); edge(x,y); edge(y,1)
    return adj


def dominates(S, adj):
    S=set(S)
    return all(v in S or any(u in S for u in adj[v]) for v in range(len(adj)))


def has_perfect_matching(vertices, adj):
    V=set(vertices)
    if len(V)%2: return False
    if not V: return True
    v=min(V)
    for u in sorted(adj[v] & V):
        R=V-{v,u}
        if has_perfect_matching(R, adj):
            return True
    return False


def paired(S, adj):
    return dominates(S, adj) and has_perfect_matching(S, adj)


def structural_type(S,n):
    S=set(S); a=0 in S; b=1 in S
    states=[]
    for i in range(n):
        x,y=2+2*i,3+2*i
        states.append((int(x in S),int(y in S)))
    c10=states.count((1,0)); c01=states.count((0,1))
    if a and b:
        if c10==0 and c01==0 and all(t in ((0,0),(1,1)) for t in states): return 1
        if c10==1 and c01==1 and all(t in ((0,0),(1,0),(0,1),(1,1)) for t in states): return 2
        return None
    if a and not b:
        if c10==1 and all(t in ((1,0),(1,1)) for t in states): return 3
        return None
    if b and not a:
        if c01==1 and all(t in ((0,1),(1,1)) for t in states): return 3
        return None
    if all(t==(1,1) for t in states): return 4
    return None


def formula(n):
    c=Counter()
    for j in range(n+1):
        from math import comb
        c[2+2*j]+=comb(n,j)
    from math import comb
    for j in range(n-1):
        c[4+2*j]+=n*(n-1)*comb(n-2,j)
    c[2*n]+=2*n+1
    return c

subset_checks=paired_sets=coefficient_checks=classification_checks=0
for n in range(1,9):
    adj=graph(n); N=len(adj); brute=Counter()
    for mask in range(1<<N):
        S=[v for v in range(N) if (mask>>v)&1]
        ok=paired(S,adj)
        subset_checks+=1
        st=structural_type(S,n)
        if ok:
            paired_sets+=1
            brute[len(S)]+=1
        if n>=2:
            assert ok == (st is not None), (n,S,ok,st)
            classification_checks+=1
    if n==1:
        assert brute==Counter({2:4,4:1}), brute
    else:
        f=formula(n)
        assert brute==f, (n,brute,f)
        coefficient_checks += 2*n+1
        assert min(brute)==2 and brute[2]==1
print(f"VERIFY_OK n_range=1..8 subset_checks={subset_checks} paired_sets={paired_sets} classification_checks={classification_checks} coefficient_checks={coefficient_checks} max_order=18")
