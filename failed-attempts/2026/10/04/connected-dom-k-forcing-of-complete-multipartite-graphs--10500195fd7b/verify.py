from itertools import combinations


def parts_of_n(n, min_part=1):
    if n == 0:
        yield []
        return
    for first in range(min_part, n+1):
        for rest in parts_of_n(n-first, first):
            yield [first]+rest


def build(parts):
    labels=[]
    for i,s in enumerate(parts):
        labels += [i]*s
    n=len(labels)
    adj=[set() for _ in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            if labels[u] != labels[v]:
                adj[u].add(v); adj[v].add(u)
    return labels,adj


def connected(D, adj):
    if not D: return False
    seen={next(iter(D))}; stack=list(seen)
    while stack:
        u=stack.pop()
        for v in adj[u] & D:
            if v not in seen:
                seen.add(v); stack.append(v)
    return seen==D


def dominating(D, adj):
    return all(v in D or bool(adj[v] & D) for v in range(len(adj)))


def kforces(D, adj, k):
    black=set(D); n=len(adj)
    while True:
        add=set()
        for u in tuple(black):
            whites=adj[u] - black
            if 1 <= len(whites) <= k:
                add |= whites
        if not add:
            return len(black)==n
        black |= add


def brute(parts,k):
    _,adj=build(parts); n=len(adj)
    V=range(n)
    for s in range(1,n+1):
        for tup in combinations(V,s):
            D=set(tup)
            if connected(D,adj) and dominating(D,adj) and kforces(D,adj,k):
                return s
    raise AssertionError('no set')


def formula(parts,k):
    n=sum(parts)
    if min(parts)==1 and k==n-1:
        return 1
    W=max(min(k,s-1)+min(k,n-s-1) for s in parts)
    return n-W


def main():
    graph_types=0; parameter_cases=0
    for n in range(2,10):
        for parts in parts_of_n(n):
            if len(parts)<2: continue
            labels,adj=build(parts)
            Delta=max(len(x) for x in adj)
            if Delta<1: continue
            graph_types += 1
            for k in range(1,Delta+1):
                parameter_cases += 1
                b=brute(parts,k); f=formula(parts,k)
                if b!=f:
                    raise AssertionError((parts,k,b,f))
    print(f'ALL CHECKS PASSED; multipartite_types={graph_types}; parameter_cases={parameter_cases}; max_order=9')

if __name__=='__main__': main()
