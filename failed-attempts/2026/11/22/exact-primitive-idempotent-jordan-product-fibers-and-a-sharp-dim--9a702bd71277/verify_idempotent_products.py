"""Literal primitive-idempotent-pair product enumeration for finite spin factors."""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (3,5,7,9)
        self.q=q
        if q!=9:
            self.add=lambda a,b:(a+b)%q
            self.neg=lambda a:(-a)%q
            self.mul=lambda a,b:a*b%q
        else:
            self.add=lambda a,b:(a%3+b%3)%3+3*((a//3+b//3)%3)
            self.neg=lambda a:(-a%3)+3*((-(a//3))%3)
            self.mul=lambda a,b:(a%3*b%3+2*(a//3)*(b//3))%3+3*((a%3*(b//3)+(a//3)*(b%3))%3)
        self.inv={a:next(b for b in range(1,q) if self.mul(a,b)==1) for a in range(1,q)}
        self.squares={self.mul(t,t) for t in range(1,q)}
    def sub(self,a,b):return self.add(a,self.neg(b))
    def chi(self,a):return (0 if a==0 else (1 if a in self.squares else -1))
    def addmulti(self,a,b):return self.add(a,b)

def rep(q,dim,eps,h):
    if dim==0:return int(h==0)
    m=dim//2
    if dim%2==0:return q**(dim-1)+eps*q**(m-1)*(q*(h==0)-1)
    return q**(dim-1)+eps*q**m*(0 if h==0 else (1 if h in SQUARES[q] else -1))
SQUARES={q:Field(q).squares for q in (3,5,7,9)}

def predicted(F,diag,c,w):
    q=F.q;d=len(diag);z=0
    for a,x in zip(diag,w):z=F.add(z,F.mul(a,F.mul(x,x)))
    if c!=F.add(z,z):return 0
    D=1
    for a in diag:D=F.mul(D,a)
    if all(x==0 for x in w):
        eps=F.chi(F.mul(D,1 if (d//2)%2==0 else F.neg(1)))
        return rep(q,d,eps,1)
    # s=4w, Q(s)=16Q(w), h=1-Q(s)/4=1-4Q(w)
    four=F.add(F.add(1,1),F.add(1,1));
    Qs=F.mul(F.mul(four,four),z)
    h=F.sub(1,F.mul(four,z))
    if Qs!=0:
        dim=d-1
        detE=F.mul(D,F.inv[Qs])
        if (dim//2)%2:detE=F.neg(detE)
        return rep(q,dim,F.chi(detE),h)
    dim=d-2
    if dim==0:return 0 # h=1, zero-dimensional quotient cannot represent it
    detW=F.neg(D)
    if (dim//2)%2:detW=F.neg(detW)
    return q*rep(q,dim,F.chi(detW),1)

def verify(q,diag):
    F=Field(q);d=len(diag);vectors=list(product(range(q),repeat=d))
    two=F.add(1,1); inv2=F.inv[two]
    sphere=[]
    for v in vectors:
        Q=0
        for a,x in zip(diag,v):Q=F.add(Q,F.mul(a,F.mul(x,x)))
        if Q==1:sphere.append(v)
    freq=Counter()
    for x in sphere:
        for y in sphere:
            u=tuple(F.mul(inv2,z) for z in x)
            v=tuple(F.mul(inv2,z) for z in y)
            B=0
            for a,b,c in zip(diag,u,v):B=F.add(B,F.mul(a,F.mul(b,c)))
            scalar=F.add(F.mul(inv2,inv2),B)
            w=tuple(F.mul(inv2,F.add(a,b)) for a,b in zip(u,v))
            freq[scalar,w]+=1
    assert sum(freq.values())==len(sphere)**2
    for c in range(q):
        for w in vectors:
            P=predicted(F,diag,c,w)
            assert freq[c,w]==P,(q,diag,c,w,P,freq[c,w])
    support={w for c,w in freq}
    if d>=4:assert len(support)==q**d
    print(f'PASS q={q}, d={d}, diag={diag}, primitive={len(sphere)}, pairs={len(sphere)**2}, supported_vectors={len(support)}/{q**d}, distinct_nonzero_fibers={len(set(freq.values()))}')

if __name__=='__main__':
    for q,diags in [(3,[(1,1),(1,2),(1,1,1),(1,1,2),(1,1,1,1),(1,1,1,2),(1,1,1,1,1)]),
                    (5,[(1,1),(1,2),(1,1,1),(1,1,2),(1,1,1,1)]),
                    (7,[(1,1),(1,3),(1,1,1)]),
                    (9,[(1,1),(1,2),(1,1,1)])]:
        for diag in diags:verify(q,diag)
    print('All prescribed primitive-idempotent product fibers passed.')
