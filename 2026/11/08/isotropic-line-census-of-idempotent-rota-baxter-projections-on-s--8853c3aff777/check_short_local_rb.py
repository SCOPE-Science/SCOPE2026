#!/usr/bin/env python3
"""Finite-field verification of idempotent weight-minus-one Rota--Baxter projections.
All calculations use algebra multiplication, not the proposed closed formula.
"""
from collections import Counter
from itertools import product

class Field:
    def __init__(self,q):
        self.q=q
        assert q in (2,3,4,5)
        self.char=2 if q==4 else q
    def add(self,a,b):return a^b if self.char==2 else (a+b)%self.q
    def neg(self,a):return a if self.char==2 else (-a)%self.q
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4: return a*b%self.q
        raw=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1:raw^=1<<(i+j)
        if raw&8:raw^=0b1110
        if raw&4:raw^=0b111
        return raw
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)

def dot(F,v,w):
    r=0
    for a,b in zip(v,w):r=F.add(r,F.mul(a,b))
    return r

def span(F,basis):
    if not basis:return frozenset({(0,0,0)})
    out=set()
    for coeffs in product(range(F.q),repeat=len(basis)):
        out.add(tuple(sum_field(F,[F.mul(c,v[i]) for c,v in zip(coeffs,basis)]) for i in range(3)))
    return frozenset(out)

def sum_field(F,it):
    x=0
    for a in it:x=F.add(x,a)
    return x

def subs(F):
    vec=list(product(range(F.q),repeat=3));zero=(0,0,0)
    d={frozenset({zero}):()}
    for v in vec:
        if v!=zero:
            s=span(F,[v]);d.setdefault(s,(v,))
    for i,v in enumerate(vec):
        if v==zero:continue
        for w in vec[i+1:]:
            s=span(F,[v,w])
            if len(s)==F.q*F.q:d.setdefault(s,(v,w))
    d.setdefault(frozenset(vec),((1,0,0),(0,1,0),(0,0,1)))
    assert len(d)==2*(F.q*F.q+F.q+1)+2
    return d

def multiply(F,B,a,b):
    # Coordinates 0,1,2 of radical, the last is the central square element.
    z=0
    for i in range(2):
        for j in range(2):z=F.add(z,F.mul(B[i][j],F.mul(a[i],b[j])))
    return (0,0,z)

def closed(F,B,basis,space):
    return all(multiply(F,B,a,b) in space for a in basis for b in basis)

def rb_count_direct(F,B):
    ss=subs(F);cs={s:b for s,b in ss.items() if closed(F,B,b,s)}
    z=(0,0,0);m=frozenset(product(range(F.q),repeat=3))
    ans=Counter();examples=[]
    for U in cs:
        for C in cs:
            if len(U)*len(C)!=len(m):continue
            if U.intersection(C)!=frozenset({z}):continue
            decomp={tuple(F.add(x,y) for x,y in zip(u,c)):(u,c) for u in U for c in C}
            assert len(decomp)==len(m)
            # Two orientations, choosing either unital side or radical side as image.
            for orient in range(2):
                P=[]
                for vec in ((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)):
                    u,c=decomp[vec[1:]]
                    P.append((vec[0],)+u if orient==0 else (0,)+c)
                for a in range(4):
                    for b in range(4):
                        lhs=prod4(F,B,P[a],P[b]);rhs=apply(F,P,tuple(F.sub(F.add(x,y),z) for x,y,z in zip(prod4(F,B,P[a],unit(b)),prod4(F,B,unit(a),P[b]),unitprod(a,b,F,B))))
                        assert lhs==rhs,(F.q,B,orient,U,C,a,b,lhs,rhs)
                k=0;x=len(U)
                while x>1:x//=F.q;k+=1
                j=0;x=len(C)
                while x>1:x//=F.q;j+=1
                ans[k+1 if orient==0 else j]+=1
                examples.append(tuple(P))
    assert len(examples)==len(set(examples)), 'duplicate projection'
    return ans

def unit(i):return tuple(int(i==j) for j in range(4))
def unitprod(i,j,F,B):return prod4(F,B,unit(i),unit(j))
def prod4(F,B,a,b):
    r=[F.mul(a[0],b[0]),0,0,0]
    for i in range(1,4):r[i]=F.add(F.mul(a[0],b[i]),F.mul(b[0],a[i]))
    r[3]=F.add(r[3],multiply(F,B,a[1:],b[1:])[2]);return tuple(r)
def apply(F,P,v):
    return tuple(sum_field(F,[F.mul(v[j],P[j][i]) for j in range(4)]) for i in range(4))

def brute_all_binary(B):
    F=Field(2);ctr=Counter()
    for coeff in product(range(2),repeat=16):
        P=[coeff[4*i:4*i+4] for i in range(4)]
        if any(apply(F,P,P[i])!=P[i] for i in range(4)):continue
        ok=True
        for i in range(4):
            for j in range(4):
                lhs=prod4(F,B,P[i],P[j]); x=prod4(F,B,P[i],unit(j)); y=prod4(F,B,unit(i),P[j]); z=unitprod(i,j,F,B)
                rhs=apply(F,P,tuple(F.sub(F.add(x[h],y[h]),z[h]) for h in range(4)))
                if lhs!=rhs:ok=False;break
            if not ok:break
        if ok:
            rank=sum(1 for v in distinct_span4(F,P)) # log_2 size
            r=0
            while rank>1:rank//=2;r+=1
            ctr[r]+=1
    return ctr

def distinct_span4(F,P):
    return set(tuple(sum_field(F,[F.mul(c,v[i]) for c,v in zip(cs,P)]) for i in range(4)) for cs in product(range(F.q),repeat=4))

def isotropic(F,B):
    points=set()
    for a,b in product(range(F.q),repeat=2):
        if not(a or b):continue
        v=(a,b,0);qf=multiply(F,B,v,v)[2]
        if qf!=0:continue
        if a:rep=(1,F.mul(b,F.inv(a)))
        else:rep=(0,1)
        points.add(rep)
    return len(points)

if __name__=='__main__':
    for q in (2,3,4,5):
        F=Field(q)
        cases={'alternating':((0,1),(1,0)),'rank_one':((1,0),(0,0)), 'diagonal':((1,0),(0,1))}
        for name,B in cases.items():
            B=tuple(tuple(row) for row in B)
            h=isotropic(F,B)
            actual=rb_count_direct(F,B)
            n=h*q*q
            predicted=Counter({0:1,1:1+n,2:2*n,3:1+n,4:1})
            assert actual==predicted,(q,name,h,actual,predicted)
            print(f'q={q} B={name:<11} isotropic_directions={h:>2} rank_counts={[actual[r] for r in range(5)]} total={sum(actual.values())} PASS')
            if q==2:
                brute=brute_all_binary(B)
                assert brute==actual,(q,name,brute,actual)
                print(f'  exhaustive check of all 65536 binary linear endomorphisms: {dict(sorted(brute.items()))} PASS')
    print('ALL_SHORT_LOCAL_RB_COUNTS_PASS')
