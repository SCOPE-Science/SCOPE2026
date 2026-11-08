"""Reproduce exact algebra and representative direct iteration checks for the stated radial map."""
from fractions import Fraction
import math
import numpy as np
from sympy import symbols, simplify, diff

s, w, c, rho, lam = symbols('s w c rho lam', positive=True)
R = (w-1)*rho+w*c/rho
rho_star_squared=w*c/(2-w)
assert simplify(R.subs(c, (2-w)*rho**2/w)-rho)==0
assert simplify(diff(R,rho).subs(c,(2-w)*rho**2/w)-(2*w-3))==0
assert simplify((s+1/s)/2-1-(s-1)**2/(2*s))==0

# Purely rational involution and the quadratic Babylonian update.
for ep in [Fraction(1,100),Fraction(2,3),Fraction(7,2),Fraction(99,4)]:
    C=Fraction(5,7)
    f=lambda x: -C/x
    assert f(f(ep))==ep
    target=Fraction(3,1)*C
    root=Fraction(1,1)
    for _ in range(8):
        nxt=(root+target/root)/2
        assert nxt-root== (target-root*root)/(2*root)
        root=nxt

# Direct vector method versus the derived radial recurrence on orthogonal columns.
checks=0
for lamb in [1.0, 4.0, 17.0]:
    A=np.vstack((math.sqrt(lamb)*np.eye(2),np.zeros((1,2))))
    xstar=np.array([1.25,-0.75])
    z=np.array([0.,0.,1.4])
    b=A@xstar+z
    cc=float(np.dot(z,z)/lamb)
    for omega in [1.,1.05,1.25,1.5,1.75,1.95]:
        for r0 in [1e-3, .21, 3.0, 50.0]:
            v=np.array([3.,4.])/5.
            x=xstar+r0*v
            rs=r0
            for k in range(60):
                residual=b-A@x
                gradient=A.T@residual
                xnew=x+omega*np.dot(residual,residual)/np.dot(gradient,gradient)*gradient
                rn=(omega-1)*rs+omega*cc/rs
                expected=xstar+(-1)**(k+1)*rn*v
                assert np.linalg.norm(xnew-expected)< 3e-5 * max(1,rn), (omega,r0,k,rn,xnew,expected)
                x=xnew;rs=rn;checks+=1
            if omega==1.0:
                assert abs(rs-r0)<1e-9*max(1,r0)
            else:
                target=math.sqrt(omega*cc/(2-omega))
                for k in range(800):
                    rs=(omega-1)*rs+omega*cc/rs
                assert abs(rs-target)<1e-8*max(1,target)
print('VERIFY_OK',checks,'direct vector steps, symbolic and exact rational identities')
