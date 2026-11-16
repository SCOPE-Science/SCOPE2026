"""Exact Gram-block and nonisotropy checks for three unequal antipodal cap pairs.
Run: python verify_unequal.py . Dependencies: SymPy and NumPy.
"""
import math
import numpy as np
import sympy as sp
x,y,z=sp.symbols('x y z',real=True)
c1,c2,c3=sp.symbols('c1 c2 c3',real=True)
cvals=[c1,c2,c3]
c=sp.symbols('c',real=True)
t=sp.symbols('t',real=True)
R=x*x+y*y+z*z
raw=[x*y*z,x*(5*x*x-3*R),y*(5*y*y-3*R),z*(5*z*z-3*R),
     x*(y*y-z*z),y*(z*z-x*x),z*(x*x-y*y)]
for f in raw:
    assert sp.expand(sum(sp.diff(f,v,2) for v in (x,y,z)))==0
poly=[x*y*z,x*(5*x*x-3),y*(5*y*y-3),z*(5*z*z-3),
      x*(y*y-z*z),y*(z*z-x*x),z*(x*x-y*y)]
ns=[sp.Rational(1,105)]+[sp.Rational(4,7)]*3+[sp.Rational(4,105)]*3

def circ_moment(a,b):
    return sp.Rational(math.factorial(2*a)*math.factorial(2*b),4**(a+b)*math.factorial(a)*math.factorial(b)*math.factorial(a+b))

def cap(P,axis,lower):
    # Integral with respect to normalized sphere measure of |coordinate_axis|>=lower.
    out=sp.Integer(0)
    indices=[i for i in range(3) if i!=axis]
    for powers,coeff in sp.Poly(sp.expand(P),x,y,z).terms():
        a,b,d=powers[axis],powers[indices[0]],powers[indices[1]]
        if a%2 or b%2 or d%2: continue
        out+=coeff*circ_moment(b//2,d//2)*sp.integrate(t**a*(1-t*t)**((b+d)//2),(t,lower,1))
    return sp.factor(out)

A=lambda c: sp.factor(cap(poly[0]**2,0,c))
Bax=lambda c: sp.factor(cap(poly[1]**2,0,c))
Btr=lambda c: sp.factor(cap(poly[1]**2,1,c))
Cax=lambda c: sp.factor(cap(poly[4]**2,0,c))
Ctr=lambda c: sp.factor(cap(poly[4]**2,1,c))
H=lambda c: sp.factor(cap(poly[1]*poly[4],1,c))
assert sp.factor(H(c) + c*(c*c-1)**2*(5*c*c+1)/16)==0
assert sp.factor(sp.diff(H(c),c) - (1-c*c)*(35*c**4-10*c*c-1)/16)==0
# 35c^4-10c^2-1 >= 35/4 - 5 -1=11/4>0 for c^2>=1/2.
assert (35*sp.Rational(1,4)-10*sp.Rational(1,2)-1)==sp.Rational(11,4)

# Matrix in the unnormalised polynomial basis; later conjugate by norm factors.
M=sp.zeros(7)
M[0,0]=sum(A(v) for v in cvals)
for i in range(3):
    j,k=(i+1)%3,(i+2)%3
    M[1+i,1+i]=Bax(cvals[i])+Btr(cvals[j])+Btr(cvals[k])
    M[4+i,4+i]=Cax(cvals[i])+Ctr(cvals[j])+Ctr(cvals[k])
    M[1+i,4+i]=M[4+i,1+i]=H(cvals[j])-H(cvals[k])

# Full 28 entry direct integration, independent of the formula assembly.
for i in range(7):
    for j in range(i,7):
        sphere=cap(poly[i]*poly[j],0,0)
        assert sp.simplify(sphere-(ns[i] if i==j else 0))==0,(i,j,'norm')
        direct=sum(cap(poly[i]*poly[j],a,cvals[a]) for a in range(3))
        assert sp.simplify(direct-M[i,j])==0,(i,j,'cap')
# Equal aperture check against three independent sector expressions.
C=sp.symbols('C',real=True)
equal={v:C for v in cvals}
L0=3-sp.Rational(105,8)*C**3+sp.Rational(63,4)*C**5-sp.Rational(45,8)*C**7
L1=3-sp.Rational(119,32)*C+sp.Rational(35,32)*C**3+sp.Rational(63,32)*C**5-sp.Rational(75,32)*C**7
L2=3-sp.Rational(105,32)*C+sp.Rational(105,32)*C**3-sp.Rational(231,32)*C**5+sp.Rational(135,32)*C**7
for i,expected in enumerate([L0]+[L1]*3+[L2]*3):
    assert sp.factor(M[i,i].subs(equal)-ns[i]*expected)==0
assert sp.factor(L0-L1)==-sp.Rational(7,32)*C*(C-1)*(C+1)*(15*C**4-48*C*C+17)
assert sp.factor(L0-L2)==-sp.Rational(105,32)*C*(C-1)**2*(C+1)**2*(3*C*C-1)
assert sp.factor(sum(M[i,i]/ns[i] for i in range(7)) - 7*sum(1-v for v in cvals))==0
print('Exact verification PASS: harmonicity, all 28 Gram pairings, block entries, trace and isotropy obstruction.')

# Independent direct 2D quadrature over each cap at three anisotropic choices.
phis=2*np.pi*(np.arange(240)+.5)/240
cosphi=np.cos(phis);sinphi=np.sin(phis)
scale=np.sqrt(np.array([float(v) for v in ns]))

def direct_numerical(cc):
    N=np.zeros((7,7))
    nodes,weights=np.polynomial.legendre.leggauss(95)
    for a,cutoff in enumerate(cc):
        nodes1=(nodes+1)*(1-cutoff)/2+cutoff
        weights1=weights*(1-cutoff)/2
        j,k=[i for i in range(3) if i!=a]
        for val,w in zip(nodes1,weights1):
            xyz=np.zeros((240,3))
            xyz[:,a]=val
            xyz[:,j]=np.sqrt(1-val*val)*cosphi
            xyz[:,k]=np.sqrt(1-val*val)*sinphi
            xx,yy,zz=xyz.T
            F=np.stack([xx*yy*zz,xx*(5*xx*xx-3),yy*(5*yy*yy-3),zz*(5*zz*zz-3),
              xx*(yy*yy-zz*zz),yy*(zz*zz-xx*xx),zz*(xx*xx-yy*yy)],axis=1)/scale
            N+=(w/240)*(F.T@F)
    return N
for cutoffs in [(1/math.sqrt(2),.80,.93),(.72,.73,.74),(.82,.86,.92),(.96,.97,.98)]:
    numeric=direct_numerical(cutoffs)
    sub={v:t for v,t in zip(cvals,cutoffs)}
    analytic=np.array([[float(sp.N(M[i,j].subs(sub)/sp.sqrt(ns[i]*ns[j]))) for j in range(7)] for i in range(7)])
    err=np.max(np.abs(numeric-analytic))
    assert err<3e-13,(cutoffs,err)
    assert np.linalg.eigvalsh(numeric)[0]>0
    print('Numerical quadrature PASS:',cutoffs,'entrywise error',err)
print('Verification complete.')
