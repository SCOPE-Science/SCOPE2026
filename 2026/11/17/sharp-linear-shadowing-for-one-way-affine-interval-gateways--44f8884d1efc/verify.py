#!/usr/bin/env python3
"""Finite and exact-arithmetic checks for the one-way affine gateway shadowing theorem."""
from fractions import Fraction as Q
import random

def f(x,k,mu,lam):
    return k*x if x < 1 else mu+lam*(x-1)

def check_instance(k,mu,lam,delta,seed):
    assert Q(1)<k<=Q(2) and Q(0)<=lam<Q(1) and Q(1)<mu<=Q(2)-lam
    assert 0<delta<min(k-1,mu-1)/2
    C=max(1/(k-1),1/(1-lam))
    rng=random.Random(seed)
    count=0
    # pseudo-orbits: exact rational errors in (-delta,delta), clipped to state space
    for x0 in [Q(0),Q(1,30),Q(1,2),Q(19,20),Q(1),Q(7,5),Q(2)]:
        for path in range(20):
            xs=[x0]
            for _ in range(35):
                x=xs[-1]
                e=delta*Q(rng.randint(-80,80),100)
                new=max(Q(0),min(Q(2), f(x,k,mu,lam)+e))
                assert abs(new-f(x,k,mu,lam))<delta
                xs.append(new)
            N=next((j for j,x in enumerate(xs) if x>=1),None)
            if N is None:
                # only 36-step left prefix, not a forever-left certificate
                continue
            if N==0:
                y=xs[0]
            else:
                # exact rational selection from [1,k), no approximation at boundary
                b=min(xs[N],k-delta/Q(1000))
                assert 1<=b<k and abs(xs[N]-b)<delta
                y=b/k**N
            for j,x in enumerate(xs):
                if j:
                    y=f(y,k,mu,lam)
                assert abs(y-x)<=delta*C, (k,mu,lam,delta,seed,path,j,y,x)
            count+=1
    # adversarial constant pseudo-orbits for each fixed point (strict error <delta)
    eps=delta*Q(999,1000)
    left=eps/(k-1)
    right_fixed=(mu-lam)/(1-lam)
    right=right_fixed-eps/(1-lam)
    assert 0<left<1 and 1<right<=2
    assert abs(f(left,k,mu,lam)-left)==eps
    assert abs(f(right,k,mu,lam)-right)==eps
    return count

if __name__=='__main__':
    choices=[(Q(3,2),Q(5,4),Q(3,4)), (Q(9,5),Q(7,5),Q(2,5)),
             (Q(7,5),Q(8,5),Q(1,5)), (Q(19,10),Q(3,2),Q(0)),
             (Q(3,2),Q(3,2),Q(1,2)), (Q(9,5),Q(11,10),Q(9,10))]
    total=0
    for i,(k,mu,lam) in enumerate(choices):
        delta=min(k-1,mu-1)/Q(5)
        n=check_instance(k,mu,lam,delta,128+i)
        print('case',i,'k',str(k),'mu',str(mu),'lambda',str(lam),'sharp_constant',str(max(1/(k-1),1/(1-lam))),'checked',n)
        total+=n
    print('VERIFY_OK exact_rational_finite_prefixes',total,'adversarial_fixed_points',len(choices)*2)
    print('FINITE_CHECK_ONLY: the theorem is established analytically, not by exhaustive enumeration')
