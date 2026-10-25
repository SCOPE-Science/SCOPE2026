"""Exact finite-field fifth-power graph pair-sum census.

Uses integer arithmetic only. A finite verification of the explicit histogram,
not a substitute for the uniform character-sum proof.
"""
from collections import Counter
import cmath
import math


class Field:
    def __init__(self, p, nonsquare=None):
        self.p=p
        self.ext=nonsquare is not None
        self.d=nonsquare
        self.q=p*p if self.ext else p
        if self.ext:
            assert pow(nonsquare,(p-1)//2,p)==p-1

    def add(self, a,b):
        p=self.p
        if not self.ext: return (a+b)%p
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)

    def mul(self,a,b):
        p=self.p
        if not self.ext: return (a*b)%p
        return ((a%p*(b%p)+self.d*(a//p)*(b//p))%p) + p*((a%p*(b//p)+(a//p)*(b%p))%p)

    def pow(self,a,k):
        v=1
        while k:
            if k&1: v=self.mul(v,a)
            a=self.mul(a,a)
            k//=2
        return v

    def neg(self,a):
        return self.mul(a,self.p-1)

    def chi(self,a):
        if a==0:return 0
        return 1 if self.pow(a,(self.q-1)//2)==1 else -1


def verify(F):
    q=F.q
    five=[F.pow(t,5) for t in range(q)]
    frequencies=Counter()
    row_histograms=[]
    for t in range(q):
        for u in range(q):
            frequencies[F.add(t,u),F.add(five[t],five[u])]+=1
    assert frequencies[(0,0)]==q
    assert all(frequencies[(0,z)]==0 for z in range(1,q))
    k=F.chi(F.neg(1))
    h=F.chi(F.neg(F.add(1,1)))
    predicted={
        0:(5*q-4+2*h-3*k)//8,
        1:(1-h)//2,
        2:(q+3*k)//4,
        3:(1+h)//2,
        4:(q-4-2*h-3*k)//8,
    }
    assert all(v>=0 for v in predicted.values())
    assert sum(predicted.values())==q
    assert sum(j*predicted[j] for j in range(5))==q
    for s in range(1,q):
        histogram=Counter(frequencies[(s,z)] for z in range(q))
        for j in range(5):
            assert histogram[j]==predicted[j], (q,s,j,dict(histogram),predicted)
        assert histogram==Counter({j:n for j,n in predicted.items() if n}), (q,s,dict(histogram),predicted)
        assert sum(j*j*histogram[j] for j in range(5))==3*(q-1-k)
        row_histograms.append(histogram)
    E=sum(v*v for v in frequencies.values())
    assert E==q*q+(q-1)*3*(q-1-k)
    assert E==4*q*q-6*q+3-3*k*(q-1)
    # Orthogonality makes the normalized constant-input fourth extension moment E/q^2.
    if not F.ext and q<=13:
        direct=0.0
        for xi in range(q):
            for eta in range(q):
                z=sum(cmath.exp(2j*math.pi*((xi*t+eta*five[t])%q)/q) for t in range(q))/q
                direct+=abs(z)**4
        assert abs(direct-E/(q*q))<1e-9, (q,direct,E/(q*q))
    return len(row_histograms), q*q, E, predicted


def main():
    fields=[Field(7),Field(11),Field(13),Field(17),Field(19),Field(23),Field(29),Field(31),Field(37),Field(7,3),Field(11,2)]
    rows=pairs=0
    for field in fields:
        r,m,e,h=verify(field)
        rows+=r
        pairs+=m
        print(f'q={field.q} characteristic={field.p} chi(-1)={field.chi(field.neg(1))} chi(-2)={field.chi(field.neg(field.add(1,1)))} histogram={h} energy={e}')
    print(f'VERIFY_OK fields={len(fields)} nonzero_rows={rows} ordered_pairs={pairs} all_histograms=PASS all_energies=PASS extension_fields=2')

if __name__=='__main__':main()
