#!/usr/bin/env python3
"""Exact independent checks for the binary-lottery EF1 balancing theorem.

No external dependencies.  Run: python3 verify.py
"""
from functools import lru_cache
from itertools import product
from math import comb

@lru_cache(None)
def pmf_num(s, t, a, b):
    if t < 0 or t > s:
        return 0
    return comb(s,t)*a**t*(b-a)**(s-t)

def via_event(counts,a,b):
    """Direct exact sum over possible counts, integer numerator / b**m."""
    ans=0
    for xs in product(*(range(s+1) for s in counts)):
        if max(xs)-min(xs) <= 1:
            x=1
            for s,t in zip(counts,xs):
                x*=pmf_num(s,t,a,b)
            ans+=x
    return ans

def via_formula(counts,a,b):
    """Exact interval-overlap formula, scaled to common denominator b**m."""
    out=0
    for t in range(max(counts)+1):
        t0=t1=1
        for s in counts:
            t0*=(pmf_num(s,t,a,b)+pmf_num(s,t+1,a,b))
            t1*=pmf_num(s,t+1,a,b)
        out+=t0-t1
    return out

def via_binary_bits(counts,a,b):
    """Independent full outcome enumeration, weighted by Bernoulli counts."""
    m=sum(counts)
    if not m:return 1
    out=0
    for mask in range(1<<m):
        xs=[];shift=0
        for s in counts:
            xs.append(((mask >> shift)&((1<<s)-1)).bit_count())
            shift+=s
        if max(xs)-min(xs)<=1:
            successes=mask.bit_count()
            out+=a**successes*(b-a)**(m-successes)
    return out

def compositions(m,n):
    if n==1:
        yield (m,)
        return
    for k in range(m+1):
        for v in compositions(m-k,n-1):
            yield (k,)+v

def balanced(m,n):
    q,r=divmod(m,n)
    return (q,)*(n-r)+(q+1,)*r

def run():
    total=pair=bits=0
    for n in range(2,6):
        for m in range(0,11):
            if n>=5 and m>8:continue
            bcounts=balanced(m,n)
            for a,b in [(1,4),(1,2),(3,4)]:
                best=via_formula(bcounts,a,b)
                for k in compositions(m,n):
                    v=via_event(k,a,b)
                    assert v==via_formula(k,a,b),('formula',k,a,b,v,via_formula(k,a,b))
                    total+=1
                    if m<=7 and n<=4:
                        assert v==via_binary_bits(k,a,b),('bits',k,a,b)
                        bits+=1
                    assert v<=best,('optimality',k,a,b,v,best)
                    if sorted(k)!=sorted(bcounts):
                        assert v<best,('strict global',k,a,b)
                    for i in range(n):
                        for j in range(n):
                            if k[j]-k[i]>=2:
                                v2=list(k);v2[i]+=1;v2[j]-=1
                                vv=via_formula(tuple(v2),a,b)
                                # coupling lower bound (b-a-1) p^2 (1-p)^(m-2)
                                # in scaled numerator b**m:
                                lb=(k[j]-k[i]-1)*a*a*(b-a)**(m-2)
                                assert vv-v>=lb>0,('pair',k,i,j,a,b,lb,vv-v)
                                pair+=1
    print('PASS: exact formula/direct count comparison, optimum, uniqueness:',total,'instances')
    print('PASS: independent complete binary-state enumeration:',bits,'instances')
    print('PASS: strict pair transfers and uniform lower bound:',pair,'comparisons')
    examples={(2,2,2):23,(1,2,3):18}
    assert via_event((2,2,2),1,2)==23*2**(6-5)
    assert via_event((1,2,3),1,2)==18*2**(6-5)
    print('PASS: 3 agents / 6 goods with p=1/2: balanced 23/32; (1,2,3) 9/16')
if __name__=='__main__':run()
