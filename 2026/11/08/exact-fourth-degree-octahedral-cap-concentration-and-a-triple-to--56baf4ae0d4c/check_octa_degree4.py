"""Exact moment and eigenspace checks for octahedral spherical-cap concentration.

Requirements: Python 3.10+, SymPy. Execute: python check_octa_degree4.py
Numerical cross-check also uses NumPy, SciPy when installed.
"""
import math
import sympy as sp

x, y, z, c, u, t = sp.symbols('x y z c u t', real=True)
r2 = x*x+y*y+z*z
solid = [
    x**4+y**4+z**4-sp.Rational(3,5)*r2**2,
    x**4-y**4-sp.Rational(6,7)*r2*(x*x-y*y),
    x**4+y**4-2*z**4-sp.Rational(6,7)*r2*(x*x+y*y-2*z*z),
    x*y*(7*z*z-r2), y*z*(7*x*x-r2), z*x*(7*y*y-r2),
    x*y*(x*x-y*y), y*z*(y*y-z*z), z*x*(z*z-x*x),
]
assert len(solid)==9
for f in solid:
    assert sp.simplify(sp.diff(f,x,2)+sp.diff(f,y,2)+sp.diff(f,z,2))==0
# Restriction of solid homogeneous harmonics to the unit sphere.
fns = [sp.expand(f).subs(r2,1) for f in solid]
# Substitution of (x^2+y^2+z^2)^2 must be done in terms of the sphere relation.
fns[0] = x**4+y**4+z**4-sp.Rational(3,5)
fns[1] = x**4-y**4-sp.Rational(6,7)*(x*x-y*y)
fns[2] = x**4+y**4-2*z**4-sp.Rational(6,7)*(x*x+y*y-2*z*z)
fns[3] = x*y*(7*z*z-1)
fns[4] = y*z*(7*x*x-1)
fns[5] = z*x*(7*y*y-1)
fns[6] = x*y*(x*x-y*y)
fns[7] = y*z*(y*y-z*z)
fns[8] = z*x*(z*z-x*x)

def circular_mean_product(f,g,axis):
    if axis=='x': sub={x:t}; a,b=y,z
    elif axis=='y':sub={y:t}; a,b=x,z
    else:sub={z:t};a,b=x,y
    expr=sp.Poly(sp.expand(f*g).subs(sub),a,b)
    out=sp.S.Zero
    for (da,db), coeff in expr.terms():
        if (da&1) or (db&1):continue
        aa=da//2; bb=db//2
        moment=sp.Rational(math.factorial(2*aa)*math.factorial(2*bb),
                          4**(aa+bb)*math.factorial(aa)*math.factorial(bb)*math.factorial(aa+bb))
        out+=coeff*(1-t*t)**(aa+bb)*moment
    return sp.expand(out)

def full_inner(f,g):
    return sp.integrate(circular_mean_product(f,g,'z'),(t,-1,1))/2

def six_caps_inner(f,g):
    return sp.integrate(sum(circular_mean_product(f,g,a) for a in 'xyz'),(t,c,1))

# Four sector formulas in dimensions 1+2+3+3.
lam = [
 -3*(c-1)*(5775*c**8+5775*c**7-7125*c**6-7125*c**5+2829*c**4+2829*c**3-391*c**2-391*c+512)/512,
 -3*(c-1)*(8085*c**8+8085*c**7-12855*c**6-12855*c**5+5919*c**4+5919*c**3-701*c**2-701*c+1024)/1024,
 -3*(c-1)**2*(15*c**5+30*c**4-18*c**3-66*c**2-49*c-32)/32,
 3*(c-1)**2*(1155*c**7+2310*c**6+705*c**5-900*c**4-363*c**3+174*c**2+151*c+128)/128,
]
sector=[0,1,1,2,2,2,3,3,3]
N=0
for i in range(9):
    for j in range(i,9):
        a=sp.factor(full_inner(fns[i],fns[j]))
        b=sp.factor(six_caps_inner(fns[i],fns[j]))
        if i!=j:
            assert a==0 and b==0,(i,j,a,b)
        else:
            assert a>0,(i,a)
            assert sp.factor(b-a*lam[sector[i]])==0,(i,a,b)
        N+=1
