#!/usr/bin/env python3
"""Exact, dependency-free orbit and contact-order census for smooth binary plane quartics."""
from collections import defaultdict
from itertools import product

MON = [(a,b,4-a-b) for a in range(5) for b in range(5-a)]
INDEX = {e:i for i,e in enumerate(MON)}
assert len(MON) == 15

def pmul(a,b):
    out=set()
    for u in a:
        for v in b:
            w=tuple(u[i]+v[i] for i in range(3))
            if w in out: out.remove(w)
            else: out.add(w)
    return out

def substitution(M):
    linear=[{tuple(int(j==k) for j in range(3)) for k in range(3) if M[i][k]} for i in range(3)]
    powers=[[{(0,0,0)}] for i in range(3)]
    for i in range(3):
        for e in range(4): powers[i].append(pmul(powers[i][-1],linear[i]))
    table=[]
    for a,b,c in MON:
        p=pmul(pmul(powers[0][a],powers[1][b]),powers[2][c])
        table.append(sum(1<<INDEX[v] for v in p))
    return table

GEN=[substitution(m) for m in (
   ((0,1,0),(1,0,0),(0,0,1)),
   ((1,0,0),(0,0,1),(0,1,0)),
   ((1,1,0),(0,1,0),(0,0,1)),
)]

def act(n,table):
    out=0
    while n:
        bit=n&-n
        out^=table[bit.bit_length()-1]
        n-=bit
    return out

def all_orbits():
    seen={0};out=[]
    for start in range(1,1<<15):
        if start in seen: continue
        orb={start};front=[start]
        while front:
            n=front.pop()
            for g in GEN:
                y=act(n,g)
                if y not in orb: orb.add(y);front.append(y)
        seen.update(orb)
        out.append((min(orb),len(orb)))
    assert len(seen)==(1<<15) and sum(k for _,k in out)==(1<<15)-1
    assert all(168%k==0 for _,k in out)
    return out

# Exact Buchberger algorithm for ideals in F_2[u,v]. Unit ideal iff no
# common zero over the algebraic closure. Monomials are (exponent_u, exponent_v).
def shift(poly, by):
    return {(a+by[0],b+by[1]) for a,b in poly}

def reduce(poly,basis):
    rem=set()
    while poly:
        t=max(poly)
        for g in basis:
            m=max(g)
            if t[0]>=m[0] and t[1]>=m[1]:
                poly^=shift(g,(t[0]-m[0],t[1]-m[1]))
                break
        else:
            poly.remove(t);rem.add(t)
    return rem

def unit_ideal(polys):
    bs=[x for x in polys if x]
    if {(0,0)} in bs:return True
    pairs=[(i,j) for i in range(len(bs)) for j in range(i)]
    while pairs:
        i,j=pairs.pop()
        a,b=max(bs[i]),max(bs[j]);L=(max(a[0],b[0]),max(a[1],b[1]))
        r=reduce(shift(bs[i],(L[0]-a[0],L[1]-a[1])) ^
                 shift(bs[j],(L[0]-b[0],L[1]-b[1])),bs)
        if r:
            if r=={(0,0)}:return True
            n=len(bs);pairs.extend((n,j) for j in range(n));bs.append(r)
    return False

def is_smooth(n):
    for fixed in range(3):
        others=[i for i in range(3) if i!=fixed]
        polys=[set() for _ in range(4)]
        for i,e in enumerate(MON):
            if not (n>>i)&1:continue
            term=(e[others[0]],e[others[1]])
            polys[0]^={term}
            for j in range(3):
                if e[j]&1:
                    h=list(e);h[j]-=1
                    polys[j+1]^={(h[others[0]],h[others[1]])}
        if not unit_ideal(polys):return False
    return True

POINTS=[tuple((n>>i)&1 for i in range(3)) for n in range(1,8)]
def value(n,p):
    return sum((n>>i&1)*p[0]**a*p[1]**b*p[2]**c
               for i,(a,b,c) in enumerate(MON))%2

def gradient(n,p):
    answer=[]
    for j in range(3):
        t=0
        for i,e in enumerate(MON):
            if not (n>>i)&1 or not (e[j]&1):continue
            h=list(e);h[j]-=1
            t^=p[0]**h[0]*p[1]**h[1]*p[2]**h[2]
        answer.append(t)
    return tuple(answer)

def contact(n,p,q):
    out=0
    for i,e in enumerate(MON):
        if not (n>>i)&1:continue
        m=1
        for power,P,Q in zip(e,p,q):
            factor=0
            for k in range(power+1):
                # Lucas' theorem: binomial(power,k) odd iff k is submask of power.
                if (k&power)==k and (not power-k or P) and (not k or Q):
                    factor ^= (1<<k)
            t=0
            for bit in range(5):
                if m>>bit&1:t^=factor<<bit
            m=t
        out^=m
    return out

def flex_counts(n):
    ordinary=hyper=0
    for p in POINTS:
        if value(n,p):continue
        L=gradient(n,p)
        assert L!=(0,0,0)
        q=next(q for q in POINTS if q!=p and not sum(x*y for x,y in zip(L,q))%2)
        jets=contact(n,p,q)
        assert jets&3==0, (n,p,q,jets)
        if not jets&(1<<2):
            if jets&(1<<3):ordinary+=1
            else:
                assert jets&(1<<4)
                hyper+=1
    return ordinary,hyper

EXPECTED={
    (0,0):(17,1764),(0,1):(14,1932),(1,0):(13,2184),
    (0,2):(3,420),(1,1):(7,1176),(2,0):(10,1512),
    (0,3):(1,28),(1,2):(2,336),(2,1):(5,672),
    (3,0):(5,728),(4,0):(1,168),
}

def main():
    orbits=all_orbits()
    tally=defaultdict(lambda:[0,0]);high=[];n_smooth=0
    for mask,orbit_size in orbits:
        if is_smooth(mask):
            ordinary,hyper=flex_counts(mask)
            tally[(ordinary,hyper)][0]+=1
            tally[(ordinary,hyper)][1]+=orbit_size
            n_smooth+=orbit_size
            if ordinary+hyper==4:high.append((mask,orbit_size,ordinary,hyper))
    assert n_smooth==10920
    assert {k:tuple(v) for k,v in tally.items()}==EXPECTED,(tally,EXPECTED)
    assert high==[(4418,168,4,0)],high
    print('ALL_ORBITS',len(orbits),'SMOOTH_PROJECTIVE_CLASSES',sum(v[0] for v in tally.values()),'SMOOTH_EQUATIONS',n_smooth)
    for k in sorted(tally):print('CONTACT',k,'CLASSES',tally[k][0],'EQUATIONS',tally[k][1])
    print('UNIQUE_FLEX_MAXIMUM',(4418,168,4,0))
    print('VERIFY_ORBITS_OK')

if __name__=='__main__':main()
