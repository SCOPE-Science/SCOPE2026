#!/usr/bin/env python3
"""Independent finite certificates for clique-fiber graph-metric Rips collapses.
Only standard-library modules are used. This program verifies illustrative finite
instances; the universal assertion requires the accompanying mathematical proof.
"""
from collections import deque
from itertools import combinations
from math import comb


def graphs():
    out=[]
    out.append(('edge', 2, [(0,1)]))
    out.append(('path_6', 6, [(i,i+1) for i in range(5)]))
    out.append(('star_4', 5, [(0,i) for i in range(1,5)]))
    out.append(('cycle_7', 7, [(i,(i+1)%7) for i in range(7)]))
    out.append(('cycle_8', 8, [(i,(i+1)%8) for i in range(8)]))
    out.append(('cycle_9', 9, [(i,(i+1)%9) for i in range(9)]))
    # Three length-four internally disjoint paths, girth 8.
    paths=[[0,2,3,4,1],[0,5,6,7,1],[0,8,9,10,1]]
    out.append(('theta_4_4_4',11,[tuple(sorted((p[i],p[i+1]))) for p in paths for i in range(4)]))
    # Two seven-cycles meeting at exactly their first vertex.
    edges=[]
    for branch in [[0,1,2,3,4,5,6],[0,7,8,9,10,11,12]]:
        edges += [tuple(sorted((branch[i],branch[(i+1)%7]))) for i in range(7)]
    out.append(('figure_eight_7_7', 13, edges))
    return out


def distances(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    dd=[]
    for z in range(n):
        d=[n+1]*n; d[z]=0; q=deque([z])
        while q:
            w=q.popleft()
            for t in adj[w]:
                if d[t]>d[w]+1:
                    d[t]=d[w]+1; q.append(t)
        assert max(d)<=n
        dd.append(d)
    return adj, dd


def all_faces(n, q, dd):
    vertices=range(n*q)
    adj=[set() for _ in vertices]
    for a in vertices:
        for b in range(a+1,n*q):
            if dd[a//q][b//q]+int(a%q!=b%q)<=2:
                adj[a].add(b)
    faces={frozenset()}
    def visit(s, choices):
        for k,x in enumerate(choices):
            t=s|{x}; faces.add(t)
            visit(t,[y for y in choices[k+1:] if y in adj[x]])
    visit(frozenset(),list(vertices))
    return faces


def face_union(carriers):
    faces={frozenset()}
    for verts in carriers:
        t=sorted(verts)
        for k in range(1,len(t)+1):
            for f in combinations(t,k): faces.add(frozenset(f))
    return faces


def apply_pair(current,lower,upper):
    assert lower in current and upper in current and len(upper)==len(lower)+1
    assert lower < upper
    # A codimension-one coface besides upper would obstruct an elementary collapse.
    universe={z for f in current for z in f}
    immediate=[lower|{w} for w in universe-lower if lower|{w} in current]
    assert immediate == [upper], ('not_free', tuple(sorted(lower)),immediate)
    current.remove(lower);current.remove(upper)


def verify_graph(name, n, edges, q):
    adj,dd=distances(n,edges)
    X=all_faces(n,q,dd)
    base_facets=[]
    for u,v in edges:
        base_facets.append({u*q+a for a in range(q)}|{v*q+a for a in range(q)})
    for v in range(n):
        for a in range(q):
            base_facets.append({v*q+b for b in range(q)} | {u*q+a for u in adj[v]})
    assert X==face_union(base_facets),(name,q,'carrier cover',len(X),len(face_union(base_facets)))
    current=set(X); count=0
    # Local star private-face matching: toggle the same-color hub vertex.
    for v in range(n):
        for a in range(q):
            p=v*q+a
            fib=[v*q+b for b in range(q) if b!=a]
            nbr=[u*q+a for u in adj[v]]
            lowers=[]
            for k in range(2,len(nbr)+1):
                for T in combinations(nbr,k):
                    for j in range(len(fib)+1):
                        for B in combinations(fib,j): lowers.append(frozenset(T+B))
            for f in sorted(lowers,key=lambda z:-len(z)):
                apply_pair(current,f,f|{p});count+=1
    core=face_union(base_facets[:len(edges)])
    assert current==core,(name,q,'residual_core',len(current),len(core))
    count1=count
    # Dominated vertices: delete every non-first color in each fiber.
    for v in range(n):
        for a in range(1,q):
            x=v*q+a; y=v*q
            lowers=[f for f in current if x in f and y not in f]
            for f in sorted(lowers,key=lambda z:-len(z)):
                apply_pair(current,f,f|{y});count+=1
    target={frozenset()}|{frozenset({v*q}) for v in range(n)}|{frozenset({u*q,v*q}) for u,v in edges}
    assert current==target,(name,q,'target',len(current),len(target))
    b1=len(edges)-n+1
    initial_b1=q*len(edges)-n+1
    expected_first=q*2**(q-1)*sum(2**len(adj[v])-len(adj[v])-1 for v in range(n))
    assert count1==expected_first
    assert 2*count+len(current)==len(X)
    print(f'{name} width={q}: faces={len(X)} first_stage_pairs={count1} total_pairs={count} b1_before={initial_b1} b1_after={b1}')


def main():
    count=0
    for name,n,edges in graphs():
        for q in (2,3,4):
            if name in ('cycle_9','figure_eight_7_7') and q==4:
                continue
            verify_graph(name,n,edges,q);count+=1
    print(f'VERIFY_OK {count} complete independent face-cover and elementary-collapse certificates')

if __name__=='__main__':
    main()
