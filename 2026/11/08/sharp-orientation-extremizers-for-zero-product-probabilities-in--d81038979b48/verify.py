"""Independent finite-field checks for zero products in radical-square-zero quiver algebras.
Run: python verify.py. No external packages required.
"""
from itertools import product
from fractions import Fraction
from math import sqrt


def algebra_zero_pairs(n, edges, q):
    """Directly multiply all ordered pairs in F_q Q/J^2, for prime q."""
    m = len(edges)
    elts = tuple(product(range(q), repeat=n+m))
    answer = 0
    for a in elts:
        for b in elts:
            if any(a[v]*b[v] % q for v in range(n)):
                continue
            if any((a[u]*b[n+i]+a[n+i]*b[v]) % q
                   for i, (u, v) in enumerate(edges)):
                continue
            answer += 1
    return answer


def expansion(n, edges, q):
    m = len(edges)
    acc = 0
    for bits in product((0, 1), repeat=m):
        indeg = [False]*n
        outdeg = [False]*n
        e_count = 0
        for take, (u, v) in zip(bits, edges):
            if take:
                e_count += 1
                outdeg[u] = True
                indeg[v] = True
        term = (q-1)**e_count
        for u in range(n):
            if indeg[u] and outdeg[u]:
                term *= 1
            elif indeg[u] or outdeg[u]:
                term *= q
            else:
                term *= 2*q-1
        acc += term
    return acc


def path_edges(n, directions):
    assert len(directions) == n-1
    return [(i, i+1) if d == 0 else (i+1,i)
            for i,d in enumerate(directions)]


def min_rec(n,q):
    a,b=1,2*q-1
    if n == 0:return a
    for _ in range(1,n):
        a,b=b,(3*q-2)*b+(q-1)**3*a
    return b


def max_rec(n,q):
    a,b=1,2*q-1
    if n == 0:return a
    for _ in range(1,n):
        a,b=b,(q*q+q-1)*b-q*(q-1)**2*a
    return b


def check():
    for q in (2,3):
        for n in range(1,7 if q == 2 else 6):
            values={dirs: expansion(n,path_edges(n,dirs),q)
                    for dirs in product((0,1),repeat=n-1)}
            lower=min_rec(n,q)
            upper=max_rec(n,q)
            assert min(values.values())==lower, (n,q,'min')
            assert max(values.values())==upper, (n,q,'max')
            for orient,val in values.items():
                if n>=3:
                    assert (val == lower) == (len(set(orient))==1)
                    assert (val == upper) == all(orient[j]!=orient[j+1]
                                                  for j in range(n-2))
        print('PATH_ORIENTATION_EXTREMA_OK',q)
    for q,n in ((2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3)):
        for dirs in product((0,1),repeat=n-1):
            edges=path_edges(n,dirs)
            assert algebra_zero_pairs(n,edges,q)==q**(n-1)*expansion(n,edges,q), (q,n,dirs)
        print('DIRECT_MULTIPLICATION_OK',q,n)
    # Independently test graphs beyond paths (including a multi-edge case).
    for n,edges in [(3,[(0,1),(0,2)]),(3,[(0,1),(1,2),(2,0)]),
                    (2,[(0,1),(1,0)]),(2,[(0,1),(0,1)])]:
        assert algebra_zero_pairs(n,edges,2)==2**len(edges)*expansion(n,edges,2)
    print('GENERAL_QUIVER_MULTIPLICATION_OK')
    # Bipartite upper extremizer: source--sink orientation of a star.
    for q in (2,3):
        graph=[(0,1),(0,2),(0,3)]
        allvals={d:expansion(4,[(u,v) if di==0 else (v,u)
                                  for (u,v),di in zip(graph,d)],q)
                 for d in product((0,1), repeat=3)}
        assert max(allvals.values())==allvals[(0,0,0)]
        assert [d for d,x in allvals.items() if x==max(allvals.values())] == [(0,0,0),(1,1,1)]
    print('BIPARTITE_SOURCE_SINK_MAXIMALITY_OK')
    for q in (2,3,5):
        ld=(3*q-2+q*sqrt(4*q-3))/2
        la=(q*q+q-1+sqrt((q*q+q-1)**2-4*q*(q-1)**2))/2
        assert 2*q-1 < ld < la < q**3
        for n in (30,60):
            cmin=min_rec(n,q)
            cmax=max_rec(n,q)
            assert cmin<cmax
            # Exponential nth-root rates converge to their transfer roots.
            assert abs((cmin**(1/n))/ld-1)<0.09
            assert abs((cmax**(1/n))/la-1)<0.09
        print('SPECTRAL_SANITY_OK',q,'lambda_min=',round(ld,8),'lambda_max=',round(la,8))
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
