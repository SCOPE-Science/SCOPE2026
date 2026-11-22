#!/usr/bin/env python3
"""Independent local-coloring constraint check for graph families from first principles."""
from itertools import combinations, product


def graph(name):
    if name.startswith('J'):
        n = int(name[1:])
        vertices = list(combinations(range(n), 2))
        return [[j for j, B in enumerate(vertices) if i != j and (a in B or b in B)]
                for i, (a,b) in enumerate(vertices)]
    if name.startswith('friend'):
        m = int(name[6:]); n = 2*m+1
        ans = [[] for _ in range(n)]
        for j in range(m):
            u,v=2*j+1,2*j+2
            for x,y in ((0,u),(0,v),(u,v)):
                ans[x].append(y);ans[y].append(x)
        return ans
    if name=='K3C3':
        return [[b*3+t for b in range(3) if b!=a]+[a*3+((t+1)%3),a*3+((t-1)%3)]
                 for a in range(3) for t in range(3)]
    if name=='K3C4':
        return [[b*4+t for b in range(3) if b!=a]+[a*4+((t+1)%4),a*4+((t-1)%4)]
                 for a in range(3) for t in range(4)]
    raise ValueError(name)


def count_balanced(adj):
    n=len(adj)
    ans=0
    for colors in product(range(3), repeat=n):
        if all(len(adj[v])%2 == 0 and
               sum(colors[w] == (colors[v]+1)%3 for w in adj[v]) == len(adj[v])//2 and
               sum(colors[w] == (colors[v]+2)%3 for w in adj[v]) == len(adj[v])//2
               for v in range(n)):
            ans+=1
    return ans


def run():
    for name, expected in [('J4',6),('J5',0),('K3C3',12),('K3C4',0),('friend3',24)]:
        actual=count_balanced(graph(name))
        print(name,'balanced_phase_configurations',actual)
        assert actual==expected
    print('ALL_COLOR_CHECKS_PASS')
if __name__=='__main__': run()
