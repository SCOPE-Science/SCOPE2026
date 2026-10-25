#!/usr/bin/env python3
from itertools import combinations, product
from collections import deque, Counter


def connected(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    if n==0: return True
    seen={0}; q=[0]
    while q:
        v=q.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); q.append(w)
    return len(seen)==n

def bipartite(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    col=[None]*n
    for s in range(n):
        if col[s] is not None: continue
        col[s]=0; q=deque([s])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if col[w] is None:
                    col[w]=1-col[v]; q.append(w)
                elif col[w]==col[v]: return False
    return True

def square_free(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    for a,b in combinations(range(n),2):
        if len(adj[a]&adj[b])>=2:
            return False
    return True

def neighborhoods(n,edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    return adj

def all_nonempty_subsets(S):
    S=sorted(S)
    for r in range(1,len(S)+1):
        for t in combinations(S,r):
            yield frozenset(t)

def neighborhood_faces(adj):
    faces=set()
    for Nv in adj:
        faces.update(all_nonempty_subsets(Nv))
    return faces

def one_collapse_check(adj, roots):
    n=len(adj)
    current=neighborhood_faces(adj)
    original=len(current)
    planned=[]
    for v in range(n):
        base=sorted(adj[v]-{roots[v]})
        for r in range(len(base),1,-1):
            for tup in combinations(base,r):
                lo=frozenset(tup); hi=lo|{roots[v]}
                planned.append((len(lo),v,lo,hi))
    planned.sort(key=lambda z:(-z[0],z[1],tuple(sorted(z[2]))))
    collapses=0
    for _,v,lo,hi in planned:
        assert lo in current and hi in current, (v,lo,hi)
        # Free-face check in the current complex: every remaining coface of lo lies in hi.
        for tau in current:
            if lo <= tau:
                assert tau <= hi, (v,lo,hi,tau)
        current.remove(lo); current.remove(hi); collapses+=1
    target={frozenset([x]) for x in range(n)}
    target_edges=set()
    for v in range(n):
        r=roots[v]
        for x in adj[v]-{r}:
            target_edges.add(frozenset((r,x)))
    target |= target_edges
    assert current==target, (current^target)
    m=sum(len(N) for N in adj)//2
    assert len(target_edges)==2*m-n
    # Target graph must be connected because collapse preserves components and N(G) is connected
    # for connected nonbipartite G. Check directly here.
    tadj=[set() for _ in range(n)]
    for e in target_edges:
        a,b=tuple(e); tadj[a].add(b); tadj[b].add(a)
    seen={0}; q=[0]
    while q:
        a=q.pop()
        for b in tadj[a]:
            if b not in seen: seen.add(b); q.append(b)
    assert len(seen)==n
    beta=len(target_edges)-n+1
    assert beta==2*m-2*n+1
    return original,collapses,len(target_edges),beta

def root_choices(adj):
    return product(*[sorted(N) for N in adj])

def main():
    total_graphs=0; total_root_tests=0; total_collapses=0
    max_faces=0; beta_hist=Counter(); by_n=Counter()
    witness=None
    for n in range(3,7):
        pairs=list(combinations(range(n),2))
        for mask in range(1,1<<len(pairs)):
            edges=[pairs[i] for i in range(len(pairs)) if mask>>i & 1]
            if not connected(n,edges) or bipartite(n,edges) or not square_free(n,edges):
                continue
            adj=neighborhoods(n,edges)
            total_graphs+=1; by_n[n]+=1
            choices=list(root_choices(adj)) if n<=5 else [tuple(min(N) for N in adj)]
            for roots in choices:
                f,c,te,b=one_collapse_check(adj,roots)
                total_root_tests+=1; total_collapses+=c; max_faces=max(max_faces,f); beta_hist[b]+=1
                if witness is None or b>witness[0]:
                    witness=(b,n,len(edges),tuple(edges),roots,f,c,te)
    print('VERIFY_OK')
    print('qualifying_labeled_graphs',total_graphs)
    print('graphs_by_n',dict(sorted(by_n.items())))
    print('root_choice_tests',total_root_tests)
    print('elementary_collapses_checked',total_collapses)
    print('max_neighborhood_faces',max_faces)
    print('beta1_test_histogram',dict(sorted(beta_hist.items())))
    print('max_beta_witness',witness)

if __name__=='__main__': main()
