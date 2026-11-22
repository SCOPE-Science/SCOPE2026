#!/usr/bin/env python3
"""Independent finite checks for the edge-cover boundary-twist identity.
No external packages; finite checks are not used as proof for all n.
"""
from collections import defaultdict
from itertools import combinations


def graph(n, twist=False):
    # Each edge is (endpoint, endpoint, weight-kind, column).
    edges=[]
    for i in range(n):
        edges.append(((i,0),(i,1),'rung',i))
        for row in range(2):
            j=(i+1)%n
            target=row if (i<n-1 or not twist) else 1-row
            edges.append(((i,row),(j,target),'rail',i))
    assert len(edges)==3*n
    assert len({frozenset((a,b)) for a,b,_,_ in edges})==3*n
    assert all(sum(a==v or b==v for a,b,_,_ in edges)==3
               for v in [(i,r) for i in range(n) for r in range(2)])
    # Triangle-free, necessary for the triangle/3-star identification in the line graph.
    es={frozenset((a,b)) for a,b,_,_ in edges}
    verts=[(i,r) for i in range(n) for r in range(2)]
    assert all(not(all(frozenset(x) in es for x in combinations(t,2)))
               for t in combinations(verts,3))
    return edges


def covers(n, twist=False, weights=None):
    edges=graph(n,twist)
    m=len(edges)
    degree_counts=defaultdict(int)
    total_weight=0
    adjacency_of_e=[]
    for a,b,_,_ in edges:
        adjacency_of_e.append((1<<(2*a[0]+a[1]))|(1<<(2*b[0]+b[1])))
    full=(1<<(2*n))-1
    if weights is None:
        edge_weights=[1]*m
    else:
        u,v=weights
        edge_weights=[v[i] if kind=='rung' else u[i] for _,_,kind,i in edges]
    for mask in range(1<<m):
        occupied=0
        num=0
        w=1
        for i in range(m):
            if mask>>i&1:
                occupied |= adjacency_of_e[i]
                num+=1
                if weights is not None:w*=edge_weights[i]
        if occupied==full:
            degree_counts[num]+=1
            total_weight+=w
    return dict(degree_counts),total_weight


def transfer(n, twist, weights):
    u,v=weights
    states=((0,0),(0,1),(1,0),(1,1))
    A=[[int(i==j) for j in range(4)] for i in range(4)]
    for i in range(n):
        M=[[u[i]**(t[0]+t[1])*(v[i]+int((s[0] or t[0]) and (s[1] or t[1])))
             for t in states] for s in states]
        A=[[sum(A[a][k]*M[k][b] for k in range(4)) for b in range(4)] for a in range(4)]
    return sum(A[i][(0,2,1,3)[i] if twist else i] for i in range(4))


def main():
    for n in (4,5,6):
        c,ct=covers(n,False)
        d,dt=covers(n,True)
        assert set(c)|set(d)==set(range(n,3*n+1)),(n,c,d)
        delta={k:c.get(k,0)-d.get(k,0) for k in sorted(set(c)|set(d))}
        assert {k:v for k,v in delta.items() if v}=={n:2*(-1)**n},(n,delta)
        assert ct-dt==2*(-1)**n
        print(f'n={n} edges={3*n} cover_total_prism={ct} cover_total_twist={dt} delta={ct-dt} nonzero_coeff={{ {n}: {2*(-1)**n} }}')
        if n<=5:
            # Independent triangle-avoidance interpretation on line-graph vertex subsets.
            for twist,expected in ((False,c),(True,d)):
                edges=graph(n,twist)
                m=len(edges)
                tris=[]
                for e1,e2,e3 in combinations(range(m),3):
                    inds=(e1,e2,e3)
                    if all(set(edges[i][:2]) & set(edges[j][:2]) for i,j in combinations(inds,2)):
                        tris.append(sum(1<<e for e in inds))
                by_nonadj=defaultdict(int)
                for s in range(1<<m):
                    # s is the set of new-point neighbors; its complement are non-neighbors.
                    if all(s&t!=t for t in tris):
                        by_nonadj[m-s.bit_count()]+=1
                assert dict(by_nonadj)==expected, (n,twist)
                print(f'  n={n}, twist={twist}: all {1<<m} line-graph assignments checked')
    for n in (4,5):
        u=[2,3,5,7,11][:n]
        v=[11,13,17,19,23][:n]
        weights=(u,v)
        w0=covers(n,False,weights)[1]
        w1=covers(n,True,weights)[1]
        assert w0==transfer(n,False,weights)
        assert w1==transfer(n,True,weights)
        assert w0-w1==2*(-1)**n*__import__('math').prod(u)
        print(f'n={n} arbitrary site weights: weighted identity verified, delta={w0-w1}')
    for n in range(4,13):
        u=[i+2 for i in range(n)]
        v=[i*i+3 for i in range(n)]
        t0=transfer(n,False,(u,v)); t1=transfer(n,True,(u,v))
        assert t0-t1==2*(-1)**n*__import__('math').prod(u)
    print('All checker assertions passed; all-order proof is algebraic, not finite extrapolation.')

if __name__=='__main__': main()
