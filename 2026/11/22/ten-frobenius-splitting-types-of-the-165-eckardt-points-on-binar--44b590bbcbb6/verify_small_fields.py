"""Independent equation-level test of tangent-cone centers over small finite fields."""
from itertools import product
from hermitian_orbits import CODES, graph, polynomial

class SmallF:
    def __init__(self,m):self.m=m;self.mod=(3 if m==1 else polynomial(m))&((1<<m)-1);self.mask=(1<<m)-1
    def mul(self,a,b):
        c=0
        while b:
            if b&1:c^=a
            a<<=1
            if a>>self.m:a^=self.mod
            a&=self.mask;b>>=1
        return c
    def square(self,a):return self.mul(a,a)

def direct_centers(code,m):
    F=SmallF(m)
    a=[[ (code>>(5*i+j))&1 for j in range(5)] for i in range(5)]
    elems=range(1<<m)
    total=0
    for first in range(5):
        for tail in product(elems, repeat=4-first):
            p=[0]*first+[1]+list(tail)
            p2=[F.square(x) for x in p]
            f=0
            for i in range(5):
                for j in range(5):
                    if a[i][j]:f^=F.mul(p2[i],p[j])
            if f:continue
            L=[0]*5;Q=[0]*5
            for i in range(5):
                for j in range(5):
                    if a[i][j]:
                        L[j]^=p2[i]
                        Q[i]^=p[j]
            z=next(i for i in range(5) if L[i])
            if all(F.mul(Q[i],F.square(L[z]))==F.mul(Q[z],F.square(L[i])) for i in range(5)):
                total+=1
    return total

if __name__=='__main__':
    for code in CODES:
        _,cycles,_=graph(code)
        for m in (1,2,3):
            expected=sum(k*n for k,n in cycles if m%k==0)
            found=direct_centers(code,m)
            assert found==expected,(code,m,found,expected)
        print('small_fields_pass',code)
    print('FROBENIUS_CUBIC_SMALL_FIELD_CHECK_PASS')
