"""Numerical consistency checks for the all-exponent Hardy second-jet formulas.
These finite calculations supplement, but do not replace, the analytic proof.
Standard-library Python 3 only.
"""
import math
import random
import cmath

rng = random.Random(31827)
checks = 0

def close(a,b,tol=1.e-10):
    global checks
    checks += 1
    assert abs(a-b) <= tol*max(1,abs(a),abs(b)), (a,b)

def optimum(q,tau):
    threshold=1/(q-2)
    if tau <= threshold:
        r=2*tau/(1+math.sqrt(1+4*(q-1)*tau*tau))
        a=1/math.sqrt(1+r*r)
        return (1+q*tau*r)*a**q,(a,0.,a*r)
    denominator=q*q-2*(q-1)/(tau*(q-2))
    a=(q-1)/math.sqrt(denominator)
    c=1/math.sqrt(denominator)
    b=math.sqrt(2*(q-1)*(1-1/(tau*(q-2)))/denominator)
    return tau*(q-1)*a**(q-2),(a,b,c)

def objective(q,tau,a,b,c):
    return a**q+tau*(q*a**(q-1)*c+q*(q-1)/2*a**(q-2)*b*b)

def frontier(q,x):
    xc=(q-1)/math.sqrt((q-1)**2+1)
    if x>=xc:
        return q*x**(q-1)*math.sqrt(max(0,1-x*x))
    return q*x**(q-2)*((q-1)/2*(1-x*x)+x*x/(2*(q-1)))

for q in [2.1,2.5,3.,4.,5.5,8.,15.]:
    tc=1/(q-2)
    xc=(q-1)/math.sqrt((q-1)**2+1)
    xmin=(q-1)/q
    assert xmin < xc < 1; checks+=1
    for tau in [0.001,0.05,0.3,0.9*tc,tc,1.1*tc,2*tc,8*tc]:
        value,(a,b,c)=optimum(q,tau)
        close(a*a+b*b+c*c,1.)
        close(value,objective(q,tau,a,b,c))
        assert c<a and b<a+c; checks+=1
        # all randomly sampled real coefficients lie below predicted global optimum
        for i in range(1500):
            X,Y,Z=(rng.random()**0.7 for j in range(3))
            s=math.sqrt(X*X+Y*Y+Z*Z)
            X,Y,Z=X/s,Y/s,Z/s
            assert objective(q,tau,X,Y,Z) <= value+2e-12,(q,tau,X,Y,Z,value)
            checks+=1
        # upper bound for complex triples follows componentwise triangle inequality
        for i in range(150):
            ph=[rng.uniform(-math.pi, math.pi) for _ in range(3)]
            X,Y,Z=(rng.random() for _ in range(3))
            scale=math.sqrt(X*X+Y*Y+Z*Z);X/=scale;Y/=scale;Z/=scale
            aa,bb,cc=(v*cmath.exp(1j*t) for v,t in zip((X,Y,Z),ph))
            complex_L=aa**q+tau*(q*(aa**(q-1))*cc+q*(q-1)/2*aa**(q-2)*bb*bb)
            assert abs(complex_L) <= value+1e-10
            checks+=1
    for frac in [j/100 for j in range(101)]:
        x=xmin+(1-xmin)*frac
        t=x**q
        f=frontier(q,x)
        assert f>=0;checks+=1
        if x>=xc:
            close(f,q*x**(q-1)*math.sqrt(max(0,1-x*x)))
        else:
            f1=q*x**(q-1)*math.sqrt(1-x*x)
            diff=q*x**(q-2)/(2*(q-1))*((q-1)*math.sqrt(1-x*x)-x)**2
            close(f-f1,diff)
    close(frontier(q,xc),q*xc**(q-1)*math.sqrt(1-xc*xc))
    val,(a,b,c)=optimum(q,tc)
    close(a,xc)
    close(b,0.)
print('PASS',checks,'finite checks')
