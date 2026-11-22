"""Standalone finite checks for the Narayana congruence theorem.
All general assertions are proved symbolically in RESULT.md; loops below are checks.
"""
from collections import Counter

def mm(A, B, modulus=None):
    C=[[sum(A[i][q]*B[q][j] for q in range(3)) for j in range(3)] for i in range(3)]
    if modulus is not None:
        C=[[v%modulus for v in row] for row in C]
    return C

def mpow(A, n, modulus=None):
    R=[[int(i==j) for j in range(3)] for i in range(3)]
    while n:
        if n&1: R=mm(R,A,modulus)
        A=mm(A,A,modulus)
        n//=2
    return R

def mv(A,v): return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]

M=[[0,1,0],[0,0,1],[1,0,1]]
I=[[int(i==j) for j in range(3)] for i in range(3)]
P=mpow(M,8)
assert P==[[4,3,6],[6,4,9],[9,6,13]]
assert all((P[i][j]-I[i][j])%3==0 for i in range(3) for j in range(3))
B=[[(P[i][j]-I[i][j])//3 for j in range(3)] for i in range(3)]
assert B==[[1,1,2],[2,1,3],[3,2,4]]
v0=[0,1,1]
expected_c=[3,4,6,9,13,19,28,41]
assert [mv(mpow(M,r),mv(B,v0))[0] for r in range(8)]==expected_c
assert all(expected_c[r]%3 in (1,2) for r in (1,4,5,6,7))

for j in range(10):
    mod=3**(j+2)
    actual=mpow(P,3**j,mod)
    target=[[(I[i][h]+3**(j+1)*B[i][h])%mod for h in range(3)] for i in range(3)]
    assert actual==target, ('matrix lifting',j)

# Separate scalar recurrence, without matrix multiplication.
def seq_mod(N,mod):
    arr=[0,1,1]
    for n in range(3,N):arr.append((arr[n-1]+arr[n-3])%mod)
    return [x%mod for x in arr[:N]]

total_checked=0
for k in range(1,9):
    mod=3**k
    period=8*3**(k-1)
    a=seq_mod(period+3,mod)
    assert a[:3]==a[period:period+3],('period',k)
    # Certify least period by direct state return, not just by divisors.
    assert not any(a[i:i+3]==a[:3] for i in range(1,period)),('least',k)
    assert set(a[:period])==set(range(mod)),('residue completeness',k)
    C=Counter(a[:period])
    assert all(C[x]==1 for x in range(2,mod,3)),('exact unique fibres',k)
    assert all(C[x]>=2 for x in range(mod) if x%3!=2),('minimum fibres',k)
    for r in (1,4,5,6,7):
        sub=[a[r+8*t] for t in range(3**(k-1))]
        assert len(set(sub))==3**(k-1),('isometry finite image',k,r)
        assert set(sub)=={x for x in range(mod) if x%3==a[r]%3}
    total_checked+=period
    print(f'k={k} modulus={mod} least_period={period} distinct_residues={len(C)} class2_all_unique=true')

# Exact integer differences on independent indices (not modular residues).
A=[0,1,1]
for n in range(3,8*55+8):A.append(A[-1]+A[-3])
def v3(v):
    if v==0:return None
    j=0
    while v%3==0: v//=3;j+=1
    return j
pair_checks=0
for r in (1,4,5,6,7):
    for t in range(55):
        for s in range(t):
            assert v3(A[8*t+r]-A[8*s+r])==1+v3(t-s),('integer valuation',r,s,t)
            pair_checks+=1
print('PASS',f'scalar_terms={total_checked}',f'exact_integer_pair_checks={pair_checks}', 'matrix_power_tests=10')
