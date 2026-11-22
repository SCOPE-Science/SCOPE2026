#!/usr/bin/env python3
"""Exact moment-polynomial checks and finite diagnostic root-order tests.

Requires only the Python standard library. These finite tests complement,
but do not replace, the analytic proof of the all-parameter theorem.
"""
from fractions import Fraction as F
from math import factorial
from itertools import permutations


def choose(a, k):
    val = F(1)
    for j in range(1, k + 1):
        val *= F(a - (j - 1), j)
    return val


def jacobi(n, alpha, beta):
    """Coefficients in increasing order of P_n^(alpha,beta)(2t-1)."""
    out = [F(0)] * (n + 1)
    for k in range(n + 1):
        c = choose(n + alpha, k) * choose(n + beta, n - k)
        for h in range(n - k + 1):
            a = choose(n - k, h) * (-1) ** (n - k - h)
            out[k + h] += c * a
    return out


def moment(j, alpha):
    """Integral t^j against normalized (alpha+1)(1-t)^alpha dt."""
    r = F(1)
    for k in range(1, j + 1):
        r *= F(k, 1) / (alpha + 1 + k)
    return r


def poly_mul(a, b):
    r = [F(0)] * (len(a) + len(b) - 1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            r[i+j] += x*y
    return r


def determinant_pencil(n, alpha, beta):
    """det(H-lambda G), for G_ij=m_{beta+i+j}, H_ij=m_{beta+i+j+1}."""
    out=[F(0)]*(n+1)
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=[F((-1)**inversions)]
        for i,j in enumerate(perm):
            term=poly_mul(term,[moment(beta+i+j+1,alpha),-moment(beta+i+j,alpha)])
        for k,v in enumerate(term):out[k]+=v
    return out


def roots(poly, slices=3000):
    """Numerical diagnostic for simple roots in (0,1)."""
    def val(x):
        s=0.
        for coeff in reversed(poly):s=s*x+float(coeff)
        return s
    r=[]
    x0=0.; y0=val(x0)
    for i in range(1,slices+1):
        x1=i/slices; y1=val(x1)
        if y1==0.0:
            r.append(x1)
        elif y0*y1<0:
            lo,hi=x0,x1
            for _ in range(55):
                m=(lo+hi)/2
                if val(lo)*val(m)<=0:hi=m
                else:lo=m
            r.append((lo+hi)/2)
        x0,y0=x1,y1
    return r


def compare_scalar(a,b):
    a=[x/a[-1] for x in a]
    b=[x/b[-1] for x in b]
    assert a==b, (a,b)


def main():
    tests=0
    for alpha in [F(-1,2),F(0),F(1),F(5,3)]:
        for q in range(1,5):
            for beta in range(0,4):
                compare_scalar(determinant_pencil(q,alpha,beta),jacobi(q,alpha,beta))
                tests+=1
        for q in range(1,8):
            r0=roots(jacobi(q,alpha,0))
            r1=roots(jacobi(q,alpha,1))
            assert len(r0)==q and len(r1)==q
            assert 0<r0[0]<r1[0]<1
            if q>1: assert r1[0]<r0[1]
            for beta in range(1,4):
                r=roots(jacobi(q,alpha,beta))
                assert len(r)==q and r[0]>=r1[0]-1e-9
                tests+=1
            for k in range(1,q):
                rn=roots(jacobi(q-k,alpha,k))
                assert len(rn)==q-k and rn[0]>r1[0]
                tests+=1
            tests+=3
    # Explicit low-order check.
    l0=roots(jacobi(2,F(0),0))[0]
    l1=roots(jacobi(2,F(0),1))[0]
    assert abs(l0-(1-1/(3**0.5))/2)<1e-10
    assert abs(l1-(6-(6**0.5))/10)<1e-10
    print('PASS',tests,'finite checks; exact moment pencils and Jacobi identities, root-order diagnostics')

if __name__=='__main__': main()
