#!/usr/bin/env python3
"""Exact sparse-polynomial check for the weighted three-leaf star Gauss map.
Uses only the Python standard library. No approximate arithmetic is used.
"""
from itertools import permutations
from fractions import Fraction
from math import prod as product_integers

ZERO = (0, 0, 0, 0)  # powers of (h,a,b,c)

def scalar(v):
    return {ZERO: int(v)} if v else {}

def variable(j):
    e = list(ZERO); e[j] = 1
    return {tuple(e): 1}

def add(*terms):
    result = {}
    for t in terms:
        for key, val in t.items():
            result[key] = result.get(key, 0) + val
    return {k:v for k,v in result.items() if v}

def neg(a):
    return {k:-v for k,v in a.items()}

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    result = {}
    for x,u in a.items():
        for y,v in b.items():
            k = tuple(i+j for i,j in zip(x,y))
            result[k] = result.get(k,0)+u*v
    return {k:v for k,v in result.items() if v}

def prod(*terms):
    ans=scalar(1)
    for p in terms: ans=mul(ans,p)
    return ans

def scale(a,c):
    return {k:c*v for k,v in a.items() if c*v}

def square(a): return mul(a,a)

def matrix_mul(X,Y):
    return [[add(*(mul(X[i][k],Y[k][j]) for k in range(len(Y))))
             for j in range(len(Y[0]))] for i in range(len(X))]

def det(M):
    n=len(M); total={}
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        total=add(total,scale(prod(*(M[i][p[i]] for i in range(n))), -1 if inv%2 else 1))
    return total

def minor(M,r,c): return [[M[i][j] for j in range(len(M)) if j!=c] for i in range(len(M)) if i!=r]

def transition_numerator(M,N,i,j):
    # Entry ij of adj(M)N, without dividing by det(M).
    return add(*(scale(mul(det(minor(M,k,i)),N[k][j]),(-1)**(i+k)) for k in range(len(M))))

h,a,b,c=[variable(i) for i in range(4)]
L=[[add(a,b,c), neg(a),neg(b),neg(c)],
   [neg(a),a,{},{}], [neg(b),{},b,{}], [neg(c),{},{},c]]
L2=matrix_mul(L,L)
I=[[scalar(1 if i==j else 0) for j in range(4)] for i in range(4)]
M=[[add(prod(square(h),L2[i][j]),scale(prod(h,L[i][j]),6),scale(I[i][j],12)) for j in range(4)] for i in range(4)]
N=[[add(prod(square(h),L2[i][j]),scale(prod(h,L[i][j]),-6),scale(I[i][j],12)) for j in range(4)] for i in range(4)]

weights=[a,b,c]
for i,x in enumerate(weights):
    others=[weights[j] for j in range(3) if j!=i]; y,z=others
    C=sub(scale(prod(y,z),3),mul(x,add(y,z)))
    A=add(prod(y,z,C,prod(square(h),square(h))),
          scale(prod(y,z,sub(add(y,z),x),prod(square(h),h)),12),
          scale(prod(sub(add(scale(square(y),2),scale(mul(y,z),3),scale(square(z),2)),mul(x,add(y,z))),square(h)),12),
          scale(prod(add(y,z),h),72),scalar(144))
    expected=scale(prod(x,h,A),144)
    actual=transition_numerator(M,N,0,i+1)
    assert actual==expected, ('hub',i,sub(actual,expected))
    print('HUB_LEAF_OK',i+1,len(actual))
for i in range(3):
    for j in range(i+1,3):
        x,y=weights[i],weights[j]; z=weights[3-i-j]
        B=add(prod(z,sub(scale(prod(z,add(x,y)),3),mul(x,y)),prod(square(h),h)),
              scale(prod(z,add(x,y,z),square(h)),12),
              scale(prod(add(x,y,scale(z,2)),h),24),scalar(72))
        expected=scale(prod(x,y,square(h),B),144)
        actual=transition_numerator(M,N,i+1,j+1)
        assert actual==expected, ('leaf_pair',i,j,sub(actual,expected))
        print('LEAF_LEAF_OK',i+1,j+1,len(actual))

# Explicit out-of-cone witness at (a,b,c)=(4,1,1), h=8.
def eval_poly(p,values):
    return sum(v*product_integers(values[j]**k for j,k in enumerate(key)) for key,v in p.items())
D=det(M)
num=transition_numerator(M,N,0,1)
v={ 'x': Fraction(eval_poly(num,(8,4,1,1)),eval_poly(D,(8,4,1,1))) }
assert v['x']==Fraction(-6240,106309), v
print('OUTSIDE_CONE_WITNESS_OK',v['x'])
print('EXACT_POLYNOMIAL_IDENTITIES_OK')
