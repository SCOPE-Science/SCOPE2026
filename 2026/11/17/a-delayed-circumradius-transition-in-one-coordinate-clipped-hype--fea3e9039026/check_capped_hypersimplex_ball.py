#!/usr/bin/env python3
"""Exact finite stress checks for minimum-enclosing balls of capped hypersimplices.

No external packages are required. The checker independently enumerates section
vertices from box-endpoint constraints and minimizes the squared-distance envelope
of those vertices by examining every quadratic stationary point and intersection.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def vertices(m, k, t):
    bounds = [F(1)] * m + [t]
    verts = set()
    for free in range(m + 1):
        indices = [i for i in range(m + 1) if i != free]
        for flags in product((0, 1), repeat=m):
            x = [F(0)] * (m + 1)
            for i, flag in zip(indices, flags):
                x[i] = bounds[i] if flag else F(0)
            x[free] = F(k) - sum(x)
            if 0 <= x[free] <= bounds[free]:
                verts.add(tuple(x))
    return sorted(verts)


def squared_distance(x, m, k, h):
    c = (F(k) - h) / m
    return sum((z-c)**2 for z in x[:m]) + (x[m]-h)**2


def independent_envelope_minimum(verts, m, k):
    # All distances are A*h*h+B*h+C with A=(m+1)/m.
    a = F(m + 1, m)
    lines = set()
    for x in verts:
        b = -2 * x[-1] * a
        c = squared_distance(x, m, k, F(0))
        lines.add((b, c))
    candidates = {-b/(2*a) for b, c in lines}
    for b1, c1 in lines:
        for b2, c2 in lines:
            if b1 != b2:
                candidates.add((c2-c1)/(b1-b2))
    def objective(h):
        return max(a*h*h+b*h+c for b,c in lines)
    opt = min((objective(h),h) for h in candidates)
    return opt, len(lines)


def predicted(m, k, t):
    q = F(m-k,m)
    h = F(0) if t <= q else (m*t-(m-k))/F(m+1)
    radius2 = F(k*(m-k),m) + F(m+1,m)*h*h
    return radius2,h


def run():
    tested = 0
    vertices_checked = 0
    contacts_checked = 0
    threshold_cases = 0
    strict_screening_cases = 0
    full_contact_cases = 0
    values = sorted({F(1,10), F(1,5), F(1,4), F(1,3), F(2,5),
                     F(1,2), F(3,5), F(2,3), F(3,4), F(4,5), F(9,10)})
    for m in range(2, 9):
        for k in range(1,m):
            for t in values:
                v = vertices(m,k,t)
                expected_count = comb(m,k)+m*comb(m-1,k-1)
                assert len(v)==expected_count, (m,k,t,len(v),expected_count)
                answer, number_types = independent_envelope_minimum(v,m,k)
                assert number_types==2,(m,k,t,number_types)
                expect = predicted(m,k,t)
                assert answer==expect, (m,k,t,answer,expect)
                radius2,h=answer
                contact = sum(squared_distance(x,m,k,h)==radius2 for x in v)
                assert all(squared_distance(x,m,k,h)<=radius2 for x in v)
                threshold=F(m-k,m)
                assert contact == (len(v) if t>=threshold else comb(m,k))
                if t<threshold:
                    strict_screening_cases+=1
                    expected_slack=2*t*(threshold-t)
                    b_distance=squared_distance(next(x for x in v if x[-1]==t),m,k,h)
                    assert radius2-b_distance==expected_slack
                elif t==threshold:
                    threshold_cases+=1
                else:
                    full_contact_cases+=1
                # Explicit support-centroid check: optimal center must be a convex
                # combination of all contacting vertices, supplying a global certificate.
                support=[x for x in v if squared_distance(x,m,k,h)==radius2]
                A=[x for x in support if x[-1]==0]
                B=[x for x in support if x[-1]==t]
                assert len(A)==comb(m,k)
                if B:
                    weight=h/t
                    assert F(0)<=weight<=F(1)
                    meanA=[sum(x[i] for x in A)/len(A) for i in range(m+1)]
                    meanB=[sum(x[i] for x in B)/len(B) for i in range(m+1)]
                    center=[(F(k)-h)/m]*m+[h]
                    assert [(1-weight)*meanA[i]+weight*meanB[i] for i in range(m+1)]==center
                else:
                    assert h==0
                tested+=1
                vertices_checked+=len(v)
                contacts_checked+=contact
    print('CAPPED_HYPERSIMPLEX_BALL_CHECKS_PASSED',
          f'cases={tested}', f'enumerated_vertices={vertices_checked}',
          f'contact_vertices={contacts_checked}',
          f'screened_cases={strict_screening_cases}',
          f'boundary_cases={threshold_cases}',
          f'full_contact_cases={full_contact_cases}')

if __name__=='__main__':
    run()
