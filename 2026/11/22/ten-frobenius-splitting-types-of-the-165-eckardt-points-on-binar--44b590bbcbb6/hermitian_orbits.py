"""Frobenius cycles on the 165 geometric cone points of the 13 smooth binary Frobenius cubics."""
from collections import Counter
from functools import reduce
from itertools import combinations

CODES=(1118480,1118482,1118484,1118485,1118486,1118616,1118680,
       1118744,1118745,1122448,1122450,1122451,1122820)
N=5
I=[1<<i for i in range(5)]
def matmul(a,b):return [reduce(int.__xor__,(b[j] for j in range(5) if (a[i]>>j)&1),0) for i in range(5)]
def transpose(a):return [sum(((a[j]>>i)&1)<<j for j in range(5)) for i in range(5)]
def inverse(a):
    b=a[:];c=I[:]
    for j in range(5):
        k=next(i for i in range(j,5) if b[i]>>j&1)
        b[j],b[k]=b[k],b[j];c[j],c[k]=c[k],c[j]
        for i in range(5):
            if i!=j and b[i]>>j&1:b[i]^=b[j];c[i]^=c[j]
    assert b==I
    return c

def poly_rem(a,m):
    d=m.bit_length()-1
    while a.bit_length()>d:a^=m<<(a.bit_length()-d-1)
    return a

def poly_gcd(a,b):
    while b:a,b=b,poly_rem(a,b)
    return a

def poly_mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        a<<=1;b>>=1
    return c

def irreducible(p):
    m=p.bit_length()-1
    x=2; v=x
    divs=[d for d in range(1,m+1) if m%d==0 and d!=m and all(d%e for e in range(2,__import__('math').isqrt(d)+1))] # unused
    # Rabin's irreducibility criterion: test each distinct prime factor of m
    primes=[]; z=m; k=2
    while k*k<=z:
        if z%k==0:
            primes.append(k)
            while z%k==0:z//=k
        k+=1
    if z>1:primes.append(z)
    checkpoints={m//a for a in primes};
    for i in range(1,m+1):
        v=poly_rem(poly_mul(v,v),p)
        if i in checkpoints and poly_gcd(v^x,p)!=1:return False
    return v==x

def polynomial(m):
    for lower in range(1,1<<m,2):
        p=(1<<m)|lower
        if irreducible(p):return p
    raise AssertionError('none')

class Field:
    def __init__(self,m):
        self.m=m;self.mask=(1<<m)-1;self.p=polynomial(m)
        self.gamma=next(v for u in range(2,100) if (v:=self.pow(u,(1<<m)//3))!=1 and self.pow(v,3)==1)
        self.g2=self.mul(self.gamma,self.gamma)
        assert self.gamma^self.g2==1
    def mul(self,a,b):
        r=0;m=self.m;mask=self.mask;p=self.p&mask
        while b:
            if b&1:r^=a
            b>>=1
            a<<=1
            if a>>m:a^=p
            a&=mask
        return r
    def pow(self,x,k):
        v=1
        while k:
            if k&1:v=self.mul(v,x)
            x=self.mul(x,x);k>>=1
        return v
    def square(self,x):return self.mul(x,x)
    def mulvec(self,g,v):return tuple(self.mul(g,x) for x in v)


def kernel_solutions(a,field,c):
    m=field.m; piv={}; basis=[]
    for j in range(5):
        for k in range(m):
            x=1<<k
            y=tuple((field.pow(x,4) if i==j else 0)^(x if ((c[i]>>j)&1) else 0) for i in range(5))
            z=sum(yi<<(m*i) for i,yi in enumerate(y))
            mask=1<<(m*j+k)
            while z:
                p=z.bit_length()-1
                if p in piv:
                    u,v=piv[p];z^=u;mask^=v
                else:
                    piv[p]=(z,mask);break
            if z==0:basis.append(mask)
    assert len(basis)==10,(len(basis),m,c)
    return basis

def to_vec(mask,m):return tuple((mask>>(m*i))&((1<<m)-1) for i in range(5))

def canonical(p,F):return min(p,F.mulvec(F.gamma,p),F.mulvec(F.g2,p))

def graph(code):
    a=[(code>>(5*i))&31 for i in range(5)]
    c=matmul(inverse(transpose(a)),a)
    r=I[:];order=0
    while True:
        order+=1;r=matmul(r,c)
        if r==I:break
        assert order<500
    F=Field(2*order)
    basis=kernel_solutions(a,F,c)
    points=set()
    for h in range(1,1<<10):
        mask=0
        for k,b in enumerate(basis):
            if (h>>k)&1:mask^=b
        p=to_vec(mask,F.m)
        val=0
        for i in range(5):
            for j in range(5):
                if (a[i]>>j)&1:
                    val^=F.mul(F.square(p[i]),p[j])
        if val==0:points.add(canonical(p,F))
    assert len(points)==165,(code,order,len(points),F.p)
    cycles=Counter()
    remaining=set(points)
    while remaining:
        p=next(iter(remaining)); start=p; length=0
        while True:
            assert p in remaining,(code,order,p)
            remaining.remove(p);length+=1
            p=canonical(tuple(F.square(v) for v in p),F)
            if p==start:break
        cycles[length]+=1
    assert sum(a*b for a,b in cycles.items())==165
    return order,tuple(sorted(cycles.items())),F.p

if __name__=='__main__':
    for code in CODES:
        order,cycles,poly=graph(code)
        print(code,'C_order',order,'cycles',cycles,'irreducible',hex(poly),flush=True)
