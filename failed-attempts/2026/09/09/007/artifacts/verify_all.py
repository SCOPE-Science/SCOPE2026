"""Independent replay verifier (stdlib only): re-derives every exact claim from (n, P1)."""
from fractions import Fraction
import math
n=799657; D=n*n
# 1. primality
assert int(math.isqrt(n))**2!=n and all(n%d for d in range(2,int(math.isqrt(n))+1))
# 2. conductor
assert 32*D==20462442164768
# 3. valuations at n: v(c4)=2, v(Delta)=6; P splits: T(T-1)(T+1)=0 at 0,1,-1 mod n
assert (-48*D)%(n*n)==0 and (-48*D)%(n**3)!=0
assert (64*D**3)%(n**6)==0 and (64*D**3)%(n**7)!=0
for r in (0,1,-1): assert (r**3-r)%n==0
# 4. 2-adic: v2(c4)=4, v2(Delta)=6
c4=-48*D; De=64*D**3
v2=lambda m: (len(bin(m))-len(bin(m).rstrip('0'))-1) if m!=0 else float('inf')
# (simple exact v2 via loop)
def ev2(m):
    e=0
    while m%2==0: m//=2; e+=1
    return e
assert ev2(abs(c4))==4 and ev2(De)==6
# 5. torsion counts mod 3 and 5
for p in (3,5):
    N=1+sum(sum(1 for y in range(p) if (y*y-(x**3-(D%p)*x))%p==0) for x in range(p))
    assert N==4, (p,N)
# 6. P1 on curve
x=Fraction(-94381225,289); y=Fraction(2049376840680,4913)
assert y*y==x**3-D*x
# 7. integral search |a|<=1e5 quick re-check (subset of the 1e6 run)
hits=[a for a in range(-10**5,10**5+1) if (lambda m: m>=0 and math.isqrt(m)**2==m)(a*(a*a-D))]
assert hits==[0], hits  # +-n outside this subset window; checked exactly below
assert (-n)*((-n)**2-D)==0 and (n)*((n)**2-D)==0
print("VERIFY_OK")
