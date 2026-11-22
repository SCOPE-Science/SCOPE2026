"""Exact small-parameter checks for sliding-cylinder collision identities.

Standard-library only. These finite checks are supplementary to the proof.
"""
from itertools import product
from fractions import Fraction
from math import comb

def collision(bits,k,N):
    return sum(tuple(bits[i:i+k])==tuple(bits[j:j+k]) for i in range(N) for j in range(i+1,N))

def walsh_sum(bits,k,N,mask):
    return sum((-1)**sum(bits[i+j] for j in range(k) if (mask>>j)&1) for i in range(N))

def check_identity():
    count=0
    for k in range(1,5):
        for N in range(2,7):
            for bits in product(range(2),repeat=N+k-1):
                left=collision(bits,k,N)
                numerator=N*N- N*(2**k)+sum(walsh_sum(bits,k,N,mask)**2 for mask in range(1,2**k))
                assert numerator==left*2**(k+1),(k,N,bits)
                count+=1
    return count

def check_fair_mean():
    count=0
    for k in range(1,5):
        for N in range(2,7):
            total=0
            for bits in product(range(2),repeat=N+k-1):
                total+=collision(bits,k,N)
            assert Fraction(total,2**(N+k-1))==Fraction(comb(N,2),2**k)
            count+=1
    return count

def check_covariance():
    # Direct exhaustive unbiased letter probability, independent of support-translation rule.
    trials=0
    for k in range(1,5):
        masks=range(1,2**k)
        for s in masks:
            for t in masks:
                brute=Fraction(0)
                for lag in range(-k+1,k):
                    length=k+abs(lag)
                    vals=0
                    for bits in product(range(2),repeat=length):
                        i=max(0,-lag);j=i+lag
                        xs=(-1)**sum(bits[i+a] for a in range(k) if (s>>a)&1)
                        xt=(-1)**sum(bits[j+a] for a in range(k) if (t>>a)&1)
                        vals+=xs*xt
                    brute+=Fraction(vals,2**length)
                supp_s=[a for a in range(k) if (s>>a)&1]
                supp_t=[a for a in range(k) if (t>>a)&1]
                equivalent=[a-min(supp_s) for a in supp_s]==[a-min(supp_t) for a in supp_t]
                assert brute==(1 if equivalent else 0),(k,s,t,brute)
                trials+=1
    return trials

def check_long_run_variance():
    # Exact evaluation of leading Gaussian variance at p=3/5 and 7/10,
    # directly from independent letter evaluations of block-frequency scores.
    counts=0
    for k in range(1,5):
        for p in (Fraction(3,5),Fraction(7,10)):
            a=p*p+(1-p)*(1-p);b=p**3+(1-p)**3
            theoretical=b**k-a**(2*k)+2*sum(a**(2*h)*b**(k-h)-a**(2*k) for h in range(1,k))
            vals=[]
            for h in range(k):
                cov=Fraction(0)
                for bits in product(range(2),repeat=k+h):
                    prob=p**sum(bits)*(1-p)**(len(bits)-sum(bits))
                    f=lambda j:__import__('functools').reduce(lambda x,y:x*y,(p if bits[j+r] else 1-p for r in range(k)),Fraction(1))
                    cov+=prob*f(0)*f(h)
                vals.append(cov-a**(2*k))
            direct=vals[0]+2*sum(vals[1:])
            assert direct==theoretical,(k,p,direct,theoretical)
            counts+=1
    return counts

if __name__=='__main__':
    print('Parseval exact strings:',check_identity())
    print('Fair exact mean instances:',check_fair_mean())
    print('Exhaustive covariance pairs:',check_covariance())
    print('Biased long-run variance instances:',check_long_run_variance())
    print('ALL_CHECKS_PASSED')
