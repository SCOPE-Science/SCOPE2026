#!/usr/bin/env python3
"""Independent finite-field original-identity and automorphism-orbit checks.
Only Python stdlib is needed; no external source or dataset is loaded.
"""
from collections import Counter, defaultdict
from itertools import product
from math import prod
from fractions import Fraction


def field(q):
    if q == 4:
        # F_4=F_2[u]/(u^2+u+1), binary polynomial encoding.
        def mul(a,b):
            r = 0
            while b:
                if b & 1: r ^= a
                b >>= 1
                a <<= 1
                if a & 4: a ^= 7
            return r
        return 2, lambda a,b:a^b, mul
    return q, lambda a,b:(a+b)%q, lambda a,b:(a*b)%q


def operations(q,m):
    p,add,mul = field(q)
    sub = lambda a,b: add(a,b) if p==2 else (a-b)%p
    zero = lambda: tuple(tuple(0 for _ in range(m)) for _ in range(m))
    def mm(A,B):
        return tuple(tuple(sum_field((mul(A[i][k], B[k][j]) for k in range(m))) for j in range(m)) for i in range(m))
    def sum_field(vals):
        t=0
        for x in vals: t=add(t,x)
        return t
    def mv(A,v):
        return tuple(sum_field(mul(A[i][j],v[j]) for j in range(m)) for i in range(m))
    def madd(a,b): return tuple(add(x,y) for x,y in zip(a,b))
    def mneg(v): return tuple(sub(0,x) for x in v)
    def rank(cols):
        cols = [list(c) for c in cols if any(c)]
        R = 0
        for i in range(m):
            pivot=next((j for j in range(R,len(cols)) if cols[j][i]),None)
            if pivot is None: continue
            cols[R],cols[pivot] = cols[pivot],cols[R]
            a=cols[R][i]
            inv=next(x for x in range(1,q) if mul(x,a)==1)
            cols[R]=[mul(inv,x) for x in cols[R]]
            for j in range(len(cols)):
                if j!=R and cols[j][i]:
                    scale=cols[j][i]
                    cols[j]=[sub(cols[j][k],mul(scale,cols[R][k])) for k in range(m)]
            R+=1
            if R==len(cols):break
        return R
    def columns(T):return [tuple(T[i][j] for i in range(m)) for j in range(m)]
    def is_derivation(T,w):
        # Original multiplication of the Kronecker path algebra A=ke+ kf+V.
        d=m+2
        def vplus(a,b):return tuple(add(x,y) for x,y in zip(a,b))
        def smul(c,a):return tuple(mul(c,x) for x in a)
        z=(0,)*d
        basis=[tuple(int(i==j) for i in range(d)) for j in range(d)]
        def product(a,b):
            v=[0]*d
            v[0]=mul(a[0],b[0]); v[1]=mul(a[1],b[1])
            for i in range(m):v[i+2]=add(mul(a[0],b[i+2]),mul(a[i+2],b[1]))
            return tuple(v)
        D=[(0,0)+w,(0,0)+mneg(w)]
        D += [(0,0)+tuple(T[i][j] for i in range(m)) for j in range(m)]
        def act(v):
            t=z
            for j in range(d):t=vplus(t,smul(v[j],D[j]))
            return t
        for x in basis:
            for y in basis:
                if act(product(x,y))!=vplus(product(act(x),y),product(x,act(y))):return False
        return True
    def is_pnilpotent_on_full_algebra(T,w):
        v1=w
        for i in range(p-1):v1=mv(T,v1)
        M=T
        for i in range(p-1):M=mm(M,T)
        return not any(v1) and M==zero()
    return mm,mv,madd,rank,columns,is_derivation,is_pnilpotent_on_full_algebra


def partitions(n,maxpart):
    def rec(s,hi):
        if not s:
            yield ()
        else:
            for a in range(min(s,hi),0,-1):
                for tail in rec(s-a,a):yield (a,)+tail
    return list(rec(n,maxpart))


def gl_order(m,q):return prod(q**m-q**i for i in range(m))

def type_count(lam,q):
    m=sum(lam); freq=Counter(lam)
    E=sum(sum(1 for z in lam if z>=j)**2 for j in range(1,max(lam)+1))
    C=Fraction(q**E)
    for n in freq.values():
        for h in range(1,n+1):C*=Fraction(q**h-1,q**h)
    assert C.denominator==1, (lam,C)
    return gl_order(m,q)//int(C)


