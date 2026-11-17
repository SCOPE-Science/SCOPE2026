"""Independent arithmetic and local-volume checks for the four-point spherical chord-energy law.
Run: python CHECK.py (requires numpy and sympy)."""
import math
import numpy as np
import sympy as sp

def energy(y):
    u,v,w,p,q=np.asarray(y).T
    a=np.sqrt(np.clip((1-u*u)*(1-v*v),0,None))
    b=np.sqrt(np.clip((1-u*u)*(1-w*w),0,None))
    c=np.sqrt(np.clip((1-v*v)*(1-w*w),0,None))
    inner=np.stack([u,v,w,u*v+a*np.cos(p),u*w+b*np.cos(q),v*w+c*np.cos(p-q)],axis=-1)
    return np.sum(np.sqrt(np.clip(2-2*inner,0,None)),axis=-1)

u,v,w,p,q=sp.symbols('u v w p q', real=True)
y=[u,v,w,p,q]
z=[u,v,w, u*v+sp.sqrt((1-u*u)*(1-v*v))*sp.cos(p), u*w+sp.sqrt((1-u*u)*(1-w*w))*sp.cos(q),v*w+sp.sqrt((1-v*v)*(1-w*w))*sp.cos(p-q)]
pt={u:-sp.Rational(1,3),v:-sp.Rational(1,3),w:-sp.Rational(1,3),p:2*sp.pi/3,q:4*sp.pi/3}
J=sp.Matrix([[sp.simplify(sp.diff(x,yy).subs(pt)) for yy in y] for x in z])
S2=sum((sp.Matrix([[sp.simplify(sp.diff(x,yy,zz).subs(pt)) for yy in y] for zz in y]) for x in z), sp.zeros(5))
a=sp.sqrt(sp.Rational(3,8))
H=sp.simplify(a**3*J.T*J+a*S2)
Hreference=sp.Matrix([
[27*sp.sqrt(6)/64,33*sp.sqrt(6)/128,33*sp.sqrt(6)/128,-sp.sqrt(2)/16,sp.sqrt(2)/16],
[33*sp.sqrt(6)/128,27*sp.sqrt(6)/64,33*sp.sqrt(6)/128,0,-sp.sqrt(2)/16],
[33*sp.sqrt(6)/128,33*sp.sqrt(6)/128,27*sp.sqrt(6)/64,sp.sqrt(2)/16,0],
[-sp.sqrt(2)/16,0,sp.sqrt(2)/16,sp.sqrt(6)/3,-sp.sqrt(6)/6],
[sp.sqrt(2)/16,-sp.sqrt(2)/16,0,-sp.sqrt(6)/6,sp.sqrt(6)/3]])
assert H==Hreference
assert sp.simplify(H.det()-1125*sp.sqrt(6)/16384)==0
assert all(float(H[:k,:k].det())>0 for k in range(1,6))
K=sp.simplify(2*sp.sqrt(2)/(15*sp.sqrt(H.det())))
assert sp.simplify(K-256*2**sp.Rational(1,4)*3**sp.Rational(3,4)*sp.sqrt(5)/3375)==0
assert abs(float(K)-0.45977952817530277)<1e-13
Hn=np.array(H.evalf(),dtype=float)
E,T=np.linalg.eigh(Hn)
assert np.min(E)>0
Tinv=T@np.diag(1/np.sqrt(E))@T.T
centers=[np.array([-1/3,-1/3,-1/3,2*np.pi/3,4*np.pi/3]),np.array([-1/3,-1/3,-1/3,4*np.pi/3,2*np.pi/3])]
D=np.diag([1,1,1,-1,-1]); Hi=[Tinv,D@Tinv@D]
for center in centers:
 assert abs(float(energy(center))-4*np.sqrt(6))<1e-12
rng=np.random.default_rng(812711)
N=150000
G=rng.normal(size=(N,5)); G=G/np.linalg.norm(G,axis=1)[:,None]
G*=rng.random(N)[:,None]**(1/5)
R=1.2
for eps in [0.002,0.0002]:
    rates=[]
    for center,linear in zip(centers,Hi):
        Y=center+np.sqrt(2*eps)*R*G@linear.T
        F=4*np.sqrt(6)-energy(Y)
        rates.append(float(np.mean(F<eps)))
    quotient=(rates[0]+rates[1])/2*R**5
    print('epsilon',eps,'local-volume ratio',round(quotient,6),'two rates',rates)
    assert 0.8<quotient<1.15
print('SPHERE_FOUR_CHORD_ENERGY_HESSIAN_AND_LOCAL_TAIL_OK',float(K))
