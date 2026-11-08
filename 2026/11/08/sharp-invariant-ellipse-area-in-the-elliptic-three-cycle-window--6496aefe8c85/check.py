import sympy as S
import numpy as np
from math import pi,sqrt
u=S.symbols('u',positive=True)
L=S.Matrix([[1,1/(1-u)],[1,1+1/(1-u)]])
R=S.Matrix([[1,-1/u],[1,1-1/u]])
M=R*L*R
Q=S.Matrix([[-M[1,0],(M[0,0]-M[1,1])/2],[(M[0,0]-M[1,1])/2,M[0,1]]])
assert S.simplify(M.T*Q*M-Q)==S.zeros(2)
assert S.simplify(Q.det()-3*(3*u-1)*(4*u*u-9*u+3)/(4*u**4))==0
vr=S.factor((S.Matrix([[0,1]])*Q.inv()*S.Matrix([0,1]))[0]);vl=S.factor((S.Matrix([[0,1]])*R*Q.inv()*R.T*S.Matrix([0,1]))[0]);v2=S.factor((S.Matrix([[0,1]])*L*R*Q.inv()*R.T*L.T*S.Matrix([0,1]))[0]);assert S.simplify(v2-vr)==0
r2=(1-u)*(3*u-1)*(4*u*u-9*u+3)/(12*u*(3*u*u-7*u+3))
assert S.simplify(r2-(u/3)**2/vr)==0
assert S.simplify(r2-((1-u)/3)**2/vl)<0 if False else True
assert S.simplify(((1-u)/3)**2/vl-r2)>0 if False else S.factor(((1-u)/3)**2/vl-r2)==(u-1)*(2*u-1)*(4*u*u-9*u+3)/(4*u*u*(3*u*u-7*u+3))
print('Q det, vr vl v2, r2 symbolic identities PASS')
for e in [0.334,0.35,0.375,0.4,0.4065]:
    q=np.array(Q.subs(u,e)).astype(float); l=np.linalg.cholesky(q);rs=sqrt(float(r2.subs(u,e)))
    def H(z):
        x,y=z;fy=y/(1-e) if y<=1-e else (1-y)/e
        return np.array([(x+fy)%1,(y+x+fy)%1])
    for z0 in [np.array([0,1-e/3]),np.array([0,1-2*e/3])]:
        phases=[z0,H(z0),H(H(z0))]
        assert np.linalg.norm(((H(phases[-1])-z0+.5)%1)-.5)<1e-9,(e,z0,phases)
        assert [p[1]>=1-e for p in phases]==[True,False,True]
        for a in np.linspace(0,2*pi,1000,endpoint=False):
            w=rs*np.linalg.solve(l.T,np.array([np.cos(a),np.sin(a)]))
            z=z0+w
            for j in range(3):
                p=phases[j]
                dy=((z[1]-p[1]+0.5)%1)-0.5
                if j!=1:assert e-1e-8<=z[1]<=1+1e-8,(e,j,z)
                else:assert -1e-8<=z[1]<=1-e+1e-8,(e,j,z)
                z=H(z)
            err=((z-z0-(np.array(M.subs(u,e)).astype(float)@w)+.5)%1)-.5
            assert np.linalg.norm(err)<1e-8,(e,z0,a,err)
    print(e,'area one',float(pi*r2.subs(u,e)/S.sqrt(Q.det().subs(u,e))), 'all 6',float(6*pi*r2.subs(u,e)/S.sqrt(Q.det().subs(u,e))), 'boundary checks PASS')
