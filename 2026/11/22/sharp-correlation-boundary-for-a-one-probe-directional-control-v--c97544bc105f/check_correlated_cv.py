"""Exact rational finite-case Wick verifier for correlated Gaussian probe descent.

This script checks the analytic polynomial coefficients in representative dimensions.
The general-dimensional proof is given separately in RESULT.md; finite checks alone
are not a universal proof. Requires only Python's standard library.
"""
from fractions import Fraction as F
from functools import lru_cache


def gaussian_wick(d, rho):
    @lru_cache(maxsize=None)
    def moment(labels):
        if not labels:
            return F(1)
        if len(labels) % 2:
            return F(0)
        a = labels[0]
        ans = F(0)
        for j in range(1, len(labels)):
            b = labels[j]
            if a % d != b % d:
                continue
            cv = F(1) if (a < d) == (b < d) else rho
            if cv:
                ans += cv * moment(labels[1:j] + labels[j+1:])
        return ans
    return lambda *indices: moment(tuple(sorted(indices)))


def polynomials(d, k, i):
    # G_j = u_i u_j + 1_{j<k} v_i v_j - sum_{l<k} u_j u_l v_i v_l
    out = []
    for j in range(d):
        terms = [(F(1), (i, j))]
        if j < k:
            terms.append((F(1), (d+i, d+j)))
        for ell in range(k):
            terms.append((F(-1), (j, ell, d+i, d+ell)))
        out.append(terms)
    return out


def formula(d, k, q):
    cs = (d*k + d + k + 2
          + q * (d*k*k + 3*d*k + 4*d + 2*k*k + 8*k + 10)
          + q*q * (2*k*k + 10*k + 12))
    ct = (d*k + d + k + 2
          + q * (d*k*k - d*k + 2*k*k)
          + q*q * (2*k*k + 2*k))
    return cs, ct


def check_case(d, k, rho):
    E = gaussian_wick(d, rho)
    q = rho*rho
    cs, ct = formula(d, k, q)
    for i in sorted(set([0, k] if k < d else [0])):
        G = polynomials(d, k, i)
        mean = sum(c*E(*indices) for c, indices in G[i])
        required_mean = 1-(k+(i<k))*q
        assert mean == required_mean, (d, k, rho, i, mean, required_mean)
        sq = sum(c*e*E(*(a+b)) for terms in G for c,a in terms for e,b in terms)
        target = cs if i < k else ct
        assert sq == target, (d,k,rho,i,sq,target)
        assert target > 0
        if q < F(1,k+1):
            h = (1-(k+1)*q)/cs
            worst_factor = 1-2*h*(1-(k+1)*q)+h*h*cs
            assert worst_factor == 1-(1-(k+1)*q)**2/cs
        if q >= F(1,k+1) and i < k:
            assert 1-(k+1)*q <= 0
    return True


def main():
    count=0
    for d in range(1,7):
        for k in range(1,d+1):
            for rho in (F(0), F(1,3), F(1,2), F(4,5), F(1)):
                check_case(d,k,rho)
                count+=1
    print('PASS: %d exact-rational dimension/rank/correlation cases, both mean and squared norm.' % count)

if __name__ == '__main__':
    main()
