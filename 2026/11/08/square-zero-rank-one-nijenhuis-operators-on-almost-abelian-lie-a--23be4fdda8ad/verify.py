"""Reproducible direct verification of finite-field rank-one Lie-Nijenhuis counts.
Only standard Python is required. Run: python verify.py
"""
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4)
        self.q=q
    def add(self,a,b):return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):return a if self.q==4 else (-a)%self.q
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q != 4:return a*b%self.q
        z=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1: z ^= 1<<(i+j)
        if z&8:z ^= 0b1110  # x^3 = x(x+1) = x^2+x;  x^3+x^2+x=0
        if z&4:z ^= 0b111   # x^2 = x+1
        return z
    def dot(self,a,b):
        out=0
        for x,y in zip(a,b):out=self.add(out,self.mul(x,y))
        return out
    def matrix_vector(self,A,v):return tuple(self.dot(row,v) for row in A)
    def bracket(self,A,x,y):
        v=self.matrix_vector(A,x[1:]); z=self.matrix_vector(A,y[1:]);
        return (0,)+tuple(self.sub(self.mul(x[0],b),self.mul(y[0],a)) for a,b in zip(v,z))
    def scale(self,a,v):return tuple(self.mul(a,x) for x in v)
    def plus(self,a,b):return tuple(self.add(x,y) for x,y in zip(a,b))
    def minus(self,a,b):return tuple(self.sub(x,y) for x,y in zip(a,b))


def verify(q,A,tag):
    F=Field(q);m=len(A);n=m+1
    basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    vs=list(product(range(q),repeat=n)); xs=vs[1:]
    AT=tuple(tuple(A[j][i] for j in range(m)) for i in range(m))
    evs=[x for x in product(range(q),repeat=m) if any(x) and any(F.matrix_vector(AT,x)==F.scale(lam,x) for lam in range(q))]
    E=len(evs)
    predicted_total=q**(m+1)-1 + q*(E*(q**(m+1)-1)+(q**m-1-E)*(q**(m-2)-1))//(q-1)
    predicted_nil=q**m-1 + q*(E*(q**m-1)+(q**m-1-E)*(q**(m-2)-1))//(q-1)
    pred_proj=q**m*(1+q*E//(q-1))
    seen={};factor_count=0
    for w in xs:
        for phi in xs:
            lam=F.dot(w,phi)
            def N(x):return F.scale(F.dot(phi,x),w)
            correct=True
            for i in range(n):
                for j in range(i+1,n):
                    x,y=basis[i],basis[j]
                    lhs=F.bracket(A,N(x),N(y))
                    rhs=N(F.minus(F.plus(F.bracket(A,N(x),y), F.bracket(A,x,N(y))),N(F.bracket(A,x,y))))
                    if lhs!=rhs:correct=False;break
                if not correct:break
            if correct:
                factor_count+=1
                # Flat matrix of N in standard basis.
                flat=tuple(F.mul(u,v) for v in phi for u in w)
                assert flat not in seen or seen[flat]==lam
                seen[flat]=lam
    assert factor_count==len(seen)*(q-1), (tag,factor_count,len(seen))
    actual_total=len(seen)
    actual_nil=sum(lam==0 for lam in seen.values())
    actual_proj=sum(lam==1 for lam in seen.values())
    assert (actual_total,actual_nil,actual_proj)==(predicted_total,predicted_nil,pred_proj), (tag,(actual_total,actual_nil,actual_proj),(predicted_total,predicted_nil,pred_proj))
    print(f'{tag}: field={q}, m={m}, nonzero eigen-covectors={E}, rank1 Nijenhuis={actual_total}, squarezero={actual_nil}, idempotent={actual_proj}; DIRECT_NIJENHUIS_OK')

if __name__=='__main__':
    verify(2,((1,0),(0,1)),'scalar_F2_m2')
    verify(3,((1,0),(0,2)),'distinct_eigenvalues_F3_m2')
    verify(3,((0,2),(1,0)),'irreducible_F3_m2')
    verify(2,((0,0,1),(1,0,1),(0,1,0)),'no_eigenvectors_F2_m3')
    verify(2,((0,0,0),(1,0,0),(0,1,0)),'nilpotent_J3_F2_m3')
    verify(2,((0,0,0,1),(1,0,0,1),(0,1,0,0),(0,0,1,0)),'degree4_irreducible_F2_m4')
    verify(4,((0,0),(0,1)),'distinct_eigenvalues_F4_m2')
    print('ALL_DIRECT_NIJENHUIS_AND_COUNT_CHECKS_OK')
