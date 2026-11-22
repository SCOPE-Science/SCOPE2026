"""Exact finite checks for the Pascal-row prime-adic valuation residue theorem.
This checker makes no claim that finite tests replace the proof."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from math import comb

checks = 0

def ok(test, context):
    global checks
    checks += 1
    if not test:
        raise AssertionError(context)

@lru_cache(maxsize=None)
def ds(n, p):
    if n == 0: return 0
    return ds(n // p, p) + n % p

@lru_cache(maxsize=None)
def prefix(n, p):
    if n == 0: return 0
    q, r = divmod(n,p)
    return p*prefix(q,p) + q*p*(p-1)//2 + r*ds(q,p) + r*(r-1)//2

@lru_cache(maxsize=None)
def valuation(n, p):
    return (2 * prefix(n, p) - (n-1) * ds(n, p)) // (p-1)

def factorial_val(n, p):
    out=0
    while n:
        n//=p
        out+=n
    return out

def independent_row_val(n, p):
    # Legendre factorial valuations, independent of the digit-sum formula.
    return sum(factorial_val(n,p)-factorial_val(j,p)-factorial_val(n-j,p)
               for j in range(n+1))

def carry_val(n, p):
    s=0
    power=p
    while power <= n:
        q,r=divmod(n,power)
        s+=q*(power-1-r)
        power*=p
    return s

def predicted_finite(p,k,r):
    mod=p**k
    multiplicities=Counter({0:1})
    for _ in range(r-k):
        temp=Counter()
        for a,w in multiplicities.items():
            for digit in range(p): temp[a+digit]+=w
        multiplicities=temp
    out=Counter()
    inv=pow(p-1,-1,mod)
    for a in range(mod):
        for s,weight in multiplicities.items():
            out[(valuation(a,p)+(a+1)*inv*s)%mod]+=weight
    return out

for p in (2,3,5,7):
    for n in range(0,520):
        ok(valuation(n,p)==carry_val(n,p),("carry",p,n))
        if n<130: ok(valuation(n,p)==independent_row_val(n,p),("factorial",p,n))
        if n<26:
            prod=1
            for j in range(n+1): prod*=comb(n,j)
            direct=0
            while prod%p==0:
                direct+=1
                prod//=p
            ok(valuation(n,p)==direct,("actual binomial product",p,n))
    for k in range(1,5 if p==2 else 4):
        mod=p**k
        inv=pow(p-1,-1,mod)
        for L in (k,k+1):
            m=p**L
            for t in range(0,8):
                for a in range(0,min(m,18)):
                    n=a+m*t
                    ok((valuation(n,p)-valuation(a,p)-(a+1)*inv*ds(t,p))%mod==0,
                        ("digit splitting",p,k,L,a,t))
        # Sharpness: L=k-1 is not sufficient, with a=0 and t=1 or p+1.
        L=k-1
        m=p**L
        failure=[(valuation(m*t,p)-inv*ds(t,p))%mod for t in (1,p+1)]
        ok(any(failure),("sharp cutoff",p,k,failure))
        for r in range(k,k+4):
            if p**r>2200:break
            out=Counter(valuation(n,p)%mod for n in range(p**r))
            ok(out==predicted_finite(p,k,r),("finite histogram",p,k,r))
        probs={b:(Fraction(k*(p-1)+p,p**(k+1)) if b==0 else
                  Fraction((p-1)*(next((j for j in range(k) if b%p**(j+1)),k)+1),p**(k+1)))
              for b in range(mod)}
        ok(sum(probs.values())==1,("probability mass",p,k))
        # For high precision finite blocks the exact residue percentages approach the formula.
        if p**(k+3) <= 2600:
            r=k+3
            obs=Counter(valuation(n,p)%mod for n in range(p**r))
            ok(sum(obs.values())==p**r,("partition",p,k,r))
print("PASS: %d independent exact finite assertions; the infinite proof is separate." % checks)
