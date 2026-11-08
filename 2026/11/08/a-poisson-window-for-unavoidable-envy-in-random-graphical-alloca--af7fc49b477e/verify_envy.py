#!/usr/bin/env python3
"""Finite checks for minimum envy in graphical fair division."""
import itertools, math, random

def tree_component_count(n, edges):
    root=list(range(n)); size=[1]*n; counts=[0]*n
    def find(x):
        while root[x]!=x:
            root[x]=root[root[x]]; x=root[x]
        return x
    for a,b in edges:
        ra,rb=find(a),find(b)
        if ra!=rb:
            if size[ra]<size[rb]: ra,rb=rb,ra
            root[rb]=ra; size[ra]+=size[rb]
    for a,b in edges: counts[find(a)]+=1
    return sum(size[i]>1 and counts[i]==size[i]-1 for i in range(n) if root[i]==i)

def envy_count(n, edges, owners):
    # Binary utility: vertex values an edge iff it is incident to the edge.
    bag=[[0]*n for _ in range(n)]
    for j,(a,b) in enumerate(edges):
        owner=owners[j]
        bag[a][owner]+=1; bag[b][owner]+=1
    return sum(any(bag[i][other]>bag[i][i] for other in range(n)) for i in range(n))

def min_envy(n, edges, unrestricted=False):
    options=([tuple(range(n))]*len(edges) if unrestricted else edges)
    return min((envy_count(n,edges,owners) for owners in itertools.product(*options)),default=0)

def exhaustive():
    cnt=0; unrestricted=0
    for n in range(1,6):
        potential=list(itertools.combinations(range(n),2))
        for mask in range(1<<len(potential)):
            edges=[e for j,e in enumerate(potential) if mask>>j&1]
            target=tree_component_count(n,edges)
            assert min_envy(n,edges)==target,(n,edges,target)
            cnt+=1
            if n<=4:
                assert min_envy(n,edges,True)==target,(n,edges,target)
                unrestricted+=1
    print('PASS exact all simple graphs n<=5:',cnt, 'including unrestricted allocation checks n<=4:',unrestricted)

def factorial_moment(n,c,r):
    L=math.log(n)+math.log(math.log(n))+c
    p=L/(2*n)
    return (math.prod(n-j for j in range(2*r)) / 2**r *p**r*(1-p)**(2*r*(n-r-1)))

def sampled():
    rng=random.Random(431104)
    for n in [100,250,500]:
        p=(math.log(n)+math.log(math.log(n)))/(2*n)
        reps=1000
        no_envy=0; no_isolated_edge=0; other_tree=0
        for _ in range(reps):
            edges=[(i,j) for i in range(n) for j in range(i+1,n) if rng.random()<p]
            t=tree_component_count(n,edges)
            degree=[0]*n
            for i,j in edges:degree[i]+=1;degree[j]+=1
            isolated_edges=sum(degree[i]==degree[j]==1 for i,j in edges)
            no_envy+=t==0
            no_isolated_edge+=isolated_edges==0
            other_tree+=t>isolated_edges
        print('n',n,'expected isolated edge count',round(factorial_moment(n,0,1),5),
              'no unavoidable envy fraction',round(no_envy/reps,3),
              'no isolated edges fraction',round(no_isolated_edge/reps,3),
              'replications with larger tree component',other_tree)
    for r in [1,2,3]:
        print('isolated-edge factorial moment',r,'n=10000',round(factorial_moment(10000,0,r),6),
              'limit',round(4**(-r),6))
if __name__=='__main__':
    exhaustive()
    sampled()
