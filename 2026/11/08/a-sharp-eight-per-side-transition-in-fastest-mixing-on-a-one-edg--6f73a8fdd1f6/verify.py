"""Independent matrix-spectrum and algebraic checks for the defective-biclique FMMC theorem.

Run: python verify.py  (Python standard library only).
All finite checks supplement the analytic infinite-family proof.
"""
from math import sqrt
from fractions import Fraction
from random import Random


def optimum(n):
    if 3 <= n <= 7:
        return 1/n, 1/(2*(n-1)), 1/sqrt(n)
    if n >= 8:
        s = sqrt(n*n - 8*n + 8)
        den = 2*(n-1) + s
        return 2/den, (n-2+s)/((n-1)*den), (n-2)/den
    raise ValueError('n must be >=3')


def reduced_spectrum(n, x, y):
    a = 1-(n-1)*x
    b = 1-x-2*(n-1)*y
    rad = sqrt((a-b)**2 + 4*(n-1)*x*x)
    return sorted([1., 1-n*x] + [1-x-(n-1)*y]*(2*(n-2)) +
                  [(a+b-rad)/2, (a+b+rad)/2])


def transition(n,x,y):
    N=2*n
    p=[[0.0]*N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i==0 and j==0:continue
            v=y if i>0 and j>0 else x
            p[i][n+j]=p[n+j][i]=v
    for i in range(N): p[i][i]=1-sum(p[i])
    return p


def jacobi_spectrum(p):
    a=[v[:] for v in p]
    n=len(a)
    for _ in range(70*n*n):
        best=0.0; r=-1;s=-1
        for i in range(n):
            for j in range(i+1,n):
                t=abs(a[i][j])
                if t>best: best=t; r=i; s=j
        if best<2e-13: break
        phi=0.5*__import__('math').atan2(2*a[r][s],a[s][s]-a[r][r])
        c=__import__('math').cos(phi); z=__import__('math').sin(phi)
        # similarity by rotation R=[[c,s],[-s,c]] in the (r,s) subspace
        arr=a[r][r]; ass=a[s][s]; ars=a[r][s]
        a[r][r]=c*c*arr-2*c*z*ars+z*z*ass
        a[s][s]=z*z*arr+2*c*z*ars+c*c*ass
        a[r][s]=a[s][r]=0.0
        for k in range(n):
            if k==r or k==s:continue
            kr,ks=a[k][r],a[k][s]
            a[k][r]=a[r][k]=c*kr-z*ks
            a[k][s]=a[s][k]=z*kr+c*ks
    else:
        raise AssertionError('Jacobi solver did not converge')
    return sorted(a[i][i] for i in range(n))


def exact_low_n(n):
    x=Fraction(1,n);y=Fraction(1,2*(n-1))
    assert n*x == 1
    assert 2*(n-1)*y == 1
    T = Fraction(1,1)-x-(n-1)*y
    assert T == Fraction(n-2,2*n)
    assert (n-2)**2 <= 4*n  # T <= 1/sqrt(n) after squaring
    # odd-block trace, determinant, and its eigenvalues +/-1/sqrt(n)
    A=1-(n-1)*x; B=1-x-2*(n-1)*y
    assert A+B==0
    assert A*A+(n-1)*x*x==Fraction(1,n)


def exact_high_n(n):
    D=n*n-8*n+8
    assert D>0
    # x solves (3n^2-4)x^2 -8(n-1)x +4=0, with smaller root.
    # For the rationalized form x=2/(2(n-1)+sqrt(D)), check
    # ((3n^2-4)4-16(n-1)(2(n-1)+s)+4(2(n-1)+s)^2)=0.
    # Constant and sqrt(D) coefficients are each exactly zero.
    coeff_s = -16*(n-1)+16*(n-1)
    const =4*(3*n*n-4)-32*(n-1)**2+16*(n-1)**2+4*D
    assert coeff_s==0 and const==0
    # x < 1/n and x > 2/(3n-2): used for subgradient optimality.
    assert 4 < D < n*n and D < (n-2)**2
    # At t=0, odd-block eigenvalues are +/-rho and other quotient eigenvalue equals rho.
    # At x=2/z, rho=(n-2)/z; equality reduces to the above quadratic.
    # Matrix row feasibility is exact by substitution in z=2(n-1)+sqrt(D).


def test():
    rng=Random(20261106)
    numeric_checks=0
    for n in range(3,17):
        for i in range(14):
            if i==0: x,y,_=optimum(n)
            else:
                x=rng.random()/(n-1)
                y=rng.random()*(1-x)/(n-1)
            p=transition(n,x,y)
            assert all(abs(sum(row)-1)<1e-12 for row in p)
            assert all(v>=-1e-12 for row in p for v in row)
            full=jacobi_spectrum(p)
            predicted=reduced_spectrum(n,x,y)
            assert len(predicted)==2*n
            assert max(abs(a-b) for a,b in zip(full,predicted))<3e-10, (n,i,full,predicted)
            numeric_checks+=1
    for n in range(3,400):
        x,y,rho=optimum(n)
        assert x>0 and y>0 and (n-1)*x<=1+1e-12 and x+(n-1)*y<=1+1e-12
        predicted=reduced_spectrum(n,x,y)
        got=max(abs(v) for v in predicted[:-1])
        assert abs(got-rho)<4e-12,(n,got,rho)
        if n<=7: exact_low_n(n)
        else: exact_high_n(n)
    # Coarse global search (symmetric invariant class only) is corroboration, not proof.
    comparisons=0
    for n in list(range(3,21))+[30,60,100]:
        xopt,yopt,rho=optimum(n)
        for _ in range(1000):
            x=rng.random()/(n-1)
            y=rng.random()*(1-x)/(n-1)
            vals=reduced_spectrum(n,x,y)
            obj=max(abs(v) for v in vals[:-1])
            assert obj+1e-11>=rho,(n,x,y,obj,rho)
            comparisons+=1
    print('PASS: exact symbolic identities and inequality boundaries for n=3,...,399')
    print(f'PASS: {numeric_checks} independent full symmetric Jacobi spectrum comparisons')
    print(f'PASS: {comparisons} numerical feasible invariant-design comparisons')
    print('PASS: constructed optimal kernels feasible and attain claimed SLEM for n=3,...,399')
    print('FINITE TESTS ARE NOT AN INFINITE-FAMILY PROOF.')

if __name__=='__main__': test()
