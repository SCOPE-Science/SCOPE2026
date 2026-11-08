"""Reproduce finite-step identities for alternating BB1/BB2 two-spectral-mode iteration.
Uses only the Python standard library. The infinite convergence theorem is analytic.
"""
from fractions import Fraction as F
import math
from random import Random
checks=0

def test(a,b,x,y,n=7):
    global checks
    # State components are scalar in the two invariant eigenspaces.
    ah,bh=F(a),F(b)
    x,y=F(x),F(y)
    assert a>b>0 and x*y
    eps0=(x/y)**2
    eps_prev=eps0
    alpha=(x*x+y*y)/(ah*x*x+bh*y*y)
    x,y=x*(1-ah*alpha),y*(1-bh*alpha)
    eps=(x/y)**2
    assert eps==1/eps0; checks+=1
    for k in range(1,n):
        # k odd: long BB1; k even: short BB2, both from preceding state
        if k%2:
            alpha=(eps_prev+1)/(ah*eps_prev+bh)
            c=F(1)
        else:
            alpha=(ah*eps_prev+bh)/(ah*ah*eps_prev+bh*bh)
            c=(bh/ah)**2
        x,y=x*(1-ah*alpha),y*(1-bh*alpha)
        eps_next=(x/y)**2
        assert eps_next==c*eps/(eps_prev**2)
        checks+=1
        eps_prev,eps=eps,eps_next

for a,b in ((9,1),(5,2),(7,3)):
    for x,y in ((1,1),(2,1),(1,3),(3,4)):
        test(a,b,x,y,7)

# Forced recurrence, no periodic exceptional initial state under first exact long step.
for a,b in ((9,1),(5,2),(17,3)):
    L=math.log(a/b)
    E,O=-L/4,-3*L/4
    assert abs(E-(O-2*E))<1e-12
    assert abs(O-(E-2*O-2*L))<1e-12
    assert abs(E+O)>1e-8
    checks+=3
    theta=math.acos(1/(2*math.sqrt(2)))
    gap=max(theta,2*math.pi-3*theta)
    assert gap<math.pi
    checks+=1
    for phi0 in (math.log(4),0.0,-0.8,0.1):
        phi=[phi0,-phi0]
        for k in range(1,150):
            c=0 if k%2 else -2*L
            phi.append(phi[k]-2*phi[k-1]+c)
        deviation=[v-(E if k%2==0 else O) for k,v in enumerate(phi)]
        for k in range(1,149):
            assert abs(deviation[k+1]-(deviation[k]-2*deviation[k-1])) < 1e-11*max(1,abs(deviation[k+1]))
            checks+=1
        # Each 4-block contains both growth signs of the deviation.
        for j in range(10,85,4):
            v=deviation[j:j+4]
            assert min(v)<0<max(v)
            checks+=1
        # Positive and negative magnitudes each at least c*lambda^j times amplitude.
        for j in range(12,75,5):
            amp=max(abs(deviation[0]),abs(deviation[1]))
            c0=0.1*amp*(math.sqrt(2)**j)
            v=deviation[j:j+4]
            assert max(v)>c0 and min(v)<-c0
            checks+=1
print(f'VERIFY_OK {checks} exact-rational and independent recurrence checks')
