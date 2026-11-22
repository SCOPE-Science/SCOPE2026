#!/usr/bin/env python3
"""Exact independent finite-field checks of conic-line fourth-moment formulas."""
from collections import defaultdict

class Field:
    def __init__(self,p,m=1,d=None):
        self.p,self.m,self.q,self.d=p,m,p**m,d
        if m not in (1,2): raise ValueError('degree 1 or 2 only')
        if m==2 and (d is None or pow(d,(p-1)//2,p)!=p-1):
            raise ValueError('d must be a quadratic nonsquare')
    def add(self,a,b):
        if self.m==1:return (a+b)%self.p
        p=self.p;return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def neg(self,a):
        return self.sub(0,a)
    def sub(self,a,b):
        if self.m==1:return (a-b)%self.p
        p=self.p;return ((a%p-b%p)%p)+p*((a//p-b//p)%p)
    def mul(self,a,b):
        if self.m==1:return a*b%self.p
        p=self.p;A,B=a%p,a//p;C,D=b%p,b//p
        return ((A*C+self.d*B*D)%p)+p*((A*D+B*C)%p)
    def sq(self,a): return self.mul(a,a)
    def chi(self,a):
        if a==0:return 0
        z=1
        for _ in range((self.q-1)//2):z=self.mul(z,a)
        return 1 if z==1 else -1

def theorem(q,eps,kind):
    if kind=='vertical':return q**3+12*q*q-23*q+11
    if kind=='exterior':return q**3+16*q*q-(9+2*eps)*q
    if kind=='tangent':return q**3+(16+2*eps)*q*q-(35+6*eps)*q+19+4*eps
    if kind=='secant':return q**3+16*q*q-(73+2*eps)*q+90+8*eps
    raise ValueError(kind)

def direct_energy(F, points):
    count=defaultdict(int)
    for a,b in points:
        for c,d in points:
            count[(F.add(a,c),F.add(b,d))]+=1
    return sum(k*k for k in count.values())

def check(F,all_lines=False):
    P={(x,F.sq(x)) for x in range(F.q)}
    eps=F.chi(F.neg(1))
    test=0
    slopes=list(range(F.q)) if all_lines else [0,1]
    for m in slopes:
        cs=list(range(F.q)) if all_lines else [0,next(x for x in range(1,F.q) if F.chi(x)==1),next(x for x in range(1,F.q) if F.chi(x)==-1)]
        for c in cs:
            L={(x,F.add(F.mul(m,x),c)) for x in range(F.q)}
            h=len(P&L)
            kind={0:'exterior',1:'tangent',2:'secant'}[h]
            actual=direct_energy(F,P|L)
            expected=theorem(F.q,eps,kind)
            assert actual==expected,(F.q,m,c,kind,actual,expected)
            test+=1
    cs=list(range(F.q)) if all_lines else [0,1]
    for c in cs:
        L={(c,y) for y in range(F.q)}
        actual=direct_energy(F,P|L)
        expected=theorem(F.q,eps,'vertical')
        assert actual==expected,(F.q,'vertical',c,actual,expected)
        test+=1
    return test

if __name__=='__main__':
    ans=[]
    for params,all_lines in [((3,),True),((5,),True),((7,),True),((11,),False),((13,),False),((17,),False),((19,),False),((3,2,2),True),((5,2,2),False),((7,2,3),False)]:
        F=Field(*params)
        n=check(F,all_lines)
        ans.append((F.q,n))
        print('PASS',F.q,n,'affine lines')
    print('ALL PASS:',sum(n for q,n in ans),'line configurations')
