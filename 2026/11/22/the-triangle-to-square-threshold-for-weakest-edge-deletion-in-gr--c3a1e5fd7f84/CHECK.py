"""Exact rational and symbolic verification of the heat-fidelity cycle theorem.

Requires Python 3 and SymPy. No probabilistic arguments or numerical integration
are used in the proof checks.
"""
import sympy as S


def restriction(n, edges, weights):
    """Matrix on the zero-sum space in the basis (e_i-e_{n-1})."""
    q = S.eye(n)[:, : n - 1]
    for i in range(n - 1):
        q[n - 1, i] = -1
    l = S.zeros(n)
    for (i, j), w in zip(edges, weights):
        v = S.zeros(n, 1)
        v[i] = 1
        v[j] = -1
        l += w * v * v.T
    return (q.T * q).inv() * q.T * l * q


def integrated_heat_error(m, n):
    """Integrate squared Frobenius norm via a finite Sylvester equation."""
    d = m.rows
    # Column-major vectorization: (I ⊗ M + N^T ⊗ I) vec(Z)=vec(I).
    k = S.kronecker_product(S.eye(d), m) + S.kronecker_product(n.T, S.eye(d))
    rhs = S.Matrix([int(i % d == i // d) for i in range(d * d)])
    z = k.inv() * rhs
    trace_z = sum(z[i * d + i] for i in range(d))
    return S.factor((S.trace(m.inv()) + S.trace(n.inv())) / 2 - 2 * trace_z)


def all_coefficients_strictly_positive(expr, variables):
    poly = S.Poly(S.expand(expr), *variables)
    return bool(poly.terms()) and all(c > 0 for c in poly.coeffs())


def proof_triangle():
    a, b, c = S.symbols('a b c', positive=True)
    vals = (a, b, c)
    edges = [(0, 1), (1, 2), (0, 2)]
    m = restriction(3, edges, vals)
    errors = []
    for i in range(3):
        removed = list(vals)
        removed[i] = S.Integer(0)
        errors.append(integrated_heat_error(m, restriction(3, edges, removed)))
    for other, edge_weight in ((1, b), (2, c)):
        # E(delete edge of weight edge_weight) - E(delete a)
        # = (edge_weight-a)*P/Q with P,Q having only positive coefficients.
        quotient = S.cancel((errors[other] - errors[0]) / (edge_weight - a))
        p, q = S.fraction(quotient)
        assert all_coefficients_strictly_positive(p, vals), 'numerator sign'
        assert all_coefficients_strictly_positive(q, vals), 'denominator sign'
        assert S.simplify((edge_weight - a) * p / q - errors[other] + errors[0]) == 0
        print('Triangle sign factor confirmed for comparison 0 vs', other,
              '| numerator monomials', len(S.Poly(p, *vals).terms()),
              '| denominator monomials', len(S.Poly(q, *vals).terms()))


def proof_four_cycle():
    w = [100, 10, 11, 11]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    m = restriction(4, edges, w)
    errors = []
    for i in range(4):
        removed = w.copy()
        removed[i] = 0
        errors.append(integrated_heat_error(m, restriction(4, edges, removed)))
    expected = [
        S.Rational(1436863131833465, 20857430364786048),
        S.Rational(12484655540506124917, 629870805581225287200),
        S.Rational(38496709664197, 2114507504264100),
        S.Rational(827146948257857, 35144400164887200),
    ]
    assert errors == expected, (errors, expected)
    assert w[1] < min(w[0], w[2], w[3])
    for i in (0, 1, 3):
        assert errors[i] - errors[2] > 0
    print('Four-cycle exact rational values:', errors)
    print('Weakest-edge deletion minus optimal:', S.factor(errors[1] - errors[2]))


if __name__ == '__main__':
    proof_triangle()
    proof_four_cycle()
    print('All exact proof checks passed.')
