#!/usr/bin/env python3
"""Independent finite checks for masked finite-field cubic Fourier extension.

Checks never replace the proof for all finite fields.
"""
import cmath
import itertools
import math
import random


def data_for_mask(mask, q):
    b = 1 if 0 in mask else 0
    k = sum(1 for t in range(1, (q+1)//2) if t in mask and (-t) % q in mask)
    r = len(mask)-b-2*k
    return b,k,r


def predicted(mask,q):
    b,k,r = data_for_mask(mask,q)
    n=len(mask)
    if k<2 and not (b and k>=1):
        return 2-1/n, {t:1/math.sqrt(n) for t in mask}
    denom=3*b+4*k
    amps={t:0.0 for t in mask}
    if b: amps[0]=math.sqrt(3/denom)
    for t in range(1,(q+1)//2):
        if t in mask and (-t)%q in mask:
            amps[t]=amps[(-t)%q]=math.sqrt(2/denom)
    return 3-6/denom,amps


def two_sum_energy(f,q):
    vals={}
    for a,fa in f.items():
        for b,fb in f.items():
            key=((a+b)%q,(a*a*a+b*b*b)%q)
            vals[key]=vals.get(key,0j)+fa*fb
    return sum(abs(z)**2 for z in vals.values())


def predicted_energy_identity(f,q):
    S=sum(abs(z)**2 for z in f.values())
    R=sum(abs(f.get(t,0j)*f.get((-t)%q,0j))**2 for t in f)
    B=sum(f[t]*f.get((-t)%q,0j) for t in f)
    return 2*S*S-sum(abs(z)**4 for z in f.values())-2*R+abs(f.get(0,0j))**4+abs(B)**2


def run():
    n_masks=0
    n_tests=0
    rng=random.Random(11745)
    for q in (5,7,11,13):
        if q<=11:
            masks=(tuple(t for t in range(q) if (bits>>t)&1) for bits in range(1,1<<q))
        else:
            masks=(tuple(t for t in range(q) if (bits>>t)&1) for bits in (rng.randrange(1,1<<q) for _ in range(350)))
        for mask in masks:
            target,f=predicted(mask,q)
            S=sum(abs(z)**2 for z in f.values())
            assert abs(S-1)<1e-11,(q,mask,S)
            e=two_sum_energy(f,q)
            assert abs(e-target)<1e-9,(q,mask,target,e)
            assert abs(e-predicted_energy_identity(f,q))<1e-9
            n_masks+=1
            for _ in range(2):
                g={t:complex(rng.randrange(-4,5),rng.randrange(-4,5)) for t in mask}
                S=sum(abs(z)**2 for z in g.values())
                if S==0: continue
                ep=two_sum_energy(g,q)
                assert abs(ep-predicted_energy_identity(g,q))<1e-7,(q,mask,ep,predicted_energy_identity(g,q))
                assert ep/(S*S)<=target+1e-9,(q,mask,ep/(S*S),target)
                n_tests+=1
    print(f'CUBIC_ERASURES_VERIFY_PASS masks={n_masks} random_tests={n_tests} primes=5,7,11,13')


if __name__=='__main__':
    run()