assert sp.factor(lam[0]+2*lam[1]+3*lam[2]+3*lam[3]-27*(1-c))==0
assert sp.factor(lam[2]-lam[3] +45*c*(c-1)**2*(c+1)**2*(7*c*c-3)*(11*c*c+1)/128)==0
assert sp.factor(lam[0]-lam[3] +63*c*(c-1)*(c+1)*(495*c**6-645*c**4+237*c**2-23)/512)==0
Q=495*u**3-645*u**2+237*u-23
# On [1/2,1], Q''>0, Q(1/2)<0, Q(3/4)>0 and Q(1)>0:
# exactly one zero in this interval, between 7/10 and 3/4.
assert sp.simplify(sp.diff(Q,u,2)-30*(99*u-43))==0
assert Q.subs(u,sp.Rational(1,2))<0
assert Q.subs(u,sp.Rational(7,10))<0<Q.subs(u,sp.Rational(3,4))
# E-T2 is strictly negative for c^2 in [1/2,3/4], certified by
# its four strictly negative cubic Bernstein coefficients on this interval.
P=1155*u**3-1713*u**2+681*u-59
power=sp.Poly(sp.expand(P.subs(u,sp.Rational(1,2)+t/4)),t)
bern=[sp.factor(sum(power.nth(j)*sp.binomial(k,j)/sp.binomial(3,j) for j in range(k+1))) for k in range(4)]
assert bern==[-sp.Rational(19,8),-sp.Rational(259,16),-sp.Rational(947,32),-sp.Rational(1571,64)]
# After the transition, A-E is positive; A-T1 always positive.
pa=385*u**3-155*u**2-29*u-9
pb=1925*u**3-2455*u**2+1199*u-221
assert pa.subs(u,sp.Rational(7,10))>0 and sp.diff(pa,u).subs(u,sp.Rational(7,10))>0
assert pb.subs(u,sp.Rational(1,2))>0 and sp.discriminant(sp.diff(pb,u),u)<0
root=sorted(float(sp.re(v)) for v in sp.nroots(Q) if abs(float(sp.im(v)))<1e-10 and float(sp.re(v))>0.5)[0]
assert .7 < root < .75
print('OCTA_DEGREE4_EXACT_PASS harmonic_basis=9 pairings=%d trace=9 transition_c=%.12f'%(N,math.sqrt(root)))

try:
    import numpy as np
    from numpy.polynomial.legendre import leggauss
    # Independent direct two-dimensional quadrature of cap masses,
    # not invoking the closed-form angular moment formula.
    nodes, weights=leggauss(80)
    phi=np.arange(256)*2*np.pi/256
    for cc in [1/np.sqrt(2), .75, .8616506523714784, .93]:
        v=(nodes+1)*(1-cc)/2+cc
        w=weights*(1-cc)/2
        integral=np.zeros((9,9))
        for axis in range(3):
            tt=v[:,None]; rr=np.sqrt(1-tt*tt)
            aa=rr*np.cos(phi)[None,:]; bb=rr*np.sin(phi)[None,:]
            coords= [ (tt,aa,bb),(aa,tt,bb),(aa,bb,tt) ][axis]
            xx,yy,zz=coords
            vals=np.stack([xx**4+yy**4+zz**4-3/5,
              xx**4-yy**4-6/7*(xx**2-yy**2),
              xx**4+yy**4-2*zz**4-6/7*(xx**2+yy**2-2*zz**2),
              xx*yy*(7*zz**2-1), yy*zz*(7*xx**2-1), zz*xx*(7*yy**2-1),
              xx*yy*(xx**2-yy**2),yy*zz*(yy**2-zz**2),zz*xx*(zz**2-xx**2)])
            vv=vals.reshape(9,-1)
            wt=np.repeat(w/len(phi),len(phi))
            integral+=np.einsum('ik,jk,k->ij',vv,vv,wt)
        # Compute norms from exact derivations, compare diagonal and cross entries.
        norms=np.array([float(full_inner(f,f)) for f in fns])
        A=integral/np.sqrt(norms[:,None]*norms[None,:])
        assert np.max(np.abs(A-np.diag([float(lam[j].subs(c,cc)) for j in sector])))<5e-11
    print('OCTA_DEGREE4_QUADRATURE_PASS radii=4 angular_nodes=256 polar_nodes=80')
except ImportError:
    print('OCTA_DEGREE4_QUADRATURE_SKIPPED dependencies numpy')
