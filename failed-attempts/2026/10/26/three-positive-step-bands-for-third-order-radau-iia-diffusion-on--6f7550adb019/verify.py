"""Exact-rational checks of a two-stage Radau IIA diffusion formula on star graphs.

This script checks finitely many instances. The all-integer classification
requires the separate analytic polynomial and root-counting argument.
"""
from fractions import Fraction as Q
from math import isqrt


def stability(z):
    return (6 - 2*z) / (6 + 4*z + z*z)


def scalar_entries(m, h):
    a = stability(h)
    b = stability((m + 1)*h)
    hub = (1 + m*b) / (m + 1)
    hub_leaf = (1 - b) / (m + 1)
    leaf = Q(1, m+1) + Q(m-1, m)*a + b / (m*(m+1))
    leaf_pair = Q(1, m+1) - a/m + b / (m*(m+1))
    return hub, hub_leaf, leaf, leaf_pair


def polys(m,h):
    d1 = h*h + 4*h + 6
    dm = (m+1)**2*h*h + 4*(m+1)*h + 6
    H = (m+1)*h*h + (4-2*m)*h + 6
    F = ((m+1)*h**4 + (-2*m*m+2*m+10)*h**3
         + (6*m*m+4*m+16)*h*h + (24*m+12)*h + 36)
    E = h*h*((m+1)*h*h + 6*(m+2)*h + 18)
    return d1,dm,H,F,E


def expected_entries(m,h):
    d1,dm,H,F,E = polys(m,h)
    return H/dm, h*((m+1)*h+6)/dm, F/(d1*dm), E/(d1*dm)


def laplacian(m):
    n=m+1
    L=[[Q(0) for _ in range(n)] for _ in range(n)]
    L[0][0]=Q(m)
    for j in range(1,n):
        L[j][j]=1
        L[0][j]=L[j][0]=-1
    return L


def matmul(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),Q(0))
             for j in range(n)] for i in range(n)]


def check_instance(m,h):
    n=m+1
    l=laplacian(m)
    l2=matmul(l,l)
    I=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    Qmat=[[6*I[i][j]+4*h*l[i][j]+h*h*l2[i][j]
           for j in range(n)] for i in range(n)]
    Nmat=[[6*I[i][j]-2*h*l[i][j] for j in range(n)]
           for i in range(n)]
    H,J,F,E=scalar_entries(m,h)
    expected=expected_entries(m,h)
    assert (H,J,F,E)==expected, ('closed-form disagreement',m,h)
    T=[[H if i==j==0 else J if i==0 or j==0 else
        F if i==j else E for j in range(n)] for i in range(n)]
    assert matmul(Qmat,T)==Nmat, ('matrix resolvent disagreement',m,h)
    assert all(sum(row,Q(0))==1 for row in T), ('row sums',m,h)
    assert all(T[i][j]==T[j][i] for i in range(n) for j in range(n))
    if h>0:
        assert J>0 and E>0, ('strict off diagonal',m,h)
    d1,dm,hpoly,fpoly,_ = polys(m,h)
    assert (H >= 0)==(hpoly >= 0)
    assert (F >= 0)==(fpoly >= 0)


def positive_roots(m):
    # Display only: the proof of exact root counts does not use root finding.
    def F(x):return ((m+1)*x**4+(-2*m*m+2*m+10)*x**3
                      +(6*m*m+4*m+16)*x*x+(24*m+12)*x+36)
    def bisect(a,b):
        fa=F(a)
        assert fa*F(b)<0
        for _ in range(100):
            c=(a+b)/2
            if F(c)*fa<=0:b=c
            else:a=c;fa=F(a)
        return (a+b)/2
    a=bisect(3.0,float(m))
    b=bisect(float(m),float(2*m))
    from math import sqrt
    x=(m-2-sqrt(m*m-10*m-2))/(m+1)
    y=(m-2+sqrt(m*m-10*m-2))/(m+1)
    assert 0<x<y<2<3<a<float(m)<b
    return x,y,a,b


def main():
    tested=0
    m_values=[2,3,4,5,9,10,11,12,15,20,30]
    hs=[Q(0),Q(1,100),Q(1,4),Q(1,2),Q(3,4),Q(1),Q(3,2),
        Q(2),Q(3),Q(4),Q(6),Q(8),Q(12),Q(16)]
    for m in m_values:
        for h in hs+[Q(m),Q(2*m)]:
            check_instance(m,h)
            tested+=1
        if m>=11:
            print('m=%d four ordered boundary steps: %s' %
                  (m, ' '.join('%.12f'%v for v in positive_roots(m))))
            assert polys(m,Q(3,4))[2]<0
            assert polys(m,Q(m))[3]<0
            assert polys(m,Q(2))[2]>0 and polys(m,Q(2))[3]>0
        else:
            assert polys(m,Q(3,4))[2]>0
    assert polys(11,Q(1,2))[2]==0 and polys(11,Q(1))[2]==0
    print('PASS: %d exact-rational full-matrix resolvent and entry-formula checks' % tested)
    print('PASS: symmetry, row sums, strict positive off-diagonals and sign-polynomial identities')
    print('PASS: exact boundary values and negative-witness polynomial evaluations')
    print('NOTE: finite checks do not certify universal root counts; the polynomial proof does.')

if __name__=='__main__':main()
