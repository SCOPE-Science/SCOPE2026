"""Exhaustive checks for commutator fibers of two rank-one idempotents in M_2(F_q).
Run: python check_commutator.py
All matrices and all idempotent pairs are enumerated for each listed field.
"""
from collections import Counter

class FiniteField:
    def __init__(self,p,poly):
        self.p=p; self.poly=poly; self.r=len(poly)-1; self.q=p**self.r
        assert poly[-1]==1
        self.digits=[tuple((a//(p**i))%p for i in range(self.r)) for a in range(self.q)]
        self.addtab=[[sum(((self.digits[a][i]+self.digits[b][i])%p)*p**i for i in range(self.r)) for b in range(self.q)] for a in range(self.q)]
        self.multab=[]
        for a in range(self.q):
            row=[]
            for b in range(self.q):
                arr=[0]*(2*self.r-1)
                for i,u in enumerate(self.digits[a]):
                    for j,v in enumerate(self.digits[b]):arr[i+j]=(arr[i+j]+u*v)%p
                for deg in range(2*self.r-2,self.r-1,-1):
                    k=arr[deg]
                    if k:
                        for j in range(self.r):arr[deg-self.r+j]=(arr[deg-self.r+j]-k*poly[j])%p
                row.append(sum(arr[i]*p**i for i in range(self.r)))
            self.multab.append(row)
        for a in range(1,self.q):assert any(self.multab[a][b]==1 for b in range(1,self.q))
    def plus(self,a,b):return self.addtab[a][b]
    def neg(self,a):return sum((-u%self.p)*self.p**i for i,u in enumerate(self.digits[a]))
    def minus(self,a,b):return self.plus(a,self.neg(b))
    def times(self,a,b):return self.multab[a][b]
    def pow(self,a,n):
        b=1
        while n:
            if n&1:b=self.times(b,a)
            a=self.times(a,a);n//=2
        return b
    def inv(self,a):assert a;return self.pow(a,self.q-2)

def matmul(F,A,B):
    return tuple(F.plus(F.times(A[2*i],B[j]),F.times(A[2*i+1],B[2+j])) for i in range(2) for j in range(2))
def comm(F,A,B):
    X=matmul(F,A,B);Y=matmul(F,B,A)
    return tuple(F.minus(x,y) for x,y in zip(X,Y))

def rank_one_projections(F):
    q=F.q
    seen=set()
    for u in [(a,b) for a in range(q) for b in range(q) if (a,b)!=(0,0)]:
        for v in [(a,b) for a in range(q) for b in range(q)]:
            if F.plus(F.times(u[0],v[0]),F.times(u[1],v[1]))==1:
                seen.add(tuple(F.times(u[i],v[j]) for i in range(2) for j in range(2)))
    assert len(seen)==q*(q+1)
    for A in seen:assert matmul(F,A,A)==A
    return sorted(seen)

def lines(F):
    return [(1,t) for t in range(F.q)]+[(0,1)]

def predicted(F,C,ls):
    q=F.q; p=F.p
    if F.plus(C[0],C[3])!=0:return 0
    if C==(0,0,0,0):return 2*q*(q+1)
    if C[1]==0 and C[2]==0 and C[0]==C[3]:return 0
    det=F.minus(F.times(C[0],C[3]),F.times(C[1],C[2]))
    # Eigenline counts, avoiding any reliance on rational canonical form.
    e=z=0
    for u in ls:
        v=(F.plus(F.times(C[0],u[0]),F.times(C[1],u[1])),F.plus(F.times(C[2],u[0]),F.times(C[3],u[1])))
        if F.minus(F.times(u[0],v[1]),F.times(u[1],v[0]))==0:e+=1
        if v==(0,0):z+=1
    if p!=2:
        delta=F.minus(1,F.times(F.plus(1,F.plus(1,F.plus(1,1))),det))
        roots=sum(1 for a in range(q) if F.minus(F.times(a,F.minus(1,a)),det)==0)
        character=0 if delta==0 else (1 if F.pow(delta,(q-1)//2)==1 else -1)
        assert roots==1+character
    else:
        roots=sum(1 for a in range(q) if F.minus(F.times(a,F.minus(1,a)),det)==0)
        t=0; u=det
        for _ in range(F.r):t=F.plus(t,u);u=F.times(u,u)
        assert t in (0,1) and roots==(2 if t==0 else 0)
    return roots*(q+1-e+q*z)

def test(F):
    q=F.q; projections=rank_one_projections(F);observed=Counter()
    for P in projections:
        for Q in projections:observed[comm(F,P,Q)]+=1
    assert sum(observed.values())==q*q*(q+1)*(q+1)
    ls=lines(F)
    mismatch=[]; im=0
    for a in range(q):
      for b in range(q):
       for c in range(q):
        for d in range(q):
            M=(a,b,c,d); expect=predicted(F,M,ls);actual=observed[M]
            if expect != actual:mismatch.append((M,expect,actual))
            im+=bool(actual)
    assert not mismatch,mismatch[:5]
    if F.p==2: image_formula=1+q*(q*q-1)//2
    else:
        chi_minusone=1 if F.pow(F.neg(1),(q-1)//2)==1 else -1
        image_formula=q*q*(q+1)//2+q*(chi_minusone-1)//2
    assert im==image_formula,(im,image_formula)
    print('PASS q=%2d prime=%d degree=%d | rank-one idempotents=%d pairs=%d targets=%d image=%d fiber0=%d' %
          (q,F.p,F.r,len(projections),sum(observed.values()),q**4,im,observed[(0,0,0,0)]))

if __name__=='__main__':
    for p,poly in [(2,[0,1]),(3,[0,1]),(5,[0,1]),(7,[0,1]),(11,[0,1]),(2,[1,1,1]),(2,[1,1,0,1]),(3,[1,0,1])]:
        test(FiniteField(p,poly))
    print('ALL_PROJECTION_COMMUTATOR_CHECKS_PASS')
