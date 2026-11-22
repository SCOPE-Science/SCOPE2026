"""Reproduce the cone-over-tree graph-elliptope volume identities.

Requires Python 3.10+ standard library only. Checks are finite diagnostics;
the theorem for all orders follows from the Gram construction and convexity proof.
"""
import itertools
import math
import random
from collections import deque


def I(d):
    """Integral from -1 to 1 of (1-x*x)^(d/2)."""
    return math.exp(math.lgamma(.5) + math.lgamma(1 + d/2) - math.lgamma(1.5 + d/2))


def volume_from_degrees(degrees):
    return 2.0 ** (-len(degrees)) * math.prod(I(d) for d in degrees)


def path_degrees(n):
    return [1, 1] + [2] * (n - 2)


def star_degrees(n):
    return [n - 1] + [1] * (n - 1)


def simpson_I(d, steps=3000):
    h = 2.0 / steps
    z = 0.0
    for k in range(steps + 1):
        x = -1 + h*k
        f = max(0.0, 1 - x*x) ** (d/2)
        z += (1 if k in (0, steps) else (4 if k % 2 else 2)) * f
    return h*z/3


def edges_from_prufer(code, n):
    deg = [1]*n
    for c in code:
        deg[c] += 1
    edges = []
    for c in code:
        v = next(i for i, d in enumerate(deg) if d == 1)
        edges.append((v,c))
        deg[v] -= 1
        deg[c] -= 1
    u, v = [i for i,d in enumerate(deg) if d == 1]
    edges.append((u,v))
    return edges


def degrees_from_prufer(code, n):
    deg = [1]*n
    for c in code:
        deg[c] += 1
    return deg


def vector_dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def verify_gram_witness(edges,n,rng):
    # Create hub inner products x_i and feasible triangle-edge correlations y_ij.
    x = [rng.uniform(-0.97,0.97) for _ in range(n)]
    c = {tuple(sorted((u,v))):rng.uniform(-0.94,0.94) for u,v in edges}
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    w = [None]*n
    w[0]=[1.0] + [0.0]*(n-1)
    que=deque([0]); visited={0}
    while que:
        u=que.popleft()
        for v in adj[u]:
            if v in visited:
                continue
            visited.add(v)
            cv=c[tuple(sorted((u,v)))]
            q=[cv*t for t in w[u]]
            q[v] += math.sqrt(1-cv*cv)
            w[v]=q
            que.append(v)
    assert len(visited) == n
    z=[[x[i]] + [math.sqrt(1-x[i]*x[i])*t for t in w[i]] for i in range(n)]
    for i in range(n):
        assert abs(vector_dot(z[i],z[i])-1)<1e-10
        assert abs(z[i][0]-x[i])<1e-12
    for u,v in edges:
        y=x[u]*x[v]+math.sqrt((1-x[u]**2)*(1-x[v]**2))*c[tuple(sorted((u,v)))]
        assert abs(vector_dot(z[u],z[v])-y)<1e-10


def main():
    checks=0
    for d in range(1,19):
        approx=simpson_I(d)
        assert abs(approx/I(d)-1)<1.5e-5, (d,approx,I(d))
        checks+=1
    assert abs(I(1)-math.pi/2)<1e-13
    assert abs(I(2)-4/3)<1e-13
    checks+=2
    for d in range(2,21):
        assert abs(I(d)/(d/(d+1)*I(d-2))-1)<1e-12
        checks+=1
    # Prüfer codes list every labeled tree, not only sampled tree shapes.
    total_tree_codes=0
    for n in range(2,9):
        vpath=volume_from_degrees(path_degrees(n))
        vstar=volume_from_degrees(star_degrees(n))
        for code in itertools.product(range(n),repeat=n-2):
            deg=degrees_from_prufer(code,n)
            v=volume_from_degrees(deg)
            assert vpath <= v*(1+1e-12)
            assert v <= vstar*(1+1e-12)
            if n>=4:
                eq_low=abs(v/vpath-1)<1e-12
                eq_high=abs(v/vstar-1)<1e-12
                assert eq_low == (sorted(deg)==sorted(path_degrees(n)))
                assert eq_high == (sorted(deg)==sorted(star_degrees(n)))
            total_tree_codes+=1
        checks+=2
    # Star is the triangular-book elliptope: independent beta-function formula.
    for m in range(1,31):
        n=m+1
        book=(math.pi/2)**m * math.exp(2*math.lgamma(m/2+1)-math.lgamma(m+2))
        assert abs(book/volume_from_degrees(star_degrees(n))-1)<1e-12
        checks+=1
    # Gram completions for random trees and local PSD-feasible edge data.
    rng=random.Random(20261118)
    for n in range(2,17):
        for _ in range(32):
            code=[rng.randrange(n) for _ in range(n-2)]
            verify_gram_witness(edges_from_prufer(code,n),n,rng)
            checks+=1
    # Strict path/star asymptotic ratio.
    for n in (200,500,1000):
        log_ratio=(math.log(I(n-1))-math.log(I(1))+(n-2)*math.log(3*math.pi/8))
        log_asym=0.5*math.log(8/(math.pi*n))+(n-2)*math.log(3*math.pi/8)
        assert abs(math.exp(log_ratio-log_asym)-1)<0.006
        checks+=1
    print(f'TREE_ELLIPTOPE_DEGREE_VOLUME_PASS explicit_trees={total_tree_codes} auxiliary_checks={checks}')

if __name__=='__main__':
    main()
