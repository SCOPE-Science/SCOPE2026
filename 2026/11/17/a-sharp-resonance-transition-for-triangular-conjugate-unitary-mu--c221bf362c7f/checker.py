"""Supplementary finite checks for conjugate-unitary triangular multiplier formulas.

Uses Python standard library only. Finite sampling is not a proof of the
infinite-dimensional statements, which are established analytically.
"""
import cmath
import math
import random


def matmul(A, B):
    return (
        A[0]*B[0]+A[1]*B[2],
        A[0]*B[1]+A[1]*B[3],
        A[2]*B[0]+A[3]*B[2],
        A[2]*B[1]+A[3]*B[3],
    )


def matpow(A, n):
    C=(1+0j, 0j, 0j, 1+0j)
    for _ in range(n):
        C=matmul(C,A)
    return C


def singular_norm(A):
    a,b,c,d=A
    frob=abs(a)**2+abs(b)**2+abs(c)**2+abs(d)**2
    discr=max(0.0, frob*frob-4*abs(a*d-b*c)**2)
    return math.sqrt((frob+math.sqrt(discr))/2)


def phi(s):
    return (s+math.hypot(s,2))/2


def inversion(A):
    a,b,c,d=A
    det=a*d-b*c
    return (d/det,-b/det,-c/det,a/det)


def almost(x,y,relative=2e-9):
    return abs(x-y) <= relative*max(1.0,abs(x),abs(y))


rng=random.Random(418921)
checks=0
for i in range(1500):
    theta=rng.uniform(-math.pi,math.pi)
    if abs(math.sin(theta))<0.02:
        theta+=0.083
    b=complex(rng.uniform(-1.5,1.5),rng.uniform(-1.5,1.5))
    z=cmath.exp(1j*theta)
    A=(1/z,b,0j,z)
    n=rng.randrange(1,18)
    P=matpow(A,n)
    w=b*math.sin(n*theta)/math.sin(theta)
    assert abs(P[0]-z**(-n))<2e-11
    assert abs(P[1]-w)<2e-11
    assert abs(P[3]-z**n)<2e-11
    assert almost(singular_norm(P),phi(abs(w)))
    checks+=4
    epsilon=10**rng.uniform(-2,0)
    R=inversion((1+epsilon-1/z,-b,0j,1+epsilon-z))
    dd=abs(1+epsilon-z)
    assert almost(singular_norm(R),phi(abs(b)/dd)/dd)
    checks+=1

# Leading power constants and sharp radial resolvent constants for a continuum of orders.
for alpha in (0.0,0.15,0.4,0.7,0.9,1.0,1.4):
    c=1.3
    if alpha<1:
        M=1.0 if alpha==0 else max(abs(math.sin(j/1200))*((j/1200)**(alpha-1)) for j in range(1,50000))
        n=2500
        # A local rescaled grid resolves the maximizing frequency.
        q=max((abs(math.sin(x/n))**(alpha-1))*abs(math.sin(x))/n**(1-alpha)
              for j in range(1,50000) for x in (j/1200,))
        if alpha==0:
            q=max(q,1.0)
        assert abs(q-M)<0.004
        checks+=1
    for eps in (0.004,0.0004):
        vals=[]
        for j in range(1,30001):
            x=j/1200
            theta=eps*x
            d=math.hypot(eps,2*math.sqrt(1+eps)*math.sin(theta/2))
            bb=c*abs(math.sin(theta))**alpha
            vals.append(eps*phi(bb/d)/d if alpha>=1 else eps**(2-alpha)*phi(bb/d)/d)
        vals.append(1.0 if alpha>1 else (c if alpha==0 else 0.0))
        got=max(vals)
        if alpha<1:
            C=1.0 if alpha==0 else .5*alpha**(alpha/2)*(2-alpha)**(1-alpha/2)
            target=c*C
            assert abs(got-target)<eps**(1-alpha)+0.012, (alpha,eps,got,target)
        elif alpha==1:
            assert abs(got-math.sqrt(1+c*c/4))<0.02
        else:
            assert abs(got-1)<0.008
        checks+=1

print('CONJUGATE_UNITARY_RESONANCE_OK',checks,'independent finite matrix checks')
