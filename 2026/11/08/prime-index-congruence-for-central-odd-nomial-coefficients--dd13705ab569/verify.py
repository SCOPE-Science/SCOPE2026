"""Independent exact-integer spot tests of the prime-index central odd-nomial congruence.
Run: python3 verify.py
"""
from math import comb

def central(d,p):
    # Coefficient of x^(d*p) in (1+x+...+x^(2d))^p.
    arr=[1]
    for _ in range(p):
        nxt=[0]*(len(arr)+2*d)
        # sliding-window convolution, independent of the proof's rational-series expansion
        running=0
        for j in range(len(nxt)):
            if j<len(arr):running+=arr[j]
            if j-2*d-1>=0 and j-2*d-1<len(arr):running-=arr[j-2*d-1]
            nxt[j]=running
        arr=nxt
    return arr[d*p]

def predicted(d,p):
    return ((2**p-1) if (2*d+1)%p==0 else 1)%(p*p)

def from_inclusion_exclusion(d,p):
    # Independent exact formula from the finite geometric series (not a congruence).
    N=2*d+1
    return sum((-1)**j*comb(p,j)*comb((d+1)*p-N*j-1,d*p-N*j)
               for j in range(d*p//N+1))

primes=[3,5,7,11,13,17,19,23,29,31,37]
cases=0; exceptional=0
for p in primes:
    for d in range(0,29):
        a=central(d,p)
        b=from_inclusion_exclusion(d,p)
        expected=predicted(d,p)
        assert a==b,(p,d,'identity',a,b)
        assert a%(p*p)==expected,(p,d,'congruence',a%(p*p),expected)
        cases+=1
        exceptional+=((2*d+1)%p==0)
print(f'VERIFY_OK exact_cases={cases} exceptional_cases={exceptional} primes={primes} d=0..28')
