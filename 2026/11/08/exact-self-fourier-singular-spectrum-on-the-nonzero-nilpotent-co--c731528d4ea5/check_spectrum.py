"""Numerical tests for the nilpotent-cone self-Fourier singular-value theorem.

Requires Python 3 and NumPy. Run: python check_spectrum.py
These finite checks are not a substitute for the general proof.
"""
import cmath
import math
import numpy as np


class FiniteField:
    def __init__(self, p, defining_polynomial):
        self.p = p
        self.mod = tuple(defining_polynomial)
        self.k = len(self.mod)-1
        self.q = p ** self.k
        assert self.mod[-1] == 1

    def digits(self, a):
        return [(a // (self.p ** j)) % self.p for j in range(self.k)]

    def number(self, d):
        return sum((v % self.p) * self.p ** j for j, v in enumerate(d))

    def add(self, a, b):
        aa, bb = self.digits(a), self.digits(b)
        return self.number([(x+y) % self.p for x, y in zip(aa, bb)])

    def neg(self, a):
        return self.number([(-x) % self.p for x in self.digits(a)])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        aa, bb = self.digits(a), self.digits(b)
        coeff = [0] * (2*self.k-1)
        for i,x in enumerate(aa):
            for j,y in enumerate(bb):
                coeff[i+j] = (coeff[i+j]+x*y) % self.p
        for j in range(len(coeff)-1,self.k-1,-1):
            top = coeff[j]
            for t in range(self.k):
                coeff[j-self.k+t] = (coeff[j-self.k+t]-top*self.mod[t]) % self.p
        return self.number(coeff[:self.k])

    def pow(self, a, e):
        res=1
        while e:
            if e&1:res=self.mul(res,a)
            a=self.mul(a,a)
            e//=2
        return res

    def trace(self, a):
        val=0
        for j in range(self.k):
            val=self.add(val,self.pow(a,self.p**j))
        assert all(d==0 for d in self.digits(val)[1:]), (self.q,a,val)
        return val % self.p


def check(p, polynomial):
    F=FiniteField(p, polynomial)
    q=F.q
    points=[(s,(1,t)) for t in range(q) for s in range(1,q)]
    points += [(s,(0,1)) for s in range(1,q)]
    assert len(points)==q*q-1
    H=np.empty((len(points),len(points)),dtype=complex)
    for i,(s,u) in enumerate(points):
        for j,(v,w) in enumerate(points):
            delta=F.sub(F.mul(u[0],w[1]),F.mul(u[1],w[0]))
            exponent=F.neg(F.mul(F.mul(s,v),F.mul(delta,delta)))
            H[i,j]=cmath.exp(2j*math.pi*F.trace(exponent)/p)
    sigma=np.sort(np.linalg.svd(H, compute_uv=False))
    if p == 2:
        expected=[1]+[q]*(q*q-2)
    else:
        expected=[1]+[math.sqrt(q)]*q+[q]*(q*q-q-3)+[q**1.5]
    expected=np.array(sorted(expected),dtype=float)
    error=float(np.max(np.abs(sigma-expected)))
    assert error < 1e-8 * max(1,q**1.5), (q,error)
    assert abs(np.sum(sigma*sigma)-len(points)**2)<1e-7*len(points)**2
    print(f"GF({q}) PASS dimension={len(points)} max_absolute_singular_error={error:.3g}")


if __name__ == '__main__':
    for p,poly in [
        (2,(0,1)), (3,(0,1)), (2,(1,1,1)), (5,(0,1)),
        (7,(0,1)), (2,(1,1,0,1)), (3,(1,0,1)), (11,(0,1))
    ]:
        check(p,poly)
    print('NILPOTENT_CONE_FOURIER_SPECTRUM_PASS')
