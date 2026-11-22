"""Finite, high-precision checks of the exact TTR symbol coefficient identity.

Requires mpmath (https://mpmath.org/). The all-order result is proved
analytically; these checks do not establish infinitely many cases.
Run: python verify.py
"""
from math import comb
from mpmath import mp

mp.dps = 110
count = 0

def check(ok, message):
    global count
    count += 1
    if not ok:
        raise AssertionError(message)

for J in range(2, 31):
    x = mp.pi / (J + 1)
    q = [mp.sin((r + 1) * x) for r in range(J)]
    S = sum(t * t for t in q)
    check(abs(S - mp.mpf(J + 1) / 2) < mp.mpf('1e-100'), f'S {J}')
    c2 = 2 * mp.cos(x) / (1 + mp.cos(x))
    normal = 4 - 2 * c2
    A = {k: normal * 2 / (J + 1) * (-1)**k *
         ((J-k) * mp.cos(k*x) + mp.sin((k+1)*x)/mp.sin(x))
         for k in range(2, J)}
    # Directly reconstruct Ferrari's optimized coefficients via the
    # inverse binomial formula (Lemma 4.3), not via the new assertion.
    c = {2: c2}
    for ell in range(3, J+1):
        c[ell] = (-1)**(ell-1) * mp.power(2, ell-4) * sum(
            comb(k-2, ell-3) * A[k] for k in range(ell-1, J))
    b = [mp.mpf(0)] * (J+2)
    b[1], b[2] = mp.mpf(1), mp.mpf('0.5')
    for ell in range(2, J+1):
        b[ell+1] = c[ell] / mp.power(2, ell)
    direct = [sum(b[k] * (-1)**j * comb(k,j)
                  for k in range(max(1,j),J+2)) for j in range(J+2)]
    a = [sum(weight * (q[m-offset] if 0 <= m-offset < J else 0)
             for offset, weight in ((0,1),(1,2),(2,1)))
         for m in range(J+2)]
    C = 1 / (2 * (J+1) * (1+mp.cos(x)))
    corr = [sum(a[t]*a[t+k] for t in range(J+2-k)) for k in range(J+2)]
    predicted = [C*corr[0]] + [2*C*(-1)**k*corr[k] for k in range(1,J+2)]
    for j in range(J+2):
        check(abs(direct[j]-predicted[j]) < mp.mpf('1e-75'), f'coefficient J={J} j={j}')
        check((-1)**j * predicted[j] > 0, f'coefficient sign J={J} j={j}')
    endpoint = sum(direct[j]*(-1)**j for j in range(J+2))
    formula = 4 / ((J+1) * mp.sin(x/2)**2)
    check(abs(endpoint-formula) < mp.mpf('1e-75'), f'endpoint J={J}')
    for r in (mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf(1), mp.mpf('1.7')):
        sharp = sum(predicted[j]*(-r)**j for j in range(J+2))
        for aidx in range(37):
            z = r * mp.e**(2j*mp.pi*aidx/37)
            val = sum(direct[j]*z**j for j in range(J+2))
            check(abs(val) <= sharp + mp.mpf('1e-70'), f'circle J={J}, r={r}')
print('VERIFY_OK',count)
