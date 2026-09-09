"""Certified fixed-twist no-go check at Sobolev cell sigma*=10 (stdlib only).

Model: 1D free transport diagnostically standing in for the principal part of
linearized Vlasov-Poisson on T_x x R_v. Single x-mode k=1, Gaussian data
  hhat(0,1,eta) = exp(-eta^2/2),  hhat(t,1,eta) = exp(-(eta+t)^2/2).
Weight W(eta) = (2+eta^2)^10. Twisted energy (k=1):
  E(t) = 1/2 ∫ W(eta) Q(eta) exp(-(eta+t)^2) d eta,
  Q(eta) = (1+a) + 2 b eta + c eta^2.
Admissible (norm-equivalent) iff c>0 and (1+a)*c > b^2.

Since sigma*=10 is an integer, W*Q is a polynomial of degree 22 and every
integral reduces to Gaussian moments mu_p = ∫ u^p e^{-u^2} du, with
mu_{2q}/sqrt(pi) = (2q-1)!!/2^q exactly. E(t)/E(0) is therefore an exact
rational number (sqrt(pi) cancels). All arithmetic below is exact via
fractions; t_* values are integers so (-t)^powers are exact.
"""
from fractions import Fraction
from math import comb

SIGMA = 10
T_STAR = 3


def odd_double_fact(q):
    # (2q-1)!! as int, q>=0; (-1)!! = 1
    if q <= 0:
        return 1
    r = 1
    for k in range(1, 2 * q, 2):
        r *= k
    return r


def mu_even_over_sqrtpi(q):
    # mu_{2q}/sqrt(pi) = (2q-1)!! / 2^q, exact Fraction
    return Fraction(odd_double_fact(q), 2 ** q)


def W_coeffs():
    # (2+eta^2)^10 = sum_{i=0}^{10} binom(10,i) 2^{10-i} eta^{2i}; return dict power->Fraction
    d = {}
    for i in range(11):
        d[2 * i] = Fraction(comb(10, i) * (2 ** (10 - i)), 1)
    return d


def E_poly_over_sqrtpi(a, b, c):
    """Return coeffs e[j] (Fraction) with E(t)/sqrt(pi) = sum_j e[j] t^j."""
    w = W_coeffs()
    # d_j coeffs of W*Q
    d = {}
    for p, coef in w.items():
        d[p] = d.get(p, Fraction(0)) + coef * (Fraction(1) + a)
        d[p + 1] = d.get(p + 1, Fraction(0)) + coef * (Fraction(2) * b)
        d[p + 2] = d.get(p + 2, Fraction(0)) + coef * c
    maxd = max(d)
    # J_m(t) = sum_{p=0}^{m} binom(m,p)(-t)^{m-p} mu_p ; odd mu_p=0
    # E/sqrt(pi) = 1/2 sum_m d_m J_m/sqrt(pi)
    e = [Fraction(0)] * (maxd + 1)
    for m in range(maxd + 1):
        dm = d.get(m, Fraction(0))
        if dm == 0:
            continue
        for p in range(0, m + 1, 2):  # odd moments vanish
            mu = mu_even_over_sqrtpi(p // 2)
            pw = m - p  # power of t, coeff binom(m,p)(-1)^{m-p}
            e[pw] += dm * Fraction(comb(m, p), 1) * (Fraction(-1) ** (m - p)) * mu
    return [v / 2 for v in e]


def eval_poly(e, t):
    t = Fraction(t)
    s = Fraction(0)
    for j, c in enumerate(e):
        s += c * (t ** j)
    return s


def base_poly_over_sqrtpi():
    e = [Fraction(0)] * 21
    w = W_coeffs()
    for m, dm in w.items():
        for p in range(0, m + 1, 2):
            mu = mu_even_over_sqrtpi(p // 2)
            e[m - p] += dm * Fraction(comb(m, p), 1) * (Fraction(-1) ** (m - p)) * mu
    return e


def admissible(a, b, c):
    return c > 0 and (Fraction(1) + a) * c - b * b > 0


def main():
    grid = []
    for a in [Fraction(0), Fraction(1, 4), Fraction(1, 2)]:
        for b in [Fraction(-1, 8), Fraction(0), Fraction(1, 8), Fraction(1, 4)]:
            for c in [Fraction(1, 8), Fraction(1, 4), Fraction(1, 2)]:
                if admissible(a, b, c):
                    grid.append((a, b, c))
    assert grid, "empty admissible grid"
    nb = base_poly_over_sqrtpi()
    n0, n3 = eval_poly(nb, 0), eval_poly(nb, T_STAR)
    assert n0 > 0 and n3 > 0
    base_ratio = n3 / n0
    print(f"sigma*=10 base H^sigma growth: N({T_STAR})^2/N(0)^2 = {base_ratio} "
          f"(~{float(base_ratio):.6g})")
    assert base_ratio > 1000, "base filamentation growth unexpectedly small"
    worst = None
    for (a, b, c) in grid:
        e = E_poly_over_sqrtpi(a, b, c)
        e0, e3 = eval_poly(e, 0), eval_poly(e, T_STAR)
        assert e0 > 0 and e3 > 0, f"non-positive energy at {a,b,c}"
        r = e3 / e0
        # leading-coefficient positivity check: coeff of t^22 equals c*sqrt(pi) part
        assert e[22] == c / 2, f"leading coeff mismatch at {a,b,c}"
        assert e[22] > 0
        print(f"  (a,b,c)=({a},{b},{c}): E({T_STAR})/E(0) = {r} (~{float(r):.6g})")
        assert r > 100, f"growth certificate failed at {a,b,c}"
        if worst is None or r < worst[0]:
            worst = (r, (a, b, c))
    print(f"certified {len(grid)} admissible triples; minimal growth {worst[0]} at {worst[1]}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
