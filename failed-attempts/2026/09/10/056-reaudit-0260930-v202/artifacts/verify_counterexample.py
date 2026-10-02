#!/usr/bin/env python3
"""Replay verification for the q=11 counterexample to the target claim.

Target claim: for every prime power q = 3 mod 4, q >= 11, the word map
w(x,y,z) = [x,y]^2 z^3 on PSL(2,q) misses the unipotent class U_q.
This script verifies a single explicit triple (X,Y,Z) in SL(2,11) whose
word value equals the representative u = [[1,1],[0,1]] in PSL(2,11),
disproving the universal claim. Pure stdlib.
"""
q = 11

X = (4, 0, 6, 3)
Y = (2, 10, 10, 1)
Z = (2, 10, 3, 10)
U = (1, 1, 0, 1)          # nontrivial unipotent representative
MINUS_U = (10, 10, 0, 10)  # -U mod 11


def mul(A, B):
    return ((A[0]*B[0]+A[1]*B[2]) % q, (A[0]*B[1]+A[1]*B[3]) % q,
            (A[2]*B[0]+A[3]*B[2]) % q, (A[2]*B[1]+A[3]*B[3]) % q)


def det(A):
    return (A[0]*A[3]-A[1]*A[2]) % q


def inv(A):
    assert det(A) == 1, "not in SL(2,q)"
    return (A[3], (-A[1]) % q, (-A[2]) % q, A[0])


def neg(A):
    return ((-A[0]) % q, (-A[1]) % q, (-A[2]) % q, (-A[3]) % q)


def mat_pow(A, n):
    R = (1, 0, 0, 1)
    B = A
    while n:
        if n & 1:
            R = mul(R, B)
        B = mul(B, B)
        n >>= 1
    return R


def fmt(A):
    return "[[%d,%d],[%d,%d]]" % A


# 1. q is in the claimed family
assert q % 4 == 3 and q >= 11, "q not in target family"
# 2. entries are valid lifts
for M in (X, Y, Z):
    assert det(M) == 1, "triple member not in SL(2,11): %s" % (M,)
# 3. U is a nontrivial unipotent (trace 2, not +/-I)
assert (U[0]+U[3]) % q == 2 and U not in ((1, 0, 0, 1), (10, 0, 0, 10))
# 4. word value with [x,y] = x y x^{-1} y^{-1}
C = mul(mul(X, Y), mul(inv(X), inv(Y)))
assert C == (10, 5, 0, 10), "commutator mismatch: %s" % fmt(C)
C2 = mul(C, C)
assert C2 == U, "commutator square mismatch: %s" % fmt(C2)
Z3 = mat_pow(Z, 3)
assert Z3 == (10, 0, 0, 10), "Z^3 mismatch: %s" % fmt(Z3)
W = mul(C2, Z3)
assert W == MINUS_U, "word value mismatch: %s" % fmt(W)
# 5. W equals U in PSL(2,11) (differ by central sign only)
assert W == neg(U) and W != U, "not a PSL identification"
print("X =", fmt(X), "det =", det(X))
print("Y =", fmt(Y), "det =", det(Y))
print("Z =", fmt(Z), "det =", det(Z))
print("[X,Y] =", fmt(C))
print("[X,Y]^2 =", fmt(C2))
print("Z^3 =", fmt(Z3))
print("w(X,Y,Z) =", fmt(W), "= -U ~ U in PSL(2,11)")
print("VERIFY_OK")
