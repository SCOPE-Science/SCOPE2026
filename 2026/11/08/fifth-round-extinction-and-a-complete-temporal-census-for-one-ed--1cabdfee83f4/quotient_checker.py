#!/usr/bin/env python3
"""Exact 441-state reduction for three-state Greenberg--Hastings dynamics
on a complete bipartite graph with one deleted cross-edge.
Run: python3 quotient_checker.py. Python standard library only.
"""
from itertools import product
from collections import Counter
from math import comb

TABLE = {
 (0,1): ((1,0,0),(0,0,0),(0,0,0)),
 (0,3): ((0,0,0),(0,3,6),(0,6,9)),
 (0,4): ((0,4,0),(4,8,0),(0,0,0)),
 (1,1): ((15,8,0),(8,4,0),(0,0,0)),
 (1,3): ((0,0,0),(0,0,1),(0,1,0)),
 (1,4): ((0,8,3),(8,20,6),(3,6,0)),
 (2,1): ((25,15,3),(15,4,0),(3,0,0)),
 (2,3): ((0,0,0),(0,0,1),(0,1,0)),
 (2,4): ((0,13,6),(13,22,6),(6,6,0)),
 (3,1): ((18,12,3),(12,4,0),(3,0,0)),
 (3,3): ((0,0,0),(0,0,1),(0,1,0)),
 (3,4): ((0,7,7),(7,12,6),(7,6,0)),
 (4,1): ((12,8,3),(8,0,0),(3,0,0)),
 (4,4): ((0,4,2),(4,4,0),(2,0,0)),
 (5,1): ((10,2,0),(2,0,0),(0,0,0)),
}

def bits(s):
    return tuple(i for i in range(3) if s & (1 << i))

def upd(c,exc):
    return ((c + 1) % 3) if c else int(exc)

def step(z):
    a,b,s,t = z   # a,b distinguish endpoints; s,t ordinary-shore color supports
    excite_s = (b == 1) or (bool(t & 2))
    excite_t = (a == 1) or (bool(s & 2))
    aa=upd(a,bool(t & 2))
    bb=upd(b,bool(s & 2))
    ss=tt=0
    for c in bits(s): ss |= (1 << upd(c,excite_s))
    for c in bits(t): tt |= (1 << upd(c,excite_t))
    return (aa,bb,ss,tt)

def orbit_info(z):
    seen={}; trace=[]
    while z not in seen:
        seen[z]=len(trace)
        trace.append(z)
        z=step(z)
        assert len(trace)<=441
    return seen[z],len(trace)-seen[z],trace

def lift_period_is_identity(z,p):
    # Track each original ordinary-shore color individually for p updates.
    # If this holds for every periodic support state, support recurrence is
    # equivalent to recurrence of each full labelled configuration.
    a,b,s,t=z
    xs={c:c for c in bits(s)}
    xt={c:c for c in bits(t)}
    cur=z
    for _ in range(p):
        ca,cb,cs,ct=cur
        exs=(cb==1) or bool(ct&2)
        ext=(ca==1) or bool(cs&2)
        xs={o:upd(v,exs) for o,v in xs.items()}
        xt={o:upd(v,ext) for o,v in xt.items()}
        cur=step(cur)
    return cur==z and all(o==v for o,v in xs.items()) and all(o==v for o,v in xt.items())

def a(j,l):
    if j>l:return 0
    return sum((-1)**(j-h)*comb(j,h)*h**l for h in range(j+1))

def count(t,p,m,n):
    M=TABLE.get((t,p),((0,)*3,)*3)
    return sum(M[j-1][k-1]*a(j,m-1)*a(k,n-1) for j in range(1,4) for k in range(1,4))

def base_step(z):
    s,t=z
    ss=tt=0
    for c in bits(s): ss |= (1 << upd(c,bool(t & 2)))
    for c in bits(t): tt |= (1 << upd(c,bool(s & 2)))
    return ss,tt

def base_orbit(z):
    seen={};i=0
    while z not in seen:
        seen[z]=i;z=base_step(z);i+=1
    return seen[z],i-seen[z]

def main():
    C=Counter(); period_states=0
    old_classes=Counter(base_orbit(z) for z in product(range(1,8),repeat=2))
    assert max(t for t,p in old_classes)==4
    for z in product(range(1,8),repeat=2):
        t,p=base_orbit(z)
        if t==0:
            curr=z
            for _ in range(p):
                nxt=base_step(curr)
                assert nxt[0].bit_count()==curr[0].bit_count()
                assert nxt[1].bit_count()==curr[1].bit_count()
                curr=nxt
    assert base_orbit((1,3))[0]==4
    for z in product(range(3),range(3),range(1,8),range(1,8)):
        t,p,trace=orbit_info(z)
        C[t,p,z[2].bit_count(),z[3].bit_count()]+=1
        if t==0:
            period_states+=1
            assert lift_period_is_identity(z,p),(z,p)
    assert sum(C.values())==441
    assert set((t,p) for t,p,j,k in C)==set(TABLE)
    for t,p in TABLE:
        for j,k in product(range(1,4),repeat=2):
            assert C[t,p,j,k]==TABLE[t,p][j-1][k-1],(t,p,j,k)
    assert max(t for t,p,j,k in C)==5
    assert set(p for t,p,j,k in C)=={1,3,4}
    assert tuple(C[5,1,j,k] for j,k in product(range(1,4),repeat=2))==(10,2,0,2,0,0,0,0,0)
    for m,n in product(range(2,16),repeat=2):
        assert sum(count(t,p,m,n) for t,p in TABLE)==3**(m+n)
        assert count(5,1,m,n)==2**m+2**n+2
        A=a(2,m-1);B=a(2,n-1);U=a(3,m-1);V=a(3,n-1)
        assert count(0,3,m,n)==3*(A*B+2*A*V+2*U*B+3*U*V)
        assert count(0,4,m,n)==4*(A+B+2*A*B)
        assert sum(count(t,p,m,n) for t,p in TABLE if t>=5)==2**m+2**n+2
    print('PASS: intact biclique 49-state reduction has maximum first entry 4')
    print('PASS: all 441 support states; 15 first-entry/period coefficients; no other classes')
    print('PASS: each of',period_states,'periodic support states has identical lifted labelled period')
    print('PASS: support periods 1,3,4; sharp first-entry 5; F^17=F^5')
    print('PASS: exact fifth-entry formula and orbit counts, 196 pairs 2<=m,n<=15')
    print('PASS: first-entry census sums to 3^(m+n) in 196 parameter pairs')

if __name__=='__main__':main()
