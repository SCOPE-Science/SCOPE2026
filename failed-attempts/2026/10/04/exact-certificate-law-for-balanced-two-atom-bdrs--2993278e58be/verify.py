import math


def cert_direct(delta, eta, p, q):
    eps = eta / p
    z = math.exp(-delta / eps)
    A = 1.0 / (2.0 * q * (1.0 + z))
    B = q
    Z = [[A * q, A * z * q], [A * z * q, A * q]]
    rows = [sum(Z[0]), sum(Z[1])]
    cols = [Z[0][0] + Z[1][0], Z[0][1] + Z[1][1]]
    U = delta * (Z[0][1] + Z[1][0])
    L = eps * math.log(A) + eps * math.log(B / 0.5)
    return z, Z, rows, cols, U, L, U - L


def cert_closed(delta, eta, p):
    z = math.exp(-p * delta / eta)
    U = delta * z / (1.0 + z)
    L = -(eta / p) * math.log1p(z)
    return U, L, U - L


def bisect_p(delta, eta, tau):
    def G(p):
        return cert_closed(delta, eta, p)[2]
    lo, hi = 1.0, 2.0
    while G(hi) > tau:
        hi *= 2.0
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if G(mid) > tau:
            lo = mid
        else:
            hi = mid
    return hi


def check(delta, eta, lam):
    assert delta > 0.0 and eta > 0.0 and 1.0 <= lam < 2.0
    # Direct reconstruction is independent of the arbitrary scalar incoming scaling q.
    for p in [1.0, 1.25, 2.0, 4.5, 10.0]:
        for q in [0.3, 1.0, 7.0]:
            z, Z, rows, cols, U, L, G = cert_direct(delta, eta, p, q)
            U2, L2, G2 = cert_closed(delta, eta, p)
            assert max(abs(v - 0.5) for v in rows + cols) < 2e-14
            assert abs(U - U2) < 2e-13 * max(1.0, abs(U2))
            assert abs(L - L2) < 2e-13 * max(1.0, abs(L2))
            assert abs(G - G2) < 3e-13 * max(1.0, abs(G2))

    # Monotonicity is checked numerically only as a supplement to the analytic derivative.
    prev = float('inf')
    for j in range(1, 2001):
        p = 1.0 + 0.01 * j
        G = cert_closed(delta, eta, p)[2]
        assert G < prev
        prev = G

    G1 = cert_closed(delta, eta, 1.0)[2]
    for frac in [0.8, 0.4, 0.1, 0.01]:
        tau = frac * G1
        pstar = bisect_p(delta, eta, tau)
        n1 = math.ceil(pstar - 1.0 - 1e-12)
        nl = math.ceil((pstar - 1.0) / lam - 1e-12)
        # Check that these are exactly the first schedule indices satisfying the tolerance.
        assert cert_closed(delta, eta, n1 + 1.0)[2] <= tau * (1.0 + 2e-12)
        if n1 > 0:
            assert cert_closed(delta, eta, n1)[2] > tau * (1.0 - 2e-12)
        assert cert_closed(delta, eta, lam * nl + 1.0)[2] <= tau * (1.0 + 2e-12)
        if nl > 0:
            assert cert_closed(delta, eta, lam * (nl - 1) + 1.0)[2] > tau * (1.0 - 2e-12)


def main():
    for delta, eta in [(1.0, 1.0), (2.3, 0.7), (0.4, 3.0)]:
        for lam in [1.0, 1.2, 1.5, 1.99]:
            check(delta, eta, lam)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
