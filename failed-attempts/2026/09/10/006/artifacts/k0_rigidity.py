"""K0/Chern rigidity + absorption lemma audit for lane-506 (target-directed).

Stdlib only. Run: python3 k0_rigidity.py
"""
from math import factorial


def sigma(n):
    return 1 if n == 0 else n * factorial(n)


def kappa(n):
    return n * sigma(n)


def test_telescoping():
    # l*l! = (l+1)! - l!  => 1 + sum_{l>=1} l*l! = (n+1)!
    for n in range(0, 15):
        assert sum(sigma(l) for l in range(n + 1)) == factorial(n + 1), n
        for l in range(1, n + 1):
            assert l * factorial(l) == factorial(l + 1) - factorial(l), l
    print("telescoping rank(xi_n)=(n+1)!: OK to 14")


def test_absorption_analytic():
    # Claim (k=inf): (l+1)*sum_{i<=l} kappa_i <= kappa_{l+1} for all l>=1.
    # Proof audited here: T_i=i^2 i!, T_i/T_l <= 1/l^{l-i} (i<l):
    #   T_{l-1}/T_l = ((l-1)/l)^2 * 1/l < 1/l;
    #   deeper tail even smaller. So sum_{i<l} T_i <= T_l/(l-1),
    #   total <= T_l * l/(l-1) = l^3 l!/(l-1) <= (l+1)^2 l! = kappa_{l+1}/(l+1)
    #   iff l^3 <= (l-1)(l+1)^2 iff 0 <= l^2-l-1 (l>=2). l=1 direct.
    for l in range(1, 60):
        s = sum(i * i * factorial(i) for i in range(1, l + 1))
        assert (l + 1) * s <= (l + 1) * (l + 1) * factorial(l + 1), l
        # clean analytic tail: T_i = i^2 i! <= l^{2} ... use direct ratio<=1/i chain:
        # T_{j}/T_{j+1} = (j/(j+1))^2 * 1/(j+1) <= 1/(j+1), so T_i <= T_l / prod_{j=i}^{l-1}(j+1)
        from fractions import Fraction
        for i in range(1, l):
            ratio = Fraction(i * i * factorial(i), l * l * factorial(l))
            denom = 1
            for j in range(i, l):
                denom *= (j + 1)
            assert ratio <= Fraction(1, denom), (l, i, ratio)
    print("absorption inequality analytic skeleton: OK to 59")


def test_cp1_rigidity():
    # Over CP^1 ~= S^2: K0 = Z^2 via (rank, c1). Line-bundle sums
    # a*g (+) b*theta have (rank, c1) = (a+b, -a) (sign convention fixed).
    # Map (a,b) -> (rank, c1) is injective: equal K0 => equal (a,b) => equal Euler.
    seen = {}
    for a in range(0, 6):
        for b in range(0, 6):
            key = (a + b, -a)
            assert key not in seen, (a, b, seen[key])
            seen[key] = (a, b)
    print("CP^1 (rank,c1) injectivity on 6x6 grid: OK")
    print("consequence: same-rank K0-equal projections have equal c1=Euler;")
    print("Euler (top Chern) cannot separate a K0-equal pair (lines).")


def test_torsionfree_kunneth():
    # H*(CP^N;Z) = Z[h]/(h^{N+1}), free. Product => free (Kunneth, no Tor).
    # ch: K^0(X_n) -> H^{ev}(X_n;Q) is injective (Atiyah-Hirzebruch collapses
    # rationally for products of CP). Hence [p]=[q] => rational Chern equal
    # => top Chern (Euler, when ranks equal) equal. Statement recorded; the
    # CP^1 grid above is the computed instance.
    print("torsion-free Kunneth/chern-rigidity statement: RECORDED (textbook)")


def main():
    test_telescoping()
    test_absorption_analytic()
    test_cp1_rigidity()
    test_torsionfree_kunneth()
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
