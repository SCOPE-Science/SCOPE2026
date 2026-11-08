#!/usr/bin/env python3
"""Reproduce finite-size laws for nearest-neighbor walk attachment trees."""
from fractions import Fraction
from collections import defaultdict
from math import factorial


def eulerian(m):
    row=[1]
    for n in range(2,m+1):
        row=[(k+1)*(row[k] if k<len(row) else 0)+(n-k)*(row[k-1] if k>0 else 0) for k in range(n)]
    return row

def tree_laws(walk_steps,max_n=6):
    # Each state is the tuple of parents of vertices 3,4,...,n (zero-based).
    # Roots 0 and 1 are joined by the initial edge.
    states={():Fraction(1)}
    check_count=0
    for n in range(2,max_n+1):
        dist=defaultdict(Fraction)
        for parents,p in states.items():
            edges=[(0,1)]+[(j+2,parents[j]) for j in range(n-2)]
            adj=[[] for _ in range(n)]
            for u,v in edges: adj[u].append(v);adj[v].append(u)
            color=[None]*n;color[0]=0
            todo=[0]
            for u in todo:
                for v in adj[u]:
                    if color[v] is None:color[v]=1-color[u];todo.append(v)
            assert len(todo)==n
            dist[color.count(0)]+=p
            check_count+=1
        assert sum(dist.values())==1
        a=[dist[k] for k in range(1,n)]
        if walk_steps%2:
            target=[Fraction(1,n-1)]*(n-1)
        else:
            target=[Fraction(x,factorial(n-1)) for x in eulerian(n-1)]
        assert a==target,(walk_steps,n,a,target)
        if n==max_n:break
        next_states=defaultdict(Fraction)
        for parents,p in states.items():
            edges=[(0,1)]+[(j+2,parents[j]) for j in range(n-2)]
            adj=[[] for _ in range(n)]
            for u,v in edges:adj[u].append(v);adj[v].append(u)
            endpoints=defaultdict(Fraction)
            for start in range(n):
                cur={start:Fraction(1,n)}
                for _ in range(walk_steps):
                    new=defaultdict(Fraction)
                    for v,mass in cur.items():
                        for w in adj[v]:new[w]+=mass/len(adj[v])
                    cur=new
                for v,mass in cur.items(): endpoints[v]+=mass
            assert sum(endpoints.values())==1
            for parent,mass in endpoints.items():
                next_states[parents+(parent,)]+=p*mass
        states=next_states
    return check_count

if __name__=='__main__':
    total=0
    for k in range(4):
        c=tree_laws(k,6);total+=c
        print('walk length',k,'exact states checked',c)
    print('all',total,'exact rational finite-state checks passed')
