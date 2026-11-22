"""Exact finite-state and asymptotic checks for the stationary rare-corner passage law.
Pure Python 3; no third-party packages. Checks are corroboration, not a proof.
"""
from fractions import Fraction as F
from math import comb, exp, log, log1p, expm1, lgamma

checks = 0

def affirm(statement, context):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(context)

def linear_solve(a, b):
    n = len(b)
    v = [list(a[i]) + [b[i]] for i in range(n)]
    for k in range(n):
        t = next(j for j in range(k,n) if v[j][k])
        v[t], v[k] = v[k], v[t]
        pivot = v[k][k]
        v[k] = [x/pivot for x in v[k]]
        for i in range(n):
            if i != k:
                fac = v[i][k]
                v[i] = [v[i][j] - fac*v[k][j] for j in range(n+1)]
    return [v[i][-1] for i in range(n)]

def lump_matrix(d, q):
    out = []
    for k in range(d+1):
        row = [F(0) for _ in range(d+1)]
        for a in range(k+1):
            for b in range(d-k+1):
                row[a+b] += F(comb(k,a)*comb(d-k,b))*(1-q)**(a+d-k-b)*q**(k-a+b)
        affirm(sum(row)==1, f'row stochastic d={d} k={k}')
        out.append(row)
    return out

def exact_cases():
    for d in range(1,8):
        for q in (F(1,5), F(1,4), F(2,7)):
            p = lump_matrix(d,q)
            h = linear_solve([[(F(i==j)-p[i+1][j+1]) for j in range(d)] for i in range(d)], [F(1)]*d)
            mean = sum(F(comb(d,k), 2**d)*h[k-1] for k in range(1,d+1))
            lam = 1-2*q
            spectral = sum((F(comb(d,j))/(1-lam**j) for j in range(1,d+1)), F(0))
            affirm(mean == spectral, f'exact mean d={d},q={q}')
            for z in (F(1,2), F(2,3)):
                f = linear_solve([[(F(i==j)-z*p[i+1][j+1]) for j in range(d)] for i in range(d)], [z*p[i+1][0] for i in range(d)])
                f_stationary = F(1,2**d)+sum(F(comb(d,k),2**d)*f[k-1] for k in range(1,d+1))
                u_z = sum((F(comb(d,j),2**d)/(1-z*lam**j) for j in range(d+1)),F(0))
                affirm(f_stationary == F(1,2**d)/((1-z)*u_z), f'exact renewal d={d},q={q},z={z}')

def normalized_mean(d,a):
    ell = log1p(-2*a/d)
    return sum(exp(lgamma(d+1)-lgamma(j+1)-lgamma(d-j+1)-d*log(2)) / (-expm1(j*ell)) for j in range(1,d+1))

def numeric_cases():
    for a in (0.4,0.8,log(3),1.4,2.5):
        r = exp(-a)
        lead = 1/(1-r)
        coeff = a*a*r*(3*r-1)/(2*(1-r)**3)
        last_scaled = None
        for d in (100,200,400,800,1600):
            m = normalized_mean(d,a)
            residual_scaled = d*d*(m-lead-coeff/d)
            affirm(abs(residual_scaled) < 20, f'O(d^-2) envelope a={a},d={d},err={residual_scaled}')
            if last_scaled is not None:
                affirm(abs(d*(m-lead)-coeff) < abs(last_scaled-coeff)+1e-6, f'first-order approach a={a},d={d}')
            last_scaled = d*(m-lead)
            if abs(a-log(3))>0.05 and d>=400:
                affirm((m-lead)*coeff>0, f'signed correction a={a},d={d}')

if __name__=='__main__':
    exact_cases()
    numeric_cases()
    print(f'PASS {checks} exact and numerical assertions')
