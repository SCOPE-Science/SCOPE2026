#!/usr/bin/env python3
"""Exact, self-contained transfer certificate for Rule 22 temporal six-cycles.

Run: python3 verify_transfer.py
No third-party modules required. The proof relies on integer traces and Newton
identities, with the graph built directly from the local Boolean rule.
"""
from collections import Counter

RULE = 22


def successor_graph(p):
    """All pairs of p-bit time columns; edges enforce the CA at every time."""
    s = 1 << p
    adj = [[] for _ in range(s * s)]
    for a in range(s):
        for b in range(s):
            for c in range(s):
                f = 0
                for t in range(p):
                    neighborhood = (((a >> t) & 1) << 2) | (((b >> t) & 1) << 1) | ((c >> t) & 1)
                    f |= ((RULE >> neighborhood) & 1) << t
                shifted = ((f << 1) & (s - 1)) | (f >> (p - 1))
                if shifted == b:
                    adj[a*s + b].append(b*s + c)
    return adj


def strongly_connected_components(adj):
    """Tarjan decomposition, including non-recurrent singleton components."""
    import sys
    sys.setrecursionlimit(20000)
    n = len(adj)
    number = [-1] * n
    low = [0] * n
    on_stack = [False] * n
    stack = []
    components = []
    current = 0
    def visit(v):
        nonlocal current
        number[v] = low[v] = current
        current += 1
        stack.append(v)
        on_stack[v] = True
        for w in adj[v]:
            if number[w] < 0:
                visit(w)
                low[v] = min(low[v], low[w])
            elif on_stack[w]:
                low[v] = min(low[v], number[w])
        if low[v] == number[v]:
            part = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                part.append(w)
                if w == v:
                    break
            components.append(sorted(part))
    for v in range(n):
        if number[v] < 0:
            visit(v)
    return components


def recurrent_components(adj):
    components = strongly_connected_components(adj)
    return sorted((c for c in components if len(c) > 1 or c[0] in adj[c[0]]),
                  key=lambda c: (-len(c), c))


def poly_multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v*w
    return out


def poly_power(a, n):
    out = [1]
    for _ in range(n):
        out = poly_multiply(out, a)
    return out


def characteristic_coefficients(adj, nodes):
    """Return monic char poly in DESCENDING powers using exact Newton identities.

    For each k, trace(A**k) is computed by counting length-k walks closed
    at each root, with only internal edges of the strongly connected block.
    """
    m = len(nodes)
    pos = {v: i for i,v in enumerate(nodes)}
    edges = [[pos[v] for v in adj[u] if v in pos] for u in nodes]
    traces = [0]*(m+1)
    for root in range(m):
        counts = [0]*m
        counts[root] = 1
        for k in range(1,m+1):
            nxt = [0]*m
            for u in range(m):
                for v in edges[u]:
                    nxt[v] += counts[u]
            counts = nxt
            traces[k] += counts[root]
    coeff = [1]
    for k in range(1,m+1):
        total = sum(coeff[k-i] * traces[i] for i in range(1,k+1))
        assert total % k == 0, ('Newton integrality', m,k,total)
        coeff.append(-total//k)
    return coeff


def expected_polynomials(p):
    # Polynomial coefficient lists here are DESCENDING, ordered by SCC size.
    # In particular, T^8-1 is [1,0,...,0,-1].
    if p in (1,3):
        return [[1,-1], [1,0,-1]]
    if p == 2:
        return [[1,-1], [1,0,-1], [1,0,0,0,-1]]
    if p == 6:
        # These factors describe the unique 60-vertex branch component.
        long_poly = [1] + [0]*30
        for factor, power in [([1,-1],2),([1,1],2),([1,0,0,0,0,-2],1),
                              ([1,0,0,0,0,2],1),([1,1,1,1,1],2),
                              ([1,-1,1,-1,1],2)]:
            long_poly = poly_multiply(long_poly,poly_power(factor,power))
        return [long_poly] + [[1]+[0]*7+[-1]]*3 + [
            [1,0,0,0,-1], [1,0,-1], [1,-1]]
    raise ValueError(p)


def main():
    observed = {}
    for p in (1,2,3,6):
        adj = successor_graph(p)
        comps = recurrent_components(adj)
        actual = [characteristic_coefficients(adj,c) for c in comps]
        expected = expected_polynomials(p)
        assert Counter(map(tuple,actual)) == Counter(map(tuple,expected)), (p, actual)
        observed[p] = actual
        print('p=%d nodes=%d edges=%d cyclic_SCC_sizes=%s: characteristic polynomials verified' %
              (p,len(adj),sum(map(len,adj)), sorted((len(c) for c in comps),reverse=True)))
    # Polynomial products for det(I-z T_p), calculated by reversing each
    # descending characteristic list and omitting zero eigenvalue factors.
    def det_one_minus_z_poly(p):
        res = [1]
        for cp in observed[p]:
            # cp represents t^m+c1*t^(m-1)+...; det(I-z A)=1+c1*z+...
            res = poly_multiply(res,cp)
        while len(res)>1 and res[-1]==0:
            res.pop()
        return res
    d2 = det_one_minus_z_poly(2)
    d6 = det_one_minus_z_poly(6)
    assert det_one_minus_z_poly(1) == det_one_minus_z_poly(3)
    rhs = poly_multiply(d2,poly_multiply(poly_power([1]+[0]*7+[-1],3),
            poly_multiply(poly_power([1]+[0]*9+[-1],2), [1]+[0]*9+[-4])))
    assert d6 == rhs, 'exact sixth-versus-second-return determinant identity'
    print('EXACT IDENTITY: D6(z)/D2(z)=(1-z^8)^3*(1-z^10)^2*(1-4*z^10)')
    print('PASS: six-time zeta, three-time exclusion, all-length formula')

if __name__ == '__main__':
    main()
