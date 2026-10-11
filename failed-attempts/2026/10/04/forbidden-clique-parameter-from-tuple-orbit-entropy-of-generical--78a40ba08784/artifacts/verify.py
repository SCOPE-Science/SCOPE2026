from itertools import combinations, permutations
from math import factorial
from fractions import Fraction

def edges(n):
    return list(combinations(range(n),2))

def contains_clique(mask,n,r):
    es=edges(n); pos={e:i for i,e in enumerate(es)}
    for S in combinations(range(n),r):
        ok=True
        for e in combinations(S,2):
            if not (mask>>pos[tuple(sorted(e))])&1:
                ok=False; break
        if ok: return True
    return False

def count_kfree(n,r):
    m=n*(n-1)//2
    return sum(1 for mask in range(1<<m) if not contains_clique(mask,n,r))

# Exact small labeled K_r-free graph counts.
expected_tri={0:1,1:1,2:2,3:7,4:41,5:388,6:5789}
for n,v in expected_tri.items():
    got=count_kfree(n,3)
    assert got==v,(n,got,v)

# For n<r every graph is K_r-free; at n=r exactly one graph is excluded.
for r in range(3,7):
    for n in range(0,r):
        assert count_kfree(n,r)==2**(n*(n-1)//2)
    assert count_kfree(r,r)==2**(r*(r-1)//2)-1

# Explicit orbit encoding check for n<=4, r=3: each graph-order pair is a distinct
# finite ordered K_3-free structure, hence there are n!*f_3(n) encodings.
for n in range(1,5):
    f=count_kfree(n,3)
    encodings=set()
    es=edges(n)
    for mask in range(1<<(len(es))):
        if contains_clique(mask,n,3):
            continue
        for pi in permutations(range(n)):
            encodings.add((mask,pi))
    assert len(encodings)==factorial(n)*f

# Exact entropy constants and inversion r = 1 + 1/(1-2 lambda_r).
prev=Fraction(-1,1)
for r in range(3,31):
    lam=Fraction(r-2,2*(r-1))
    assert lam>prev
    recovered=1+Fraction(1,1-2*lam)
    assert recovered==r,(r,lam,recovered)
    prev=lam
assert all(Fraction(r-2,2*(r-1)) < Fraction(1,2) for r in range(3,31))

# Display small injective orbit profile for the triangle-free ordered case.
profile=[]
for n in range(1,7):
    profile.append(factorial(n)*expected_tri[n])
print('ordered_triangle_free_profile_n1_to_6=',profile)
print('VERIFY_OK')
