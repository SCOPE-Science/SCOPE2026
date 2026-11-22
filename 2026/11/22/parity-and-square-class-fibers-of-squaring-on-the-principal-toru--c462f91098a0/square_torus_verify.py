"""Finite exhaustive tests for square-map fibers in cyclic truncated path algebras.
The independent count uses the path-concatenation multiplication rule.
"""
from itertools import product
from collections import defaultdict

class F:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return (a^b) if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4: return a*b%self.q
        r=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1): r^=1<<(i+j)
        if r&8:r^=0b1110 # x^3=x^2+x
        if r&4:r^=0b111 # x^2=x+1
        return r
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)
    def sub(self,a,b):
        return self.add(a,b if self.q==4 else (-b)%self.q)

def square_direct(n,F,a,b):
    # compute coefficients by path concatenation, not using inversion or other fiber formulas
    paths={}
    for degree,coeff in ((1,a),(2,b)):
        for i,v in enumerate(coeff):paths[(i,degree)]=v
    out2=[0]*n;out3=[0]*n
    for (i,di),x in paths.items():
        for (j,dj),y in paths.items():
            if (i+di)%n!=j or di+dj>=4:continue
            if di+dj==2: out2[i]=F.add(out2[i],F.mul(x,y))
            else:out3[i]=F.add(out3[i],F.mul(x,y))
    return tuple(out2),tuple(out3)

def predicted(n,F,u,v):
    q=F.q
    if not all(u):return None
    s=[1]
    for i in range(n):s.append(F.mul(u[i],F.inv(s[-1])))
    roots=[]
    for t in range(1,q):
        if n%2 and F.mul(t,t)!=s[-1]:continue
        if n%2==0 and s[-1]!=1:continue
        a=[F.mul(s[i],t if i%2==0 else F.inv(t)) for i in range(n)]
        if any(F.mul(a[i],a[(i+1)%n])!=u[i] for i in range(n)):
            raise AssertionError('root reconstruction failed')
        d=[F.mul(F.mul(a[i],a[(i+1)%n]),a[(i+2)%n]) for i in range(n)]
        if n%2 and q%2:good=True
        else:
            acc=0
            for i in range(n):
                val=F.mul(v[i],F.inv(d[i]))
                if q%2 and i%2:val=F.sub(0,val)
                acc=F.add(acc,val)
            good=(acc==0)
        if good:roots.append(t)
    kernel_size=(1 if n%2 and q%2 else q)
    return len(roots)*q**n*kernel_size

def test(n,q):
    F=globals()['F'](q)
    cnt=defaultdict(int)
    for a in product(range(q),repeat=n):
        if any(x==0 for x in a):continue # u fully nonzero iff all a nonzero
        for b in product(range(q),repeat=n):
            u,v=square_direct(n,F,a,b)
            cnt[(u,v)]+=1
    universe=0
    for u in product(range(1,q),repeat=n):
        for v in product(range(q),repeat=n):
            expect=predicted(n,F,u,v)
            actual=cnt.get((u,v),0)*q**n # free degree-three coefficients
            if expect!=actual:
                raise AssertionError((n,q,u,v,expect,actual))
            if expect:universe+=1
    if n%2:
        expected_image=((q-1)**n*q**(n-1)) if q%2==0 else (((q-1)**n//2)*q**n)
    else:
        g=1 if q%2==0 else 2
        expected_image=(q-1)**(n-1)*q**(n-2)*(1+(q-1)**2//g)
    assert universe==expected_image,(n,q,universe,expected_image)
    print('PASS',n,q,'image_torus',universe,'fibers',len(cnt))

if __name__=='__main__':
    for n,q in ((3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(4,5),(5,2),(5,3),(6,2)):
        test(n,q)
    print('NAKAYAMA_SQUARE_TORUS_OK')
