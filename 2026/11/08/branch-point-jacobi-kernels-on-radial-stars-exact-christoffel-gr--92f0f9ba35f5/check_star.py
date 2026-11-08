"""Numerical identity and hard-edge checks for Jacobi-star polynomial kernels.

Requires Python 3 and mpmath. All assertions are finite tests; the analytical
proof establishes the general theorem.
"""
import mpmath as mp

mp.mp.dps = 60


def h(j, a, b):
    if j == 0:
        return mp.beta(a, b + 1)
    return (mp.gamma(j + a) * mp.gamma(j + b + 1)
            / ((2 * j + a + b) * mp.factorial(j)
               * mp.gamma(j + a + b)))


def star_kernel(q, n, beta, alpha, z, w):
    a0 = (beta + 1) / q
    out = 0
    for m in range(q):
        am = (beta + 2 * m + 1) / q
        nm = (n - m) // q
        if nm < 0:
            continue
        block = 0
        for j in range(nm + 1):
            block += (mp.jacobi(j, am - 1, alpha, 1 - 2 * z**q)
                      * mp.jacobi(j, am - 1, alpha, 1 - 2 * mp.conj(w)**q)
                      / h(j, am, alpha))
        out += (z * mp.conj(w))**m * block
    return mp.beta(a0, alpha + 1) * out


def gram_kernel(q, n, beta, alpha, z, w):
    a0 = (beta + 1) / q
    mat = mp.matrix(n + 1)
    for k in range(n + 1):
        for l in range(n + 1):
            mat[k, l] = (mp.beta((beta + k + l + 1) / q, alpha + 1)
                         / mp.beta(a0, alpha + 1)
                         if (k - l) % q == 0 else 0)
    rhs = mp.matrix([w**k for k in range(n + 1)])
    sol = mp.lu_solve(mat, rhs)
    return sum(z**k * mp.conj(sol[k]) for k in range(n + 1))


def closed_center(q, n, beta, alpha):
    n0 = n // q
    a = (beta + 1) / q
    return (mp.gamma(alpha + 1) * mp.gamma(n0 + a + 1)
            * mp.gamma(n0 + a + alpha + 1)
            / (mp.gamma(a + 1) * mp.gamma(a + alpha + 1)
               * mp.gamma(n0 + 1) * mp.gamma(n0 + alpha + 1)))


def f(a, v):
    return mp.hyper([], [a], -v) / mp.gamma(a)


def hard_edge(q, beta, alpha, xi, eta):
    a0 = (beta + 1) / q
    total = 0
    for m in range(q):
        am = (beta + 2 * m + 1) / q
        total += (xi * mp.conj(eta))**m * mp.quad(
            lambda s: s**(2 * am - 1)
            * f(am, s**2 * xi**q)
            * f(am, s**2 * mp.conj(eta)**q), [0, 1])
    return 2 * mp.beta(a0, alpha + 1) * total


def test():
    count = 0
    z = mp.mpc('0.13', '0.11')
    w = mp.mpc('-0.12', '0.05')
    for q, n, beta, alpha in (
        (2, 7, '1.2', '0.4'),
        (3, 8, '0.7', '0.5'),
        (4, 11, '0.2', '0.3'),
        (3, 10, '0.4', '-0.2'),
    ):
        beta, alpha = mp.mpf(beta), mp.mpf(alpha)
        k1 = star_kernel(q, n, beta, alpha, z, w)
        k2 = gram_kernel(q, n, beta, alpha, z, w)
        assert abs(k1 - k2) < mp.mpf('1e-33')
        count += 1
        k0 = star_kernel(q, n, beta, alpha, 0, 0)
        assert abs(k0 - closed_center(q, n, beta, alpha)) < mp.mpf('1e-44')
        count += 1
    xi, eta = mp.mpc('0.7', '0.2'), mp.mpc('-0.3', '0.1')
    for q in (2, 3, 4):
        beta, alpha = mp.mpf('0.6'), mp.mpf('0.3')
        a0 = (beta + 1) / q
        target = hard_edge(q, beta, alpha, xi, eta)
        old = None
        for n_shell in (20, 70):
            n = q * n_shell + q - 1
            scaled = star_kernel(
                q, n, beta, alpha,
                xi / n_shell**(mp.mpf(2) / q),
                eta / n_shell**(mp.mpf(2) / q)) / n_shell**(2 * a0)
            err = abs(scaled - target) / abs(target)
            assert err < (mp.mpf('0.08') if n_shell == 20 else mp.mpf('0.03'))
            if old is not None:
                assert err < old
            old = err
            count += 1
    # Center-normalized universality: outer Jacobi exponent disappears.
    q, beta = 3, mp.mpf('0.6')
    a0 = (beta + 1) / q
    target0 = hard_edge(q, beta, mp.mpf('-0.3'), xi, eta)
    target1 = hard_edge(q, beta, mp.mpf('1.3'), xi, eta)
    center0 = mp.beta(a0, mp.mpf('0.7')) / (a0 * mp.gamma(a0)**2)
    center1 = mp.beta(a0, mp.mpf('2.3')) / (a0 * mp.gamma(a0)**2)
    assert abs(target0 / center0 - target1 / center1) < mp.mpf('1e-40')
    count += 1
    for shell in (40, 80):
        normvals = []
        for alpha in (mp.mpf('-0.3'), mp.mpf('1.3')):
            n = q * shell + q - 1
            v = star_kernel(q, n, beta, alpha,
                            xi / shell**(mp.mpf(2) / q),
                            eta / shell**(mp.mpf(2) / q))
            normvals.append(v / closed_center(q, n, beta, alpha))
        assert abs(normvals[0] - normvals[1]) < (mp.mpf('0.04') if shell == 40 else mp.mpf('0.02'))
        count += 1
    print(f'JACOBI_STAR_KERNEL_CHECK_PASS moment_and_center=8 hard_edge=6 normalized_universality=3 total={count}')


if __name__ == '__main__':
    test()
