"""Exact finite checks for the pendant-biclique Lipschitz-free inball theorem.

Run: python3 verify.py
Uses only Python 3 standard library. These are finite corroborations, not
substitutes for the all-parameter proof.
"""
from itertools import product
from math import comb
from fractions import Fraction


def closed_form(p, q):
    assert p >= 5 and q >= 2
    n = p + q + 1
    a = (q + 1) * n - ((q + 1) % 2)
    b = (p + 4) * n - (p % 2)
    count_a = (comb(q + 1, (q + 1) // 2) if q % 2 else
               2 * comb(q + 1, q // 2))
    count_b = (2 * comb(p - 1, (p - 4) // 2) if p % 2 == 0 else
               2 * comb(p, (p - 3) // 2))
    if q < p + 3:
        return max(a, b), count_b, q + (p % 2 == 0)
    if q > p + 3:
        return max(a, b), count_a, p if q % 2 else p - 1
    return max(a, b), count_a + count_b, 0 if p % 2 else 1


def candidate_vertices(p, q):
    # Each potential is represented after normalizing its value at a_0 to 0.
    # The resulting array indexes A, B, leaf in that order.
    seen = set()
    for b in product((-1, 1), repeat=q):
        for z in (-1, 1):
            seen.add((0,) * p + b + (z,))
    for a in product((-1, 1), repeat=p):
        for edge in (-1, 1):
            f = a + (0,) * q + (a[0] + edge,)
            seen.add(tuple(x - a[0] for x in f))
    return seen


def numerator(f):
    n = len(f)
    return n * sum(x*x for x in f) - sum(f)**2


def exact_rank(rows):
    # Streaming fraction-free-like elimination with rational pivot basis.
    # On submission the number of checked coordinates is small.
    basis = {}
    for row in rows:
        w = [Fraction(t) for t in row]
        for pivot in sorted(basis):
            t = w[pivot]
            if t:
                v = basis[pivot]
                w = [a - t*b for a, b in zip(w, v)]
        for j, val in enumerate(w):
            if val:
                basis[j] = [x / val for x in w]
                break
    return len(basis)


def tight_graph_connected(f, p, q):
    n = p + q + 1
    graph = [[] for _ in range(n)]
    for i in range(p):
        for j in range(p, p+q):
            gap = abs(f[i]-f[j])
            if gap > 1:
                return False
            if gap == 1:
                graph[i].append(j); graph[j].append(i)
    z = n-1
    if abs(f[z]-f[0]) != 1:
        return False
    graph[0].append(z); graph[z].append(0)
    vis = {0}; stack = [0]
    while stack:
        for j in graph[stack.pop()]:
            if j not in vis:
                vis.add(j); stack.append(j)
    return len(vis) == n


def independent_integer_vertices(p, q):
    # This enumeration does not use candidate_vertices(). Each coordinate
    # is bounded by its graph distance to vertex a_0, and all vertices are
    # integral because connected tight-edge graphs contain spanning trees.
    ans = set()
    for aa in product(range(-2,3), repeat=p-1):
        for bb in product(range(-1,2), repeat=q):
            for leaf in (-1,1):
                f = (0,) + aa + bb + (leaf,)
                if tight_graph_connected(f,p,q):
                    ans.add(f)
    return ans


def trial(p, q):
    vs = candidate_vertices(p,q)
    n = p+q+1
    weights = {f:numerator(f) for f in vs}
    top = max(weights.values())
    tops = [f for f,w in weights.items() if w==top]
    rank = exact_rank([tuple(n*x - sum(f) for x in f) for f in tops])
    got=(top,len(tops),n-1-rank)
    expect=closed_form(p,q)
    assert got == expect, (p,q,got,expect)
    return len(vs),len(tops)


def main():
    tested_integer=0
    for p,q in [(2,2),(2,3),(3,2),(3,3),(4,2),(5,2)]:
        u=independent_integer_vertices(p,q)
        v=candidate_vertices(p,q)
        assert u==v,(p,q,len(u),len(v),len(u-v),len(v-u))
        tested_integer += len(u)
    print('INDEPENDENT_TIGHT_EDGE_INTEGER_VERTEX_ENUMERATION_PASS',
          'cases=6 vertices='+str(tested_integer))
    profiles=[]; total=0; contacts=0
    for p in range(5,9):
        for q in sorted(set([2,3,p+1,p+2,p+3,p+4,p+5])):
            if q<=13:
                cnt,num=trial(p,q)
                profiles.append((p,q));total+=cnt;contacts+=num
    assert len(profiles)==28
    print('EXACT_MAXIMUM_CONTACTS_AND_CENTER_RANK_PASS',
          'profiles='+str(len(profiles)),
          'vertices='+str(total),'contact_normals='+str(contacts))
    parity_profiles=0
    for p in range(5,81):
        for q in range(2,121):
            parity_profiles += 1
            n=p+q+1
            a=(q+1)*n-((q+1)%2)
            b=(p+4)*n-(p%2)
            assert (a>b)==(q>p+3)
            assert (a==b)==(q==p+3)
    print('EXACT_PARITY_THRESHOLD_ARITHMETIC_PASS profiles='+str(parity_profiles))
    print('PENDANT_BICLIQUE_INBALL_ALL_CHECKS_PASS')


if __name__=='__main__':
    main()
