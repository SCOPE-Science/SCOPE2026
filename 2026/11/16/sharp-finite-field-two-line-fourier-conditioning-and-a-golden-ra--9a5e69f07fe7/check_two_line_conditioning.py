#!/usr/bin/env python3
"""Direct small-field checks for the two-line Fourier conditioning formulas.

No external packages beyond NumPy. Run: python check_two_line_conditioning.py
"""
import cmath
import math
from collections import Counter
import numpy as np


class Field:
    def __init__(self, p, poly):
        # Irreducible monic polynomial coefficients (ascending) for F_p[x].
        self.p, self.poly = p, poly
        self.degree = len(poly) - 1
        self.q = p ** self.degree
        self.digits = [self.unpack(k) for k in range(self.q)]
        self.add_table = [[self.pack([(u+v) % p for u,v in zip(self.digits[a],self.digits[b])])
                           for b in range(self.q)] for a in range(self.q)]
        self.mul_table = [[self.mul_long(self.digits[a], self.digits[b]) for b in range(self.q)]
                          for a in range(self.q)]
    def unpack(self,n):
        out=[]
        for _ in range(self.degree):
            out.append(n%self.p); n//=self.p
        return out
    def pack(self,d):
        return sum(v * self.p**k for k,v in enumerate(d))
    def mul_long(self, x, y):
        p=self.p; deg=self.degree
        z=[0]*(2*deg-1)
        for i,a in enumerate(x):
            for j,b in enumerate(y): z[i+j]=(z[i+j]+a*b)%p
        for k in range(2*deg-2,deg-1,-1):
            a=z[k]
            for j in range(deg): z[k-deg+j]=(z[k-deg+j]-a*self.poly[j])%p
            z[k]=0
        return self.pack(z[:deg])
    def add(self,a,b):return self.add_table[a][b]
    def mul(self,a,b):return self.mul_table[a][b]
    def pow(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out
    def trace(self,a):
        out=0
        for i in range(self.degree):out=self.add(out,self.pow(a,self.p**i))
        assert out<self.p
        return out
    def char(self,a):return cmath.exp(2j*math.pi*self.trace(a)/self.p)
    def dot(self,a,b):return self.add(self.mul(a[0],b[0]),self.mul(a[1],b[1]))
    def mulv(self,a,v):return (self.mul(a,v[0]),self.mul(a,v[1]))


def classification(q,a,b,c):
    if c==0:return 'perpendicular'
    if a==0 and b==0:return 'two_isotropic'
    if (a==0)!=(b==0):return 'one_isotropic'
    return 'singular'


def spectrum(q,kind):
    if kind in ('perpendicular','two_isotropic'):
        return sorted([1.,1.,1./q**2]+[1./q]*(2*q-4),reverse=True)
    if kind=='one_isotropic':
        v=math.sqrt(4*q+1)
        phi=(1+math.sqrt(5))/2
        return sorted([1.,((v+1)/(2*q))**2,((v-1)/(2*q))**2]
                      +[phi**2/q]*(q-2)+[phi**(-2)/q]*(q-2),reverse=True)
    raise ValueError(kind)


def check(field):
    q=field.q
    representatives=[(1,t) for t in range(q)]+[(0,1)]
    counts=Counter(); tested=0; errors=0
    for i,v in enumerate(representatives):
        for w in representatives[i+1:]:
            a=field.dot(v,v); b=field.dot(w,w); c=field.dot(v,w)
            typ=classification(q,a,b,c)
            counts[typ]+=1
            S=[(0,0)]+[field.mulv(t,v) for t in range(1,q)]+[field.mulv(t,w) for t in range(1,q)]
            assert len(set(S))==2*q-1
            mat=np.array([[field.char(field.dot(x,y))/q for y in S] for x in S])
            actual=np.sort(np.linalg.svd(mat,compute_uv=False)**2)[::-1]
            if typ!='singular':
                expected=spectrum(q,typ)
                if np.max(np.abs(actual-expected))>4e-10:
                    raise AssertionError((q,v,w,typ,actual,expected))
                got=math.sqrt(actual[0]/actual[-1])
                phi=(1+math.sqrt(5))/2
                wanted=2 if (q==2) else (q if typ!='one_isotropic' else phi*math.sqrt(q))
                assert abs(got-wanted)<3e-8,(q,typ,got,wanted)
            else:
                # The arithmetic rank criterion from the established two-line theorem.
                # Invert c^2 by direct finite-field search, and count its order.
                d=field.mul(c,c)
                cinv=next(z for z in range(1,q) if field.mul(d,z)==1)
                r=field.mul(field.mul(a,b),cinv)
                z=1;ord_r=0
                while True:
                    z=field.mul(z,r);ord_r+=1
                    if z==1:break
                nullity=(q-1)//ord_r
                observed=sum(x<3e-12 for x in actual)
                assert observed==nullity,(q,v,w,observed,nullity)
            tested+=1
    if q%2==1 and q%4==3:
        expected={'perpendicular':(q+1)//2,'one_isotropic':0,'two_isotropic':0}
    elif q%2==1:
        expected={'perpendicular':(q-1)//2,'one_isotropic':2*(q-1),'two_isotropic':1}
    else:
        expected={'perpendicular':q//2,'one_isotropic':q,'two_isotropic':0}
    for typ,n in expected.items():assert counts[typ]==n,(q,typ,counts[typ],n)
    assert sum(counts.values())==q*(q+1)//2
    print(f'q={q:2} pairs={tested:3} nonsingular={tested-counts["singular"]:3} types='+str(dict(counts)))
    return tested


if __name__=='__main__':
    cases=[(2,[1,1]),(3,[0,1]),(5,[0,1]),(7,[0,1]),
           (2,[1,1,1]),(2,[1,1,0,1]),(3,[1,0,1]),
           (11,[0,1]),(13,[0,1]),(2,[1,1,0,0,1]),(17,[0,1])]
    total=0
    for p,poly in cases:total+=check(Field(p,poly))
    print('PASS: '+str(total)+' complete two-line matrices independently checked.')
