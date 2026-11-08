"""Reproduce stationary moment, endpoint density and Gaussian-tail calculations.

Run: python verify.py
Only finite checks are performed; the all-parameter statements use the proof.
"""
from fractions import Fraction as F
from math import factorial, gamma, sqrt, pi, exp
import mpmath as mp


def variance_moments(q2, alpha, nmax):
    values = [F(1)]
    for n in range(1, nmax + 1):
        values.append(values[-1] * n / (n + alpha * (1 - q2 ** n)))
    return values


def prefactor_series(q2, alpha, nmax):
    # Exact for nonnegative integer alpha; suitable for rational examples.
    vals = variance_moments(q2, alpha, nmax)
    coeff = F(1)
    out = F(0)
    for n in range(nmax + 1):
        out += coeff * (q2 ** n) * vals[n]
        coeff *= F(alpha + n, n + 1)
    return out


def test_exact():
    count = 0
    for alpha in [F(1, 3), F(1, 2), F(1), F(2), F(5, 2), F(4)]:
        for q in [F(0), F(1, 4), F(1, 2), F(3, 4)]:
            q2 = q*q
            moments = variance_moments(q2, alpha, 12)
            for n in range(1, len(moments)):
                assert (n + alpha * (1-q2**n))*moments[n] == n*moments[n-1]
                count += 1
            mu = moments[1]
            k = moments[2]/mu**2 - 1
            assert k == alpha*(1-q2)**2/(2+alpha*(1-q2**2))
            count += 1
            assert F(0) < mu <= F(1)
            count += 1
    return count


def test_asymptotics():
    mp.mp.dps = 70
    count = 0
    for q2, alpha in [(mp.mpf('0'), mp.mpf('1')), (mp.mpf('0.25'), mp.mpf('1')), (mp.mpf('0.36'), mp.mpf('1.5'))]:
        sig2 = mp.mpf('1')
        # Positive convergent moment series for B=E(1-q^2 V)^(-alpha).
        moment, bsum, coeff = mp.mpf(1), mp.mpf(1), mp.mpf(1)
        for n in range(1, 1500):
            moment *= n/(n+alpha*(1-q2**n))
            coeff *= (alpha+n-1)/n
            term = coeff*q2**n*moment
            bsum += term
            if abs(term) < mp.mpf('1e-50'):
                break
        assert bsum >= 1
        count += 1
        delta = 1-q2
        # For u<delta, stationary deficit density is exactly alpha*B*u^(alpha-1).
        for x in [mp.mpf('15'), mp.mpf('30')]:
            s=x*x/(2*sig2)
            local=mp.quad(lambda u: alpha*bsum*u**(alpha-1)/mp.sqrt(1-u)*mp.exp(-s*u/(1-u)), [0,delta])
            leading=mp.gamma(alpha+1)*bsum*s**(-alpha)
            ratio=local/leading
            assert abs(ratio-1)<mp.mpf('0.12'), (q2,alpha,x,ratio)
            # Upper bound for the missing u>=delta integral, normalized by the leading term.
            if q2 != 0:
                c=alpha*delta**(-alpha)
                remainder_bound = c*mp.quad(lambda u: u**(alpha-1)/mp.sqrt(1-u)*mp.exp(-s*u/(1-u)), [delta,1])
                assert remainder_bound/leading < mp.mpf('1e-20')
            count += 1
    # Coefficient B rises as the contraction gets less severe, on a fixed alpha slice.
    seq=[]
    for q in [F(0),F(1,4),F(1,2),F(3,4)]:
        seq.append(float(prefactor_series(q*q, 1, 80)))
    assert all(a<b for a,b in zip(seq,seq[1:]))
    count += 1
    return count,seq

if __name__ == '__main__':
    a=test_exact()
    b,seq=test_asymptotics()
    print(f'PASS: {a} exact moment/kurtosis checks, {b} high-precision asymptotic/constant checks')
    print('Monotone numerical prefactor series (alpha=1, q=0,1/4,1/2,3/4):',seq)
