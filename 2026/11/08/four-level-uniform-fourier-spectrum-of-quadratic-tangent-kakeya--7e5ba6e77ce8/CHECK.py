"""Direct finite-field checks for the quadratic-tangent Kakeya Fourier theorem.
Pure Python 3; no third-party dependencies.
"""
from collections import Counter
from cmath import exp, pi
from math import isclose, sqrt

class Field:
    def __init__(self,p,coeffs):
        self.p=p; self.mod=tuple(coeffs); self.m=len(coeffs)-1
        self.q=p**self.m
        self.vectors=[tuple((a//(p**i))%p for i in range(self.m)) for a in range(self.q)]
        self.add_table=[[self.pack(tuple((x+y)%p for x,y in zip(self.vectors[a],self.vectors[b]))) for b in range(self.q)] for a in range(self.q)]
        self.mul_table=[[self.mul_slow(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inv2=self.inv(2%p)
        self.inv4=self.inv(4%p)
    def pack(self,v): return sum(a*(self.p**i) for i,a in enumerate(v))
    def add(self,a,b):return self.add_table[a][b]
    def neg(self,a): return self.pack(tuple((-v)%self.p for v in self.vectors[a]))
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul_slow(self,a,b):
        p=self.p;m=self.m;u=self.vectors[a];v=self.vectors[b];r=[0]*(2*m-1)
        for i in range(m):
            for j in range(m):r[i+j]=(r[i+j]+u[i]*v[j])%p
        for k in range(2*m-2,m-1,-1):
            c=r[k]
            for i in range(m):r[k-m+i]=(r[k-m+i]-c*self.mod[i])%p
        return self.pack(r[:m])
    def mul(self,a,b):return self.mul_table[a][b]
    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n>>=1
        return r
    def inv(self,a):return self.pow(a,self.q-2)
    def trace(self,a):
        s=0;t=a
        for _ in range(self.m):s=self.add(s,t);t=self.pow(t,self.p)
        assert self.vectors[s][1:]==(0,)*(self.m-1)
        return self.vectors[s][0]
    def chi(self,a):return 0 if a==0 else (1 if self.pow(a,(self.q-1)//2)==1 else -1)
    def psi(self,a):return exp(2j*pi*self.trace(a)/self.p)

def verify(p,coeffs,full=True):
    F=Field(p,coeffs);q=F.q
    neg=F.neg;add=F.add;mul=F.mul;chi=F.chi;psi=F.psi
    sq={mul(a,a) for a in range(q)}
    U={(x,y) for x in range(q) for y in range(q) if chi(F.sub(mul(x,x),mul(4%p,y)))>=0}
    V={(0,y) for y in range(q)}
    K=U|V
    assert len(K)==(q*q+2*q-1)//2
    for t in range(q):
        assert {(x,F.sub(mul(t,x),mul(t,t))) for x in range(q)}<=K
    G=sum(chi(z)*psi(z) for z in range(q))
    assert abs(G*G-chi(neg(1))*q)<1e-7
    norms=Counter(); count=0
    freqs=[(a,b) for a in range(q) for b in range(q)]
    if not full: freqs=freqs[::max(1,len(freqs)//100)]
    for a,b in freqs:
        direct=sum(psi(neg(add(mul(a,x),mul(b,y)))) for x,y in K)
        if a==b==0:pred=complex(len(K))
        elif b==0:pred=complex((q-1)/2)
        else:
            z=mul(mul(a,a),F.inv(b));
            pred=(psi(z)*(q+chi(neg(b))*G)-(1+chi(b)*G))/2
        assert abs(direct-pred)<1e-7,(p,coeffs,a,b,direct,pred)
        assert abs(pred)>1e-6
        if p==3 and F.m%2==1 and F.m>=3 and full and (a,b)!=(0,0):
            h=3**((F.m-1)//2)
            lo=(q+1)*(q+1-3*h)/4
            hi=(q+1)*(q+1+3*h)/4
            levels=[(q-1)**2/4,(q+1)**2/4,lo,hi]
            near=min(range(4),key=lambda i: abs(abs(direct)**2-levels[i]))
            assert abs(abs(direct)**2-levels[near])<1e-6
            norms[near]+=1
        count+=1
    if p==3 and F.m>=3 and F.m%2==1 and full:
        h=3**((F.m-1)//2)
        assert norms==Counter({0:q-1,1:q*(q-1)//3,2:(q-1)*(q//3+h),3:(q-1)*(q//3-h)}),(q,norms)
    return q,count,dict(norms)
if __name__=='__main__':
    for p,poly in [(3,[0,1]),(5,[0,1]),(7,[0,1]),(3,[1,2,0,1])]:
        q,n,counts=verify(p,poly)
        print('verified',q,'frequencies',n,'level_counts',counts)
    print('CHECK_OK')
