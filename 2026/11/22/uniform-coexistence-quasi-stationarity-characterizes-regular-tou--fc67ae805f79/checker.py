"""Exact algebraic checks for a killed tournament Wright--Fisher diffusion.

The mathematical proof establishes every dimension; these tests check
independent polynomial identities in finite representative dimensions.
"""
from fractions import Fraction
from itertools import product

assertions=0

def check(b):
    global assertions
    assert b
    assertions += 1

def tournament(d):
    A=[[0]*d for _ in range(d)]
    for i in range(d):
        for j in range(i+1,d):
            sign = 1 if (i-j)%d <= (d-1)//2 else -1
            A[i][j]=sign; A[j][i]=-sign
    return A

for d in (3,5,7,9):
    A=tournament(d)
    check(all(sum(row)==0 for row in A))
    check(all(A[i][j] == -A[j][i] for i in range(d) for j in range(d)))
    for k in range(1,25):
        x=[Fraction(k+i+1, sum(k+j+1 for j in range(d))) for i in range(d)]
        y=[sum(A[i][j]*x[j] for j in range(d)) for i in range(d)]
        check(sum(y)==0)
        check(sum(x[i]*y[i] for i in range(d))==0)
        check(sum(x[i]*(1/x[i]-d) for i in range(d))==0)
        # Selection generator acting on the diversity product is zero.
        h=Fraction(1)
        for v in x: h*=v
        check(h*sum(y)==0)
    # Sum of second derivatives of the covariance matrix in affine coordinates.
    m=d-1
    second_derivative_sum=-2*m-m*(m-1)
    check(second_derivative_sum==-d*(d-1))

# Enumeration of every tournament on 2..5 vertices:
# balancing is equivalent to equal in- and out-degrees and requires odd d.
counts={}
for d in (2,3,4,5):
    edges=[(i,j) for i in range(d) for j in range(i+1,d)]
    regular=0
    for signs in product((1,-1),repeat=len(edges)):
        A=[[0]*d for _ in range(d)]
        for (i,j),s in zip(edges,signs): A[i][j]=s;A[j][i]=-s
        row=[sum(a) for a in A]
        balanced=all(v==0 for v in row)
        check(balanced == (all(sum(a>0 for a in A[i])==(d-1)//2 for i in range(d)) and d%2==1))
        if balanced: regular+=1
    counts[d]=regular
check(counts=={2:0,3:2,4:0,5:24})

print('PASS:',assertions,'exact integer/rational assertions')
print('regular tournament counts:',counts)
print('finite polynomial cancellations and tournament regularity checked')
