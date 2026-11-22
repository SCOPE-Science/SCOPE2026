"""Reproducible finite consistency checks for the Chebyshev-cone theorem.

Requires Python 3 and SymPy. Tests examples; the uniform theorem rests on the
algebraic and intersection-theoretic proof, not on these finite computations.
"""
from math import gcd
from sympy import Symbol, Poly, chebyshevt, expand, gcd as polygcd

u = Symbol('u')
x = Symbol('x')


def h_polynomial(m):
    n = 2*m + 1
    coefficients = Poly(chebyshevt(n, u) / u, u).as_dict()  # exact polynomial
    h = 0
    for (exponent,), coefficient in coefficients.items():
        assert exponent % 2 == 0
        h += coefficient * ((x+1)/2)**(exponent//2)
    return Poly(expand(h), x)


def numerical_semigroup(a, b, c):
    assert gcd(a,gcd(b,c)) == 1
    import heapq
    dist = [10**20]*a
    dist[0] = 0
    heap = [(0,0)]
    while heap:
        d,r = heapq.heappop(heap)
        if d != dist[r]:
            continue
        for g in (b,c):
            target = (r+g)%a
            value = d+g
            if value < dist[target]:
                dist[target] = value
                heapq.heappush(heap, (value,target))
    return dist


def check(m):
    n = 2*m+1
    h = h_polynomial(m)
    assert h.degree() == m
    assert h.eval(-1) != 0
    assert polygcd(h, h.diff()).degree() == 0
    # All m affine points where the two normalization branches coalesce.
    assert expand(chebyshevt(n,u) - u*h.as_expr().subs(x,2*u*u-1)) == 0
    a=n-4
    semigroup_apery=numerical_semigroup(a,a+2,a+4)
    expected=[10**20]*a
    for j in range(a):
        w=a*((j+1)//2)+2*j
        expected[w%a]=w
    assert semigroup_apery == expected
    delta=sum(semigroup_apery)//a-(a-1)//2
    assert delta == m*(m-2)
    arithmetic_genus=m*(m-1)
    assert arithmetic_genus == m+delta
    # Castelnuovo bound in P^3 for odd degree 2m+1.
    assert arithmetic_genus == ((n-2)**2)//4
    # Hilbert polynomial of a reduced union of n ruling lines on the cone.
    for d in range(m,m+7):
        H=sum(min(n,2*j+1) for j in range(d+1))
        assert H == n*d+1-arithmetic_genus
    conductor=max(semigroup_apery)-a+1
    assert conductor == (m-2)*(2*m-1)
    print('n=%d, affine nodes=%d, infinity delta=%d, p_a=%d, conductor=%d: PASS' %
          (n,m,delta,arithmetic_genus,conductor))


if __name__ == '__main__':
    for m in range(2,17):
        check(m)
    print('All finite consistency checks passed; uniform proof is separate.')
