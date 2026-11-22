"""Standalone exact and numerical checks for the square-book Kemeny allocation theorem.
Run with python verify.py (SymPy required)."""
from fractions import Fraction
from math import isclose
import sympy as sp

m,x,y,z,w,h=sp.symbols('m x y z w h',positive=True)
K=(m-1+1/(m+1))/x+(m-1)/(x+2*z)+((m+1)*x+2*y+2*z)/(2*m*x*z+2*x*y+4*y*z)

def verify(a,b,message):
    assert sp.cancel(a-b)==0, message

# Exact spectral formula, using the tridiagonal-equitable decomposition.
D=sp.Matrix([[m*x+2*y,-m*x],[-x,x+2*z]])
verify(sp.factor(sp.trace(D)/D.det()),
       ((m+1)*x+2*y+2*z)/(2*m*x*z+2*x*y+4*y*z),"2x2 resolvent")

# Holding coordinates u=1-mx-y; v=1-x-z. These are the derivatives
# of K with respect to u, v and y, after eliminating x and z.
U=sp.diff(K,z)/m-sp.diff(K,x)/m
V=-sp.diff(K,z)
Y=U+sp.diff(K,y)
corner={x:1/m,y:0,z:1-1/m}
U0=sp.factor(U.subs(corner));V0=sp.factor(V.subs(corner));Y0=sp.factor(Y.subs(corner))
U_poly=8*m**7-24*m**6+32*m**5-28*m**4+13*m**2-6*m+1
V_poly=4*m**4-8*m**3+12*m**2-7*m+1
Y_poly=m**4-3*m**3+2*m**2-2*m+1
verify(U0,U_poly/(2*(m-1)**2*(m+1)*(2*m-1)**2),'U corner')
verify(V0,m*V_poly/(2*(m-1)**2*(2*m-1)**2),'V corner')
verify(Y0,4*m**3*Y_poly/((m-1)**2*(m+1)*(2*m-1)**2),'Y corner')
for p in (U_poly,V_poly,Y_poly):
    expanded=sp.Poly(sp.expand(p.subs(m,h+3)),h)
    assert all(c>0 for c in expanded.all_coeffs()),('positive shifted coefficients',p)

# The two-page exception and positive gradient in the holding directions.
curve={m:sp.Integer(2),x:(1-w)/2,y:w,z:(1+w)/2}
Q=sp.factor(K.subs(curve));q=15*w**3+31*w**2+21*w-3
verify(sp.diff(Q,w),32*q/(3*(w-1)**2*(w+3)**2*(3*w+1)**2),'cubic derivative')
U2=sp.factor(U.subs(curve));V2=sp.factor(V.subs(curve))
U2num=9*w**6+42*w**5+39*w**4+972*w**3+1927*w**2+1002*w+105
V2num=3*w**4+20*w**3+114*w**2+84*w+35
verify(U2,U2num/(6*(w-1)**2*(w+3)**2*(3*w+1)**2),'U two-page')
verify(V2,V2num/((w+3)**2*(3*w+1)**2),'V two-page')
assert all(c>0 for c in sp.Poly(U2num,w).all_coeffs())
assert all(c>0 for c in sp.Poly(V2num,w).all_coeffs())
assert q.subs(w,0)<0 and q.subs(w,1)>0
assert all(c>0 for c in sp.Poly(sp.diff(q,w),w).all_coeffs())

# Exact minima and the standard maximum-degree weighting.
km=sp.factor(K.subs(corner))
km_ref=(4*m**5-4*m**4+6*m**3-m**2-2*m+1)/(2*(m-1)*(m+1)*(2*m-1))
verify(km,km_ref,'all-size optimum')
kmd=sp.factor(K.subs({x:1/(m+1),y:1/(m+1),z:1/(m+1)}))
verify(kmd,(8*m**3+27*m**2+16*m+9)/(6*(m+3)),'max-degree baseline')
assert sp.limit(kmd/km,m,sp.oo)==sp.Rational(4,3)

# Independent exact full grounded graph computations.
checks=0
for n in range(2,9):
    nverts=2*(n+1)
    for ww in (sp.Rational(1,5),sp.Rational(1,3),sp.Rational(2,5)):
        xx=(1-ww)/n
        zz=1-xx
        pairs=[]
        # Hub vertices: 0 and n+1; layer-i leaves: i+1 and n+i+2.
        for i in range(n):
            pairs.extend([(0,i+1,xx),(n+1,n+i+2,xx),(i+1,n+i+2,zz)])
        pairs.append((0,n+1,ww))
        L=sp.zeros(nverts)
        for a,b,c in pairs:
            L[a,a]+=c;L[b,b]+=c;L[a,b]-=c;L[b,a]-=c
        J=sp.ones(nverts)/nverts
        direct=sp.trace((L+J).inv())-1
        symbolic=K.subs({m:n,x:xx,y:ww,z:zz})
        assert direct==symbolic, ('full matrix',n,ww,sp.factor(direct-symbolic))
        checks+=1
# Boundary y=0 also has connected support for n>=2.
for n in range(2,9):
    xx=sp.Rational(1,n);zz=1-xx
    size=2*n+2; L=sp.zeros(size)
    for i in range(n):
        for a,b,c in [(0,i+1,xx),(n+1,n+i+2,xx),(i+1,n+i+2,zz)]:
            L[a,a]+=c;L[b,b]+=c;L[a,b]-=c;L[b,a]-=c
    assert sp.trace((L+sp.ones(size)/size).inv())-1 == K.subs({m:n,x:xx,y:0,z:zz})
    checks+=1
root=sp.nroots(q, maxsteps=150)
r=float([sp.re(v) for v in root if abs(float(sp.im(v)))<1e-12 and 0<float(sp.re(v))<1][0])
assert isclose(r,0.120263939217473,abs_tol=1e-13)
print('PASS; exact spectral, KKT, asymptotic, full-matrix checks',checks,'; exceptional root',r)
