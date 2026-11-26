"""Standalone finite checks for general-position games on Cartesian grids.
Uses BFS graph distances and recursive exact minimax, not the proof's corner antichain argument.
No third-party dependencies. Run: python3 verify_grid_game.py
"""
from collections import deque
from functools import lru_cache
from math import comb


def check(m, n):
    N = m*n
    adj = [[] for _ in range(N)]
    for i in range(m):
        for j in range(n):
            u=i*n+j
            for a,b in ((i+1,j),(i,j+1)):
                if a<m and b<n:
                    v=a*n+b
                    adj[u].append(v)
                    adj[v].append(u)
    dist=[]
    for s in range(N):
        d=[-1]*N
        d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==-1:
                    d[v]=d[u]+1
                    q.append(v)
        assert all(x>=0 for x in d)
        dist.append(d)
    forbidden=[]
    for a in range(N):
        for b in range(a+1,N):
            for c in range(b+1,N):
                if (dist[a][b]+dist[b][c]==dist[a][c] or
                    dist[a][c]+dist[c][b]==dist[a][b] or
                    dist[b][a]+dist[a][c]==dist[b][c]):
                    forbidden.append((1<<a)|(1<<b)|(1<<c))
    forbidden_by=[[] for _ in range(N)]
    for t in forbidden:
        for i in range(N):
            if t>>i&1:
                forbidden_by[i].append(t & ~(1<<i))
    @lru_cache(None)
    def legal(mask, x):
        return not any(mask&b == b for b in forbidden_by[x])
    @lru_cache(None)
    def solve(mask,turn):
        choices=[solve(mask | (1<<v),1-turn) for v in range(N) if not mask>>v&1 and legal(mask,v)]
        if not choices: return mask.bit_count()
        return max(choices) if turn==0 else min(choices)
    actual=(solve(0,0),solve(0,1))
    expected=(2,2 if m==n==2 else 3)
    assert actual==expected, (m,n,actual,expected)
    for corner in (0,n-1,(m-1)*n,N-1):
        gp_triples=0
        maximal_pairs=set()
        for x in range(N):
            if x==corner:continue
            s=(1<<corner)|(1<<x)
            options=[y for y in range(N) if not s>>y&1 and legal(s,y)]
            if not options:maximal_pairs.add(x)
            else:
                gp_triples+=len(options)
                # Every three-set containing a corner is maximal.
                for y in options:
                    t=s|(1<<y)
                    assert not any(not t>>z&1 and legal(t,z) for z in range(N))
        gp_triples//=2
        assert gp_triples==comb(m,2)*comb(n,2)-(m-1)*(n-1), (m,n,gp_triples)
        assert len(maximal_pairs)==3,(m,n,maximal_pairs)
    return N, solve.cache_info().currsize


if __name__=='__main__':
    cases=[(m,n) for m in range(2,6) for n in range(m,7)]
    cases += [(2,7),(2,8),(3,7),(3,8)]
    states=0
    for m,n in cases:
        N,z=check(m,n)
        states+=z
        print(f"PASS m={m} n={n} vertices={N} minimax_states={z}")
    print(f"VERIFICATION_OK graph_cases={len(cases)} total_minimax_states={states} corner_classifications={4*len(cases)}")
