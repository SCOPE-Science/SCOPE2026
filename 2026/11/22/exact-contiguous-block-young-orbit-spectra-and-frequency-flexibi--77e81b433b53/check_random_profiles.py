#!/usr/bin/env python3
"""Independent finite checks for contiguous-block Parikh profiles in mechanical words."""
import itertools, math, fractions

def lower_mechanical(alpha, count, rho=0.0):
    return [math.floor((j+1)*alpha+rho)-math.floor(j*alpha+rho) for j in range(count)]

def profiles(word, lengths, starts):
    n=sum(lengths)
    ans={}
    for t in starts:
        pos=t
        sig=[]
        for ell in lengths:
            sig.append(sum(word[pos:pos+ell]));pos+=ell
        ans[tuple(sig)]=ans.get(tuple(sig),0)+1
    return ans

def expected(alpha,lengths):
    n=sum(lengths);s=0
    pts={0.0}
    for L in lengths:
        s+=L
        z=(s*alpha)%1
        if z>1e-10 and z<1-1e-10:pts.add(round(1-z,12))
    return len(pts)

ct=0; rational=0; irrational=0
import random
rng=random.Random(20261119)
for q in range(2,16):
    for p in range(1,q):
        if math.gcd(p,q)!=1: continue
        alpha=p/q
        for n in range(1,30):
            w=lower_mechanical(alpha,q+n)
            for r in range(1,min(n,6)+1):
                for j in range(8):
                    cuts=tuple(sorted(rng.sample(range(1,n),r-1)))
                    ends=(0,)+cuts+(n,)
                    lengths=tuple(ends[i+1]-ends[i] for i in range(r))
                    ps=profiles(w,lengths,range(q))
                    residues={0};s0=0
                    for L in lengths:
                        s0+=L;residues.add(s0%q)
                    assert len(ps)==len(residues),(p,q,lengths,ps,residues)
                    ct+=1;rational+=1
for alpha in [(math.sqrt(5)-1)/2,math.sqrt(2)-1,math.pi-3]:
    w=lower_mechanical(alpha,5040,0.173)
    for n in range(1,26):
        for r in range(1,min(n,6)+1):
            for j in range(8):
                cuts=tuple(sorted(rng.sample(range(1,n),r-1)))
                ends=(0,)+cuts+(n,)
                lengths=tuple(ends[i+1]-ends[i] for i in range(r))
                ps=profiles(w,lengths,range(5000))
                assert len(ps)==r+1,(alpha,lengths,ps)
                ct+=1;irrational+=1
print('PASS; rational compositions',rational,'irrational compositions',irrational,'total',ct)
