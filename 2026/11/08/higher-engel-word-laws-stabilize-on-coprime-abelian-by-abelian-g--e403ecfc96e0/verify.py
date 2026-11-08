#!/usr/bin/env python3
"""Exact finite checks for the Engel word distribution of coprime abelian semidirect products."""
from collections import Counter
from itertools import product
from fractions import Fraction
from math import gcd, tau
from cmath import exp

CASES = [
    ('S3', (3,), (2,), ((2,),)),
    ('AGL1_5', (5,), (4,), ((2,),)),
    ('C7_C3', (7,), (3,), ((2,),)),
    ('nonfree_7sq_6', (7,7), (2,3), ((6,1),(1,2))),
    ('nonfree_3sq_4', (3,3), (2,2), ((2,1),(1,2))),
    ('nonfree_5x7_6', (5,7), (2,3), ((4,1),(1,2))),
    ('C9_C2', (9,), (2,), ((8,),)),
    ('nonfree_7sq_3', (7,7), (3,), ((2,1),)),
    ('A4_nondiagonal', (2,2), (3,), ((1,1),)),
    ('nonfaithful_C3_C4', (3,), (4,), ((2,),)),
]

class Semi:
    def __init__(self, amods, hmods, generators):
        self.amods, self.hmods, self.gen = amods, hmods, generators
        self.A=list(product(*[range(t) for t in amods])); self.H=list(product(*[range(t) for t in hmods]))
        self.za=(0,)*len(amods); self.zh=(0,)*len(hmods)
        for order,units in zip(hmods,generators):
            for m,u in zip(amods,units):
                assert gcd(u,m)==1 and pow(u,order,m)==1
        self.units={h:tuple(self._factor(h,i) for i in range(len(amods))) for h in self.H}
        self.G=[(a,h) for a in self.A for h in self.H]
        self.one=(self.za,self.zh)
    def _factor(self,h,i):
        m=self.amods[i]; out=1
        for e,us in zip(h,self.gen):out=(out*pow(us[i],e,m))%m
        return out
    def add(self,a,b):return tuple((x+y)%m for x,y,m in zip(a,b,self.amods))
    def neg(self,a):return tuple(-x % m for x,m in zip(a,self.amods))
    def act(self,h,a):return tuple((u*x)%m for u,x,m in zip(self.units[h],a,self.amods))
    def hplus(self,u,v):return tuple((x+y)%m for x,y,m in zip(u,v,self.hmods))
    def hneg(self,u):return tuple((-x)%m for x,m in zip(u,self.hmods))
    def mul(self,x,y):
        a,u=x;b,v=y
        return self.add(a,self.act(u,b)),self.hplus(u,v)
    def inv(self,x):
        a,u=x;v=self.hneg(u)
        return self.neg(self.act(v,a)),v
    def comm(self,x,y):return self.mul(self.mul(self.mul(self.inv(x),self.inv(y)),x),y)
    def word(self,x,y,k):
        z=x
        for _ in range(k):z=self.comm(z,y)
        return z
    def B(self,v):return set(self.add(self.act(v,a),self.neg(a)) for a in self.A)
    def C(self,v):return {a for a in self.A if self.act(v,a)==a}
    def hfixed_character(self,v,chi):
        # v fixes a character iff the character vanishes on all (v-1)A.
        return all(sum(Fraction(c*b,m) for c,b,m in zip(chi,a,self.amods)).denominator==1 for a in self.B(v))


class A4Semidirect(Semi):
    # A4 = (C2)^2 ⋊ C3, with the non-diagonal order-three linear action.
    def act(self,h,a):
        for _ in range(h[0]):
            a=(a[1],(a[0]+a[1])%2)
        return a

