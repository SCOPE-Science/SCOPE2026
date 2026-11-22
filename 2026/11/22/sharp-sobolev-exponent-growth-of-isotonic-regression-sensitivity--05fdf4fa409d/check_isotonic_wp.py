"""Finite reproducibility checks for isotonic projection gradient-lp sensitivity."""
from fractions import Fraction
from itertools import combinations
import math, random

def partitions(n):
    for mask in range(1 << (n-1)):
        bounds=[0]+[i for i in range(1,n) if mask & (1 << (i-1))]+[n]
        yield list(zip(bounds,bounds[1:]))

def block_gradient_matrix(n, blocks):
    # Independent step-function construction of D Q D^{-1}.
    M=[[Fraction(0) for _ in range(n-1)] for _ in range(n-1)]
    for j in range(n-1):
        x=[Fraction(int(i>j)) for i in range(n)]
        y=x[:]
        for a,b in blocks:
            avg=sum(x[a:b])/ (b-a)
            for k in range(a,b): y[k]=avg
        for i in range(n-1): M[i][j]=y[i+1]-y[i]
    return M

def pava(x):
    blocks=[]
    for val in x:
        blocks.append([float(val),1])
        while len(blocks)>1 and blocks[-2][0]/blocks[-2][1] >= blocks[-1][0]/blocks[-1][1]:
            s,c=blocks.pop();blocks[-1][0]+=s;blocks[-1][1]+=c
    return [s/c for s,c in blocks for _ in range(c)]

def gradnorm(x,p):
    ds=[abs(x[i+1]-x[i]) for i in range(len(x)-1)]
    return max(ds) if p==math.inf else sum(v**p for v in ds)**(1/p)

for n in range(2,11):
    matrices=0; max_col=Fraction(0);max_row=Fraction(0)
    for bs in partitions(n):
        M=block_gradient_matrix(n,bs);matrices+=1
        assert all(v>=0 for row in M for v in row)
        row=max(sum(row) for row in M)
        col=max(sum(M[i][j] for i in range(n-1)) for j in range(n-1))
        assert row <= Fraction(n,2),(n,bs,'row')
        assert col <= 1,(n,bs,'col')
        max_col=max(max_col,col); max_row=max(max_row,row)
    assert max_col==1 and max_row==Fraction(n,2), (n,max_col,max_row)
    print(f'EXACT_PARTITIONS_AND_TWO_ENDPOINT_MATRIX_NORMS_PASS n={n} partitions={matrices}')

for n in range(3,55):
    m=n-2;M=m+3
    x=[-M]+[m-1-2*r for r in range(m)]+[M]
    h=list(range(n)); t=1.e-6
    px=pava(x); pxt=pava([x[i]+t*h[i] for i in range(n)])
    assert max(abs(px[i]-(-M if i==0 else M if i==n-1 else 0)) for i in range(n))<1.e-9
    for p in [1,1.3,2,3,8,math.inf]:
        ratio=gradnorm([pxt[i]-px[i] for i in range(n)],p)/(t*gradnorm(h,p))
        lower=((n-1)/2)**(1-1/p)
        assert abs(ratio/lower-1)<1.e-7,(n,p,ratio,lower)
    # Two-block witness for the exact W^{1,infinity} factor.
    m=n-1;x=[-M]+[m-1-2*r for r in range(m)]
    px=pava(x);pxt=pava([x[i]+t*h[i] for i in range(n)])
    ratio=gradnorm([pxt[i]-px[i] for i in range(n)],math.inf)/(t*gradnorm(h,math.inf))
    assert abs(ratio-n/2)<1.e-7,(n,ratio)
print('STRICT_ISOTONIC_WITNESSES_LOWER_AND_EXACT_INFINITY_PASS n=3..54')

rng=random.Random(137)
for n in [3,4,5,6,8,12,17,30]:
    for _ in range(300):
        x=[rng.uniform(-5,5) for _ in range(n)]
        y=[rng.uniform(-5,5) for _ in range(n)]
        px=pava(x);py=pava(y)
        for p in [1,1.3,2,4,math.inf]:
            a=gradnorm([px[i]-py[i] for i in range(n)],p)
            b=gradnorm([x[i]-y[i] for i in range(n)],p)
            assert a<=b*(n/2)**(1-1/p)+1e-9,(n,p,a,b)
print('RANDOM_TWO_INPUT_SOBOLEV_BOUND_PASS cases=2400 exponents=5')
print('ALL_ISOTONIC_WP_CHECKS_PASS')
