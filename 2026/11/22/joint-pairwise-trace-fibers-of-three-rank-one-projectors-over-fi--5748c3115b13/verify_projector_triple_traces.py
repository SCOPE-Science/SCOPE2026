"""Exhaustive independent prescribed pairwise-trace test for rank-one projections."""
from collections import Counter

class Field:
    def __init__(self,q):
        self.q=q
        if q in (4,8):
            self.p=2; self.poly={4:0b111,8:0b1011}[q]
        elif q==9:
            self.p=3; self.poly=None
        else:
            self.p=q; self.poly=None
    def add(self,a,b):
        if self.q in (4,8):return a^b
        if self.q==9:return (a%3+b%3)%3+3*((a//3+b//3)%3)
        return (a+b)%self.q
    def neg(self,a):return self.sub(0,a)
    def sub(self,a,b):
        if self.q in (4,8):return a^b
        if self.q==9:return (a%3-b%3)%3+3*((a//3-b//3)%3)
        return (a-b)%self.q
    def mul(self,a,b):
        if self.q in (4,8):
            c=0; x=a; y=b
            while y:
                if y&1:c^=x
                y>>=1;x<<=1
                if x&self.q:x^=self.poly
            return c
        if self.q==9:
            a0,a1=a%3,a//3;b0,b1=b%3,b//3
            return (a0*b0-a1*b1)%3+3*((a0*b1+a1*b0)%3)
        return (a*b)%self.q
    def inv(self,a):
        assert a
        for x in range(1,self.q):
            if self.mul(a,x)==1:return x
        raise ValueError

def formula(F,a,b,c):
    q=F.q
    A=F.mul(a,F.sub(1,a));C=F.mul(c,F.sub(1,c))
    d=F.sub(b,F.add(F.add(1,F.neg(a)),F.add(F.neg(c),F.mul(2%F.p,F.mul(a,c)))))
    if A and C:
        roots=sum(F.sub(F.sub(F.mul(s,s),F.mul(d,s)),F.neg(F.mul(A,C)))==0 for s in range(1,q))
        return (q-1)*roots
    if bool(A)!=bool(C):return (q-1)*(1 if d==0 else 2)
    return 2*q*q-1 if d==0 else 2*(q-1)

def check(q):
    F=Field(q);Q=range(q)
    projectors=[]
    for a in Q:
        A=F.mul(a,F.sub(1,a))
        for x in Q:
            for y in Q:
                if F.mul(x,y)==A: projectors.append((a,x,y,F.sub(1,a)))
    assert len(projectors)==q*(q+1),(q,len(projectors))
    def traceprod(P,H):
        return F.add(F.add(F.mul(P[0],H[0]),F.mul(P[1],H[2])),F.add(F.mul(P[2],H[1]),F.mul(P[3],H[3])))
    E=(1,0,0,0);actual=Counter()
    for P in projectors:
        a=traceprod(E,P)
        for H in projectors:
            c=traceprod(E,H);b=traceprod(P,H)
            actual[(a,b,c)]+=1
    for a in Q:
        for b in Q:
            for c in Q:
                expected=formula(F,a,b,c)
                assert actual[(a,b,c)]==expected,(q,(a,b,c),actual[(a,b,c)],expected)
    assert sum(actual.values())==len(projectors)**2
    support=sum(actual[(a,b,c)]>0 for a in Q for b in Q for c in Q)
    assert support==(q**3+4*q*q-4*q+(q%2))//2
    assert max(actual.values())==2*q*q-1
    assert sum(v==2*q*q-1 for v in actual.values())==4
    print('PASS',q,'projectors',len(projectors),'fibers',len(actual),'triples',len(projectors)**2,'maxfiber',max(actual.values()))
if __name__=='__main__':
    for q in [2,3,4,5,7,8,9,11]: check(q)
    print('PROJECTOR_TRIPLE_TRACE_PASS')
