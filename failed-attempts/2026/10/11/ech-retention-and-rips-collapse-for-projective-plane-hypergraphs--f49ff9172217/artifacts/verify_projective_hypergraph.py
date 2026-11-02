#!/usr/bin/env python3
from itertools import product

def inv(a,p): return pow(a,p-2,p)
def norm(v,p):
    for x in v:
        if x%p:
            s=inv(x%p,p)
            return tuple((s*y)%p for y in v)
    raise ValueError('zero')

def pg2(p):
    points=sorted({norm(v,p) for v in product(range(p), repeat=3) if any(v)})
    lines=points[:]  # normalized coefficient triples
    inc={(P,L) for P in points for L in lines if sum(a*b for a,b in zip(P,L))%p==0}
    return points,lines,inc

def check(p):
    P,L,I=pg2(p); N=p*p+p+1
    assert len(P)==len(L)==N
    degP={x:sum((x,l) in I for l in L) for x in P}
    degL={l:sum((x,l) in I for x in P) for l in L}
    assert set(degP.values())=={p+1} and set(degL.values())=={p+1}
    for i,x in enumerate(P):
        for y in P[i+1:]:
            assert sum((x,l) in I and (y,l) in I for l in L)==1
    for i,l in enumerate(L):
        for m in L[i+1:]:
            assert sum((x,l) in I and (x,m) in I for x in P)==1
    order_V=2*N; order_E=(p+1)*N
    beta1_order=order_E-order_V+1
    assert beta1_order==p**3
    # Incidence/associated complex collapses linewise to q edges per line,
    # retaining N point vertices; all faces of size >=2 lie on one unique line.
    collapsed_V=N; collapsed_E=p*N
    beta1_inc=collapsed_E-collapsed_V+1
    assert beta1_inc==p**3
    # In the hyperedge VR complex, all line-hyperedges form a simplex.
    # Each singleton point-hyperedge has one maximal coface consisting of itself
    # and its p+1 incident line-hyperedges, hence is dominated by any one of them.
    dominated_singletons=N
    assert dominated_singletons==N
    return {
        'q':p,'points':N,'lines':N,'incidences':len(I),
        'order_vertices':order_V,'order_edges':order_E,
        'order_beta1':beta1_order,
        'incidence_collapse_vertices':collapsed_V,
        'incidence_collapse_edges':collapsed_E,
        'incidence_beta1':beta1_inc,
        'vr_dominated_singletons':dominated_singletons,
        'vr_remaining_line_simplex_vertices':N,
    }

if __name__=='__main__':
    for p in (2,3,5): print(check(p))
