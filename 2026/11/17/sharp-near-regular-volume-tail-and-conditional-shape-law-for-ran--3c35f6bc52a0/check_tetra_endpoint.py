"""Reproducibility checks for the unit-sphere tetrahedral endpoint law.

The mathematical proof is analytic. Numerical samples do not prove an asymptotic.
Run: python check_tetra_endpoint.py
"""
import math
import numpy as np
import sympy as s

x,y,z,phi,psi=s.symbols('x y z phi psi',real=True)
a=s.sqrt(1-x*x); b=s.sqrt(1-y*y); c=s.sqrt(1-z*z)
D=(x-1)*b*c*s.sin(psi-phi)-(y-1)*c*a*s.sin(psi)+(z-1)*a*b*s.sin(phi)
star=16*s.sqrt(3)/9
variables=(x,y,z,phi,psi)
qstar={x:-s.Rational(1,3),y:-s.Rational(1,3),z:-s.Rational(1,3),phi:2*s.pi/3,psi:4*s.pi/3}
assert s.simplify(D.subs(qstar)+star)==0
assert all(s.simplify(s.diff(D,v).subs(qstar))==0 for v in variables)
H=s.hessian(1+D/star,variables).subs(qstar).applyfunc(s.simplify)
H_target=s.Matrix([
[s.Rational(27,32),s.Rational(9,64),s.Rational(9,64),s.sqrt(3)/8,-s.sqrt(3)/8],
[s.Rational(9,64),s.Rational(27,32),s.Rational(9,64),0,s.sqrt(3)/8],
[s.Rational(9,64),s.Rational(9,64),s.Rational(27,32),-s.sqrt(3)/8,0],
[s.sqrt(3)/8,0,-s.sqrt(3)/8,s.Rational(2,3),-s.Rational(1,3)],
[-s.sqrt(3)/8,s.sqrt(3)/8,0,-s.Rational(1,3),s.Rational(2,3)]
])
assert H==H_target
pivots=[s.factor(H[:k,:k].det()) for k in range(1,6)]
assert pivots==[s.Rational(27,32),s.Rational(2835,4096),s.Rational(18225,32768),s.Rational(1215,4096),s.Rational(243,2048)]
assert s.factor(H.det())==s.Rational(243,2048)
vol5=8*s.pi**2/15
coef=s.simplify(2/(32*s.pi**2)*vol5*2**s.Rational(5,2)/s.sqrt(H.det()))
assert s.simplify(coef-128*s.sqrt(3)/405)==0

rng=np.random.default_rng(157321)
# Independent Cartesian determinant: orientation and normalization, not only the trigonometric identity.
for _ in range(150):
    xx,yy,zz=rng.uniform(-0.9,0.9,3)
    p,q=rng.uniform(0,2*math.pi,2)
    u1=np.array([0.,0.,1.])
    u2=np.array([math.sqrt(1-xx*xx),0,xx])
    u3=np.array([math.sqrt(1-yy*yy)*math.cos(p),math.sqrt(1-yy*yy)*math.sin(p),yy])
    u4=np.array([math.sqrt(1-zz*zz)*math.cos(q),math.sqrt(1-zz*zz)*math.sin(q),zz])
    direct=np.linalg.det(np.column_stack((u2-u1,u3-u1,u4-u1)))
    formula=(xx-1)*math.sqrt((1-yy*yy)*(1-zz*zz))*math.sin(q-p)-(yy-1)*math.sqrt((1-xx*xx)*(1-zz*zz))*math.sin(q)+(zz-1)*math.sqrt((1-xx*xx)*(1-yy*yy))*math.sin(p)
    assert abs(direct-formula)<1e-12

Hf=np.array(H,dtype=float)
base=np.array([-1/3,-1/3,-1/3,2*math.pi/3,4*math.pi/3],dtype=float)
def deficit(q):
    xx,yy,zz,p,qq=q
    aa,bb,cc=math.sqrt(1-xx*xx),math.sqrt(1-yy*yy),math.sqrt(1-zz*zz)
    d=(xx-1)*bb*cc*math.sin(qq-p)-(yy-1)*cc*aa*math.sin(qq)+(zz-1)*aa*bb*math.sin(p)
    return 1-abs(d)/(16*math.sqrt(3)/9)
for _ in range(50):
    direction=rng.normal(size=5)
    direction/=np.linalg.norm(direction)
    h=0.002*direction
    approx=h@Hf@h/2
    assert abs(deficit(base+h)-approx)<1e-7

N=9_000_000
thresholds=np.array([0.016,0.025,0.040,0.060])
counts=np.zeros(len(thresholds),dtype=np.int64)
volsum=0.0
volsqsum=0.0
for start in range(0,N,250_000):
    size=min(N-start,250_000)
    xyz=rng.uniform(-1,1,size=(size,3))
    pp=rng.uniform(0,2*math.pi,size=size)
    qq=rng.uniform(0,2*math.pi,size=size)
    xx,yy,zz=xyz.T
    aa=np.sqrt(1-xx*xx); bb=np.sqrt(1-yy*yy); cc=np.sqrt(1-zz*zz)
    d=(xx-1)*bb*cc*np.sin(qq-pp)-(yy-1)*cc*aa*np.sin(qq)+(zz-1)*aa*bb*np.sin(pp)
    volume=np.abs(d)/6
    volsum+=np.sum(volume)
    volsqsum+=np.dot(volume,volume)
    small=1-np.abs(d)/(16*math.sqrt(3)/9)
    counts+=np.count_nonzero(small[:,None]<thresholds[None,:],axis=0)

assert abs(volsum/N-4*math.pi/105)<0.001
assert abs(volsqsum/N-2/81)<0.0003
print(f"mean_volume={volsum/N:.9f} expected={4*math.pi/105:.9f}; mean_squared_volume={volsqsum/N:.9f} expected={2/81:.9f}")
for delta,k in zip(thresholds,counts):
    pred=float(coef)*delta**2.5
    observed=k/N
    sd=math.sqrt(pred*(1-pred)/N)
    # Allow finite-delta bias; asymptotic convergence is not an exact finite-delta identity.
    assert abs(observed-pred)<6*sd+0.12*pred
    print(f"relative_deficit={delta:g}: hits={k}, observed={observed:.9g}, leading={pred:.9g}, ratio={observed/pred:.5f}")
print('SPHERE_TETRA_UPPER_VOLUME_ELLIPSOID_CHECKS_OK')
