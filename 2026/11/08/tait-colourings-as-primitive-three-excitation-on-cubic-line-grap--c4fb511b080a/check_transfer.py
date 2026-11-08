"""Standalone nine-state strip seam transfer check (standard Python only)."""
from itertools import product

pairs=list(product(range(3),repeat=2))
T=[[int(a!=c and b!=d and {a,c}=={b,d}) for c,d in pairs] for a,b in pairs]
P=[[int((a,b)==(d,c)) for c,d in pairs] for a,b in pairs]

def mult(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def trace(A): return sum(A[i][i] for i in range(len(A)))

assert all(sum(row)==(2 if pairs[i][0]==pairs[i][1] else 1) for i,row in enumerate(T))
Q=[[int(i==j) for j in range(9)] for i in range(9)]
for n in range(1,21):
    Q=mult(Q,T)
    if n>=3:
        straight=trace(Q)
        twisted=trace(mult(Q,P))
        expect_straight=2**n+3+5*(-1)**n
        expect_twisted=2**n+3-(-1)**n
        assert (straight,twisted)==(expect_straight,expect_twisted),(n,straight,twisted)
        assert straight-twisted==6*(-1)**n
        print(f"n={n}: straight={straight}; twisted={twisted}; difference={straight-twisted}")
print('PASS: nine-state transfer, parity seam and formulas for n=3..20')
