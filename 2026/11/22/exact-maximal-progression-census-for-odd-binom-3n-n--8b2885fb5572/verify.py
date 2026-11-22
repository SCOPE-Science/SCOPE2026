#!/usr/bin/env python3
"""Exact finite-state certificate for maximal arithmetic progressions in fibbinary integers."""
from collections import deque, defaultdict
from math import comb

ZERO = (0,0,0,0,0)

def next_states(s):
    c1,c2,px,py,pz = s
    choices = defaultdict(int)
    for abit in (0,1):
        for dbit in (0,1):
            mid = abit + dbit + c1
            ybit, nc1 = mid%2, mid//2
            top = ybit + dbit + c2
            zbit, nc2 = top%2, top//2
            if (px and abit) or (py and ybit) or (pz and zbit):
                continue
            choices[(nc1,nc2,abit,ybit,zbit)] += 1
    return choices

S = {ZERO}
queue = deque([ZERO])
while queue:
    q = queue.popleft()
    for t in next_states(q):
        if t not in S:
            S.add(t); queue.append(t)
S = sorted(S)
n = len(S)
assert n == 8, (n,S)
M = [[next_states(s).get(t,0) for t in S] for s in S]
U = [int(s == ZERO) for s in S]
V = [int(s[0] == 0 and s[1] == 0) for s in S]

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def matpow(A,k):
    I = [[int(i==j) for j in range(n)] for i in range(n)]
    ans = I
    while k:
        if k&1: ans = matmul(ans,A)
        A = matmul(A,A); k>>=1
    return ans

def mulrow(row,A):
    return [sum(row[i]*A[i][j] for i in range(n)) for j in range(n)]

def dot(row,col):
    return sum(x*y for x,y in zip(row,col))

# The annihilating polynomial of the initial row (not merely a guessed scalar recurrence):
# Q(X) = (X^2-X-1)(X^4-X^3-3X^2+2)
Qcoeff = [-2,-2,5,4,-3,-2,1]
for j in range(n):
    assert sum(Qcoeff[k]*mulrow(U,matpow(M,k))[j] for k in range(7)) == 0

F = []
row = U[:]
for r in range(28):
    F.append(dot(row,V))
    row = mulrow(row,M)
assert F[:6] == [1,2,4,7,15,29], F[:6]
Pcoeff = [1,-2,-3,4,5,-2,-2]
for r in range(6,28):
    assert sum(Pcoeff[k]*F[r-k] for k in range(7)) == 0
# P(z)F(z) = 1-3z^2-3z^3+2z^4+2z^5.
Ncoeff = [1,0,-3,-3,2,2]
for r in range(28):
    assert sum(Pcoeff[k]*F[r-k] for k in range(min(6,r)+1)) == (Ncoeff[r] if r < 6 else 0)

# Subtract d=0 (Fibonacci word count) to get nonconstant three-term progressions.
fib=[1,2]
for i in range(2,29): fib.append(fib[-1]+fib[-2])
A=[F[r]-fib[r] for r in range(28)]
assert A[:15] == [0,0,1,2,7,16,40,92,211,476,1063,2362,5218,11496,25257]
for r in range(28):
    # P(z) A(z) = z^2, hence exact numerator.
    assert sum(Pcoeff[k]*A[r-k] for k in range(min(6,r)+1)) == int(r==2)

# Independent finite check: enumerate triples with no use of the automaton.
for r in range(0,13):
    N=1<<r
    vals=[j for j in range(N) if not (j&(j>>1))]
    yes=set(vals)
    count=sum(a+2*(b-a) in yes for a in vals for b in vals if b>a and a+2*(b-a)<N)
    assert count==A[r], (r,count,A[r])
    # No four-term progression: a parity/4-adic proof handles all r, this is a test.
    assert all(a+3*(b-a) not in yes or a+2*(b-a) not in yes
               for a in vals for b in vals if b>a and a+3*(b-a)<N)

# C(3n,n) is odd exactly at fibbinary n (Kummer's theorem, two-adic carries).
for k in range(80):
    assert (comb(3*k,k)%2==1) == (k&(k>>1)==0)

print('PASS: 8-state transition matrix; row annihilator; all-coefficient rational identity;')
print('       28 dyadic depths; independent enumeration through 2^12;')
print('       four-term finite checks and 80 binomial-parity checks.')
print('Three-term counts r=0..14:',A[:15])
print('Reachable states:',S)
print('Transition matrix:',M)
