#!/usr/bin/env python3
"""Independent Hasse-jet check for all 10,920 smooth quartic equations."""
from collections import Counter
from itertools import product
from verify_orbits import MON, GEN, all_orbits, is_smooth, act

P=[tuple(map(int,p)) for p in product(range(2),repeat=3) if any(p)]

def evaluate(f,p):
    return sum((f>>j&1)*p[0]**a*p[1]**b*p[2]**c
               for j,(a,b,c) in enumerate(MON))&1

def gradient(f,p):
    g=[]
    for direction in range(3):
        v=0
        for j,e in enumerate(MON):
            if f>>j&1 and (e[direction]&1):
                exp=list(e);exp[direction]-=1
                v^=int(all(p[k] or not exp[k] for k in range(3)))
        g.append(v)
    return tuple(g)

def jet_coeff(f,p,q,degree):
    out=0
    for j,e in enumerate(MON):
        if not (f>>j&1):continue
        for a in range(degree+1):
            for b in range(degree-a+1):
                c=degree-a-b
                u=(a,b,c)
                if any(u[k]>e[k] for k in range(3)):continue
                if any((u[k]&e[k])!=u[k] for k in range(3)):continue
                if all((p[k] or u[k]==e[k]) and (q[k] or u[k]==0)
                       for k in range(3)):
                    out^=1
    return out

def contact_counts(f):
    o=h=0
    for p in P:
        if evaluate(f,p):continue
        g=gradient(f,p)
        assert any(g)
        q=next(q for q in P if q!=p and sum(g[k]*q[k] for k in range(3))%2==0)
        assert jet_coeff(f,p,q,0)==0
        assert jet_coeff(f,p,q,1)==0
        assert jet_coeff(f,p,q,2)==0 or jet_coeff(f,p,q,2)==1
        if jet_coeff(f,p,q,2)==0:
            if jet_coeff(f,p,q,3):o+=1
            else:
                assert jet_coeff(f,p,q,4)==1
                h+=1
    return o,h

def main():
    tally=Counter();extremal=[];forms=0
    for representative,size in all_orbits():
        if not is_smooth(representative):continue
        orbit={representative};stack=[representative]
        while stack:
            mask=stack.pop()
            for g in GEN:
                new=act(mask,g)
                if new not in orbit:orbit.add(new);stack.append(new)
        assert len(orbit)==size
        for f in orbit:
            k=contact_counts(f)
            tally[k]+=1;forms+=1
            if sum(k)==4:extremal.append(f)
    assert forms==10920
    expected={(0,0):1764,(0,1):1932,(1,0):2184,(0,2):420,(1,1):1176,
              (2,0):1512,(0,3):28,(1,2):336,(2,1):672,(3,0):728,(4,0):168}
    assert tally==expected,(tally,expected)
    assert len(extremal)==168
    assert 4418 in extremal
    assert all(contact_counts(f)==(4,0) for f in extremal)
    print('DIRECT_EQUATIONS',forms)
    print('DIRECT_CONTACT_DISTRIBUTION',sorted(tally.items()))
    print('DIRECT_EXTREMAL_EQUATIONS',len(extremal))
    print('VERIFY_DIRECT_OK')

if __name__=='__main__':main()
