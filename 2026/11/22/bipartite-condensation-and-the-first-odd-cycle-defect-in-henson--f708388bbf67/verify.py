#!/usr/bin/env python3
"""Independent direct and inclusion-exclusion checks for triangle-free tuple-type spectra."""
from itertools import product
from collections import Counter
from math import comb


def edge_list_c5():
    return [(i,(i+1)%5) for i in range(5)]

def is_independent(mask, edges):
    return all(not ((mask >> i) & (mask >> j) & 1) for i,j in edges)

def independent_count(mask,edges):
    sub=mask; count=0
    while True:
        count+=is_independent(sub,edges)
        if sub==0:break
        sub=(sub-1)&mask
    return count

def surjective_count(mask,n,edges):
    sub=mask; count=0
    while True:
        count+=(-1)**((mask^sub).bit_count())*independent_count(sub,edges)**n
        if sub==0:break
        sub=(sub-1)&mask
    return count

def exact_count(edges,r,n):
    F=[surjective_count(mask,n,edges) for mask in range(1<<r)]
    result=0
    for assign in product((0,1,2),repeat=r):
        A=sum(1<<j for j,v in enumerate(assign) if v==1)
        B=sum(1<<j for j,v in enumerate(assign) if v==2)
        result+=F[A]*F[B]
    return result

def direct_count(edges,r,n):
    # Base vertex bit positions 0..n-1 in shore A, n..2n-1 in shore B.
    opts=[0]+list(range(1,1<<n))+[m<<n for m in range(1,1<<n)]
    result=0
    for neigh in product(opts,repeat=r):
        if all(not(neigh[i]&neigh[j]) for i,j in edges):
            result+=1
    return result

def triangle_free_graphs(r):
    pairs=[(i,j) for i in range(r) for j in range(i+1,r)]
    for mask in range(1<<len(pairs)):
        E=[p for idx,p in enumerate(pairs) if mask>>idx&1]
        adj={(min(a,b),max(a,b)) for a,b in E}
        if any((i,j) in adj and (j,k) in adj and (i,k) in adj for i in range(r) for j in range(i+1,r) for k in range(j+1,r)):
            continue
        yield E

def no_triangle_on_new_and_base(neigh,internal,r):
    return all((neigh[i]&neigh[j])==0 for i,j in internal)

def direct_total(r,n):
    opts=[0]+list(range(1,1<<n))+[m<<n for m in range(1,1<<n)]
    graphs=list(triangle_free_graphs(r))
    total=0
    for neigh in product(opts,repeat=r):
        total+=sum(no_triangle_on_new_and_base(neigh,E,r) for E in graphs)
    return total

def coefficient_exponential(edges,r):
    result=Counter()
    for assign in product((0,1,2),repeat=r):
        A=sum(1<<j for j,v in enumerate(assign) if v==1)
        B=sum(1<<j for j,v in enumerate(assign) if v==2)
        subA=A
        while True:
            subB=B
            while True:
                b=independent_count(subA,edges)*independent_count(subB,edges)
                sign=(-1)**((A^subA).bit_count()+(B^subB).bit_count())
                result[b]+=sign
                if subB==0:break
                subB=(subB-1)&B
            if subA==0:break
            subA=(subA-1)&A
    return dict(sorted((k,v) for k,v in result.items() if v))

def is_bipartite(edges,r):
    adjacency=[[] for _ in range(r)]
    for i,j in edges:
        adjacency[i].append(j)
        adjacency[j].append(i)
    colors=[-1]*r
    for start in range(r):
        if colors[start]!=-1:continue
        colors[start]=0
        stack=[start]
        while stack:
            v=stack.pop()
            for u in adjacency[v]:
                if colors[u]==-1:
                    colors[u]=1-colors[v]
                    stack.append(u)
                elif colors[u]==colors[v]:
                    return False
    return True

def defect_coefficient(r):
    coefficient=0
    graph_types=Counter()
    for E in triangle_free_graphs(r):
        if is_bipartite(E,r):
            continue
        count=sum(sum(((mask>>i)&1)==((mask>>j)&1) for i,j in E)==1
                  for mask in range(1<<r))
        graph_types[(len(E),count)]+=1
        coefficient+=count
    return coefficient, graph_types

def check():
    cyc=edge_list_c5()
    for n in [0,1,2,3]:
        a=exact_count(cyc,5,n)
        if n<=3:
            b=direct_count(cyc,5,n)
            assert a==b,(n,a,b)
        print('C5_FIXED',n,a)
    poly=coefficient_exponential(cyc,5)
    print('C5_EXPONENTIAL_POLYNOMIAL',poly)
    assert poly[24]==10
    assignment_bases=Counter()
    optimal=[]
    for col in product((0,1),repeat=5):
        A=sum(1<<i for i,v in enumerate(col) if v==0)
        B=31^A
        base=independent_count(A,cyc)*independent_count(B,cyc)
        assignment_bases[base]+=1
        if base==24:
            mono=[(i,j) for i,j in cyc if col[i]==col[j]]
            assert len(mono)==1
            optimal.append(mono[0])
    assert assignment_bases==Counter({24:10,16:10,15:10,11:2})
    assert all(optimal.count(edge)==2 for edge in cyc)
    print('COLORING_PARTITION_BASES',dict(assignment_bases))
    print('UNIFORM_DEFECT_EDGES', dict(Counter(optimal)))
    assert max(poly)==24
    assert max(k for k in poly if k<24)==15
    assert sum(poly.values())==1  # zero old parameters: one fixed internal graph
    for n in (1,2,3,4,5,8,12):
        count=exact_count(cyc,5,n)
        check=sum(coef*base**n for base,coef in poly.items())
        assert count==check
        print('C5_RATIO_TO_24_POWER',n,count/24**n)
    for r,n in [(2,1),(3,1),(4,1),(5,1),(3,2)]:
        a=sum(exact_count(E,r,n) for E in triangle_free_graphs(r))
        b=direct_total(r,n)
        assert a==b,(r,n,a,b)
        print('TOTAL_DIRECT',r,n,a)
    for r in range(1,7):
        theta=sum(comb(r,j)*2**(j*(r-j)) for j in range(r+1))
        print('LIMIT_NORMALIZER',r,theta)
    assert sum(comb(5,j)*2**(j*(5-j)) for j in range(6))==1442
    assert defect_coefficient(5)[0]==120
    a6,profiles=defect_coefficient(6)
    assert a6==6120
    assert profiles==Counter({(5,20):72,(6,10):360,(7,6):180})
    print('ODD_DEFECT_COEFFICIENTS',120,a6,dict(profiles))
    print('VERIFY_OK')

if __name__=='__main__':check()
