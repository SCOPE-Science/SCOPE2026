#!/usr/bin/env python3
"""Exact finite-field checks for contact supports of the symmetric Ciani pencil.

Only standard Python is used. The algebraic theorem is proved separately;
finite enumeration here checks prime-field instances and degree-four obstructions.
"""
from math import comb
from collections import Counter

def chi(x,p):
    x%=p
    if x==0:return 0
    return 1 if pow(x,(p-1)//2,p)==1 else -1

def mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
    return out

def restrict(x,y,z,lam,p):
    x2,y2,z2=mul(x,x,p),mul(y,y,p),mul(z,z,p)
    terms=[(1,mul(x2,x2,p)),(1,mul(y2,y2,p)),(1,mul(z2,z2,p)),
           (lam,mul(x2,y2,p)),(lam,mul(x2,z2,p)),(lam,mul(y2,z2,p))]
    return [sum(coef*f[k] for coef,f in terms)%p for k in range(5)]

def binary_square(f,p):
    # return the quadratic up to a scalar; coefficients ascending in S
    a,b,c,d,e=f
    if e:
        inv=pow(e,-1,p)
        u=d*inv*pow(2,-1,p)%p
        v=(c*inv-u*u)*pow(2,-1,p)%p
        if b*inv%p==2*u*v%p and a*inv%p==v*v%p:
            return (v,u,1)
        return None
    if d:return None
    if c:
        if (b*b-4*c*a)%p:return None
        # quadratic is v*T^2+u*S*T; choose u=1
        return (b*pow(2*c,-1,p)%p,1,0)
    if b==0 and a:
        return (1,0,0)
    return None

def rational_lines(p):
    for b in range(p):
        for c in range(p):
            yield (1,b,c), ((-b%p,-c%p),(1,0),(0,1))
    for c in range(p):
        yield (0,1,c), ((1,0),(0,-c%p),(0,1))
    yield (0,0,1),((1,0),(0,1),(0,0))

def ground_contacts(p,lam):
    out=Counter()
    for abc,xyz in rational_lines(p):
        q=binary_square(restrict(*xyz,lam,p),p)
        if q is None:continue
        A,B,C=q
        D=(B*B-4*A*C)%p
        out['lines']+=1
        if D==0:out['rational_support']+=1;out['hyperflex']+=1
        elif chi(D,p)==1:out['rational_support']+=2
        else:out['degree2_support']+=1
    return out

def model_rational(p,lam):
    d=(-1-lam)%p;e=(lam+2)%p
    r=chi(d,p);s=chi(e,p)
    count1=4*(1 if chi(-3,p)==1 else 0)*2
    # the 4 sign bitangents have 8 or 0 rational contacts
    count2=4*(1 if chi(-3,p)==-1 else 0)
    h=0
    if r==1:
        if lam==3:
            count1+=12;h+=12
        elif chi(3-lam,p)==1:count1+=24
        else:count2+=12
    if r==1 and s==1:
        if lam==0:
            count1+=12;h+=12
        else:
            w=next(x for x in range(p) if x*x%p==d)
            delta=(-4*lam*pow((1-w)%p,-1,p))%p
            if chi(delta,p)==1:count1+=24
            else:count2+=12
    nlines=4+12*(r==1)+12*(r==1 and s==1)
    return (nlines,count1,count2,h)

class GF2:
    def __init__(self,p):
        self.p=p
        self.n=next(i for i in range(2,p) if chi(i,p)==-1)
        self.z=(0,0);self.one=(1,0)
        self.elements=[(a,b) for a in range(p) for b in range(p)]
        self.roots={}
        for a in self.elements:
            self.roots[self.mul(a,a)]=a
    def add(self,a,b):return ((a[0]+b[0])%self.p,(a[1]+b[1])%self.p)
    def neg(self,a):return (-a[0]%self.p,-a[1]%self.p)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):return ((a[0]*b[0]+self.n*a[1]*b[1])%self.p,(a[0]*b[1]+a[1]*b[0])%self.p)
    def sq(self,a):return self.mul(a,a)
    def norm(self,a):return (a[0]*a[0]-self.n*a[1]*a[1])%self.p
    def sqrt(self,a):return self.roots.get(a)
    def div(self,a,b):
        assert b!=self.z
        n=pow(self.norm(b),-1,self.p)
        return self.mul(a,(b[0]*n%self.p,-b[1]*n%self.p))
    def embed(self,a):return (a%self.p,0)
    def is_sq(self,a):return a in self.roots

