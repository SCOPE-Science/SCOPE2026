"""Deterministic finite checks of the stated parity and cycle formulas.
Exhaustive only over the generated finite test families; the theorem relies on a proof.
"""
from itertools import product
from math import prod
import random

def components(n,edges):
    parent=list(range(n))
    def root(i):
        while parent[i]!=i: i=parent[i]
        return i
    for a,b in edges:
        ra,rb=root(a),root(b)
        parent[ra]=rb
    classes={}
    for a in range(n): classes.setdefault(root(a),[])
    for i,(a,b) in enumerate(edges):classes[root(a)].append(i)
    return [a for a in classes.values() if a]

def count_min(n,edges):
    m=len(edges)
    degree=[0]*n
    for a,b in edges: degree[a]+=1;degree[b]+=1
    assert all(d%2==0 for d in degree)
    r=sum(len(C)%2 for C in components(n,edges))
    counts=[0]*(m+1)
    for mask in range(1<<m):
        red=[0]*n
        for i,(a,b) in enumerate(edges):
            if mask>>i&1:red[a]+=1;red[b]+=1
        if all(2*red[v]>=degree[v] for v in range(n)):
            counts[mask.bit_count()]+=1
    first=next(k for k,c in enumerate(counts) if c)
    assert first==(m+r)//2,(edges,first,m,r)
    for h in range(5):
        pred=((m+r)//2)<=((m+h+1)//2)
        # Can place any number of neutral goods on either side, and may add red edges.
        got=any(c and any(abs(2*(k+j)-(m+h))<=1 for j in range(h+1)) for k,c in enumerate(counts))
        assert pred==got,(edges,h,pred,got)
    return counts,r

def cycle(length,offset=0):
    return [(offset+i,offset+(i+1)%length) for i in range(length)]

def check_cycle_components(lengths):
    n=sum(lengths);edges=[];off=0
    for length in lengths:
        assert length>=3
        edges.extend(cycle(length,off));off+=length
    counts,r=count_min(n,edges)
    expected=prod((2 if k%2==0 else k) for k in lengths)
    assert counts[(len(edges)+r)//2]==expected,(lengths,counts,expected)
    return 1

def run():
    num=0
    for z in ([],[3],[4],[5],[6],[7],[3,3],[3,4],[4,4],[3,5],[3,3,3],[3,3,4]):
        if z:
            check_cycle_components(z);num+=1
    # Multigraphs formed by edge-disjoint closed walks (each vertex even degree).
    rng=random.Random(431117)
    for _ in range(750):
        n=rng.randint(3,7)
        edges=[]
        for _ in range(rng.randint(1,3)):
            length=rng.randint(2,min(n,5))
            vertices=rng.sample(range(n),length)
            edges += list(zip(vertices,vertices[1:]+vertices[:1]))
        if len(edges)>12:continue
        count_min(n,edges)
        num+=1
    print('PASS',num,'finite test graphs, including null-goods ranges h=0..4')
    # Sharp six-edge obstruction: two triangles and one indifferent second-group agent.
    edges=cycle(3,0)+cycle(3,3)
    counts,r=count_min(6,edges)
    assert r==2 and counts[3]==0 and counts[4]==3*3
    print('Sharp instance: two triangles, six valued goods; minimum preferred goods=4; optimal allocations=9; balanced=impossible; one neutral good suffices.')
if __name__=='__main__':run()

# Labeled undirected 2-regular graph enumeration and EGF check.
def random_graph_count_checks():
    from itertools import permutations
    from fractions import Fraction
    from collections import Counter
    from math import factorial
    D=[Fraction(0)]*9;D[0]=Fraction(1)
    E=[Fraction(0)]*5;E[0]=Fraction(1)
    for n in range(3,9):D[n]=sum(D[:n-2],Fraction(0))/(2*n)
    for s in range(2,5):E[s]=sum(E[:s-1],Fraction(0))/(4*s)
    checked=0
    for n in range(3,9):
        seen=set()
        for p in permutations(range(n)):
            # Cycle decomposition of a permutation, retain all cycles of length >=3.
            used=set(); good=True; edges=[]
            for v in range(n):
                if v in used:continue
                c=[];u=v
                while u not in used:
                    used.add(u);c.append(u);u=p[u]
                if len(c)<3:good=False;break
                edges.extend(tuple(sorted((c[i],c[(i+1)%len(c)]))) for i in range(len(c)))
            if good:seen.add(tuple(sorted(edges)))
        fav=0
        for e in seen:
            r=sum(len(comp)%2 for comp in components(n,e))
            fav+=int(r<=1)
        s=n//2
        favorable = E[s] if n%2==0 else sum((E[s-k]/(2*(2*k+1)) for k in range(1,s+1)),Fraction(0))
        assert len(seen)==factorial(n)*D[n],(n,len(seen),factorial(n)*D[n])
        assert fav==factorial(n)*favorable,(n,fav,factorial(n)*favorable)
        checked+=len(seen)
    print('PASS',checked,'labeled simple 2-regular graphs n=3..8 against exact EGF numerator and denominator')

if __name__=='__main__':random_graph_count_checks()
