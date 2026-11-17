"""Reproducibility checks for orthogonally separated cubic support families.
Uses exact SymPy identities for endpoint degeneracies and deterministic
finite numerical probes. Finite probes do not replace the analytic proof.
"""
import math
import itertools
import numpy as np
import sympy as sp

C = 4*sp.sqrt(6)/9
L = sp.simplify(1/C)
assert sp.simplify(L - 3*sp.sqrt(6)/8)==0
checks = 1

def curvature(u,v,coeffs,rho=1.0):
    u=np.asarray(u,dtype=float);v=np.asarray(v,dtype=float)
    assert abs(np.dot(u,u)-1)<1.e-10 and abs(np.dot(v,v)-1)<1.e-10
    assert abs(np.dot(u,v))<1.e-10
    a=float(rho)
    for j,beta in enumerate(coeffs):
        x,y,z = u[3*j:3*j+3];p,q,r=v[3*j:3*j+3]
        a += 2*float(beta)*(x*q*r+y*p*r+z*p*q-x*y*z)
    return a

# All exact endpoint curvature witnesses, both coefficient signs, up to 3 blocks.
for m in (2,3):
    n=3*m
    for beta_sign in (-1,1):
        coeffs=[sp.Integer(beta_sign)*L]*m
        seen=set()
        for j in range(m):
            for heavy in range(3):
                pair=[i for i in range(3) if i!=heavy]
                for signs in itertools.product((-1,1),repeat=3):
                    if math.prod(signs)!=beta_sign: continue
                    u=sp.zeros(n,1)
                    for i in range(3): u[3*j+i]=(2 if i==heavy else 1)*signs[i]/sp.sqrt(6)
                    v=sp.zeros(n,1)
                    v[3*j+pair[0]]=signs[pair[0]]/sp.sqrt(2)
                    v[3*j+pair[1]]=-signs[pair[1]]/sp.sqrt(2)
                    assert sp.simplify(u.dot(v))==0
                    assert sp.simplify(u.dot(u)-1)==0
                    assert sp.simplify(v.dot(v)-1)==0
                    val=sp.Integer(1)
                    for k,beta in enumerate(coeffs):
                        x,y,z=u[3*k:3*k+3];p,q,r=v[3*k:3*k+3]
                        val+=2*beta*(x*q*r+y*p*r+z*p*q-x*y*z)
                    assert sp.simplify(val)==0
                    seen.add(tuple(u))
                    checks+=4
        assert len(seen)==12*m
        checks+=1

# Check that the pointwise radius matrix has one, and only one,
# tangential null direction at the exact witnesses.
for m in (2,3):
    n=3*m
    for j in range(m):
        u=sp.zeros(n,1)
        u[3*j:3*j+3,0]=sp.Matrix([2,1,1])/sp.sqrt(6)
        beta=[L]*m
        B=sp.eye(n)
        for k in range(m):
            a,b,c=u[3*k:3*k+3]
            F=a*b*c
            D=sp.zeros(n)
            D[3*k,3*k+1]=D[3*k+1,3*k]=c
            D[3*k,3*k+2]=D[3*k+2,3*k]=b
            D[3*k+1,3*k+2]=D[3*k+2,3*k+1]=a
            B+=beta[k]*(D-2*F*sp.eye(n))
        v=sp.zeros(n,1)
        v[3*j+1]=1/sp.sqrt(2)
        v[3*j+2]=-1/sp.sqrt(2)
        assert (B*v).applyfunc(sp.simplify)==sp.zeros(n,1)
        P=sp.eye(n)-u*u.T
        assert (P*B*P).rank()==n-2
        checks+=2

# Deterministic random Stiefel pairs. Includes extra ambient coordinates.
rng=np.random.default_rng(20261108)
for m in (2,3,4):
  for extra in (0,2):
    n=3*m+extra
    for trial in range(2400):
        raw=rng.normal(size=(n,2))
        q,_=np.linalg.qr(raw)
        u,v=q[:,0],q[:,1]
        coeffs=rng.uniform(-float(L),float(L),size=m)
        k=curvature(u,v,coeffs)
        assert k> -1.e-10
        t=[sum(u[3*j:3*j+3]**2+v[3*j:3*j+3]**2) for j in range(m)]
        assert sum(t)<=2+1.e-10
        checks+=2

# Every coefficient beyond the box yields an explicit negative curvature.
for m in (2,3,5):
    n=3*m
    for j in range(m):
        u=np.zeros(n);v=np.zeros(n)
        u[3*j:3*j+3]=np.array([2,1,1])/math.sqrt(6)
        v[3*j:3*j+3]=np.array([0,1,-1])/math.sqrt(2)
        co=np.zeros(m); co[j]=float(L)*1.01
        assert curvature(u,v,co)<0
        checks+=1
# Independent trapezoidal area integration for every planar projected support.
for m in (2,3):
    n=3*m
    for trial in range(128):
        raw=rng.normal(size=(n,2)); Q,_=np.linalg.qr(raw)
        u,v=Q[:,0],Q[:,1]
        coeffs=rng.uniform(-float(L),float(L),size=m)
        z=u-1j*v
        amplitude=sum(coeffs[j]*np.prod(z[3*j:3*j+3]) for j in range(m))
        expected=np.pi*(1-abs(amplitude)**2/4)
        angles=2*np.pi*np.arange(256)/256
        co=np.cos(angles); si=np.sin(angles)
        hh=np.ones(256); dh=np.zeros(256)
        for j,beta in enumerate(coeffs):
            us=u[3*j:3*j+3]; vs=v[3*j:3*j+3]
            vals=np.array([us[i]*co+vs[i]*si for i in range(3)])
            ders=np.array([-us[i]*si+vs[i]*co for i in range(3)])
            hh+=beta*np.prod(vals,axis=0)
            dh+=beta*sum(ders[i]*vals[(i+1)%3]*vals[(i+2)%3] for i in range(3))
        integral=np.pi/256*np.sum(hh*hh-dh*dh)
        assert abs(expected-integral)<1.e-10
        assert expected>=np.pi*(1-2*max(abs(coeffs))**2/27)-1.e-10
        checks+=2

# Exact sharp brightness deficit at the endpoint, in a single active block.
u=np.array([1,-1,0,0,0,0],dtype=float)/np.sqrt(2)
v=np.array([1,1,-2,0,0,0],dtype=float)/np.sqrt(6)
alpha=np.prod((u-1j*v)[:3]); squared=abs(alpha)**2
assert abs(squared-8/27)<1.e-12
assert abs(1-float(L)**2*squared/4-15/16)<1.e-12
checks+=2
print('PASS: %s checks; critical amplitude 3 sqrt(6)/8; 12 endpoint normals per active block; minimum shadow 15 pi/16 at endpoint' % checks)
