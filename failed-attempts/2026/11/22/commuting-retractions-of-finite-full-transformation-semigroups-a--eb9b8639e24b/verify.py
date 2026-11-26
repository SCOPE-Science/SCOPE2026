"""Finite checks for the rooted-fiber commuting-retraction theorem.

Standard-library only. Finite checks corroborate the separate all-degree proof.
"""
from collections import deque
from fractions import Fraction
from itertools import product
from math import comb, factorial


def multiplication(a, b):
    """Apply the tuple transformation a, then b."""
    return tuple(b[i] for i in a)


def odd_permutation(a):
    n = len(a)
    if len(set(a)) != n:
        return False
    seen = set()
    cycles = 0
    for i in range(n):
        if i not in seen:
            cycles += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = a[j]
    return (n - cycles) % 2 == 1


def involutions_on(b, signed=False):
    return sum(((-1)**k if signed else 1) * factorial(b) //
               (2**k * factorial(k) * factorial(b-2*k))
               for k in range(b//2 + 1))


def multiply_numbers(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def raw_counts(n):
    ident = tuple(range(n))
    maps = list(product(range(n), repeat=n))
    idem = [e for e in maps if multiplication(e, e) == e]
    odd_inv = [t for t in maps
               if multiplication(t, t) == ident and odd_permutation(t)]
    pages = {}
    for e in idem:
        pages[e] = [t for t in odd_inv if multiplication(t,e)==e
                    and multiplication(e,t)==e]
        roots = [i for i in range(n) if e[i] == i]
        leaves = [sum(e[j] == i for j in range(n)) - 1 for i in roots]
        expected = (multiply_numbers(involutions_on(b) for b in leaves)
                    - multiply_numbers(involutions_on(b,True) for b in leaves)) // 2
        assert len(pages[e]) == expected
        assert (len(pages[e]) == 0) == (max(leaves,default=0) <= 1)
    I = len(idem)
    B = sum(len(ts) for ts in pages.values())
    H = sum(len(ts)==0 for ts in pages.values())
    assert I == sum(comb(n,r)*r**(n-r) for r in range(1,n+1))
    assert H == sum(factorial(n)//(factorial(k)*factorial(n-2*k))
                    for k in range(n//2+1))
    return idem,pages,I,B,H


def formal_exp(f, degree):
    """Exp of a truncated series f with f[0]=0, exact rationals."""
    assert f[0] == 0
    out = [Fraction(0)] * (degree+1)
    out[0] = 1
    for n in range(1,degree+1):
        out[n] = sum(Fraction(k)*f[k]*out[n-k]
                     for k in range(1,n+1)) / n
    return out


def triangle_egf_coefficients(degree):
    ans = []
    for sign in (1,-1):
        inner = [Fraction(0)]*(degree+1)
        if degree >= 1: inner[1] = 1
        if degree >= 2: inner[2] = Fraction(sign,2)
        exp_inner = formal_exp(inner,degree)
        outer = [Fraction(0)]*(degree+1)
        for k in range(1,degree+1):
            outer[k] = exp_inner[k-1]
        ans.append(formal_exp(outer,degree))
    return [factorial(n)*(ans[0][n]-ans[1][n])/2
            for n in range(degree+1)]


def direct_compositions(n,idem,pages,I,B,H):
    ident = tuple(range(n))
    vertices = []
    vertex_labels = {}
    def add(key,label):
        assert key not in vertex_labels
        vertices.append(key)
        vertex_labels[key] = label
    for e in idem:
        add((e,e,e),('u',e))
        if e != ident:
            add((ident,ident,e),('v',e))
        for t in pages[e]:
            add((t,ident,e),('w',e))
    # Each triple records an endomorphism's output on (odd,even,singular).
    def eval_map(f,s):
        if len(set(s)) != n: return f[2]
        return f[0] if odd_permutation(s) else f[1]
    def composition(f,g):
        return tuple(eval_map(g,s) for s in f)
    adj = {v:set() for v in vertices}
    for i,a in enumerate(vertices):
        for b in vertices[i+1:]:
            commuting = composition(a,b)==composition(b,a)
            x,e = vertex_labels[a]
            y,f = vertex_labels[b]
            c = ident
            expected = ((x=='u' and e==c and y in ('v','w')) or
                        (y=='u' and f==c and x in ('v','w')) or
                        (e==f and frozenset((x,y)) in
                         (frozenset(('u','v')),frozenset(('u','w')),
                          frozenset(('v','w')))))
            assert commuting == expected, (x,y,e,f)
            if commuting:
                adj[a].add(b)
                adj[b].add(a)
    triangles = sum(len(adj[a]&adj[b]) for a in vertices for b in adj[a])//6
    edges = sum(len(v) for v in adj.values())//2
    maximal_edges = sum(not(adj[a]&adj[b]) for a in vertices for b in adj[a])//2
    assert len(vertices)==2*I-1+B
    assert edges==2*(I-1)+3*B
    assert triangles==2*B
    assert maximal_edges==2*(H-1)
    assert triangles+maximal_edges==2*B+2*(H-1)
    diameter=0
    for v in vertices:
        dist={v:0}
        frontier=deque([v])
        while frontier:
            u=frontier.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w]=dist[u]+1
                    frontier.append(w)
        assert len(dist)==len(vertices)
        diameter=max(diameter,max(dist.values()))
    assert diameter==4
    print('EXHAUSTIVE_PAIR_COMPOSITION_OK',n,'V',len(vertices),
          'E',edges,'triangles',triangles,'diameter',diameter,'maximal_cliques',triangles+maximal_edges)


def main():
    egf=triangle_egf_coefficients(6)
    for n in range(3,7):
        idem,pages,I,B,H=raw_counts(n)
        assert egf[n]==B
        print('ROOTED_FIBERS_AND_EGF_OK',n,'I',I,'pages',B,'zero_pages',H)
        if n==5:
            direct_compositions(n,idem,pages,I,B,H)
    print('FULL_TRANSFORMATION_RETRACTION_CHECKS_PASSED')

if __name__=='__main__':
    main()
