"""Standalone checks for one-defect four-cycle heat-Lipschitz formulas.

Uses standard-library exact fractions and 80-digit Decimal arithmetic.
Finite tests corroborate the separate analytic argument; they do not prove
its continuum parameter claims.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from itertools import product

EDGES = [(0, 1), (1, 2), (2, 3), (3, 0)]


def matmul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum(A[i][u] * B[u][j] for u in range(k))
             for j in range(m)] for i in range(n)]


def generator(r):
    L = [[Q(0) for _ in range(4)] for _ in range(4)]
    for (i, j), w in zip(EDGES, (r, Q(1), Q(1), Q(1))):
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    return L


def gradient_matrices(r):
    G = [[Q(0) for _ in range(4)] for _ in range(4)]
    for row, (i, j) in enumerate(EDGES):
        G[row][j] = Q(1)
        G[row][i] = Q(-1)
    B = [[-2*r, Q(1), Q(0), Q(1)],
         [r, Q(-2), Q(1), Q(0)],
         [Q(0), Q(1), Q(-2), Q(1)],
         [r, Q(0), Q(1), Q(-2)]]
    return G, B


def decimal_ratio(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


def uniformized_heat(r, t):
    """Independent stochastic uniformization of exp(-t L), no eigensystems."""
    L = generator(r)
    nu = max(L[i][i] for i in range(4))
    P = [[(Q(1) if i == j else Q(0)) - L[i][j]/nu
          for j in range(4)] for i in range(4)]
    assert all(v >= 0 for row in P for v in row)
    assert all(sum(row) == 1 for row in P)
    P = [[decimal_ratio(v) for v in row] for row in P]
    K = [[Decimal(i == j) for j in range(4)] for i in range(4)]
    H = [[Decimal(0) for _ in range(4)] for _ in range(4)]
    z = decimal_ratio(nu*t)
    coeff = (-z).exp()
    for k in range(400):
        for i in range(4):
            for j in range(4):
                H[i][j] += coeff*K[i][j]
        K = matmul(K, P)
        coeff = coeff*z/Decimal(k+1)
        if k+1 > 2*z and coeff < Decimal('1e-72'):
            # The tail is at most twice this next Poisson probability.
            assert 2*coeff < Decimal('1e-71')
            break
    else:
        raise RuntimeError('uniformization tail not certified')
    return H, k + 1


def extreme_potentials():
    pots = []
    for g in product((-1, 1), repeat=4):
        if sum(g) != 0:
            continue
        f = (0, g[0], g[0]+g[1], g[0]+g[1]+g[2])
        assert f[0]-f[3] == g[3]
        pots.append(f)
    assert len(pots) == 6
    return pots


def theoretical(r, t):
    rr = decimal_ratio(r)
    tt = decimal_ratio(t)
    D = ((rr-1)**2+1).sqrt()
    alpha = rr+2-D
    beta = rr+2+D
    if rr < 1:
        return ((1+(2-rr)/D)/2)*(-alpha*tt).exp() + \
               ((1-(2-rr)/D)/2)*(-beta*tt).exp()
    return (-2*tt).exp() + (rr-1)/(2*D)*(
        (-alpha*tt).exp()-(-beta*tt).exp())


def independent_norm(H):
    pots = extreme_potentials()
    vals = []
    for i, j in EDGES:
        vals.append(max(abs(sum((H[i][u]-H[j][u])*Decimal(f[u])
                                for u in range(4))) for f in pots))
    return vals


def main():
    exact_checks = 0
    with localcontext() as ctx:
        ctx.prec = 85
        qs = [Q(1,5),Q(1,2),Q(3,4),Q(1),Q(4,3),Q(2),Q(3),Q(4),Q(5),Q(10)]
        ts = [Q(1,100),Q(1,10),Q(1,2),Q(1)]
        uniformization_terms = 0
        for r in qs:
            L = generator(r)
            G, B = gradient_matrices(r)
            assert matmul(B,G) == [[-v for v in row] for row in matmul(G,L)]
            exact_checks += 1
            if r < 1:
                assert -(r+Q(2))+(Q(2)-r) == -2*r
            elif r > 1:
                assert -Q(2)+(r-Q(1)) == r-Q(3)
            for t in ts:
                H, terms = uniformized_heat(r, t)
                uniformization_terms += terms
                n = independent_norm(H)
                expected = theoretical(r,t)
                assert abs(max(n)-expected) < Decimal('1e-66'), (r,t,n,expected)
                if r < 1:
                    assert n[0] > max(n[1:]) + Decimal('1e-67')
                if r > 1:
                    assert n[1] > max(n[0],n[2]) + Decimal('1e-67')
                    assert abs(n[1]-n[3]) < Decimal('1e-67')
                if r == 1:
                    assert max(n)-min(n) < Decimal('1e-67')
        # Prove derivative-at-zero sign exactly from the formula's
        # first-order coefficient: r-3 for r>1 and -2r for r<1.
        assert [q-Q(3) for q in (Q(2),Q(3),Q(4))] == [Q(-1),Q(0),Q(1)]
        # Check the high-conductance limiting envelope is approached.
        rr = Decimal(10)**7
        tt = rr.ln()/rr
        D = ((rr-1)**2+1).sqrt()
        al = rr+2-D
        be = rr+2+D
        peak_witness = (-2*tt).exp()+(rr-1)/(2*D)*(
            (-al*tt).exp()-(-be*tt).exp())
        assert Decimal('1.49998') < peak_witness < Decimal('1.5')
    print('CHECK_OK exact_intertwining_parameter_cases=%d independent_heat_dual_cases=%d' %
          (exact_checks, len(qs)*len(ts)))
    print('CHECK_OK certified_uniformization_poisson_terms=%d branch_winners=all_cases' %
          uniformization_terms)
    print('CHECK_OK derivative_threshold_r=3 upper_envelope_approached=3/2')


if __name__ == '__main__':
    main()
