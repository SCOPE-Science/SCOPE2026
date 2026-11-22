"""Direct finite verification of minimum-cut reconfiguration on rectangular grids.

Python standard library only. Run: python3 verify_grid_bruteforce.py
"""
from collections import deque
from itertools import combinations


def neighbor_list(n, w):
    v = n*w
    adj = [[] for _ in range(v)]
    for y in range(w):
        for x in range(n):
            i = y*n+x
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                X,Y=x+dx,y+dy
                if 0<=X<n and 0<=Y<w: adj[i].append(Y*n+X)
    return adj


def disconnected(adj, s, t, removed):
    seen={s}; q=deque([s])
    while q:
        v=q.popleft()
        for u in adj[v]:
            if u not in seen and u not in removed:
                seen.add(u); q.append(u)
    return t not in seen


def predicted(n,w,r):
    result=set()
    for b in range(1,n-1):
        for a in range(max(0,b-1),min(n,b+2)):
            if r>=2 and a not in (0,n-1): continue
            for c in range(max(0,b-1),min(n,b+2)):
                if r<=w-3 and c not in (0,n-1): continue
                result.add(frozenset((n*(r-1)+a,n*r+b,n*(r+1)+c)))
    return result


def components(states,edges):
    links={x:set() for x in states}
    for a,b in edges: links[a].add(b);links[b].add(a)
    out=[]; unseen=set(states)
    while unseen:
        z=next(iter(unseen)); Q=[z];unseen.remove(z); comp={z}
        for t in Q:
            for u in links[t]:
                if u in unseen: unseen.remove(u);comp.add(u);Q.append(u)
        out.append(comp)
    return sorted([len(c) for c in out]),links


def predicted_metrics(n,w,r):
    if r in (1,w-2):
        return (6,4,[3,3],9 if n==3 else 6,[6] if n==3 else [3,3])
    if n==3: return (4,0,[1]*4,4,[4])
    return (2,0,[1,1],0,[1,1])


def check_one(n,w,r):
    adj=neighbor_list(n,w);s=n*r;t=n*r+n-1
    allowed=[v for v in range(n*w) if v not in (s,t)]
    assert not any(disconnected(adj,s,t,frozenset(X)) for k in range(3) for X in combinations(allowed,k))
    cuts=set()
    for triple in combinations(allowed,3):
        S=frozenset(triple)
        if disconnected(adj,s,t,S):cuts.add(S)
    theory=predicted(n,w,r)
    assert cuts==theory,(n,w,r,'missing',theory-cuts,'extra',cuts-theory)
    slides=set();jumps=set()
    for S in cuts:
        for v in S:
            for u in range(n*w):
                if u in S: continue
                T=frozenset((S-{v})|{u})
                if T not in cuts: continue
                e=frozenset((S,T))
                jumps.add(e)
                if u in adj[v]: slides.add(e)
    sm, _=components(cuts,slides)
    jm,jadj=components(cuts,jumps)
    N,E,SC,JE,JC=predicted_metrics(n,w,r)
    assert (len(cuts),len(slides),sm,len(jumps),jm)==(N,E,SC,JE,JC), (n,w,r,len(cuts),len(slides),sm,len(jumps),jm)
    if r in (1,w-2) and n==3: assert all(len(jadj[S])==3 for S in cuts)
    if r not in (1,w-2) and n==3: assert all(len(jadj[S])==2 for S in cuts)
    return len(cuts)


def main():
    test_count=0
    for w in range(4,8):
        for n in range(3,7):
            for r in range(1,w-1):
                check_one(n,w,r); test_count+=1
    print('BRUTE_FORCE_PASS',test_count,'rectangular-grid/terminal-row instances; sizes 0,1,2,3 verified; both reconfiguration graphs verified')


if __name__=='__main__':main()
