#!/usr/bin/env python3
"""Finite-field verification of square-zero commuting pairs in J_4.
Independent direct six-coordinate enumeration and upper-triangular conjugacy orbits.
Python 3 standard library only. No external data.
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
        self.elements=range(q)
        if q==4:
            self.add=lambda x,y:x^y
            # F4=F2[z]/(z^2+z+1), bit 1 is constant and bit 2 is z.
            def mul(x,y):
                p=0
                for i in range(2):
                    for j in range(2):
                        if (x>>i)&1 and (y>>j)&1: p^=1<<(i+j)
                if p&4:p^=7  # z^2=z+1, so z^2+z+1=0
                return p
            self.mul=mul
            self.neg=lambda x:x
            self.primitive=2
        else:
            self.add=lambda x,y:(x+y)%q
            self.mul=lambda x,y:(x*y)%q
            self.neg=lambda x:(-x)%q
            self.primitive=2 if q in (3,5) else 1
    def sub(self,x,y):return self.add(x,self.neg(y))
    def inv(self,x):
        assert x
        return next(y for y in self.elements if self.mul(x,y)==1)

def scalar_checks(q):
    F=Field(q);a=F.add;m=F.mul;sub=F.sub
    sq=[]
    for x in product(F.elements,repeat=6):
        aa,b,c,d,e,f=x
        if m(aa,b) or m(b,c) or a(m(aa,e),m(d,c)):continue
        sq.append(x)
    hist=Counter()
    for x in sq:
        aa,b,c,d,e,f=x
        for y in sq:
            A,B,C,D,E,F_=y
            if sub(m(aa,B),m(A,b)) or sub(m(b,C),m(B,c)):
                continue
            if sub(a(m(aa,E),m(d,C)),a(m(A,e),m(D,c))):
                continue
            xy=a(m(aa,E),m(d,C))
            assert a(m(aa,B),0)==0 and m(b,C)==0, 'Noncentral product'
            hist[xy]+=1
    total=q**8+2*q**7-2*q**5
    each=q**3*(q-1)*(q*q-1)
    predicted={0:total-(q-1)*each}
    predicted.update({v:each for v in range(1,q)})
    assert hist==predicted,(q,hist,predicted)
    assert sum(hist.values())==total
    print(f'F_{q}: squarezero={len(sq)}, product_fibers={dict(sorted(hist.items()))}, PASS')
    return hist

def ident(F):return tuple(1 if i==j else 0 for i in range(4) for j in range(4))
def mat(F,entries):return tuple(entries.get((i,j),0) for i in range(4) for j in range(4))
def mm(F,A,B):
    a=F.add;m=F.mul
    return tuple(a(a(m(A[4*i],B[j]),m(A[4*i+1],B[4+j])),a(m(A[4*i+2],B[8+j]),m(A[4*i+3],B[12+j]))) for i in range(4) for j in range(4))
def mi(F,M):
    a=F.add;m=F.mul
    Z=[[M[4*i+j] for j in range(4)]+[int(i==j) for j in range(4)] for i in range(4)]
    for j in range(4):
        k=next(i for i in range(j,4) if Z[i][j]);Z[j],Z[k]=Z[k],Z[j]
        t=F.inv(Z[j][j]);Z[j]=[m(t,v) for v in Z[j]]
        for i in range(4):
            if i!=j and Z[i][j]:
                t=Z[i][j];Z[i]=[F.sub(x,m(t,y)) for x,y in zip(Z[i],Z[j])]
    return tuple(Z[i][4+j] for i in range(4) for j in range(4))
def orbit_checks(q):
    F=Field(q);I=ident(F)
    # s on basis (st,s,t,1): e_{13}+e_{24}
    # t on basis (st,s,t,1): e_{12}+e_{34}
    S=mat(F,{(0,2):1,(1,3):1})
    T=mat(F,{(0,1):1,(2,3):1})
    gs=[]
    for i in range(3):gs.append(mat(F,{**{(j,j):1 for j in range(4)},(i,i+1):1}))
    for i in range(4):gs.append(mat(F,{(j,j):(F.primitive if i==j else 1) for j in range(4)}))
    gg=[(g,mi(F,g)) for g in gs]
    used=set();orbit_sizes=[]
    # one adapted basis for each line in span(s,t)
    for w in F.elements:
        # columns of P: (st, s+w t, t, 1)
        P=mat(F,{(0,0):1,(1,1):1,(2,1):w,(2,2):1,(3,3):1})
        Pinv=mi(F,P)
        x=mm(F,Pinv,mm(F,S,P));y=mm(F,Pinv,mm(F,T,P))
        start=(x,y);assert start not in used
        orb={start};queue=[start]
        for xx,yy in queue:
            for g,gi in gg:
                z=(mm(F,g,mm(F,xx,gi)),mm(F,g,mm(F,yy,gi)))
                if z not in orb:orb.add(z);queue.append(z)
        assert not (used&orb)
        used|=orb;orbit_sizes.append(len(orb))
    # line infinity: (st,t,s,1)
    P=mat(F,{(0,0):1,(2,1):1,(1,2):1,(3,3):1})
    Pinv=mi(F,P)
    start=(mm(F,Pinv,mm(F,S,P)),mm(F,Pinv,mm(F,T,P)))
    assert start not in used
    orb={start};queue=[start]
    for xx,yy in queue:
        for g,gi in gg:
            z=(mm(F,g,mm(F,xx,gi)),mm(F,g,mm(F,yy,gi)))
            if z not in orb:orb.add(z);queue.append(z)
    assert not (used&orb)
    used|=orb;orbit_sizes.append(len(orb))
    size=q**3*(q-1)**3
    assert sorted(orbit_sizes)==[size]*(q+1)
    assert len(used)==q**3*(q-1)**2*(q*q-1)
    print(f'F_{q}: Borel_orbits={q+1}, sizes={orbit_sizes}, PASS')

if __name__=='__main__':
    for q in (2,3,4,5):scalar_checks(q)
    for q in (2,3,4):orbit_checks(q)
    print('ALL_J4_RESTRICTED_PRODUCT_FIBERS_AND_BOREL_ORBITS_PASS')
