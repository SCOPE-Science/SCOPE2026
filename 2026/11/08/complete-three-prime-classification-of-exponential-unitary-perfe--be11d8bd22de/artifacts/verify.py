"""Independent exact-arithmetic consistency tests for the three-prime e-unitary-perfect classification.
Run with Python 3 standard library: python verify_eunitary_ternary.py
"""
from math import gcd
from itertools import combinations, product

def eunitary_local(p,a):
    return sum(p**d for d in range(1,a+1) if a%d==0 and gcd(d,a//d)==1)

def is_eu_perfect(factors):
    left=right=1
    for p,a in factors:
        left*=eunitary_local(p,a)
        right*=p**a
    return left == 2*right

def prime_list(limit):
    return [p for p in range(2,limit+1) if all(p%d for d in range(2,int(p**.5)+1))]

primes=prime_list(31)
assert is_eu_perfect([(2,2),(3,2)])
assert is_eu_perfect([(2,3),(3,2),(5,2)])
assert is_eu_perfect([(2,2),(3,3),(5,2)])
for p in primes:
    for a in range(2,31):
        # local bound and uniqueness of its equality case
        assert eunitary_local(p,a)*p <= (p+1)*p**a
        assert (eunitary_local(p,a)*p == (p+1)*p**a) == (a==2)

checks=0
solutions=[]
# All squarefull, three-prime-factor patterns in this finite region.
for pair in combinations(primes[1:],2):
    q,r=pair
    for a,b,c in product(range(2,18),repeat=3):
        checks+=1
        if is_eu_perfect([(2,a),(q,b),(r,c)]):
            solutions.append((2,a,q,b,r,c))
assert sorted(solutions)==[(2,2,3,3,5,2),(2,3,3,2,5,2)],solutions

# Direct independent classification using factorization for all integers in an interval.
N=350000
spf=list(range(N+1))
for p in range(2,int(N**0.5)+1):
    if spf[p]==p:
        for k in range(p*p,N+1,p):
            if spf[k]==k:spf[k]=p

actual=[]
for n in range(2,N+1):
    rem=n; factor=[]
    while rem>1:
        p=spf[rem];e=0
        while rem%p==0:rem//=p;e+=1
        factor.append((p,e))
    if len(factor)==3 and is_eu_perfect(factor):
        actual.append(n)
expected=[36*p for p in primes if p>3 and 36*p<=N]
# extend expectation beyond prime_list limit by sieve
expected=[36*p for p in range(5,N//36+1) if spf[p]==p]
expected.extend([1800,2700])
assert actual==sorted(expected),(actual[:20],expected[:20])
print(f'VERIFY_OK local_bound={len(primes)*29} squarefull_triples={checks} exact_solutions={solutions} direct_interval=2..{N} ternary_count={len(actual)} core_36=PASS')