def verify_case(label,amods,hmods,gens):
    S=(A4Semidirect if label=='A4_nondiagonal' else Semi)(amods,hmods,gens)
    na,nh=len(S.A),len(S.H)
    assert gcd(na,nh)==1
    B={v:S.B(v) for v in S.H}
    C={v:S.C(v) for v in S.H}
    assert all(len(B[v])*len(C[v])==na for v in S.H)
    expected={a:Fraction(na*na*nh)*sum((Fraction(1,len(B[v])) for v in S.H if a in B[v]),Fraction(0)) for a in S.A}
    assert all(q.denominator==1 for q in expected.values())
    total=na*na*nh*nh
    assert sum(expected.values())==total
    stats=[]
    prev=None
    for k in (2,3,4):
        counts=Counter()
        for x in S.G:
            for y in S.G:
                z=S.word(x,y,k)
                assert z[1]==S.zh
                counts[z[0]]+=1
        assert all(counts[a]==expected[a] for a in S.A),(label,k)
        if prev is not None:assert counts==prev
        prev=counts
        stats.append((k,counts[S.za]))
    # Stronger fiber check: for every (u,b,v), varying 'a' exactly uniformly covers B_v.
    fiberchecks=0
    for v in S.H:
        # Compute the unique coprime decomposition and inverse of (v-1) on its image.
        bpart={S.add(c,z):z for c in C[v] for z in B[v]}
        tinv={S.add(S.act(v,t),S.neg(t)):t for t in B[v]}
        assert len(bpart)==na and len(tinv)==len(B[v])
        for b in S.A:
            y=(b,v)
            E={x for x in S.G if S.word(x,y,2)==S.one}
            assert len(E)==nh*len(C[v]),(label,v,b,len(E))
            t=tinv[bpart[b]]
            predictedE={(S.add(c,S.add(S.act(u,t),S.neg(t))),u) for c in C[v] for u in S.H}
            assert E==predictedE,(label,v,b,'wrong conjugate Engelizer')
            for u in S.H:
                c=Counter(S.word((a,u),y,2)[0] for a in S.A)
                assert set(c)==B[v]
                assert set(c.values())=={na//len(B[v])}
                fiberchecks+=1
            # exact subgroup check on small group or first b in larger cases
            if na*nh<=40 or b==S.za:
                assert all(S.inv(x) in E for x in E)
                assert all(S.mul(x,y1) in E for x in E for y1 in E)
    # Fourier transform from the independently counted word-value distribution.
    for chi in S.A:
        lhs=sum(prev[a]*exp(tau*1j*sum(c*z/m for c,z,m in zip(chi,a,S.amods))) for a in S.A)/total
        rhs=Fraction(sum(S.hfixed_character(v,chi) for v in S.H),nh)
        assert abs(lhs-float(rhs))<1e-10,(label,chi,lhs,rhs)
    orbit_count=Fraction(sum(len(C[v]) for v in S.H),nh)
    assert orbit_count.denominator==1
    assert Fraction(expected[S.za],total)==orbit_count/na
    lower=Fraction(na+nh-1,na*nh)
    assert orbit_count/na>=lower
    if orbit_count/na==lower:assert all(len(C[v])==1 for v in S.H if v!=S.zh)
    else:assert any(len(C[v])>1 for v in S.H if v!=S.zh)
    print('%s: |G|=%d |H|=%d p_Engel=%s nonzero_support=%d fiberchecks=%d exact k=2,3,4: PASS' %
         (label,na*nh,nh,str(orbit_count/na),sum(bool(expected[x]) for x in S.A)-1,fiberchecks))
    return na*nh, fiberchecks

def noncoprime():
    # D_16: C_8 acted on by inversion from C_2. 2-Engel and 3-Engel laws differ.
    S=Semi((8,),(2,),((7,),))
    x2=sum(S.word(x,y,2)==S.one for x in S.G for y in S.G)
    x3=sum(S.word(x,y,3)==S.one for x in S.G for y in S.G)
    assert x2==192 and x3==256
    print('noncoprime_D16: k=2 density=3/4, k=3 density=1: PASS')

if __name__=='__main__':
    total=0;fs=0
    for case in CASES:
        n,f=verify_case(*case);total+=n*n*3;fs+=f
    noncoprime()
    print('VERIFY_OK cases=10 direct_word_evaluations=%d conditional_fibers=%d' %(total,fs))
