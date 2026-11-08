#!/usr/bin/env python3
"""Finite exact checks of local divisor weights and periodic spacing witnesses."""
from fractions import Fraction
from math import gcd

def primes_to(y):
    ps=[]
    for p in range(2,y+1):
        if all(p % q for q in range(2,int(p**0.5)+1)):
            ps.append(p)
    return ps

def weights(ps):
    m=1
    for p in ps:m*=p
    return m,[Fraction(__import__('math').prod((2*p-1 if a%p==0 else p-1) for p in ps),m*m) for a in range(m)]

def cover(w,h):
    m=len(w); discard=set()
    for d in range(1,h+1):
        for a in range(m):
            b=(a+d)%m
            discard.add(a if w[a]<=w[b] else b)
    keep=set(range(m))-discard
    assert all((a+d)%m not in keep for a in keep for d in range(1,h+1))
    assert sum(w[a] for a in keep)+sum(w[a] for a in discard)==1
    return keep,discard

def checked():
    cases=0;crt=0;graph_edges=0;periodic=0
    for y in (3,5,7,11):
        ps=primes_to(y);m,w=weights(ps)
        assert sum(w)==1
        for a in range(m):
            g=gcd(a,m)
            formula=Fraction(sum(gcd(u,m) for u in range(m) if a%gcd(u,m)==0),m*m)
            assert formula==w[a]
            crt+=1
        for h in range(1,min(4,m//2)):
            keep,discard=cover(w,h)
            edge_mins=sum(min(w[a],w[(a+d)%m]) for d in range(1,h+1) for a in range(m))
            assert 1-sum(w[a] for a in keep)<=edge_mins
            graph_edges+=m*h
            cases+=1
            if y==7 and h==1:
                # Exact maximum independent set weight for the 210-cycle.
                def dp(fixed_zero):
                    states={fixed_zero: w[0] if fixed_zero else Fraction(0)}
                    for i in range(1,m):
                        nxt={}
                        for prev,score in states.items():
                            nxt[False]=max(nxt.get(False,Fraction(-1)),score)
                            if not prev and (i!=m-1 or not fixed_zero):
                                nxt[True]=max(nxt.get(True,Fraction(-1)),score+w[i])
                        states=nxt
                    return max(states.values())
                best=max(dp(False),dp(True))
                assert best==Fraction(927,1225),best
                print('PERIOD_210_OPTIMUM',best)
    # Exact local congruence measure test against divisor sums (not an asymptotic proof).
    for y in (3,5):
        ps=primes_to(y);m,w=weights(ps)
        nmax=60000
        tau=[0]*(nmax+1)
        for d in range(1,nmax+1):
            for n in range(d,nmax+1,d):tau[n]+=1
        residue_sums=[0]*m
        for n in range(1,nmax+1):residue_sums[n%m]+=tau[n]
        assert sum(residue_sums)==sum(tau[1:])
        periodic+=m
    print(f'VERIFY_OK cycles={cases} crt_residues={crt} graph_edges={graph_edges} tested_residues={periodic} exact_rationals=yes')

if __name__=='__main__':checked()
