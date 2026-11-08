#!/usr/bin/env python3
"""Exact tests for the Frobenius number of quotients of three consecutive generators."""
from fractions import Fraction


def proposed(a, p):
    eps = a & 1
    t = (a-eps)//2
    for j in range((p+2)//2+1):
        r = ((t-j)*a-1) % p
        if r <= eps+2*j:
            return ((t-j)*a-1-r)//p, eps+2*j, r, j
    raise AssertionError(('no top interval',a,p))


def independent_dp(a, p):
    # No gap intervals or formula used; ordinary unrestricted coin DP.
    upper = 1+(a*(a+1))
    reach = bytearray(upper)
    reach[0]=1
    for coin in (a,a+1,a+2):
        for n in range(coin,upper):
            if reach[n-coin]: reach[n]=1
    # All n beyond a*(a+1) belong to <a,a+1>, hence <a,a+1,a+2>.
    ans = max((n//p for n in range(p,upper,p) if not reach[n]), default=-1)
    return ans

cases=0
for p in range(2,42):
    for a in range(2*p+4,172):
        predicted = proposed(a,p)[0]
        actual = independent_dp(a,p)
        assert predicted==actual, (a,p,predicted,actual)
        cases+=1
print('DIRECT_DP_MATCH',cases,'p=2..41','2*p+4<=a<172')

# Exact polynomial in a, obtained directly from symbolic formula for each residue.
# (B,R) is invariant modulo 2p. Test both against further direct evaluations.
branch_tests=0
minimality_tests=0
for p in range(2,121):
    K=2*p
    patterns=[]
    for r in range(K):
        a=r+K*20
        v,B,R,j=proposed(a,p)
        poly=(Fraction(1,2*p), Fraction(-B,2*p), Fraction(-(1+R),p))
        patterns.append((B,R))
        for m in (21,23,29):
            A=r+K*m
            assert proposed(A,p)[0] == poly[0]*A*A + poly[1]*A + poly[2]
            branch_tests+=1
    # Check period by exhaustively inspecting every shift dividing 2p.
    divs=[d for d in range(1,K+1) if K%d==0]
    min_period=next(d for d in divs if all(patterns[i]==patterns[(i+d)%K] for i in range(K)))
    assert min_period==K,(p,min_period)
    # The special two-residue branch signature asserted in the proof.
    signatures=[i for i in range(K) if patterns[i]==patterns[0]]
    expected=[0,p] if p%2==0 else [0,p-1]
    assert signatures==expected,(p,signatures,expected)
    minimality_tests+=1
print('QUADRATIC_BRANCH_IDENTITIES_OK',branch_tests)
print('LEAST_PERIODS_EXACT_OK',minimality_tests,'p=2..120')

for p,a in [(2,26),(3,47),(4,58),(5,71),(7,85),(11,105)]:
    F,B,R,j=proposed(a,p)
    print('SAMPLE',p,a,'F',F,'B',B,'R',R,'j',j)
print('VERIFY_OK finite_tests_only=True proof_separate=True independent_audit=False')
