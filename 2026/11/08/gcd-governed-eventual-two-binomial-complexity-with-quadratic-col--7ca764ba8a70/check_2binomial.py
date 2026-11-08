#!/usr/bin/env python3
"""Independent direct-window and arithmetic checks of two-binomial complexity."""
from math import comb, gcd

def pair_count(w):
    zero=0
    count=0
    for c in w:
        if c == '0': zero+=1
        elif c == '1': count+=zero
        else: raise ValueError('nonbinary word')
    return count

def signature(w):
    return (w.count('1'),pair_count(w))

def direct_complexity(a,b,n):
    p='0'*a+'1'*b
    X=p*((n//len(p))+3)
    sigs=set()
    for s in range(len(p)):
        w=X[s:s+n]
        sigs.add(signature(w))
    return len(sigs)

def phase_vectors(a,b,r):
    p=a+b
    block='0'*a+'1'*b
    circular=block*2
    result=[]
    for s in range(p):
        B=circular[s:s+p]
        T=B[:r]
        result.append((B.count('1'),pair_count(B),T.count('1'),pair_count(T)))
    return result

def arithmetic_complexity(a,b,m,r):
    # Common terms C(m,2) a b and common m*b cancel between signatures.
    return len({(t,m*(q+a*t)+u) for _,q,t,u in phase_vectors(a,b,r)})


def full_binomial_signature(w):
    counts=[w.count('0'),w.count('1'),0,0,0,0]
    keys={'00':2,'01':3,'10':4,'11':5}
    for i in range(len(w)):
        for j in range(i+1,len(w)):
            counts[keys[w[i]+w[j]]]+=1
    return tuple(counts)

def brute_full_complexity(a,b,n):
    period='0'*a+'1'*b
    word=period*((n//len(period))+3)
    return len({full_binomial_signature(word[s:s+n]) for s in range(len(period))})

def verify():
    tested_full=0
    for a in range(1,8):
        for b in range(1,8):
            for n in range(1,3*(a+b)+1):
                assert brute_full_complexity(a,b,n)==direct_complexity(a,b,n),(a,b,n)
                tested_full+=1
    tested_direct=0
    tested_eventual=0
    tested_exact=0
    tested_late=0
    for a in range(1,13):
        for b in range(1,13):
            p=a+b
            for n in range(1,4*p+1):
                m,r=divmod(n,p)
                assert direct_complexity(a,b,n)==arithmetic_complexity(a,b,m,r),(a,b,n)
                tested_direct+=1
            expected=p-gcd(a,b)+1
            for m in (1,2,7,30):
                assert arithmetic_complexity(a,b,m,0)==expected,(a,b,m)
                tested_exact+=1
    for a in range(1,31):
        for b in range(1,31):
            p=a+b
            threshold=comb(p-1,2)+1
            for r in range(p):
                for m in (threshold,threshold+1,threshold+73):
                    c=arithmetic_complexity(a,b,m,r)
                    expected=p-gcd(a,b)+1 if r==0 else p
                    assert c==expected,(a,b,m,r,c,expected)
                    tested_eventual+=1
    for h in range(1,41):
        a,b=2*h+1,2*h+3
        p=a+b
        m=h*(h+2)
        r=2*h+2
        s=h+1; t=3*h+2
        phases=phase_vectors(a,b,r)
        _,qs,os,ts=phases[s]
        _,qt,ot,tt=phases[t]
        assert (os, m*qs+m*a*os+ts)==(ot,m*qt+m*a*ot+tt)
        assert arithmetic_complexity(a,b,m,r)<p,(a,b,m,r)
        tested_late+=1
    print(f'PASS full_binomial_subsequence_counts={tested_full}, direct_window_vs_arithmetic={tested_direct}, exact_multiple_period={tested_exact}, eventual_lengths={tested_eventual}, quadratic_delay_witnesses={tested_late}')

if __name__=='__main__': verify()
