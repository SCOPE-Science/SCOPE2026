"""Exact integer run-count formulas and independent cyclic-word validation."""
from math import comb

def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def oscillating_equal_hubs(n):
    total = 0
    for k in range(1,n):
        for r in range(1,min(k//3,n-k)+1):
            if 2*k > n+1 and 2*(k-2*r) < n-1:
                num = n*choose(k-2*r-1,r-1)*choose(n-k-1,r-1)
                assert num % r == 0
                total += num//r
    return total

def balanced_majority_fixed(n):
    if n%2: return 0
    m=n//2
    total=0
    for r in range(1,m//2+1):
        num=n*choose(m-r-1,r-1)**2
        assert num % r == 0
        total += num//r
    return total

def predicted(n):
    return 2*oscillating_equal_hubs(n)+(2*(balanced_majority_fixed(n)+2) if n%2==0 else 0)

def valid_equal_hubs(bits):
    n=len(bits); k=sum(bits)
    if not (2*k>n+1) or k == n: return False
    y=[bits[(i-1)%n]&bits[i]&bits[(i+1)%n] for i in range(n)]
    if not (2*(sum(y))<n-1): return False
    back=[y[(i-1)%n]|y[i]|y[(i+1)%n] for i in range(n)]
    return back==bits

def valid_opposite_hubs(bits):
    n=len(bits); k=sum(bits)
    if n%2 or k!=n//2: return False
    y=[int(bits[(i-1)%n]+bits[i]+bits[(i+1)%n]>=2) for i in range(n)]
    if sum(y)!=n//2: return False
    back=[int(y[(i-1)%n]+y[i]+y[(i+1)%n]>=2) for i in range(n)]
    return back==bits

for n in range(3,17):
    equal=opposite=0
    for mask in range(1<<n):
        b=[(mask>>i)&1 for i in range(n)]
        equal+=valid_equal_hubs(b)
        opposite+=valid_opposite_hubs(b)
    expected_opposite=balanced_majority_fixed(n)+(2 if n%2==0 else 0)
    assert equal==oscillating_equal_hubs(n),(n,equal,oscillating_equal_hubs(n))
    assert opposite==expected_opposite,(n,opposite,expected_opposite)
    print(n,equal,opposite,predicted(n))
# A structural exponential subfamily at n=5m, m>=2.
for m in range(2,7):
    n=5*m
    for pattern in range(1<<m):
        word=''.join('11110' if (pattern>>j)&1 else '11100' for j in range(m))
        bits=[int(c) for c in word]
        assert valid_equal_hubs(bits)
    assert oscillating_equal_hubs(n)>=2**m
print('FORMULA_AND_RUN_CLASSIFICATION_PASS')
