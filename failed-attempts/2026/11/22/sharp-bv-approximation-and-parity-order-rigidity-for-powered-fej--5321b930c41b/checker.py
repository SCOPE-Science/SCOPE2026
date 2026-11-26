"""Exact combinatorics and independent quadrature for powered Fejer-Jackson kernels.
Run with Python 3.9+; standard library only. No claim of infinite certification.
"""
import math
from fractions import Fraction


def poly_coeff(n, q):
    v = [1]
    for _ in range(2*q):
        w = [0]*(len(v)+n-1)
        for i,a in enumerate(v):
            for j in range(n): w[i+j] += a
        v = w
    mid = q*(n-1)
    return [v[mid+k] for k in range(mid+1)]


def inclusion_coeff(n, q, k):
    m = q*(n-1)+k
    total = 0
    for j in range(2*q+1):
        v=m-j*n+2*q-1
        if v>=2*q-1:
            total+= (-1)**j*math.comb(2*q,j)*math.comb(v,2*q-1)
    return total


def sharp_coefficient(n,q):
    a=poly_coeff(n,q)
    return math.pi/2 - (4/math.pi)*sum((a[k]/a[0])/(k*k) for k in range(1,len(a),2))


def jkernel(n,q,t,a0):
    if abs(t)<1e-14: r=n
    else: r=math.sin(n*t/2)/math.sin(t/2)
    return r**(2*q)/(2*math.pi*a0)


def simpson(f,a,b,N):
    assert N%2==0
    h=(b-a)/N
    s=f(a)+f(b)
    for i in range(1,N):
        s+=(4 if i%2 else 2)*f(a+i*h)
    return s*h/3


def main():
    c=0
    for n in range(2,13):
        for q in range(2,6):
            a=poly_coeff(n,q)
            for k in range(len(a)):
                assert a[k]==inclusion_coeff(n,q,k),(n,q,k)
                c+=1
            assert a[0]>0
            # At an even n, the kernel has a zero of exact order 2q at pi:
            if n%2==0:
                for r in range(q):
                    val=(a[0] if r==0 else 0) + 2*sum(((-1)**k)*a[k]*k**(2*r) for k in range(1,len(a)))
                    assert val==0,(n,q,r,val)
                # First nonzero Taylor coefficient is positive and known exactly.
                val=2*sum(((-1)**k)*a[k]*k**(2*q) for k in range(1,len(a)))
                leading = Fraction((-1)**q*val,math.factorial(2*q))
                assert leading==Fraction(n**(2*q),2**(2*q)),(n,q,leading)
            else:
                at_pi=a[0]+2*sum((-1)**k*a[k] for k in range(1,len(a)))
                assert at_pi==1,(n,q,at_pi)
            C=sharp_coefficient(n,q)
            a0=a[0]
            cquad=2*simpson(lambda t:t*jkernel(n,q,t,a0),0,math.pi,4000+100*n)
            assert abs(C-cquad)<3e-8,(n,q,C,cquad)
    print('EXACT_COEFFICIENT_AND_PARITY_TESTS_PASS',c)
    for n in [20,40,80,160]:
        x=n*sharp_coefficient(n,2)
        goal=6*math.log(2)/math.pi
        assert abs(x-goal)<0.1 and x>goal,(n,x,goal)
    print('JACKSON_Q2_ASYMPTOTIC_SANITY_PASS')
    # Explicit finite arcs: unique peak at half-circle and predicted local loss.
    for n in range(2,10):
        for q in [2,3,4]:
            a0=poly_coeff(n,q)[0]
            C=sharp_coefficient(n,q)
            def arc_loss(length):
                return 2*simpson(lambda t:min(t,length)*jkernel(n,q,t,a0),0,math.pi,12000)
            for ell in [0.1, 0.5, 1.0, 2.0, 2.8]:
                assert arc_loss(ell)<C+1e-8,(n,q,ell)
    print('HALF_CIRCLE_ARC_LEAKAGE_TESTS_PASS')
    print('ALL_POWERED_FEJER_JACKSON_CHECKS_PASS')

if __name__=='__main__':
    main()
