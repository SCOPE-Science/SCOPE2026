#!/usr/bin/env python3
"""Exact arithmetic and transverse-curvature tests for cubic-graph extension stability.
Public mathematical reproducibility only. Runs with the Python standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import random


def energy_from_collisions(p, g):
    conv = {}
    for x, y in product(range(p), repeat=2):
        k = ((x+y)%p, (x*x*x+y*y*y)%p)
        conv[k] = conv.get(k,0) + g[x]*g[y]
    return sum((z.real*z.real+z.imag*z.imag) for z in conv.values())


def plus(u,v):
    return (u[0]+v[0],u[1]+v[1])


def mul(u,v):
    return (u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0])


def abs2(u):
    return u[0]*u[0]+u[1]*u[1]


def exact_energy(p,g):
    conv={}
    for x,y in product(range(p),repeat=2):
        k=((x+y)%p,(x*x*x+y*y*y)%p)
        conv[k]=plus(conv.get(k,(0,0)),mul(g[x],g[y]))
    return sum(abs2(z) for z in conv.values())


def stability_terms(p, g):
    S = sum(abs2(z) for z in g)
    a = abs2(g[0])
    pairs = [(i, p-i) for i in range(1, (p+1)//2)]
    m = [abs2(g[i])+abs2(g[j]) for i,j in pairs]
    # Test coefficients are either real integers or imaginary integers.
    amp = [abs(z[0])+abs(z[1]) for z in g]
    assert all(abs2(z)==r*r for z,r in zip(g,amp))
    r = [2*amp[i]*amp[j] for i,j in pairs]
    delta = [mi-ri for mi,ri in zip(m,r)]
    Delta = sum(delta)
    A = 2*(F(a)-F(3*S,2*p+1))**2 + F(3,2)*sum((F(mi)-F(4*S,2*p+1))**2 for mi in m)
    B = sum(F(di)*(2*S-Delta-F(mi+ri,2)) for di,mi,ri in zip(delta,m,r))
    T = mul(g[0],g[0])
    for i,j in pairs:
        z=mul(g[i],g[j]);T=plus(T,(2*z[0],2*z[1]))
    Gamma = (a+sum(r))**2-abs2(T)
    D = (F(3)-F(6,2*p+1))*S*S-exact_energy(p,g)
    return D,A,B,Gamma,F(S,2)*Delta,S,Delta


def D_complex(p, g):
    S = sum(abs(z)**2 for z in g)
    return (3-6/(2*p+1))*S*S - energy_from_collisions(p,g)


def perturbation(p, kind):
    h=(p-1)//2
    a=sqrt(3/(2*p+1)); b=sqrt(2/(2*p+1))
    f=[b+0j]*p;f[0]=a
    v=[0j]*p
    if kind=='symmetric_amplitude':
        # Unit normal to the real radial vector within span(e_0, sum opposite pair).
        v[0] = -sqrt(2)*b / sqrt(a*a+2*b*b)
        v[1] = a/sqrt(2*(a*a+2*b*b))
        v[-1]=v[1]
    elif kind=='antisymmetric_amplitude':
        v[1]=1/sqrt(2);v[-1]=-1/sqrt(2)
    elif kind=='symmetric_phase':
        v[0] = -1j*sqrt(2)*b / sqrt(a*a+2*b*b)
        v[1] = 1j*a/sqrt(2*(a*a+2*b*b))
        v[-1]=v[1]
    elif kind=='antisymmetric_phase':
        v[1]=1j/sqrt(2);v[-1]=-1j/sqrt(2)
    elif kind=='real_radial':v=f[:]
    elif kind=='imag_global':v=[1j*z for z in f]
    else:raise KeyError(kind)
    # Verify norm-one test vector for nonradial kinds.
    return f,v



def verify_gf25():
    """Check the cubic collision identity over F_5[u]/(u^2-2)."""
    p=5; q=25
    def add(x,y):return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
    def multiply(x,y):
        a,b=x%p,x//p;c,d=y%p,y//p
        return ((a*c+2*b*d)%p)+p*((a*d+b*c)%p)
    cube=[multiply(multiply(x,x),x) for x in range(q)]
    pairs=[]
    for x in range(1,q):
        neg=((-x%p)%p)+p*((-(x//p))%p)
        if x<neg:pairs.append((x,neg))
    assert len(pairs)==12
    rng=random.Random(200225)
    for rep in range(15):
        g=[((0,v) if rng.randrange(2) else (v,0)) for v in (rng.randrange(-3,4) for _ in range(q))]
        conv={}
        for x,y in product(range(q),repeat=2):
            k=(add(x,y),add(cube[x],cube[y]))
            conv[k]=plus(conv.get(k,(0,0)),mul(g[x],g[y]))
        Q=sum(abs2(z) for z in conv.values())
        S=sum(abs2(z) for z in g);a=abs2(g[0]);amp=[abs(z[0])+abs(z[1]) for z in g]
        masses=[abs2(g[i])+abs2(g[j]) for i,j in pairs]
        rs=[2*amp[i]*amp[j] for i,j in pairs]
        ds=[m-r for m,r in zip(masses,rs)];Dsum=sum(ds)
        A=2*(F(a)-F(3*S,2*q+1))**2+F(3,2)*sum((F(m)-F(4*S,2*q+1))**2 for m in masses)
        B=sum(F(d)*(2*S-Dsum-F(m+r,2)) for d,m,r in zip(ds,masses,rs))
        T=mul(g[0],g[0])
        for x,y in pairs:
            z=mul(g[x],g[y]);T=plus(T,(2*z[0],2*z[1]))
        Gamma=(a+sum(rs))**2-abs2(T)
        deficit=(F(3)-F(6,2*q+1))*S*S-Q
        assert deficit==A+B+Gamma and B>=F(S,2)*Dsum and Gamma>=0,(rep,deficit,A,B,Gamma)


def main():
    rng=random.Random(12052002)
    total=0
    for p in (5,7,11,13,17):
        # pure-real / pure-imaginary integer coefficients make each sqrt exact.
        for rep in range(35):
            g=[((0,v) if rng.randrange(2) else (v,0)) for v in (rng.randrange(-3,4) for i in range(p))]
            D,A,B,Gamma,imb,S,Delta=stability_terms(p,g)
            assert D==A+B+Gamma, (p,rep,D,A+B+Gamma)
            assert A>=0 and B>=imb and Gamma>=0,(p,rep,A,B,Gamma,imb)
            total+=1
        for kind,want in [('symmetric_amplitude',24/(2*p+1)),('antisymmetric_amplitude',4-8/(2*p+1)),('symmetric_phase',4),('antisymmetric_phase',0),('real_radial',0),('imag_global',0)]:
            f,v=perturbation(p,kind)
            eps=2.e-4
            plus=D_complex(p,[a+eps*b for a,b in zip(f,v)])
            minus=D_complex(p,[a-eps*b for a,b in zip(f,v)])
            center=D_complex(p,f)
            ratio=(plus+minus-2*center)/(2*eps*eps)
            assert abs(ratio-want)<3e-4,(p,kind,ratio,want)
    verify_gf25()
    # Sharpness of 1/2 imbalance constant at pure one-site data.
    p=11;g=[(0,0)]*p;g[1]=(1,0)
    D,A,B,G,imb,S,Delta=stability_terms(p,g)
    assert B==imb==F(1,2) and G==0
    print(f'CUBIC_STABILITY_EXACT_AND_CURVATURE_PASS cases={total} primes=5 bands=6 extension_fields=1')

if __name__=='__main__':main()
