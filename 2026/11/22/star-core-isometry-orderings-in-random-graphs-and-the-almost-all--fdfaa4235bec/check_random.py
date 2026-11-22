"""Deterministic-seed empirical corroboration; NOT a proof of the limit law."""
from collections import deque
import random

def distances(g, subset):
    selected = set(subset)
    out = {}
    for x in selected:
        d = {x: 0}
        q = deque([x])
        while q:
            u = q.popleft()
            for w in g[u] & selected:
                if w not in d:
                    d[w] = d[u] + 1
                    q.append(w)
        out[x] = d
    return out

def certificate(g,v):
    n=len(g)
    w=g[v] | {v}
    for x in range(n):
        for y in range(x+1,n):
            if y not in g[x] and not (g[x] & g[y] & w):
                return False
    return True

def random_graph(n,p,rng):
    a=[set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if rng.random()<p:
                a[i].add(j)
                a[j].add(i)
    return a

def run():
    rng=random.Random(20261121)
    tested=0; certified=0
    for n,p,reps in ((7,0.75,200),(9,0.70,200),(12,0.75,100),(16,0.70,100),(20,0.75,30)):
        for _ in range(reps):
            g=random_graph(n,p,rng)
            full=distances(g,range(n))
            for v in range(n):
                if not certificate(g,v): continue
                certified+=1
                near=list(g[v]);far=list(set(range(n))-{v}-g[v])
                rng.shuffle(near);rng.shuffle(far)
                ordering=[v]+near+far
                for k in range(1,n+1):
                    selected=ordering[:k]
                    local=distances(g,selected)
                    for x in selected:
                        for y in selected:
                            assert local[x].get(y)==full[x].get(y),(n,p,v,k,x,y)
            tested+=1
    assert certified>0
    print(f"PASS {tested} seeded random graphs; {certified} independently certified centers, every prefix BFS-checked")
if __name__=='__main__':run()
