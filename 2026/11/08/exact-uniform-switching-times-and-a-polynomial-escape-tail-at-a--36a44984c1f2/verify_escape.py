"""Exact independent interval calculation for two open negative-doubling maps."""
from fractions import Fraction as F

def intersect_intervals(left, right):
    out=[]
    for a,b in left:
        for c,d in right:
            e,f=max(a,c),min(b,d)
            if e<f:out.append((e,f))
    return out

def merge(intervals):
    intervals=sorted(intervals)
    result=[]
    for a,b in intervals:
        if result and a<=result[-1][1]:
            result[-1]=(result[-1][0],max(b,result[-1][1]))
        else:result.append((a,b))
    return result

def inverse_image(intervals):
    out=[]
    for a,b in intervals:
        # x in [0,1/2], T(x)=1-2x; x in [1/2,1], T(x)=2-2x.
        out.extend([((1-b)/2,(1-a)/2),((2-b)/2,(2-a)/2)])
    return out

def survive(a,n):
    safe=[(F(0),a),(1-a,F(1))]
    intervals=safe
    for _ in range(n-1):
        intervals=merge(intersect_intervals(inverse_image(intervals),safe))
    return intervals

def length(intervals):return sum((b-a for a,b in intervals),F(0))

def matrix_multiply(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B)))) for j in range(len(B[0]))] for i in range(len(A))]

def power(A,n):
    I=[[int(i==j) for j in range(len(A))] for i in range(len(A))]
    while n:
        if n&1:I=matrix_multiply(I,A)
        A=matrix_multiply(A,A)
        n//=2
    return I

A=[[0,0,1,1],[0,1,0,0],[0,0,1,0],[1,1,0,0]]
B=[[0,1],[1,0]]
for n in range(1,26):
    mat=power(A,n-1)
    terminal=[sum(row[j] for row in mat) for j in range(4)]
    initial=[sum(row) for row in mat]
    assert terminal==[1,n,n,1], (n,terminal)
    assert initial==[n,1,1,n], (n,initial)
    p=length(survive(F(2,5),n))
    assert p==F(4*(n+1),5*2**n),(n,p)
    q=length(survive(F(1,3),n))
    assert q==F(4,3*2**n),(n,q)
    assert sum(sum(row) for row in power(B,n-1))==2
# Count all admissible Markov itineraries by the first visit to an inner cell.
for n in range(1,26):
    paths=[(j,) for j in range(4)]
    for _ in range(n-1):
        paths=[p+(j,) for p in paths for j in range(4) if A[p[-1]][j]]
    switches=[next((k for k,j in enumerate(p) if j in (1,2)),n) for p in paths]
    assert len(paths)==2*(n+1)
    assert [switches.count(k) for k in range(n+1)]==[2]*(n+1),(n,switches)
# terminal conditional distribution: exact total variation to its 2-inner-cell limit
for n in range(1,26):
    p=[F(k,2*(n+1)) for k in (1,n,n,1)]
    q=[F(0),F(1,2),F(1,2),F(0)]
    tv=sum((abs(x-y) for x,y in zip(p,q)),F(0))/2
    assert tv==F(1,n+1)
print('VERIFY_OK independent_exact_interval_horizons=1..25 matrix_terminal_initial=1..25 conditional_TV=1..25')
