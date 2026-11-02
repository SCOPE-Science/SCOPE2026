from itertools import combinations
from collections import deque, Counter
from math import prod

def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n+1):
        for rest in partitions(n-x, x):
            yield (x,) + rest

def graph_from_parts(parts):
    labels=[]
    for i,s in enumerate(parts):
        labels.extend([i]*s)
    N=len(labels)
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if labels[u] != labels[v]:
                adj[u].add(v); adj[v].add(u)
    return labels, adj

def all_dist(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj); d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1
                    q.append(v)
        D.append(d)
    return D

def actual_nonlocal(labels, D, S):
    S=set(S)
    N=len(labels)
    for u,v in combinations(range(N),2):
        if labels[u] == labels[v]:
            if not any(D[w][u] != D[w][v] for w in S):
                return False
    return True

def predicted_nonlocal(labels,S):
    S=set(S)
    parts={}
    for v,i in enumerate(labels):
        parts.setdefault(i,[]).append(v)
    for vs in parts.values():
        if len(vs)>=2 and sum(v in S for v in vs) < len(vs)-1:
            return False
    return True

def expected_counts(parts):
    # Product (1+z) for singleton parts and
    # (n z^(n-1)+z^n) for every non-singleton part.
    coeff=[1]
    for n in parts:
        factor=[1,1] if n==1 else [0]*(n-1)+[n,1]
        new=[0]*(len(coeff)+len(factor)-1)
        for i,a in enumerate(coeff):
            for j,b in enumerate(factor):
                new[i+j]+=a*b
        coeff=new
    return coeff

types=0
subset_trials=0
basis_trials=0
for N in range(2,11):
    for parts in partitions(N):
        if len(parts)<2:
            continue
        labels,adj=graph_from_parts(parts)
        D=all_dist(adj)
        types+=1
        counts=Counter()
        good_sets=[]
        for mask in range(1<<N):
            subset_trials+=1
            S=[v for v in range(N) if (mask>>v)&1]
            a=actual_nonlocal(labels,D,S)
            p=predicted_nonlocal(labels,S)
            assert a==p,(parts,S,a,p)
            if a:
                counts[len(S)]+=1
                good_sets.append(S)
        expected=expected_counts(parts)
        actual=[counts[k] for k in range(N+1)]
        assert actual==expected,(parts,actual,expected)

        dim=min(counts)
        assert dim == N-len(parts),(parts,dim,N-len(parts))
        basis_count=counts[dim]
        expected_bases=prod(n for n in parts if n>=2)
        assert basis_count==expected_bases,(parts,basis_count,expected_bases)
        basis_trials += basis_count

print("VERIFY_OK")
print("complete_multipartite_types_checked =",types)
print("orders = 2..10")
print("vertex_subsets_checked =",subset_trials)
print("minimum_bases_checked =",basis_trials)
print("all direct nonlocal-resolving tests matched the partwise omission classification")
print("all cardinality enumerators matched the product formula")
print("all dimensions matched N-r")
print("all minimum-basis counts matched the product of non-singleton part sizes")
