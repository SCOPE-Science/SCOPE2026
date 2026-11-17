"""Independent exact-integer checks for the graph-period upper-bound arithmetic.
The complete mathematical proof is in RESULT.md.
"""
from math import factorial

def bound(n,d):
    return d*(2**d-1)*factorial(n-d+1)

expected_small={1:1,2:6,3:21,4:60,5:155}
for n, expected in expected_small.items():
    assert max(bound(n,d) for d in range(1,n+1))==expected
assert [bound(6,d) for d in range(1,7)]==[720,720,504,360,310,378]
for n in range(6,101):
    assert 2**(n+1)<=factorial(n)
    for d in range(1,n+1):
        assert bound(n,d)<=factorial(n)
for n in range(1,101):
    assert max(bound(n,d) for d in range(1,n+1))==max(factorial(n),n*(2**n-1))
for n in range(1,20):
    assert (n+1)!=0
print('CHECK_OK')
print('small dimensions:', ', '.join(f'{n}:{expected_small[n]}' for n in expected_small))
print('dimension 6 period bounds: 720 720 504 360 310 378')
print('integer inequalities and extremal formula checked for dimensions 1 through 100')
