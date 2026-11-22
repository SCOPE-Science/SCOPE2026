"""Exhaustive original-graph min-FVS token-sliding and odd-girth test.
Python 3.9+, standard library only. Run: python check_finite.py
"""
from itertools import combinations
from collections import deque

def graph(n):
    # Completely separate integer modulo 2n model (circumference plus antipodes)
    N=2*n
    E={tuple(sorted((i,(i+1)%N))) for i in range(N)}
    E|={tuple(sorted((i,(i+n)%N))) for i in range(N)}
    return N,sorted(E)

def forest(N, E, removed):
    parent=list(range(N))
    def find(x):
        while parent[x]!=x: x=parent[x]
        return x
    for a,b in E:
        if a in removed or b in removed:continue
        x,y=find(a),find(b)
        if x==y:return False
        parent[x]=y
    return True

def min_states(n):
    N,E=graph(n)
    for k in range(0,N+1):
        sets=[frozenset(comb) for comb in combinations(range(N),k) if forest(N,E,set(comb))]
        if sets:return k,sets,E
    raise AssertionError('impossible')

def odd_girth(adj):
    # BFS in bipartite parity lift; shortest odd closed walk has a simple odd cycle
    best=None
    for start in range(len(adj)):
        q=deque([(start,0)])
        seen={(start,0):0}
        while q:
            v,p=q.popleft(); d=seen[v,p]
            if best is not None and d+1>=best:continue
            for w in adj[v]:
                if w==start and p==0:best=d+1;break
                np=1-p
                if (w,np) not in seen:
                    seen[w,np]=d+1;q.append((w,np))
        # Best already found at this starting node or remains None
    return best

if __name__=='__main__':
    expected={3:(2,6,None),4:(3,32,5),5:(3,20,None),6:(4,132,7),7:(4,56,None),8:(5,448,9)}
    for n,(k0,count0,g0) in expected.items():
        k,states,E=min_states(n)
        d={s:i for i,s in enumerate(states)}
        adj=[set() for _ in states]
        for i,s in enumerate(states):
            for a,b in E:
                if (a in s) != (b in s):
                    t=frozenset(s.symmetric_difference((a,b)))
                    j=d.get(t)
                    if j is not None: adj[i].add(j)
        got=odd_girth(adj)
        assert (k,len(states),got)==(k0,count0,g0),(n,k,len(states),got)
        print(f'n={n}: minimum size={k}, optima={len(states)}, edges={sum(map(len,adj))//2}, shortest odd cycle={got or "none"}')
    print('PASS: exhaustive six original-graph instances, minimum verification from all smaller subsets')
