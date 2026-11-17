"""Independent finite and asymptotic diagnostics for damped Hardy monomial products.

Uses only the Python standard library. All infinite assertions require the paper proof.
"""
import math


def diag(M, N, q, cutoff):
    assert math.gcd(M, N) == 1 and M != N and M > 0 and N > 0
    s = [0.0] * (cutoff + 1)
    for j in range(1, cutoff // M + 1):
        s[M * j] += q ** (2 * j)
    for j in range(1, cutoff // N + 1):
        s[N * j] -= q ** (2 * j)
    return s


def closed_p1(M, N, q):
    L = max(M, N)
    return 2 * (q**2 / (1-q**2) - q**(2*L) / (1-q**(2*L)))


def closed_p2square(M, N, q):
    S = M + N
    return 2 * (q**4 / (1-q**4) - q**(2*S) / (1-q**(2*S)))


def boundary_constant(M, N, p):
    a, b = sorted((M, N))
    x = p*a/(b-a)
    beta = math.exp(math.lgamma(x) + math.lgamma(p+1) - math.lgamma(x+p+1))
    return (2 - 1/M - 1/N)/(2*p) + beta/(2*(b-a))


def independent_matrix_diagonal(M, N, q, cutoff):
    # Build the finite weighted monomial-product matrix, then form both Gram diagonals.
    incoming = [0.0] * (cutoff+1)
    outgoing = [0.0] * (cutoff+1)
    for j in range(1, cutoff // max(M,N) + 1):
        column, row, weight = M*j, N*j, q**j
        incoming[column] += weight*weight
        outgoing[row] += weight*weight
    return [incoming[k]-outgoing[k] for k in range(cutoff+1)]


def test():
    tests = 0
    for M in range(1, 8):
        for N in range(1, 8):
            if M == N or math.gcd(M, N) != 1:
                continue
            for q in (0.24, 0.52, 0.77):
                vals = diag(M, N, q, 1500)
                independent = independent_matrix_diagonal(M,N,q,1500)
                limit = 1500 // max(M,N)
                assert all(abs(independent[k]-vals[k])<1e-12 for k in range(limit+1))
                tests += 1
                p1 = sum(abs(x) for x in vals)
                p2 = sum(x*x for x in vals)
                assert abs(p1-closed_p1(M,N,q)) < 1e-9
                assert abs(p2-closed_p2square(M,N,q)) < 1e-9
                assert abs(sum(vals)) < 1e-9
                tests += 3
    # The endpoint coefficients reduce exactly to the closed ideal formulas.
    for M, N in ((1,2),(2,3),(3,4),(2,5),(5,7)):
        for p, expected in ((1, 1-1/max(M,N)), (2, 0.5-1/(M+N))):
            assert abs(boundary_constant(M,N,p)-expected) < 1e-12
            tests += 1
    # Confirm all-p boundary constants with explicit long finite sums.
    h = 0.0005
    q = math.exp(-h)
    for M,N in ((1,2),(2,3),(3,5),(4,7)):
        vals = diag(M,N,q,110000)
        for p in (0.5,1,1.5,2,3):
            estimate=h*sum(abs(x)**p for x in vals)
            target=boundary_constant(M,N,p)
            assert abs(estimate-target) / target < 0.025, (M,N,p,estimate,target)
            tests += 1
    print('CHECKS_OK',tests)

if __name__ == '__main__':
    test()
