"""Reproduce algebraic certificates and numerical sanity tests for four-mode circular Fourier observation.
Run: python CHECK.py  (requires numpy, sympy). Scientific theorem is proved in RESULT.md.
"""
import math
import numpy as np
import sympy as s

c,t=s.symbols('c t', real=True)
b1=t
b2=c*(2*t*t-1)
b3=(4*c*c-1)*(4*t**3-3*t)/3
B=s.Matrix([[0,b1,b2,b3], [b1,0,b1,b2], [b2,b1,0,b1], [b3,b2,b1,0]])
J=s.eye(4)*c
P=s.Matrix([[1,0],[0,1],[0,1],[1,0]])
Q=s.Matrix([[1,0],[0,1],[0,-1],[-1,0]])
# Orthonormality is up to factor 2; the nonzero 2x2 blocks are P.T M P/2 etc.
assert s.simplify(P.T*P-2*s.eye(2)) == s.zeros(2)
assert s.simplify(Q.T*Q-2*s.eye(2)) == s.zeros(2)
assert P.T*Q==s.zeros(2)
assert s.simplify(P.T*B*Q)==s.zeros(2)
checks=4
exp_plus=[4*t*(c*c-1)*(4*c*t*t-3*c+t**3)/3,
          4*t*(c*c-1)*(-4*c*t*t+3*c+t**3)/3]
exp_minus=[4*t*(-4*c**3*t*t+3*c**3+c*c*t**3-2*c*t*t-t**3)/3,
           4*t*( 4*c**3*t*t-3*c**3+c*c*t**3+2*c*t*t-t**3)/3]
for sign, exps in [(1,exp_plus),(-1,exp_minus)]:
    C=J+sign*B
    for U, rhs in [(P,exps[0]),(Q,exps[1])]:
        blk=s.simplify(U.T*C*U/2)
        assert s.factor(blk.det()-rhs)==0
        checks+=1
assert s.factor(exp_plus[0]+exp_plus[1]-8*t**4*(c*c-1)/3)==0
assert s.factor(exp_minus[0]+exp_minus[1]-8*t**4*(c*c-1)/3)==0
checks+=2

def gram(halfwidth, halfsep):
    m=[2*halfwidth/math.pi]
    for k in range(1,4):
        m.append(2*math.sin(k*halfwidth)*math.cos(k*halfsep)/(k*math.pi))
    return np.array([[m[abs(i-j)] for j in range(4)] for i in range(4)])

# Independently integrate the complex character products on the original arc endpoints.
def gram_via_midpoints(halfwidth, halfsep, n=10000):
    ans=np.zeros((4,4),dtype=complex)
    for center in [-halfsep,halfsep]:
        ts=center-halfwidth+(np.arange(n)+0.5)*2*halfwidth/n
        v=np.exp(1j*np.outer(ts,np.arange(4)))
        ans+= (v.conj().T@v)*halfwidth/(math.pi*n)
    return ans

for a in [0.025,0.15,0.36,0.71,1.02,1.35,1.53]:
    cval=math.cos(a)
    star=(2*a-math.sin(2*a))/math.pi
    high=(2*a+math.sin(2*a))/math.pi
    for theta in np.linspace(a,math.pi/2,38):
        gg=gram(a,theta)
        eig=np.linalg.eigvalsh(gg)
        assert eig[0]>0 and eig[-1]<1+1e-12
        if abs(theta-math.pi/2)<1e-12:
            assert abs(eig[0]-star)<1e-12
            assert abs(eig[1]-star)<1e-12
            assert abs(eig[2]-high)<1e-12
            assert abs(eig[3]-high)<1e-12
            checks+=4
        else:
            assert eig[0]<star-1e-13
            assert eig[-1]>high+1e-13
            assert eig[-1]/eig[0]>high/star+1e-10
            checks+=3
        assert abs(gg[0,1] - 2*math.sin(a)*math.cos(theta)/math.pi)<1e-13
        checks+=1
    for theta in [a, (a+math.pi/2)/2,math.pi/2]:
        err=np.max(np.abs(gram(a,theta)-gram_via_midpoints(a,theta,n=1500)))
        assert err<2e-6, (a,theta,err)
        checks+=1
for a in [0.1,0.04,0.02,0.01]:
    star=(2*a-math.sin(2*a))/math.pi
    ratio=star/(4*a**3/(3*math.pi))
    assert abs(ratio-1) < a*a
    checks+=1
print('FOUR_MODE_TWO_ARC_CHECKS_PASS',checks)
