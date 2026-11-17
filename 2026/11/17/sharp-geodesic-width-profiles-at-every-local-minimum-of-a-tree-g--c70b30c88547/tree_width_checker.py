"""Standalone exact-rational checks for the tree-zonotope angular-width theorem.

Run: python3 tree_width_checker.py
Only Python's standard library is used.  The proof, not this finite check,
handles arbitrary trees and arbitrary real unit directions.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, atan, sin, cos
import random


def trees_from_prufer(n):
    if n == 2:
        yield [(0, 1)]
        return
    for code in product(range(n), repeat=n - 2):
        deg = [1] * n
        for x in code:
            deg[x] += 1
        edges = []
        for x in code:
            leaf = next(i for i in range(n) if deg[i] == 1)
            edges.append(tuple(sorted((leaf, x))))
            deg[leaf] -= 1
            deg[x] -= 1
        a, b = [i for i in range(n) if deg[i] == 1]
        edges.append((a, b))
        yield sorted(edges)


def cut_sides(n, edges):
    out = []
    for a, b in edges:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            if (x, y) == (a, b):
                continue
            adj[x].append(y)
            adj[y].append(x)
        seen, todo = {a}, [a]
        while todo:
            v = todo.pop()
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
        assert b not in seen
        out.append(frozenset(seen))
    return out


def gram(n, sides):
    m = len(sides)
    return [[F(len(sides[e] & sides[f]))-
             F(len(sides[e])*len(sides[f]), n)
             for f in range(m)] for e in range(m)]


def slope_squared(K, e):
    diag = K[e][e]
    ratios = {}
    for f in range(len(K)):
        if f == e:
            continue
        c = K[e][f]/diag
        assert abs(c) < 1, ('nonpositive angular slope', e, f)
        norm_sq = K[f][f]-K[e][f]**2/diag
        assert norm_sq > 0
        ratios[f] = (1-abs(c))**2/norm_sq
    return min(ratios.values()), ratios


def check_one(n, edges, rng, full_sample=False):
    sides = cut_sides(n, edges)
    K = gram(n, sides)
    cuts = [[F(int(v in S))-F(len(S), n) for v in range(n)] for S in sides]
    count = 0
    for e, (a,b) in enumerate(edges):
        ke = K[e][e]
        assert ke == F(len(sides[e])*(n-len(sides[e])),n)
        assert cuts[e][a]-cuts[e][b] == 1
        for f in range(len(edges)):
            assert cuts[f][a]-cuts[f][b] == (1 if e == f else 0)
        gamma2, ratios = slope_squared(K,e)
        for f, value in ratios.items():
            assert value >= gamma2
        projections = {}
        for f in ratios:
            c = K[e][f]/ke
            projections[f] = [cuts[f][i]-c*cuts[e][i] for i in range(n)]
            assert sum(projections[f]) == 0
            assert sum(projections[f][i]*cuts[e][i] for i in range(n)) == 0
        # For 1-edge tangent directions, the optimal signed projection
        # exactly attains the formula, not just its first-order bound.
        fstar = min(ratios, key=ratios.get)
        cstar = K[e][fstar]/ke
        sign = 1 if cstar > 0 else -1
        xstar = [sign*v for v in projections[fstar]]
        dsq = sum(v*v for v in xstar)
        hstar = sum(abs(xstar[x]-xstar[y]) for i,(x,y) in enumerate(edges) if i!=e)
        hstar += xstar[a]-xstar[b]
        assert hstar > 0 and hstar*hstar == gamma2*dsq
        # Random mixtures check the exact sharp tangent inequality.
        if full_sample:
            for _ in range(8):
                coeffs = {f:rng.randint(-5,5) for f in ratios}
                if not any(coeffs.values()):
                    continue
                delta = [sum(coeffs[f]*projections[f][i] for f in ratios) for i in range(n)]
                norm2 = sum(t*t for t in delta)
                if norm2 == 0:continue
                h = sum(abs(delta[x]-delta[y]) for i,(x,y) in enumerate(edges) if i!=e)
                h += delta[a]-delta[b]
                assert h > 0 and h*h >= gamma2*norm2
                count += 1
        if full_sample:
            w = 1/sqrt(float(ke))
            g = sqrt(float(gamma2))
            u = [float(x)/sqrt(float(ke)) for x in cuts[e]]
            vnorm = sqrt(float(dsq))
            v = [float(z)/vnorm for z in xstar]
            for factor in (0.11, 0.37, 0.93):
                theta = atan(factor*w/sqrt(2))
                point=[cos(theta)*u[i]+sin(theta)*v[i] for i in range(n)]
                width=sum(abs(point[x]-point[y]) for x,y in edges)
                expected=w*cos(theta)+g*sin(theta)
                assert abs(width-expected)<1e-10, (n,edges,e,width,expected)
    return count


def main():
    rng=random.Random(11242021)
    profile_count=0
    checks=0
    for n in range(3,7):
        for edges in trees_from_prufer(n):
            # All labelled trees up to six vertices, exhaustive.
            checks += check_one(n,edges,rng,full_sample=True)
            profile_count+=1
    path_count=0
    star_count=0
    for n in range(3,15):
        P=[(i,i+1) for i in range(n-1)]
        cuts=cut_sides(n,P)
        KP=gram(n,cuts)
        for e in range(n-1):
            gamma2,_=slope_squared(KP,e)
            size=max(e+1,n-e-1)
            assert gamma2==F(1,size*(size-1)), (n,e,gamma2)
            path_count+=1
        S=[(0,i) for i in range(1,n)]
        KS=gram(n,cut_sides(n,S))
        for e in range(n-1):
            gamma2,_=slope_squared(KS,e)
            assert gamma2==F(n-2,n-1)
            star_count+=1
    print('TREE_ZONOTOPE_ANGULAR_PASS labelled_trees=%d exact_tangent_mixtures=%d path_edges=%d star_edges=%d'%
          (profile_count,checks,path_count,star_count))

if __name__=='__main__':
    main()
