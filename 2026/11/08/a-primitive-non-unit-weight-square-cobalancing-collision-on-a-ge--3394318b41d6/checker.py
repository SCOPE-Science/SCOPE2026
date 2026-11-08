"""Exact integer checks for a non-unit-weight square-cobalancing collision."""
from math import gcd

def pyramidal(n: int) -> int:
    assert isinstance(n, int) and n >= 0
    return n*(n+1)*(2*n+1)//6

def direct(n: int) -> int:
    return sum(j*j for j in range(1,n+1))

# The unrestricted algebraic identity is proved in RESULT.md; the tests below
# check the concrete certificate independently by direct integer summation.
a,b=563,11
assert gcd(a,b)==1 and b>1
solutions=[(5,15),(142,390)]
assert len(set(n for n,r in solutions))==2
for n,r in solutions:
    assert n>1 and r>0
    m=n+r
    assert pyramidal(n)==direct(n)
    assert pyramidal(m)==direct(m)
    assert a*direct(n) == b*sum(j*j for j in range(n+1,m+1))
    assert (a+b)*pyramidal(n) == b*pyramidal(m)
    x,y=2*n+1,2*m+1
    assert b*y*(y*y-1)==(a+b)*x*(x*x-1)
    print(f'CERTIFICATE n={n} r={r} endpoint={m} left_sum={pyramidal(n)} right_sum={pyramidal(m)-pyramidal(n)} exact=YES')

# An independent bounded scan is optional supporting evidence only.
# It does not assert uniqueness of integral points or global solutions.
upper=10_000
m=1
seen=[]
for n in range(1,upper+1):
    target,rem=divmod((a+b)*pyramidal(n),b)
    if rem: continue
    while pyramidal(m)<target: m+=1
    if pyramidal(m)==target and m>n: seen.append((n,m-n))
assert seen==solutions, seen
print(f'BOUNDED_CHECK n=1..{upper} found={seen}; no global completeness claim')
print('VERIFY_OK two_distinct_nontrivial_indices=YES coprime_coefficients=YES exact_sums=YES cubic_points=YES')
