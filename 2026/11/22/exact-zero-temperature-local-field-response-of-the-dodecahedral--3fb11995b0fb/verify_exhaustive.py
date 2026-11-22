#!/usr/bin/env python3
"""Independent exhaustive spin enumeration and exact susceptibility characteristic polynomial."""
from collections import Counter, deque
from math import comb

EDGES = [(0,1),(0,10),(0,19),(1,2),(1,8),(2,3),(2,6),(3,4),(3,19),(4,5),(4,17),(5,6),(5,15),(6,7),(7,8),(7,14),(8,9),(9,10),(9,13),(10,11),(11,12),(11,18),(12,13),(12,16),(13,14),(14,15),(15,16),(16,17),(17,18),(18,19)]
N=20
mins=31
winners=[]
for mask in range(1<<N):
    bad=sum((((mask>>u)^(mask>>v))&1)==0 for u,v in EDGES)
    if bad<mins: mins=bad;winners=[]
    if bad==mins: winners.append(mask)
assert mins==6 and len(winners)==250,(mins,len(winners))
assert Counter(2*m.bit_count()-N for m in winners)=={-4:5,0:240,4:5}
C=[[sum((1 if ((m>>a)^(m>>b))&1==0 else -1) for m in winners) for b in range(N)] for a in range(N)]
# Standard-library Newton power-trace characteristic polynomial calculation (20x20 exact integer).
def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
trace=[0]
powmat=[[int(i==j) for j in range(N)] for i in range(N)]
for k in range(1,N+1):
    powmat=mm(powmat,C)
    trace.append(sum(powmat[i][i] for i in range(N)))
coeff=[1]
for k in range(1,N+1):
    num=-sum(coeff[k-i]*trace[i] for i in range(1,k+1))
    assert num%k==0
    coeff.append(num//k)

def multiply(f,g):
    h=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g):h[i+j]+=a*b
    return h
expected=[1]
for f,exp in [([1,-408],4),([1,-72],4),([1,-48],5),([1,-8],1),([1,-944,22784],3)]:
    for _ in range(exp): expected=multiply(expected,f)
assert coeff==expected
print('PASS: exhaustive 2^20 spin states; minimum energy -18 with 250 minimizers')
print('PASS: 20x20 exact integer correlation-numerator characteristic polynomial')
print('Char poly: (x-408)^4 (x-72)^4 (x-48)^5 (x-8) (x^2-944x+22784)^3')
