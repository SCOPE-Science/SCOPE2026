#!/usr/bin/env python3
from itertools import product

class Field:
    def __init__(self, q):
        self.q=q
        if q in (2,3):
            self.add=lambda a,b:(a+b)%q
            self.mul=lambda a,b:(a*b)%q
            self.neg=lambda a:(-a)%q
            self.one=1
        elif q==4:
            # GF(4)=F2[w]/(w^2+w+1), bit encoding a0+a1*w
            self.add=lambda a,b:a^b
            def mul(a,b):
                a0,a1=a&1,(a>>1)&1
                b0,b1=b&1,(b>>1)&1
                c0=(a0*b0) ^ (a1*b1)       # w^2=w+1
                c1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
                return c0 | (c1<<1)
            self.mul=mul
            self.neg=lambda a:a
            self.one=1
        else:
            raise ValueError(q)
        self.zero=0
        self.elems=tuple(range(q))
    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a); n//=2
        return r
    def inv(self,a):
        assert a
        for b in self.elems[1:]:
            if self.mul(a,b)==1:return b
        raise AssertionError


def vadd(F,u,v): return tuple(F.add(a,b) for a,b in zip(u,v))
def smul(F,a,u): return tuple(F.mul(a,x) for x in u)
def vmul(F,u,v):
    u0,u1,u2=u; v0,v1,v2=v
    return (F.mul(u0,v0),
            F.add(F.mul(u0,v1),F.mul(u1,v0)),
            F.add(F.add(F.mul(u0,v2),F.mul(u1,v1)),F.mul(u2,v0)))

def apply(F, cols, u):
    out=(0,0,0)
    for a,c in zip(u,cols):
        out=vadd(F,out,smul(F,a,c))
    return out

def is_rb(F,cols):
    basis=((1,0,0),(0,1,0),(0,0,1))
    for x in basis:
        for y in basis:
            px,py=apply(F,cols,x),apply(F,cols,y)
            lhs=vmul(F,px,py)
            rhs=apply(F,cols,vadd(F,vmul(F,px,y),vmul(F,x,py)))
            if lhs!=rhs:return False
    return True

def exhaustive(F):
    sols=[]
    for flat in product(F.elems, repeat=9):
        cols=(flat[0:3],flat[3:6],flat[6:9])
        if is_rb(F,cols): sols.append(cols)
    return sols

def predicted_char2(F):
    return {((0,0,a),(0,0,b),(0,0,0)) for a in F.elems for b in F.elems}

def rank_small(F,cols):
    # span size / q determines rank; tiny exact enumeration.
    imgs=set()
    for x in product(F.elems, repeat=3): imgs.add(apply(F,cols,x))
    n=len(imgs); r=0
    while n>1: n//=F.q; r+=1
    assert F.q**r==len(imgs)
    return r

def phi_apply(F,u,v,x):
    # t -> u t + v t^2
    a0,a1,a2=x
    return (a0, F.mul(a1,u), F.add(F.mul(a1,v), F.mul(a2,F.mul(u,u))))

def phi_inv_apply_char2(F,u,v,x):
    ui=F.inv(u)
    beta=F.mul(v,F.pow(ui,3)) # minus equals plus in characteristic 2
    a0,a1,a2=x
    return (a0, F.mul(a1,ui), F.add(F.mul(a1,beta),F.mul(a2,F.pow(ui,2))))

def conjugate_char2(F,cols,u,v):
    basis=((1,0,0),(0,1,0),(0,0,1))
    out=[]
    for x in basis:
        y=phi_inv_apply_char2(F,u,v,x)
        z=apply(F,cols,y)
        out.append(phi_apply(F,u,v,z))
    return tuple(out)

def orbit_checks(F):
    pred=predicted_char2(F)
    autos=[(u,v) for u in F.elems if u for v in F.elems]
    unseen=set(pred); orbits=[]
    while unseen:
        p=next(iter(unseen))
        orb={conjugate_char2(F,p,u,v) for u,v in autos}
        assert orb <= pred
        unseen-=orb; orbits.append(orb)
    sizes=sorted(map(len,orbits))
    assert len(orbits)==F.q+2, (F.q,len(orbits),sizes)
    assert sizes==[1]+[F.q-1]*(F.q+1), sizes
    # verify invariant/classifier on mixed locus.
    invvals=set()
    for a in F.elems:
        for b in F.elems:
            if a and b:
                rho=F.mul(a,F.pow(F.inv(b),2))
                invvals.add(rho)
                base=((0,0,a),(0,0,b),(0,0,0))
                for u,v in autos:
                    qcols=conjugate_char2(F,base,u,v)
                    aa=qcols[0][2]; bb=qcols[1][2]
                    rho2=F.mul(aa,F.pow(F.inv(bb),2))
                    assert rho2==rho
    assert len(invvals)==F.q-1
    return sizes

def odd_prediction(F):
    # For q=3 only: P(1)=a1*t+a2*t^2, P(t)=b*t^2, P(t^2)=0,
    # with a1=0 or a1=2b.
    two=F.add(1,1)
    return {((0,a1,a2),(0,0,b),(0,0,0))
            for a1 in F.elems for a2 in F.elems for b in F.elems
            if a1==0 or a1==F.mul(two,b)}

def main():
    for q in (2,3,4):
        F=Field(q)
        sols=set(exhaustive(F))
        if q in (2,4):
            pred=predicted_char2(F)
            assert sols==pred, (q,len(sols),len(pred),len(sols^pred))
            ranks={r:0 for r in range(4)}
            for p in sols:ranks[rank_small(F,p)]+=1
            assert ranks[0]==1 and ranks[1]==q*q-1 and ranks[2]==ranks[3]==0, ranks
            sizes=orbit_checks(F)
            print(f"GF({q}) exhaustive_RB={len(sols)} ranks={ranks} orbits={len(sizes)} sizes={sizes}")
        else:
            pred=odd_prediction(F)
            assert sols==pred, (q,len(sols),len(pred),len(sols^pred))
            print(f"GF({q}) contrast_exhaustive_RB={len(sols)} expected={2*q*q-q}")
    print("VERIFY_OK")
if __name__=='__main__': main()
