#!/usr/bin/env python3
"""Exact finite-field and tangent-cone checks for a six-coordinate quartic.

Requires only Python 3 standard library. The geometric exhaustiveness over
algebraically closed fields is proved separately by a cubic-root argument.
"""
from itertools import combinations, product

P = 3

def esym(values, n):
    coeff = [1] + [0] * n
    for a in values:
        for j in range(n, 0, -1):
            coeff[j] = (coeff[j] + a * coeff[j-1]) % P
    return coeff[n]

def proj_normalize(values):
    values = [a % P for a in values]
    first = next(a for a in values if a)
    scale = pow(first, -1, P)
    return tuple((scale * a) % P for a in values)

def projective_points(n):
    for j in range(n):
        for tail in product(range(P), repeat=n-j-1):
            yield (0,) * j + (1,) + tail

def is_singular_B(x):
    assert esym(x, 1) == 0 and esym(x, 4) == 0
    partials = [esym(x[:j] + x[j+1:], 3) for j in range(6)]
    return len(set(partials)) == 1

def section_to_full(point):
    return point + (0,)

def is_point_S(point):
    return sum(point) % P == 0 and esym(point, 4) == 0

def predicted_node_section():
    nodes = set()
    for i, j in combinations(range(6), 2):
        d = [0] * 6
        d[i] = 1
        d[j] = -1
        d = [(a - d[5]) % P for a in d]
        nodes.add(proj_normalize(d[:5]))
    return nodes

def predicted_singular_lines():
    all_points = set()
    v = [1] * 6
    for i, j in combinations(range(6), 2):
        d = [0] * 6
        d[i] = 1
        d[j] = -1
        for a, b in [(1,0), (0,1), (1,1), (1,2)]:
            all_points.add(proj_normalize([(a*v[k] + b*d[k]) % P for k in range(6)]))
    return all_points

def mat_det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])) % P

def chart_hessian(x):
    # x0=1, x4=-1-x1-x2-x3: tangent vectors e1-e4,e2-e4,e3-e4.
    vectors = [(0,1,0,0,-1), (0,0,1,0,-1), (0,0,0,1,-1)]
    H = [[0 if i==j else esym([x[k] for k in range(5) if k!=i and k!=j],2)
          for j in range(5)] for i in range(5)]
    return [[sum(vectors[r][i]*H[i][j]*vectors[s][j]
                 for i in range(5) for j in range(5)) % P
             for s in range(3)] for r in range(3)]

def main():
    S_points = {a for a in projective_points(5) if is_point_S(a)}
    S_singular = {a for a in S_points if is_singular_B(section_to_full(a))}
    predicted_S = predicted_node_section()
    assert len(S_points) == 25, len(S_points)
    assert len(S_singular) == len(predicted_S) == 15
    assert S_singular == predicted_S
    assert mat_det3(chart_hessian((1,2,0,0,0))) == 1
    assert mat_det3(chart_hessian((1,1,1,1,2))) == 1

    B_points = {a for a in projective_points(6)
                if esym(a,1)==0 and esym(a,4)==0}
    B_singular = {a for a in B_points if is_singular_B(a)}
    predicted_B = predicted_singular_lines()
    assert len(B_points) == 76, len(B_points)
    assert len(B_singular) == len(predicted_B) == 46
    assert B_singular == predicted_B
    for a in B_points:
        for c in range(P):
            assert esym([(t+c)%P for t in a],4) == esym(a,4)
    assert len(B_points) == 1 + P*len(S_points)
    print('S(F3)=25; singular S(F3)=15; nodal-chart Hessian dets=1,1')
    print('B(F3)=76; singular B(F3)=46; 15 predicted singular lines')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
