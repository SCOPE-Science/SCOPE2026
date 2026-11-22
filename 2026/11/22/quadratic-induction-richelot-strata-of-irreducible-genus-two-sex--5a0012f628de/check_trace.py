"""Independent small-field character-sum tests of the odd-extension trace theorem.
Python 3 standard library. Check q=3 and 5 at extension degrees 1 and 3.
"""
from itertools import product
from check_richelot import is_irred, involutions

def choose_cubic(p):
    for a0,a1,a2 in product(range(p), repeat=3):
        if all((r**3+a2*r*r+a1*r+a0)%p for r in range(p)):
            return (a0,a1,a2)
    raise AssertionError

class Fp3:
    def __init__(self,p):
        self.p=p; self.m=choose_cubic(p); self.q=p**3
        self.coeff=[(a%p,a//p%p,a//(p*p)%p) for a in range(self.q)]
        self.mul_table=[[self._mul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.char=[0 if a==0 else (1 if self.power(a,(self.q-1)//2)==1 else -1) for a in range(self.q)]
        assert self.char.count(1)==(self.q-1)//2
    def _mul(self,a,b):
        p=self.p;u=self.coeff[a];v=self.coeff[b];t=[0]*5
        for i in range(3):
            for j in range(3):t[i+j]=(t[i+j]+u[i]*v[j])%p
        for k in (4,3):
            lead=t[k]
            for i in range(3):t[k-3+i]=(t[k-3+i]-lead*self.m[i])%p
        return t[0]+p*t[1]+p*p*t[2]
    def power(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul_table[out][a]
            a=self.mul_table[a][a];n//=2
        return out
    def value(self,f,x):
        # Horner in field: add integer c in constant coefficient.
        result=0
        for c in f[::-1]:
            result=self.mul_table[result][x]
            a,b,d=self.coeff[result]
            result=(a+c)%self.p+self.p*b+self.p*self.p*d
        return result

def type_of(f,p,invols):
    hits=[]
    for _,split,mat in invols:
        transformed=[sum(f[i]*mat[i][j] for i in range(7))%p for j in range(7)]
        k=transformed[-1]
        if k and transformed==[(k*x)%p for x in f]:hits.append(split)
    assert len(hits)<2
    return hits[0] if hits else None

def main(p):
    fld=Fp3(p); invols=involutions(p); count=0
    for coeff in product(range(p),repeat=6):
        f=list(coeff)+[1]
        if not is_irred(f,p):continue
        t=type_of(f,p,invols)
        if t is not False:continue
        count+=1
        n1=p+2+sum(1 if sum(f[i]*pow(x,i,p) for i in range(7))%p in [v*v%p for v in range(1,p)] else -1 for x in range(p))
        n3=p**3+2+sum(fld.char[fld.value(f,x)] for x in range(p**3))
        assert n1==p+1,(p,f,n1)
        assert n3==p**3+1,(p,f,n3)
    assert count==p*p*(p-1)*(p-1)*(p+1)//12
    print(f'GF({p}): {count} nonsplit-involution sextics all have #{p}-points={p+1} and #{p**3}-points={p**3+1}')
if __name__=='__main__':
    main(3);main(5)
    print('All extension-trace checks passed.')
