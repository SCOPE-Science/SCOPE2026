"""Direct finite-field enumeration for the two-radius sphere convolution theorem.

Python 3, standard library only. Directly counts ordered vector sums and compares
with closed expressions. Runs over prime fields and two quadratic extensions.
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self, p, nonresidue=None):
        self.p = p
        self.nu = nonresidue
        self.q = p if nonresidue is None else p*p
        self.zero = 0
        self.one = 1
        self.elems = range(self.q)
        self.squares = {self.mul(x,x) for x in range(1,self.q)}
        assert len(self.squares)==(self.q-1)//2
    def add(self,a,b):
        p=self.p
        if self.nu is None: return (a+b)%p
        return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
    def minus(self,a):
        p=self.p
        if self.nu is None:return (-a)%p
        return (-a%p)+p*((-(a//p))%p)
    def sub(self,a,b): return self.add(a,self.minus(b))
    def mul(self,a,b):
        p=self.p
        if self.nu is None:return a*b%p
        x,y=a%p,a//p
        z,w=b%p,b//p
        return (x*z+self.nu*y*w)%p+p*((x*w+y*z)%p)
    def scalar(self,n): return n%self.p
    def chi(self,x):
        if x==0:return 0
        return 1 if x in self.squares else -1
    def Q(self,x):
        z=0
        for y in x:z=self.add(z,self.mul(y,y))
        return z

def closed_convolution(F,a,b,x):
    q=F.q
    Q=F.Q
    chi=F.chi
    zero=all(t==0 for t in x)
    u,v=chi(F.minus(a)),chi(F.minus(b))
    s=Q(x)
    if zero:return 2*q*q+q*(u+v)
    if s==0:return q*(4+u+v)
    four=F.scalar(4)
    # Delta(s) = (s+a-b)^2 - 4 a s.
    t=F.add(F.add(s,a),F.minus(b))
    delta=F.sub(F.mul(t,t),F.mul(F.mul(four,a),s))
    c=int(s==F.mul(four,a))+int(s==F.mul(four,b))+2*int(delta==0)
    w=chi(F.minus(s))
    return 4*(q-w)+q*w*c

def closed_energy(F,a,b):
    q=F.q
    u,v=F.chi(F.minus(a)),F.chi(F.minus(b))
    t=F.chi(F.mul(a,b))
    H=int(b==F.mul(F.scalar(9),a))+int(a==F.mul(F.scalar(9),b))
    # Valid because H>0 forces u=v.
    c=u+v
    return (16*(q-1)*(q**4-q*q)
        +q*q*(q*q-1)*(4+c)**2+(2*q*q+q*c)**2
        +24*q*q*(q*q-1)*c
        +q**4*(6+4*t)+5*q**3*c+4*q**3*(q+u)*H)

def direct_check(F,a,b):
    q=F.q
    pts=list(product(F.elems,repeat=3))
    surf=[x for x in pts if F.Q(x) in (a,b)]
    sums=Counter((F.add(x[0],y[0]),F.add(x[1],y[1]),F.add(x[2],y[2]))
        for x in surf for y in surf)
    assert len(sums)==q**3,(q,a,b,len(sums))
    for x in pts:
        got=sums[x]
        want=closed_convolution(F,a,b,x)
        assert got==want,(q,a,b,x,got,want)
    e=sum(v*v for v in sums.values())
    want=closed_energy(F,a,b)
    assert e==want,(q,a,b,e,want)
    return e

def check_minimum(F, radius_pairs):
    from fractions import Fraction
    q=F.q
    scored=[]
    for a,b in radius_pairs:
        u,v=F.chi(F.minus(a)),F.chi(F.minus(b))
        size=2*q*q+q*(u+v)
        scored.append((Fraction(closed_energy(F,a,b),size**4),a,b,u,v))
    best=min(x[0] for x in scored)
    winners=[x for x in scored if x[0]==best]
    if q==5:
        assert best==Fraction(353,43200)
        assert len(winners)==1 and all(x[3]==x[4]==1 for x in winners)
    elif q==9:
        assert best==Fraction(913,648000)
        assert len(winners)==6 and all(x[3]==x[4]==1 for x in winners)
    else:
        assert best==Fraction(8*q*q+3*q-8,8*q**5)
        assert len(winners)==((q-1)//2)**2 and all(x[3]==-x[4] for x in winners)

def test():
    count=0
    for p in (3,5,7,11):
        F=Field(p)
        allpairs=[(a,b) for a in range(1,p) for b in range(a+1,p)]
        check_minimum(F,allpairs)
        for a in range(1,p):
            for b in range(a+1,p):
                direct_check(F,a,b)
                count+=1
        print('prime field',p,'all',((p-1)*(p-2))//2,'radius pairs passed')
    for p,nu in ((3,2),(5,2)):
        F=Field(p,nu)
        # all unordered pairs for F9; representative comparison classes for F25
        pairs=[(a,b) for a in F.elems if a for b in F.elems if b>a]
        check_minimum(F,pairs)
        if F.q==25:
            chosen=[]
            signatures=set()
            for a,b in pairs:
                u=F.chi(F.minus(a));v=F.chi(F.minus(b)); H=int(b==F.mul(F.scalar(9),a))+int(a==F.mul(F.scalar(9),b))
                sig=(min(u,v),max(u,v),H)
                if sig not in signatures:
                    signatures.add(sig);chosen.append((a,b))
            pairs=chosen
        for a,b in pairs:
            direct_check(F,a,b)
            count+=1
        print('extension field',F.q,'sampled pairs',len(pairs),'passed')
    print('PASS',count,'direct convolution and energy enumerations')

if __name__=='__main__':test()
