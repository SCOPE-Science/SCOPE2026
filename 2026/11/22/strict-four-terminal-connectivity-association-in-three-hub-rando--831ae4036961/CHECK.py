"""Independent finite-neighborhood census and finite-graph spot checks.
Run: python CHECK.py (requires SymPy)."""
from itertools import product
from collections import Counter
import sympy as sp

v, m = sp.symbols('v m')
A = 1 + 3*v

def connections(patterns):
    # A hub-mask for each vertex; cycles detected by disjoint sets.
    parent = list(range(3 + len(patterns)))
    def root(u):
        while parent[u] != u:
            u = parent[u]
        return u
    for i, mask in enumerate(patterns):
        for h in range(3):
            if mask & (1 << h):
                a, b = root(3+i), root(h)
                if a == b:
                    return None
                parent[a] = b
    return root(3)==root(4), root(5)==root(6)

# Every unmarked vertex has degree 0/1 or is one of at most two
# branching vertices; the two-branch possibility has distinct pairs.
branch_cases = [((), 0, 0, 0)]
branch_cases += [((p,), 1, 1 if p in (3, 5, 6) else 0, p.bit_count())
                 for p in (3, 5, 6, 7)]
branch_cases += [((p, q), 2, 2, 4) for p, q in ((3,5), (3,6), (5,6))]
# Branching multiplicities: one marked unmarked vertex m,
# two distinct vertices m(m-1) with each assignment counted once.
poly = [sp.Integer(0)]*3
for marked in product(range(8), repeat=4):
    base = sum(mask.bit_count() for mask in marked)
    for branch, count, div_power, branch_edges in branch_cases:
        conn = connections(marked + branch)
        if conn is None:
            continue
        factor = [1, m, m*(m-1)][count] * v**(base+branch_edges)/A**count
        for i, active in enumerate((True, conn[0], conn[0] and conn[1])):
            if active:
                poly[i] += factor

P0 = 3*m**2*v**4 + 24*m*v**4 + 10*m*v**3 + 3*m*v**2 + 48*v**4 + 40*v**3 + 21*v**2 + 6*v + 1
P1 = 9*m**2*v**4 + 72*m*v**4 + 30*m*v**3 + 5*m*v**2 + 144*v**4 + 120*v**3 + 47*v**2 + 10*v + 1
P2 = 81*m**2*v**4 + 648*m*v**4 + 318*m*v**3 + 25*m*v**2 + 1296*v**4 + 1224*v**3 + 411*v**2 + 58*v + 3
R = 36*m**3*v**6 + 12*m**3*v**5 + 396*m**2*v**6 + 315*m**2*v**5 + 106*m**2*v**4 + 9*m**2*v**3 + 1440*m*v**6 + 1824*m*v**5 + 1090*m*v**4 + 331*m*v**3 + 48*m*v**2 + m*v + 1728*v**6 + 3024*v**5 + 2556*v**4 + 1261*v**3 + 372*v**2 + 60*v + 4
refs = (A**2*P0, 3*v**2*P1, 3*v**4*P2/A**2)
for lhs,rhs in zip(poly,refs):
    assert sp.cancel(lhs-rhs)==0
assert sp.cancel(poly[0]*poly[2]-poly[1]**2-12*v**5*R)==0
assert all(int(c)>0 for (i,j),c in sp.Poly(R,m,v).terms())
print('NEIGHBORHOOD_POLYNOMIAL_IDENTITIES_OK')

# A genuinely separate exhaustive edge-subset enumeration on K_{3,n}.
for n in (4,5,6):
    edges = [(h, 3+j) for h in range(3) for j in range(n)]
    coeff = [[0]*(3*n+1) for _ in range(3)]
    for state in range(1 << len(edges)):
        parent = list(range(n+3))
        def root(u):
            while parent[u] != u:
                u = parent[u]
            return u
        for i,(a,b) in enumerate(edges):
            if state & (1<<i):
                x,y = root(a),root(b)
                if x == y:
                    break
                parent[x] = y
        else:
            j = state.bit_count()
            ab = root(3)==root(4)
            cd = root(5)==root(6)
            for k,yes in enumerate((True, ab, ab and cd)):
                if yes: coeff[k][j]+=1
    M = n-4
    expected = [sp.cancel(expr.subs(m,M)*A**M) for expr in refs]
    for i in range(3):
        observed = sum(k*v**j for j,k in enumerate(coeff[i]))
        assert sp.cancel(observed-expected[i])==0, (n,i)
    print('EXHAUSTIVE_FOREST_CHECK_OK', n, sum(coeff[0]))
print('ALL_K3N_FOREST_CHECKS_PASSED')
