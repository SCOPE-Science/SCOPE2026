"""Finite arithmetic checks for cubic-graph Fourier fourth moments.

Run with Python 3 standard library: python verify.py
For F_25, the element omega satisfies omega^2=2 over F_5.
Finite tests corroborate, but do not replace, the proof for all prime powers.
"""
from collections import defaultdict
from fractions import Fraction
from cmath import exp
from math import pi, sqrt, isclose
from random import Random

class Field:
    def __init__(self, p, quadratic=False):
        self.p = p
        self.quadratic = quadratic
        self.q = p*p if quadratic else p
        self.elements = range(self.q)
        assert not quadratic or p == 5

    def add(self, a, b):
        p = self.p
        if not self.quadratic:
            return (a+b) % p
        return (a%p+b%p)%p + p*((a//p+b//p)%p)

    def neg(self, a):
        p = self.p
        if not self.quadratic:
            return (-a)%p
        return (-a%p) + p*(-(a//p)%p)

    def mul(self, a, b):
        p = self.p
        if not self.quadratic:
            return a*b % p
        x,y = a%p,a//p
        u,v = b%p,b//p
        return ((x*u+2*y*v)%p) + p*((x*v+y*u)%p)

    def cube(self, a):
        return self.mul(self.mul(a,a),a)

    def trace(self, a):
        return (2*(a%self.p))%self.p if self.quadratic else a

    def psi(self, a):
        return exp(2j*pi*self.trace(a)/self.p)


def gmul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def gadd(a,b):
    return (a[0]+b[0],a[1]+b[1])

def gabs2(a):
    return a[0]**2+a[1]**2

def fibers(F):
    out=defaultdict(list)
    for a in F.elements:
        for b in F.elements:
            k=(F.add(a,b),F.add(F.cube(a),F.cube(b)))
            out[k].append((a,b))
    assert len(out[(0,0)]) == F.q
    assert set(out[(0,0)]) == {(a,F.neg(a)) for a in F.elements}
    for (s,c), pairs in out.items():
        if s==0:
            assert c==0
        else:
            assert len(pairs) == (1 if pairs[0][0] == pairs[0][1] else 2)
            assert set(pairs) == {(a,b) for a,b in pairs} and \
                set(pairs)=={(pairs[0][0],pairs[0][1]),
                              (pairs[0][1],pairs[0][0])}
    return out

def exact_energy(F,f):
    conv=defaultdict(lambda:(0,0))
    for a in F.elements:
        for b in F.elements:
            k=(F.add(a,b),F.add(F.cube(a),F.cube(b)))
            conv[k] = gadd(conv[k],gmul(f[a],f[b]))
    return sum(gabs2(z) for z in conv.values())

def formula_energy(F,f):
    w=[gabs2(z) for z in f]
    A=sum(w)
    B=sum(w[x]*w[F.neg(x)] for x in F.elements)
    diagonal=sum(w[x]*w[x] for x in F.elements if x != 0)
    Z=(0,0)
    for x in F.elements:
        Z=gadd(Z,gmul(f[x],f[F.neg(x)]))
    return 2*A*A-2*B-diagonal+gabs2(Z)

def deficit_formula(F,f):
    w=[gabs2(z) for z in f]
    A=sum(w)
    z=w[0]
    picked=set()
    masses=2*(z-3*A/(2*F.q+1))**2
    pairs=[]
    B=z
    P=complex(f[0][0],f[0][1])**2
    for x in F.elements:
        if x==0 or x in picked:
            continue
        y=F.neg(x)
        assert x != y
        picked.update((x,y))
        s=w[x]+w[y]
        r=sqrt(w[x]*w[y])
        tau=s-2*r
        masses+=1.5*(s-4*A/(2*F.q+1))**2
        pairs.append((s,r,tau))
        B+=2*r
        zx=gmul(f[x],f[y])
        P+=2*complex(zx[0],zx[1])
    assert len(pairs)==(F.q-1)//2
    phase=B*B-abs(P)**2
    imbalance=sum(tau*(A+B-.5*(s+2*r)) for s,r,tau in pairs)
    return masses,phase,imbalance

def direct_fourier(F,f):
    total=0.0
    for u in F.elements:
        for v in F.elements:
            T=0j
            for t in F.elements:
                phase=F.add(F.mul(u,t),F.mul(v,F.cube(t)))
                T+=f[t]*F.psi(phase)
            total+=abs(T)**4
    return total/(F.q*F.q)

def sample_extremizer(F):
    rng=Random(45+F.q)
    f=[0j]*F.q
    f[0]=sqrt(3)
    used={0}
    for x in F.elements:
        if x in used:
            continue
        y=F.neg(x)
        used.update((x,y))
        theta=rng.uniform(-pi,pi)
        f[x]=sqrt(2)*exp(1j*theta)
        f[y]=sqrt(2)*exp(-1j*theta)
    return f


def main():
    rng=Random(5103)
    arithmetic=0
    direct=0
    for F in [Field(p) for p in (5,7,11,13)] + [Field(5,True)]:
        fibers(F)
        for j in range(8):
            f=[(rng.randint(-3,3),rng.randint(-3,3)) for t in F.elements]
            if all(z==(0,0) for z in f):
                f[0]=(1,0)
            E=exact_energy(F,f)
            assert E==formula_energy(F,f),(F.q,j,E,formula_energy(F,f))
            A=sum(gabs2(z) for z in f)
            C=Fraction(3,1)-Fraction(6,2*F.q+1)
            assert C*A*A >= E
            defects=deficit_formula(F,f)
            assert min(defects)>=-1e-8*max(A*A,1), (F.q,j,defects)
            assert isclose(sum(defects),float(C*A*A-E),rel_tol=2e-11,abs_tol=1e-7)
            arithmetic+=1
        f=sample_extremizer(F)
        assert isclose(sum(abs(z)**2 for z in f),2*F.q+1,abs_tol=1e-10)
        E=direct_fourier(F,f)
        expected=(3-6/(2*F.q+1))*(2*F.q+1)**2
        assert isclose(E,expected,rel_tol=5e-11,abs_tol=1e-7),(F.q,E,expected)
        direct+=1
        for j in range(3):
            f=[complex(rng.randint(-3,3),rng.randint(-3,3)) for x in F.elements]
            E=direct_fourier(F,f)
            gint=[(round(z.real),round(z.imag)) for z in f]
            assert isclose(E,formula_energy(F,gint),rel_tol=5e-11,abs_tol=1e-7)
            direct+=1
    print('VERIFY_OK finite_fields=5 quadratic_extension=F25 exact_integer_convolution_cases='+str(arithmetic)+' direct_fourier_cases='+str(direct)+' deficit_checks=PASS')

if __name__=='__main__':
    main()
