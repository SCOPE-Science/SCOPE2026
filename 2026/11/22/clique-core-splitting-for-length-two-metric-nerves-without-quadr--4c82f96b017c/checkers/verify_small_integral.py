#!/usr/bin/env python3
"""Integral chain checks of selected quadrilateral-free graph length-two tuple nerves.
Run: python3 verify_small_integral.py
Requires: sympy.
"""
from itertools import permutations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def calculate(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    triangles=sum(len(adj[a]&adj[b]) for a,b in edges)//3
    pairs=set(tuple(sorted(e)) for e in edges)
    for b in range(n):
        for a in adj[b]:
            for c in adj[b]:
                if a!=c:pairs.add(tuple(sorted((a,c))))
    cells1=[(a,b) for a,b in permutations(range(n),2) if tuple(sorted((a,b))) in pairs]
    cells2=[(a,b,c) for a in range(n) for b in sorted(adj[a]) for c in sorted(adj[b])]
    index={edge:j for j,edge in enumerate(cells1)}
    d2=Matrix.zeros(len(cells1),len(cells2))
    for j,(a,b,c) in enumerate(cells2):
        d2[index[(b,c)],j]+=1
        if a!=c: d2[index[(a,c)],j]-=1
        d2[index[(a,b)],j]+=1
    d1=Matrix.zeros(n,len(cells1))
    for j,(a,b) in enumerate(cells1):
        d1[a,j]-=1;d1[b,j]+=1
    assert d1*d2==Matrix.zeros(n,len(cells2))
    s=smith_normal_form(d2,domain=ZZ)
    diag=[abs(int(s[i,i])) for i in range(min(s.rows,s.cols)) if s[i,i]]
    assert all(d==1 for d in diag),diag
    b1=len(cells1)-(n-1)-len(diag)
    b2=len(cells2)-len(diag)
    assert (b1,b2)==(len(edges)-n+1-triangles,len(edges)+5*triangles)
    return b1,b2,len(cells1),len(cells2),len(diag)

def main():
    tests={
      'triangle':(3,[(0,1),(1,2),(0,2)]),
      'pentagon':(5,[(0,1),(1,2),(2,3),(3,4),(0,4)]),
      'triangular friendship':(5,[(0,1),(1,2),(0,2),(0,3),(3,4),(0,4)]),
      'pentagon sharing an edge with a triangle':(6,[(0,1),(1,2),(2,3),(3,4),(0,4),(0,5),(1,5)]),
      'triangle with an attached path':(6,[(0,1),(1,2),(0,2),(0,3),(3,4),(4,5)]),
    }
    for name,(n,edges) in tests.items():
        print(name, 'n=',n,'e=',len(edges),'(H1,H2,#C1,#C2,rank d2)=',calculate(n,edges))
    print('All selected Smith nonzero invariant factors equal one; d1*d2=0.')
if __name__=='__main__':main()