def geometric_contact_cycles(p,lam):
    # Independently traverse the full geometric 4+12+12 line list over F_{p^2},
    # using root fields and quadratic discriminants to infer Frobenius orbit degrees.
    F=GF2(p);d=F.embed(-1-lam);e=F.embed(lam+2)
    w=F.sqrt(d);s=F.sqrt(e)
    assert w is not None and s is not None
    lines=[]
    for sign1 in [1,-1]:
        for sign2 in [1,-1]:
            lines.append(('A',F.embed(1),F.embed(sign1),F.embed(sign2)))
    for distinguished in range(3):
        for s1 in [1,-1]:
            for s2 in [1,-1]:
                v=[F.embed(s1),F.embed(s2)]
                v.insert(distinguished,w)
                lines.append(('C',*v))
    ratios=[]
    for z in [w,F.neg(w)]:
        for sign in [1,-1]:
            t=F.div(F.add(F.one,z),s)
            ratios.append(t if sign==1 else F.neg(t))
    for distinguished in range(3):
        for t in ratios:
            v=[F.one,t];v.insert(distinguished,F.z)
            lines.append(('B',*v))
    assert len(lines)==28
    def normalize(v):
        for x in v:
            if x!=F.z:
                return tuple(F.div(a,x) for a in v)
    assert len(set(normalize(l[1:]) for l in lines))==28
    counts=Counter()
    for typ,a,b,c in lines:
        rational=all(v[1]==0 for v in normalize((a,b,c)))
        if typ=='A':delta=F.embed(-3)
        elif typ=='C':delta=F.embed(3-lam)
        else:
            t=next(v for v in (a,b,c) if v!=F.z and v!=F.one) if False else None
            # whichever coordinate vanishes, the other two have ratio in K
            nonzero=[v for v in (a,b,c) if v!=F.z]
            # these are [1,t], up to order
            t=nonzero[1]
            delta=F.mul(F.embed(-2*lam),F.add(F.one,F.sq(t)))
        if delta==F.z:
            counts[1 if rational else 2]+=1 if rational else .5
            continue
        if rational:
            if delta[1]==0 and chi(delta[0],p)==1:counts[1]+=2
            elif F.is_sq(delta):counts[2]+=1
            else:raise AssertionError('a rational line quadratic must split over quadratic field')
        else:
            if F.is_sq(delta):counts[2]+=1 # two contacts per degree-two line, aggregated over pair
            else:counts[4]+=.5 # two contacts per degree-two line, aggregated over pair
    counts={int(k):int(v) for k,v in counts.items() if v}
    return counts

def main():
    seen4=[]
    for p in [5,7,11,13,17,19,23,29]:
        counts4=0
        for lam in range(p):
            if lam in {2,p-2,p-1}:continue
            got=ground_contacts(p,lam)
            exp=model_rational(p,lam)
            assert (got['lines'],got['rational_support'],got['degree2_support'],got['hyperflex'])==exp,(p,lam,got,exp)
            gc=geometric_contact_cycles(p,lam)
            assert gc.get(1,0)==got['rational_support'],(p,lam,gc,got)
            assert sum(k*v for k,v in gc.items())==(44 if lam in {0,3} else 56),(p,lam,gc)
            d=chi(-1-lam,p);e=chi(lam+2,p)
            expected4=6 if d==-1 and e==-1 and lam!=0 else 0
            assert gc.get(4,0)==expected4,(p,lam,gc,expected4)
            counts4+=bool(expected4)
        predicted=(p-chi(-1,p))//4 - (1 if p%8==3 else 0)
        assert counts4==predicted,(p,counts4,predicted)
        seen4.append((p,counts4))
    print('CIANI_CONTACT_SUPPORT_FROBENIUS_VERIFIED',seen4)
if __name__=='__main__':main()
