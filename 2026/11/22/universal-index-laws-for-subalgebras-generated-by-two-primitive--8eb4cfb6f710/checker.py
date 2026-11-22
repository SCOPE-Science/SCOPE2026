"""Independent finite-ring enumeration for two primitive matrix idempotents.
Run: python checker.py
"""
from collections import Counter
from itertools import product

class ChainRing:
    def __init__(self, p, length, dual=False):
        self.p,self.m,self.dual=p,length,dual
        if dual:
            assert length==2
            self.size=p*p
            self.one=1
        else:
            self.size=p**length
            self.one=1
        self.elements=range(self.size)
    def add(self,a,b):
        if not self.dual: return (a+b)%self.size
        p=self.p
        return (a%p+b%p)%p + p*((a//p+b//p)%p)
    def neg(self,a):
        return self.sub(0,a)
    def sub(self,a,b):
        if not self.dual: return (a-b)%self.size
        p=self.p
        return (a%p-b%p)%p + p*((a//p-b//p)%p)
    def mul(self,a,b):
        if not self.dual: return (a*b)%self.size
        p=self.p
        return (a%p*b%p)%p + p*((a%p*(b//p)+(a//p)*(b%p))%p)
    def val(self,a):
        if a==0: return self.m
        if self.dual:
            return 0 if a%self.p else 1
        k=0
        while a%self.p==0:
            a//=self.p; k+=1
        return k
    def matrix_mul(self,A,B):
        a=self.add; u=self.mul
        return tuple(a(u(A[2*i],B[j]),u(A[2*i+1],B[2+j])) for i in range(2) for j in range(2))
    def matadd(self,A,B):
        return tuple(self.add(x,y) for x,y in zip(A,B))
    def matscale(self,x,A):
        return tuple(self.mul(x,y) for y in A)

def inspect(R, check_span=False):
    E=(1,0,0,0); I=(1,0,0,1)
    hist=Counter(); count=0; witnesses={}
    for t,b,c in product(R.elements, repeat=3):
        F=(t,b,c,R.sub(1,t))
        if R.matrix_mul(F,F)!=F: continue
        count+=1
        i,j=R.val(b),R.val(c)
        hist[i+j]+=1
        witnesses[(i,j)]=F
        assert R.mul(b,c)==R.mul(t,R.sub(1,t))
        if check_span:
            EF=R.matrix_mul(E,F)
            FE=R.matrix_mul(F,E)
            gens=[I,E,F,EF,FE]
            sp={tuple(0 for _ in range(4))}
            for G in gens:
                sp={R.matadd(A,R.matscale(z,G)) for A in sp for z in R.elements}
            bi={R.mul(b,z) for z in R.elements}
            ci={R.mul(c,z) for z in R.elements}
            expected={(x,y,z,w) for x,y,z,w in product(R.elements,bi,ci,R.elements)}
            assert sp==expected,(R.p,R.m,R.dual,F,len(sp),len(expected))
    q,m=R.p,R.m
    B=[(q-1)*q**(m-i-1) for i in range(m)]+[1]
    predicted={0:(q-2)*(q-1)*q**(2*m-2)}
    predicted.update({d:2*sum(B[i]*B[d-i] for i in range(m+1) if 0<=d-i<=m) for d in range(1,2*m+1)})
    assert count==q**(2*m-1)*(q+1),(R.p,R.m,R.dual,count)
    assert hist==Counter(predicted),(R.p,R.m,R.dual,hist,predicted)
    assert len(witnesses)==(m+1)**2-(q==2)
    print(f'PASS ring={"F"+str(q)+"[eps]/eps^2" if R.dual else "Z/"+str(q**m)} q={q} m={m}  rank-one idempotents={count} index histogram={dict(sorted(hist.items()))} distinct orders={len(witnesses)} span_checked={check_span}')

if __name__=='__main__':
    for p,m,dual,span in [(2,1,False,True),(3,1,False,True),(5,1,False,False),(2,2,False,True),(3,2,False,False),(2,3,False,False),(3,3,False,False),(2,2,True,True),(3,2,True,False)]:
        inspect(ChainRing(p,m,dual),span)
