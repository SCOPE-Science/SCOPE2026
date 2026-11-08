"""Exact arithmetic sanity checks for dyadic Tribonacci power-window valuations.

These are bounded checks; the general theorem relies on the algebraic proof.
"""
from math import gcd

def val2(x):
    if x == 0:
        return float('inf')
    return (x & -x).bit_length() - 1

def expected(r, e):
    return 0 if r == 1 else 1 if r == 2 else r - 1 if e % 2 == 0 else r - 2

# Modular independent representation of the original recurrence.
MOD = 1 << 16
T = [0, 0, 1]
for j in range(3, 2200):
    T.append(sum(T[-3:]) % MOD)
assert [x % 2 for x in T[:16]] == ([0,0,1,1] * 4)
assert [T[j+4] % 2 for j in range(2100)] == [T[j] % 2 for j in range(2100)]

cases = 0
for e in range(3, 34):
    V = [pow(t, e, MOD) for t in T]
    ps = [0]
    for w in V:
        ps.append((ps[-1] + w) % MOD)
    for r in range(1, 11):
        target = expected(r,e)
        got = []
        for n in range(80):
            v = (ps[n+(1<<r)] - ps[n]) % MOD
            assert val2(v) >= target, (e,r,n,v,target)
            if e%2 == 0 and r>=3:
                assert val2(v)==target, ('even',e,r,n,v,target)
            got.append(v)
            cases +=1
        assert min(map(val2,got)) == target, (e,r,target,got[:10])
        if e%2 and r>=3:
            assert val2(got[0]) == target

# Independent unbounded-integer recurrence (not just mod 2^16), checking base windows.
X=[0,0,1]
for n in range(3,180):X.append(X[-1]+X[-2]+X[-3])
exact=0
for e in range(3,10):
    for r in range(1,7):
        K=1<<r
        sums=[sum(pow(X[n+j],e) for j in range(K)) for n in range(25)]
        g=0
        for a in sums: g=gcd(g,a)
        assert val2(g)==expected(r,e), (e,r,g)
        exact+=len(sums)

print(f'VERIFY_OK modular_windows={cases} exact_integer_windows={exact} exponents=3..33 dyadic_r=1..10 starts=0..79')
