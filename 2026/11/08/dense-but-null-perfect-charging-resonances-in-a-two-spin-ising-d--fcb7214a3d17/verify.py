#!/usr/bin/env python3
"""Standalone deterministic checks for exact Ising--DM dimer charging.

Requires Python >= 3.9, standard library only. Run: python verify.py
These checks supplement, but cannot replace, the infinite-family proof.
"""
import cmath
import math
from fractions import Fraction
from itertools import product

CHECKS = 0

def check(condition, label):
    global CHECKS
    assert condition, label
    CHECKS += 1


def triple_data(n):
    n0, n1, n2 = map(int, n)
    check(n0 < 0 < n1 < n2 and all(k % 2 for k in n), 'admissible odd triple')
    s1 = n0+n1+n2
    s2 = n0*n1+n0*n2+n1*n2
    s3 = n0*n1*n2
    q = Fraction(s1**3-4*s1*s2+8*s3, 16*s1)
    check(s1 > 0 and q > 0 and s3 < 0, 'positive physical family')
    return s1,s2,s3,q


def parameters(n, omega=1.):
    s1,s2,s3,q = triple_data(n)
    a=omega/math.sqrt(float(q))
    return a, a*s1/8, a*math.sqrt(-s3/(2*s1)), math.pi/a


def matmul(A,B):
    d=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(d)) for j in range(d)] for i in range(d)]


def exp_scaled(A, t):
    """Matrix exponential by Taylor series with scaling and squaring."""
    d=len(A)
    z=abs(t)*max(sum(abs(x) for x in row) for row in A)
    s=max(0, math.ceil(math.log2(z/0.4))) if z > 0.4 else 0
    B=[[-1j*t*x/(2**s) for x in row] for row in A]
    identity=[[complex(i==j) for j in range(d)] for i in range(d)]
    power=[row[:] for row in identity]
    ans=[row[:] for row in identity]
    for k in range(1,72):
        power=matmul(power,B)
        for i in range(d):
            for j in range(d):
                power[i][j]/=k
                ans[i][j]+=power[i][j]
        if max(abs(e) for row in power for e in row)<1e-17:
            break
    for _ in range(s):
        ans=matmul(ans,ans)
    return ans


def hamiltonian(J,D,omega=1.):
    return [[0,omega,omega,2*J],
            [omega,0,2*(J+1j*D),omega],
            [omega,2*(J-1j*D),0,omega],
            [2*J,omega,omega,0]]


def jacobi_eig_3(a):
    a=[row[:] for row in a]
    for _ in range(70):
        p,q=max(((0,1),(0,2),(1,2)), key=lambda ix: abs(a[ix[0]][ix[1]]))
        if abs(a[p][q]) < 1e-14:
            break
        tau=(a[q][q]-a[p][p])/(2*a[p][q])
        t=math.copysign(1.,tau)/(abs(tau)+math.sqrt(1+tau*tau))
        c=1/math.sqrt(1+t*t)
        s=c*t
        app=a[p][p]; aqq=a[q][q]; apq=a[p][q]
        a[p][p]=app-t*apq
        a[q][q]=aqq+t*apq
        a[p][q]=a[q][p]=0.
        for k in range(3):
            if k not in (p,q):
                akp=a[k][p]; akq=a[k][q]
                a[k][p]=a[p][k]=c*akp-s*akq
                a[k][q]=a[q][k]=s*akp+c*akq
    return sorted(a[i][i] for i in range(3))


def nearest_odd(y):
    return 2*round((y-1)/2)+1


def main():
    # Rational, exact elementary symmetric coefficient identities.
    for m in range(1,30):
        n=(-1,2*m+1,2*m+3)
        s1,s2,s3,q=triple_data(n)
        check(q==Fraction(3*(4*m+5), 16*(4*m+3)), 'closed family Q')
        check(Fraction(-s3,2*s1)/q == Fraction(8*(2*m+1)*(2*m+3),3*(4*m+5)), 'family D^2')
    for n in [(-1,1,3),(-1,3,5),(-1,5,7),(-3,5,9),(-5,9,13),(-1,21,23)]:
        try:
            s1,s2,s3,q=triple_data(n)
        except AssertionError:
            continue
        a,J,D,t=parameters(n)
        check(abs(8*J-a*s1)<1e-11, 'trace invariant')
        check(abs(16*J*J-4*(D*D+1)-a*a*s2)<1e-10, 'quadratic invariant')
        check(abs(-16*J*D*D-a**3*s3)<1e-10, 'determinant invariant')
        U=exp_scaled(hamiltonian(J,D),t)
        check(abs(abs(U[3][0])-1)<3e-11, 'exact transfer fidelity')
        check(max(abs(U[k][0]) for k in range(3))<2e-11, 'no undesired amplitude')
        check(abs(sum(abs(U[k][0])**2 for k in range(4))-1)<3e-11, 'unitary column')
    # Test the independent Jacobi eigensolver and dense approximation step.
    for J,D in [(0.3,0.2),(1.,1.),(0.1,4.),(4.,0.15),(2.,3.)]:
        beta=jacobi_eig_3([[4*J,2.,0.],[2.,4*J,-2*D],[0.,-2*D,0.]])
        check(beta[0]<0<beta[1]<beta[2], 'sign ordering')
        check(abs(sum(beta)-8*J)<1e-10,'trace of Jacobi matrix')
        check(abs(beta[0]*beta[1]*beta[2]+16*J*D*D)<1e-9,'Jacobi determinant')
        approximations=[]
        for k in [200,1000,5000,20000]:
            n=tuple(nearest_odd(k*b) for b in beta)
            if n[0]>=0 or n[1]<=0 or not (n[1]<n[2]):
                continue
            _,_,_,q=triple_data(n)
            a,Ja,Da,_=parameters(n)
            approximations.append(max(abs(J-Ja),abs(D-Da)))
            check(max(abs(J-Ja),abs(D-Da))<100/k, 'density reconstruction O(1/k)')
        check(len(approximations)>=3, 'sufficient approximants')
        check(approximations[-1]<0.01, 'close resonant pair')
    # Exact witness for (-1,1,3).
    a,J,D,t=parameters((-1,1,3))
    check(abs(J-3/(2*math.sqrt(5)))<1e-14,'J explicit')
    check(abs(D-2*math.sqrt(2/5))<1e-14,'D explicit')
    check(abs(t-math.pi*math.sqrt(5)/4)<1e-14,'time explicit')
    print('PASS',CHECKS,'deterministic assertions; analytic proof covers the infinite families.')

if __name__=='__main__':
    main()
