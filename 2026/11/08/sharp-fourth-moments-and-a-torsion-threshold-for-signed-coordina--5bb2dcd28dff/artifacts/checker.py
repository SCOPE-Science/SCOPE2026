"""Reproducibility checks for sharp fourth moments of signed-coordinate Fourier spectra.

Usage: python artifacts/checker.py
Python standard library only. Exact arithmetic is used for the convolution test;
finite numerical tests corroborate, but do not prove, the universal result.
"""
from itertools import product
from fractions import Fraction
import cmath
import math
import random

rng = random.Random(20261104)

def imul(z,w):
    a,b=z; c,d=w
    return (a*c-b*d, a*d+b*c)

def iadd(z,w):
    return (z[0]+w[0], z[1]+w[1])

def iconj(z):
    return (z[0], -z[1])

def ipow2(z):
    return imul(z,z)

def mag2(z):
    return z[0]*z[0]+z[1]*z[1]

def frequencies(d,m):
    origin=(0,)*d
    vals=[origin]
    for j in range(d):
        plus=list(origin); minus=list(origin)
        plus[j]=1; minus[j]=m-1
        vals.extend([tuple(plus),tuple(minus)])
    return vals

def exact_fourth(coefs,d,m):
    accum={}
    freqs=frequencies(d,m)
    for k,a in enumerate(freqs):
        for j,b in enumerate(freqs):
            s=tuple((u+v)%m for u,v in zip(a,b))
            accum[s]=iadd(accum.get(s,(0,0)),imul(coefs[k],coefs[j]))
    return sum(mag2(z) for z in accum.values())

def analytic_fourth(coefs,d,m):
    c=coefs[0]
    z=mag2(c)
    v=[]; w=[]; four=[]
    for j in range(d):
        a,b=coefs[2*j+1:2*j+3]
        vj=mag2(a)+mag2(b)
        bj=imul(a,b)
        wj=(2*bj[0],2*bj[1])
        mj=vj*vj+2*mag2(bj)
        if m==4:
            mj+=2*imul(ipow2(a),iconj(ipow2(b)))[0]
        v.append(vj); w.append(wj); four.append(mj)
    Q=ipow2(c)
    out=z*z+4*z*sum(v)+2*sum(imul(iconj(Q),w0)[0] for w0 in w)+sum(four)
    for j in range(d):
        for k in range(j+1,d):
            out+=4*v[j]*v[k]+2*imul(w[j],iconj(w[k]))[0]
    return out

def constant(d,m):
    return Fraction(6*d+1,2*d+1) if m==4 else Fraction(3*(4*d+1),4*d+3)

def direct_fourth(coefs,d,m):
    total=0.0
    for x in product(range(m),repeat=d):
        f=complex(coefs[0])
        for j in range(d):
            w=cmath.exp(2j*math.pi*x[j]/m)
            f+=coefs[2*j+1]*w+coefs[2*j+2]/w
        total+=abs(f)**4
    return total/m**d

cases=0
for m in (4,5,6,7):
    for d in (1,2,3):
        for t in range(52):
            coefs=[(rng.randrange(-3,4),rng.randrange(-3,4)) for _ in range(2*d+1)]
            n=exact_fourth(coefs,d,m)
            p=analytic_fourth(coefs,d,m)
            if n!=p:
                raise AssertionError(('exact convolution',m,d,t,n,p))
            S=sum(mag2(z) for z in coefs)
            if Fraction(n,S*S)>constant(d,m) if S else False:
                raise AssertionError(('sharp bound',m,d,t))
            cases+=1
for m in (4,5,6,7):
    for d in (1,2,3):
        a=1.0 if m==4 else math.sqrt(2.0)
        c=1.0 if m==4 else math.sqrt(3.0)
        v=[c]+[a for _ in range(2*d)]
        S=sum(abs(z)**2 for z in v)
        theoretical=float(constant(d,m))*S*S
        observed=direct_fourth(v,d,m)
        if abs(observed-theoretical)>2e-8*max(1,theoretical):
            raise AssertionError(('attainment Fourier grid',m,d,observed,theoretical))
        cases+=1
# Higher-dimensional phase fibers (non-real, complex) and coefficient-normalized stability.
for m,d in ((4,2),(5,2),(7,3)):
    for t in range(24):
        coefs=[complex(rng.randrange(-4,5),rng.randrange(-4,5)) for _ in range(2*d+1)]
        s=sum(abs(z)**2 for z in coefs)
        if s==0:
            continue
        empirical=direct_fourth(coefs,d,m)
        exact=exact_fourth([(int(z.real),int(z.imag)) for z in coefs],d,m)
        if abs(empirical-exact)>1e-8*max(1,exact):
            raise AssertionError(('direct Fourier',m,d,t))
        if empirical>float(constant(d,m))*s*s+1e-8:
            raise AssertionError(('sharp bound direct',m,d,t))
        cases+=1
# Quantitative energy-deficit bound and non-real extremizers.
for m in (4,5,7):
    for d in (2,3):
        for t in range(16):
            xs=[complex(rng.randrange(-5,6),rng.randrange(-5,6)) for _ in range(2*d+1)]
            S=sum(abs(x)**2 for x in xs)
            if not S: continue
            z=abs(xs[0])**2
            vs=[abs(xs[2*j+1])**2+abs(xs[2*j+2])**2 for j in range(d)]
            if m==4:
                deficiency=2*(z-S/(2*d+1))**2+sum((v-2*S/(2*d+1))**2 for v in vs)
            else:
                deficiency=2*(z-3*S/(4*d+3))**2+1.5*sum((v-4*S/(4*d+3))**2 for v in vs)
            actual=exact_fourth([(int(x.real),int(x.imag)) for x in xs],d,m)
            if float(constant(d,m))*S*S-actual+1e-7<deficiency:
                raise AssertionError(('stability deficit',m,d,t))
            cases+=1
        for t in range(12):
            phi=rng.random()*2*math.pi
            c=(1.0 if m==4 else math.sqrt(3.0))*cmath.exp(1j*phi)
            coeff=[c]
            for j in range(d):
                theta=(phi+math.pi*rng.randrange(4)/2) if m==4 else rng.random()*2*math.pi
                aa=(1.0 if m==4 else math.sqrt(2.0))*cmath.exp(1j*theta)
                bb=(1.0 if m==4 else math.sqrt(2.0))*cmath.exp(1j*(2*phi-theta))
                coeff.extend((aa,bb))
            S=sum(abs(x)**2 for x in coeff)
            observed=direct_fourth(coeff,d,m)
            if abs(observed-float(constant(d,m))*S*S)>1e-8*S*S:
                raise AssertionError(('complex extremizers',m,d,t))
            cases+=1
print(f'SIGNED_COORDINATE_CROSS_L4_PASS cases={cases} exact_integer_convolutions=624')
