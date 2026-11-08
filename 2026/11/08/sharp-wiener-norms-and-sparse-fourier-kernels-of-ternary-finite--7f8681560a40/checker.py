#!/usr/bin/env python3
"""Independent finite-field FFT check of a quadratic-shell endpoint norm.
Scientific reproducibility: uses only stdlib and numpy; no research infrastructure.
"""
import math
import cmath
import numpy as np
from itertools import product

class Field:
    def __init__(self,p,mod=None):
        self.p=p; self.mod=mod; self.s=1 if mod is None else len(mod)-1
        self.q=p**self.s
        self.coords=[tuple((a//p**i)%p for i in range(self.s)) for a in range(self.q)]
        self.encoding={u:i for i,u in enumerate(self.coords)}
        self.add=[[self.encoding[tuple((x+y)%p for x,y in zip(self.coords[a],self.coords[b]))] for b in range(self.q)] for a in range(self.q)]
        self.neg=[self.encoding[tuple((-x)%p for x in self.coords[a])] for a in range(self.q)]
        self.mul=[[self.rawmul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.one=self.encoding[(1,)+(0,)*(self.s-1)]
        self.square=[self.mul[a][a] for a in range(self.q)]
        self.sqset={a for a in self.square[1:]}
        self.delta=next(a for a in range(1,self.q) if a not in self.sqset)
        self.inv=[None]+[self.pow(a,self.q-2) for a in range(1,self.q)]
        self.trace=[self.tr(a) for a in range(self.q)]
        self.basis=[self.encoding[tuple(int(i==j) for i in range(self.s))] for j in range(self.s)]
        self.dual={tuple(self.trace[self.mul[a][b]] for b in self.basis):a for a in range(self.q)}
        assert len(self.dual)==self.q
    def rawmul(self,a,b):
        p=self.p;s=self.s
        if s==1:return (a*b)%p
        d=[0]*(2*s-1)
        for i,x in enumerate(self.coords[a]):
            for j,y in enumerate(self.coords[b]):d[i+j]=(d[i+j]+x*y)%p
        for k in range(2*s-2,s-1,-1):
            coeff=d[k]
            for j in range(s):d[k-s+j]=(d[k-s+j]-coeff*self.mod[j])%p
        return self.encoding[tuple(d[:s])]
    def pow(self,a,n):
        x=self.one
        while n:
            if n&1:x=self.mul[x][a]
            a=self.mul[a][a];n//=2
        return x
    def tr(self,a):
        x=0;v=a
        for _ in range(self.s):x=self.add[x][v];v=self.pow(v,self.p)
        assert self.coords[x][1:]==(0,)*(self.s-1)
        return self.coords[x][0]
    def qform(self,x,y,z):
        return self.add[self.add[self.square[x]][self.square[y]]][self.neg[self.mul[self.delta][self.square[z]]]]
    def qdual(self,x,y,z):
        return self.add[self.add[self.square[x]][self.square[y]]][self.neg[self.mul[self.inv[self.delta]][self.square[z]]]]

def check_field(p,mod,elliptic):
    F=Field(p,mod);q=F.q;s=F.s
    inv4=F.inv[F.add[F.add[F.one][F.one]][F.add[F.one][F.one]]]
    radius=F.mul[inv4][F.delta] if elliptic else inv4
    eps=1 if radius in {F.mul[F.inv[F.delta]][x] for x in F.sqset} else -1
    assert eps==(1 if elliptic else -1)
    roots={}
    for a in range(1,q):roots.setdefault(F.square[a],a)
    mass=np.zeros((p,)*(3*s),dtype=np.int8)
    for u,x,y in product(range(q),repeat=3):
        if F.qform(u,x,y)==radius:
            mass[F.coords[u]+F.coords[x]+F.coords[y]]=1
    assert mass.sum()==q*(q+eps),(q,int(mass.sum()))
    fourier=np.fft.fftn(mass)
    predicted=np.zeros_like(fourier)
    zero=0;iso=0;ns=0;sq=0
    for idx in np.ndindex(fourier.shape):
        v=[F.dual[idx[s*i:s*(i+1)]] for i in range(3)]
        if v==[0,0,0]:
            z=q*(q+eps);zero+=1
        else:
            t=F.qdual(*v)
            if t==0:
                z=eps*q;iso+=1
            elif F.mul[radius][t] not in F.sqset:
                z=0;ns+=1
            else:
                h=roots[F.mul[radius][t]]
                z=eps*q*2*math.cos(2*math.pi*F.trace[h]/p)
                sq+=1
        predicted[idx]=z
    error=float(np.max(np.abs(fourier-predicted)))
    assert error<2e-8,(q,error)
    assert (zero,iso,ns,sq)==(1,q*q-1,(q-1)*(q*q-eps*q)//2,(q-1)*(q*q+eps*q)//2), (q,zero,iso,ns,sq)
    C=sum(abs(math.cos(2*math.pi*j/p)) for j in range(p))
    formula=(q+eps)/p*C+(1-eps)/q-(1-eps)/q**2
    observed=float(np.sum(np.abs(fourier))/q**3)
    assert abs(observed-formula)<2e-8,(q,observed,formula)
    assert abs(np.sum(np.abs(fourier)**2)-q**3*q*(q+eps))<1e-5
    print(f'q={q:2d} p={p:2d} degree={s} epsilon={eps:+d} spectrum: zero={ns} iso={iso} square={sq}; norm_direct={observed:.12f} formula={formula:.12f}; max_error={error:.2e}')

if __name__=='__main__':
    for p,mod in [(3,None),(5,None),(7,None),(11,None),(3,[1,0,1]),(5,[-2,0,1]),(3,[1,-1,0,1])]:
        for elliptic in (False,True):check_field(p,mod,elliptic)
    print('TERNARY_QUADRATIC_SHELL_ENDPOINT_PASS')
