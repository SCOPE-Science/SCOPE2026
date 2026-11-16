"""Exact rational diagnostics for one-harmonic Sobolev circle polynomials.

Usage: python3 CHECK.py
Only the Python 3 standard library is needed.
This finite test supplements, and does not replace, the all-degree proof.
"""
from fractions import Fraction as F


def coefficients(m, beta, tau, n):
    """Return monic coefficients in increasing degree, exactly as Fractions."""
    assert m >= 1 and n >= 1 and 0 <= beta <= F(1, 2) and tau > 0
    a = [F(0)] * (n + 1)
    a[n] = F(1)
    if beta == 0:
        return a
    r = n % m or m
    # Backward solve a chain in the congruence class of n modulo m.
    # First compute pivots by forward elimination.
    ks = list(range(r, n + 1, m))
    diag = {}
    for k in ks[:-1]:
        ap = 1 + tau*k*k
        coupling = tau*beta*(k-m)*k if k > m else 0
        diag[k] = ap - (coupling * coupling / diag[k-m] if k > m else 0)
        assert diag[k] > 0
    for k in reversed(ks[:-1]):
        b = tau*beta*k*(k+m)
        a[k] = -b*a[k+m]/diag[k]
    return a


def inner_monomial(j, k, m, beta, tau):
    if j == k:
        return 1 + tau*j*j
    if abs(j-k) == m:
        return tau*beta*j*k
    return F(0)


def run():
    count=0
    for m in range(1, 9):
        betas = [F(0), F(1, 8), F(1, m+1)]
        if m > 1:
            betas += [F(1, 2)]
        for beta in set(betas):
            for tau in [F(1, 9), F(1), F(17)]:
                for n in range(1, 26):
                    a=coefficients(m,beta,tau,n)
                    assert a[n] == 1 and a[0] == 0
                    for k in range(n):
                        inner=sum((a[j]*inner_monomial(j,k,m,beta,tau)
                                   for j in range(n+1)), F(0))
                        assert inner == 0, (m,beta,tau,n,k,inner)
                        count+=1
                    if beta > 0 and beta <= F(1,m+1):
                        r=n % m or m
                        R=(m+1)*beta
                        for k in range(r,n-m+1,m):
                            assert a[k] and a[k+m]
                            assert -a[k]/a[k+m] > 0
                            assert -a[k]/a[k+m] < R
                            count+=2
                    if n==m+1:
                        assert a[1] == -tau*beta*(m+1)/(1+tau)
                        count+=1
    for m in range(2, 9):
        beta=F(1, 2)
        R=(m+1)*beta
        assert R>1
        tau=F(2,1)/(R-1)
        a=coefficients(m,beta,tau,m+1)
        assert -a[1] > 1
        count+=1
    print('PASS:',count,'exact rational identities and inequalities')


if __name__ == '__main__':
    run()
