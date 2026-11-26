"""Independent finite-field convolution and Fourier checks for the split conic.
Run: python3 verify_hyperbola.py
Uses only Python's standard library. Numerical DFT checks corroborate an algebraic proof.
"""
from collections import defaultdict
import cmath
import math
import random

class Field:
    def __init__(self, q):
        assert q in (3, 5, 7, 9, 11)
        self.q = q
        self.p = 3 if q == 9 else q
        self.elems = list(range(q))
        self.nz = list(range(1, q))

    def add(self, x, y):
        if self.q != 9:
            return (x+y) % self.q
        return ((x%3+y%3)%3)+3*((x//3+y//3)%3)

    def neg(self, x):
        return self.add(0, self.mul(-1%self.p, x)) if self.q != 9 else ((-x%3)%3) + 3*((-(x//3))%3)

    def mul(self, x, y):
        if self.q != 9:
            return (x*y) % self.q
        a, b = x%3, x//3
        c, d = y%3, y//3
        return ((a*c-b*d)%3) + 3*((a*d+b*c)%3)

    def pow(self, x, n):
        y=1
        for _ in range(n):
            y=self.mul(x,y)
        return y

    def inv(self,x):
        assert x
        return self.pow(x,self.q-2)

    def trace(self,x):
        return x%self.q if self.q != 9 else (2*(x%3))%3

    def chi(self,x):
        return cmath.exp(2j*math.pi*self.trace(x)/self.p)


def objects(F):
    return {t:(t,F.inv(t)) for t in F.nz}

def sum_pair(F, a, b):
    return F.add(a[0],b[0]), F.add(a[1],b[1])

def energy(F, f, objs):
    h=defaultdict(complex)
    for t in F.nz:
        for u in F.nz:
            h[sum_pair(F,objs[t],objs[u])]+=f[t]*f[u]
    return sum(abs(x)**2 for x in h.values()), h

def defect(F, f):
    n=F.q-1; k=n//2
    pairs=[]; visited=set()
    for t in F.nz:
        if t not in visited:
            u=F.neg(t)
            assert t!=u
            visited.update((t,u));pairs.append((t,u))
    assert len(pairs)==k
    M=sum(abs(f[t])**2 for t in F.nz)
    A=[abs(f[t])**2+abs(f[u])**2 for t,u in pairs]
    B=[2*f[t]*f[u] for t,u in pairs]
    Btotal=sum(B)
    D1=sum((x-M/k)**2 for x in A)
    D2=0.5*sum(abs(x-Btotal/k)**2 for x in B)
    D3=(1-1/(2*k))*(M*M-abs(Btotal)**2)
    return (3-3/n)*M*M-(D1+D2+D3), (D1,D2,D3), M

def check():
    rng=random.Random(47611)
    direct=0; random_checks=0; extremizers=0
    for q in (3,5,7,9,11):
        F=Field(q); ob=objects(F); n=q-1
        # Verify each nonzero pair sum has at most two ordered representations.
        _, collision=energy(F,{t:1 for t in F.nz},ob)
        assert len(collision) == n*n//2+1, (q,len(collision))
        for s,c in collision.items():
            assert s == (0,0) or round(c.real)<=2, (q,s,c)
        assert collision[(0,0)] == n
        for sample in range(45):
            f={t:complex(rng.randrange(-3,4),rng.randrange(-3,4)) for t in F.nz}
            if not any(f.values()): f[1]=1
            e,h=energy(F,f,ob)
            exact, terms, M=defect(F,f)
            assert abs(e-exact)<1e-7*(1+e+abs(exact)),(q,e,exact)
            assert all(x>-1e-7 for x in terms),(q,terms)
            assert e<=(3-3/n)*M*M + 1e-7
            norm_direct=0.
            for a in F.elems:
                for b in F.elems:
                    z=sum(f[t]*F.chi(F.add(F.mul(a,ob[t][0]),F.mul(b,ob[t][1]))) for t in F.nz)/n
                    norm_direct+=abs(z)**4
            norm_energy=q*q*e/n**4
            assert abs(norm_direct-norm_energy)<1e-7*(1+norm_energy),(q,norm_direct,norm_energy)
            direct+=q*q;random_checks+=1
        # Every antipodal pair may carry opposite unit phases independently.
        f={};visited=set()
        phases=[1,-1,1j,-1j]
        for t in F.nz:
            if t in visited:continue
            u=F.neg(t);visited.add(t);visited.add(u)
            ph=rng.choice(phases)
            f[t]=ph; f[u]=ph.conjugate()
        e,_=energy(F,f,ob)
        exact, terms, M=defect(F,f)
        assert abs(e-3*n*(n-1))<1e-7
        assert abs(exact-e)<1e-7
        assert max(abs(z) for z in terms)<1e-7
        extremizers+=1
    print('VERIFY_OK finite_fields=5 random_cases=%d direct_Fourier_character_sums=%d extremizer_checks=%d' % (random_checks,direct,extremizers))

if __name__ == '__main__':check()
