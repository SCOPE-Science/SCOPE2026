"""gamma_check.py — verify the degree (Waldschmidt) half of the target locally.

Claim checked: for the generic/ladder-type shape filtration with gamma_t(a)=max(0,a-t+1),
  alpha(s) := min{ sum of minor sizes : total gamma_t >= s }  equals  k*m - l
  where s = k*(m-t+1) - l, 0 <= l <= m-t (Kumar--Mukundan Thm 2.4 / 4.3(1) formula),
hence alpha-hat = m/(m-t+1) and alpha/alpha-hat = t*(m-t+1)/m.

This checks ONLY the degree half of the target; it says nothing about rho_a.
Run: python3 output/artifacts/gamma_check.py
"""
import math


def alpha_bruteforce(m, t, s):
    best = None

    def rec(a_lo, rem, deg):
        nonlocal best
        if best is not None and deg >= best:
            return
        if rem <= 0:
            best = deg
            return
        if a_lo > m:
            return
        g = a_lo - t + 1  # >= 1 since a_lo >= t; sizes < t give gamma 0, never optimal
        maxc = (rem + g - 1) // g
        for c in range(maxc + 1):
            rec(a_lo + 1, rem - c * g, deg + c * a_lo)

    rec(t, s, 0)
    return best


def alpha_formula(m, t, s):
    w = m - t + 1
    k = math.ceil(s / w)
    l = k * w - s
    assert 0 <= l <= m - t, (m, t, s, k, l)
    return k * m - l


if __name__ == "__main__":
    cases = [(3, 2), (4, 2), (4, 3), (5, 2), (5, 3), (6, 2), (6, 4)]
    nfail = 0
    for m, t in cases:
        for s in range(1, 25):
            b = alpha_bruteforce(m, t, s)
            f = alpha_formula(m, t, s)
            if b != f:
                print(f"MISMATCH m={m} t={t} s={s}: brute={b} formula={f}")
                nfail += 1
        what = m / (m - t + 1)
        print(f"m={m} t={t}: alpha-hat={what:.4f} "
              f"alpha/alpha-hat={t * (m - t + 1) / m:.4f} (s<=24 checked)")
    print("ALL MATCH" if nfail == 0 else f"{nfail} FAILURES")
