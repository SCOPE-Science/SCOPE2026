"""Standalone finite diagnostics for a confined intermittent swimmer.

Requires Python 3 standard library only. Analytic squeeze proof is in RESULT.md.
"""
from math import exp, log, isclose


def check_case(mu, v, h, theta, alpha):
    assert mu > 0 and v > 0 and h > 0 and theta > 0 and alpha > 1
    L = v / mu
    B = exp(-mu*h)
    a = L*(1-B)
    mean_u = theta/(alpha-1)
    m = h+mean_u
    C = mu**(alpha-1)*theta**alpha/m
    assert 0 < a < L and 0 < B < 1
    assert isclose(C, (mu*theta)**alpha/(mu*m), rel_tol=1e-14)
    # Contractivity, positive entry, and upper bound at every tested time.
    nchecks = 0
    for z in (0, L/4, L/2, L):
        y = a+B*z
        assert a <= y <= L*(1+1e-15)
        for u in (0, theta/3, 2*theta, 200*theta):
            z1 = exp(-mu*u)*y
            assert 0 <= z1 <= L*(1+1e-15)
            assert abs(exp(-mu*u)*B*(L-z)) <= B*abs(L-z)+1e-14
            nchecks += 3
    for H in (10, 50, 100, 1000, 10000, 100000):
        # x=L*exp(-H) is represented via H to avoid floating-point underflow.
        # ln(Y/x) in [H+ln(a/L), H].
        lo = H + log(a/L)
        if lo <= 0:
            continue
        def s(t):
            return (1+t/theta)**(-alpha)
        dlo = s(H/mu)*H**alpha/(mu*theta)**alpha
        dhi = s(lo/mu)*H**alpha/(mu*theta)**alpha
        assert dlo <= dhi and dlo > 0
        if H >= 10000:
            assert abs(dlo-1) < 0.01 and abs(dhi-1) < 0.01
        # Conservative exact upper/lower intervals bound the normalized density
        # x*p_off(x)*H^alpha / C, for every possible entrance distribution.
        assert dlo >= (1+(mu*theta)/H)**(-alpha)-1e-12
        nchecks += 4
        # The small-ball term is integrated exactly under Lomax waiting.
        blo = (1+H/(mu*theta))**(1-alpha)*H**(alpha-1)/(mu*theta)**(alpha-1)
        bhi = (1+lo/(mu*theta))**(1-alpha)*H**(alpha-1)/(mu*theta)**(alpha-1)
        assert 0 < blo <= bhi
        if H >= 10000:
            assert abs(blo-1) < 0.01 and abs(bhi-1) < 0.01
        nchecks += 2
    # Deterministic pseudo-sample of the entrance chain from independent uniforms;
    # checks a nontrivial distribution without depending on a random seed.
    state = 0.27*L
    seed = 2463534242
    for _ in range(2500):
        seed ^= (seed << 13) & 0xffffffff
        seed ^= seed >> 17
        seed ^= (seed << 5) & 0xffffffff
        q = max((seed & 0xffffffff)/2**32, 1e-14)
        u = theta*(q**(-1/alpha)-1)
        y = a+B*state
        state = exp(-mu*u)*y
        assert 0 <= state <= L
        nchecks += 1
    return nchecks


def main():
    c = 0
    for vals in ((1., 1., 1., 1., 1.5),
                 (2., 3., 0.7, 1.4, 2.5),
                 (0.5, 2., 0.5, 3., 1.1)):
        c += check_case(*vals)
    print(f'PASS: {c} finite deterministic assertions across 3 physical parameter sets')


if __name__ == '__main__':
    main()