def expected(m,q):
    p,_,_=field(q); out=Counter(); orbit_sizes=[]
    for lam in partitions(m,p):
        r=m-len(lam); b=lam.count(p); t=type_count(lam,q)
        out[r]+=t*q**r
        out[r+1]+=t*(q**(m-b)-q**r)
        orbit_sizes.append((lam,0,t*q**r,r))
        freq=Counter(lam); c=0
        for j in range(1,p):
            if freq[j]:
                d=c+freq[j]
                orbit_sizes.append((lam,j,t*q**r*(q**d-q**c),r+1))
                c=d
    return out,orbit_sizes


def actual(q,m,verify_aut=False):
    p,add,mul=field(q)
    mm,mv,madd,rank,cols,is_derivation,powercheck=operations(q,m)
    allvals=range(q); z=(0,)*m
    I=tuple(tuple(int(i==j) for j in range(m)) for i in range(m))
    valid=[]; ranks=Counter()
    for flat in product(allvals,repeat=m*m):
        T=tuple(flat[i*m:(i+1)*m] for i in range(m))
        P=T
        for j in range(p-1):P=mm(P,T)
        if any(any(c) for c in P):continue
        for w in product(allvals,repeat=m):
            v=w
            for j in range(p-1):v=mv(T,v)
            if any(v):continue
            assert is_derivation(T,w)
            assert powercheck(T,w)
            rr=rank(cols(T)+[w]);ranks[rr]+=1
            valid.append((T,w))
    group_orbits=None
    if verify_aut:
        # Orbits under every actual automorphism F_{G,u}: e->e+u, f->f-u, v->Gv.
        matrices=[]
        for flat in product(allvals,repeat=m*m):
            G=tuple(flat[i*m:(i+1)*m] for i in range(m))
            if rank(cols(G))==m:matrices.append(G)
        us=list(product(allvals,repeat=m))
        group_orbits=[]; unseen=set(valid)
        while unseen:
            T,w=next(iter(unseen))
            orb=set()
            for G in matrices:
                # use G T G^-1 instead of inverse, identical group parameter range.
                # Find inverse by linear solver via brute small m.
                Tprimecols=[mv(G,c) for c in cols(T)]
                # G T = T' G; evaluate T' via basis images through inverse of G.
                inversecols=[]
                for ei in cols(I):
                    vec=next(v for v in product(allvals,repeat=m) if mv(G,v)==ei)
                    inversecols.append(vec)
                Tprimecols=[mv(G,mv(T,c)) for c in inversecols]
                Tprime=tuple(tuple(Tprimecols[j][i] for j in range(m)) for i in range(m))
                Gw=mv(G,w)
                for u in us:
                    wp=madd(Gw,mv(Tprime,u))
                    orb.add((Tprime,wp))
            assert orb<=set(valid)
            unseen-=orb
            group_orbits.append(len(orb))
    return ranks,group_orbits,len(valid)


def run():
    configs=[(2,2,True),(2,3,True),(2,4,False),(3,2,True),(4,2,True)]
    for q,m,orb in configs:
        prediction,by_type=expected(m,q)
        counted,orbits,total=actual(q,m,orb)
        assert counted==prediction,(q,m,counted,prediction)
        if orbits is not None:
            assert sorted(orbits)==sorted(t[2] for t in by_type),(q,m,orbits,by_type)
        print(f'FIELD_{q}_ARROWS_{m}: ranks={dict(sorted(counted.items()))}; total={total}; '
              f'aut_orbits={sorted(orbits) if orbits is not None else "not_enumerated"}; PASS')
    # A separate rational-generating-function identity check for m<=16, p=2,3,5.
    for p in (2,3,5):
        for m in range(17):
            # m=0 is excluded as a path-algebra family but included in formal GF.
            orbit_count=sum(1+len({a for a in lam if a<p}) for lam in partitions(m,p))
            # coefficient of 1/[(1-z)^2 prod_{j=2}^{p-1}(1-z^j)]
            seq=[0]*(m+1);seq[0]=1
            for j in [1,1]+list(range(2,p)):
                for h in range(j,m+1):seq[h]+=seq[h-j]
            assert orbit_count==seq[m]
    print('ALL_DIRECT_MULTIPLICATION_AND_AUTOMORPHISM_ORBITS_OK')

if __name__=='__main__':run()
