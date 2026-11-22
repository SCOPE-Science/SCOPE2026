#!/usr/bin/env python3
"""Reproduce finite algebraic identities for affine Fock composition spectral projections.
The infinite-dimensional conclusions in RESULT.md use separate analytic arguments.
No data files or external packages are required.
"""
from fractions import Fraction as Q
from math import comb, factorial, exp, sqrt, pi, log


def laguerre_at_negative(n, x):
    return sum((Q(comb(n, j), factorial(j)) * x ** j for j in range(n + 1)), Q(0))


def norm_shifted_polynomial_sq(n, u):
    return sum((Q(comb(n, k)**2 * factorial(k), factorial(n)) * u ** (2 * (n-k))
                for k in range(n + 1)), Q(0))


def dual_pairing(m, n, u):
    # <(z-u)^m, z^n exp(u z)> for real u (unnormalized).
    return sum((Q(comb(m, k) * factorial(k), factorial(k-n)) * (-u) ** (m-k) * u ** (k-n)
                for k in range(n, m+1)), Q(0))


def poly_mult(p, q):
    r = [Q(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return r


def shifted_power(n, u):
    return [Q(comb(n,k)) * (-u)**(n-k) for k in range(n+1)]


def poly_comp_affine(p, a, d):
    out = [Q(0)]*len(p)
    for m, v in enumerate(p):
        if not v: continue
        for k in range(m+1):
            out[k] += v * comb(m,k) * a**k * d**(m-k)
    return out


def rank_one_on_monomial(n, m, u):
    if n > m: return [Q(0)]*(m+1)
    val = Q(comb(m,n))*u**(m-n)
    p = [val*x for x in shifted_power(n, u)]
    return p + [Q(0)]*(m+1-len(p))


def approx_dual_norm(n, x, cutoff=120):
    # || z^n exp(u z) / sqrt(n!) ||^2.
    term = 1.0
    total = term
    for j in range(1, cutoff+1):
        term *= x*(n+j)/(j*j)
        total += term
    return total


checks=0
for u in [Q(0),Q(1,4),Q(2,3),Q(1)]:
    x=u*u
    for n in range(11):
        assert norm_shifted_polynomial_sq(n,u)==laguerre_at_negative(n,x)
        checks+=1
        assert abs(approx_dual_norm(n,float(x)) - exp(float(x))*float(laguerre_at_negative(n,x))) < 1.e-10*max(1,approx_dual_norm(n,float(x)))
        checks+=1
        for m in range(11):
            assert dual_pairing(m,n,u) == (Q(factorial(n)) if m==n else Q(0))
            checks+=1

for a in [Q(1,2),Q(2,3)]:
    for u in [Q(1,3), Q(2,5)]:
        d=(1-a)*u
        for m in range(10):
            p=[Q(0)]*m+[Q(1)]
            Cp=poly_comp_affine(p,a,d)
            for n in range(10):
                Pm=rank_one_on_monomial(n,m,u)
                CP=poly_comp_affine(Pm,a,d)
                PC=[Q(0)]*(m+1)
                for k,ck in enumerate(Cp):
                    r=rank_one_on_monomial(n,k,u)
                    for j,v in enumerate(r):PC[j]+=ck*v
                rhs=[a**n*c for c in Pm]
                assert CP==rhs and PC==rhs, (a,u,m,n,CP,PC,rhs)
                checks+=1

# Verify fixed-displacement leading coefficient, which converges slowly (~n^-1/2).
for x in (0.5,1.0,2.0):
    vals=[]
    for n in (100,300,900):
        # stable positive polynomial recurrence
        a0=1.0
        a1=1.0+x
        for k in range(1,n):
            a0,a1=a1,((2*k+1+x)*a1-k*a0)/(k+1)
        P=exp(x/2)*a1
        appr=exp(2*sqrt(n*x))/(2*sqrt(pi)*(n*x)**0.25)
        vals.append(abs(P/appr-1))
        checks+=1
    assert vals[2]<vals[1]<vals[0] and vals[2]<0.04,(x,vals)

# Boundary scaling n|u_n|^2 = tau^2: I_0(2*tau) limit from its series.
for tau in (0.,0.4,1.,2.):
    target=sum(tau**(2*j)/factorial(j)**2 for j in range(30))
    errs=[]
    for n in (100,500,2000):
        x=Q(str(tau*tau))/n
        L=0.0
        term=1.0
        for j in range(n+1):
            if j: term *= (n-j+1)*float(x)/(j*j)
            L+=term
            if j>70 and term<1.e-16:break
        errs.append(abs(exp(float(x)/2)*L-target))
        checks+=1
    assert errs[-1]<0.025 and errs[-1]<=errs[0]+1.e-12, (tau,errs)

print('VERIFICATION_OK',checks)
