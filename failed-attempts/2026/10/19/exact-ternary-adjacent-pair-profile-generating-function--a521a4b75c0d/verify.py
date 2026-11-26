#!/usr/bin/env python3
"""Check finite coefficients of the ternary linear bigram-profile generating function."""
from itertools import product
from math import comb

ORDER = 14  # coefficients through z^13, i.e. lengths 1..14

def convolve(a, b):
    return [sum(a[i] * b[k-i] for i in range(k+1)) for k in range(ORDER)]

def inv_binomial(step, power):
    a = [0] * ORDER
    for k in range(ORDER):
        if k % step == 0:
            a[k] = comb(k // step + power-1, power-1)
    return a

def shift(a, k):
    return [0]*k + a[:ORDER-k]

u = inv_binomial(1,3)
v = inv_binomial(2,3)
w = inv_binomial(3,1)
g = convolve(convolve(u,v),w)
h = convolve(u,inv_binomial(2,1))
B = [g[k]+(g[k-3] if k>=3 else 0) for k in range(ORDER)]
A = [g[k-1] if k>=1 else 0 for k in range(ORDER)]
A = [A[k]+(g[k-2] if k>=2 else 0) for k in range(ORDER)]
Q = []
for k in range(ORDER):
    q = B[k]+6*A[k]-u[k]+(1 if k==0 else 0)+(3 if k>=1 else 0)
    q -= (3*h[k-3] if k>=3 else 0) + (6*h[k-2] if k>=2 else 0)
    Q.append(q)

# Independent test: enumerate word profiles directly, without the graph formula.
for n in range(1, 10):
    observed = set()
    for word in product(range(3), repeat=n):
        c = [0]*9
        for left,right in zip(word,word[1:]):
            c[3*left+right] += 1
        observed.add(tuple(c))
    assert len(observed) == Q[n-1], ("word",n,len(observed),Q[n-1])

# Second independent test: enumerate matrices and test Euler-trail existence.
def compositions(total, parts):
    if parts==1:
        yield (total,)
    else:
        for x in range(total+1):
            for rest in compositions(total-x,parts-1):
                yield (x,)+rest

def realizes_profile(c):
    N=sum(c)
    if N==0:
        return True
    b = [sum(c[3*i+j] for j in range(3))
         -sum(c[3*j+i] for j in range(3)) for i in range(3)]
    if b != [0,0,0] and sorted(b) != [-1,0,1]:
        return False
    active={i for i in range(3) if any(c[3*i+j] or c[3*j+i] for j in range(3))}
    visited={min(active)}
    stack=list(visited)
    while stack:
        i=stack.pop()
        for j in range(3):
            if j in active and j not in visited and (c[3*i+j] or c[3*j+i]):
                visited.add(j)
                stack.append(j)
    return visited==active

for N in range(0, 13):
    count=sum(realizes_profile(c) for c in compositions(N, 9))
    assert count==Q[N], ("matrix",N,count,Q[N])

# Check equivalent reduced rational identity as a formal series.
def polynomial_multiply(a,b):
    return convolve(a,b)

def polynomial_pow(a,power):
    result=[1]+[0]*(ORDER-1)
    for _ in range(power):
        result=polynomial_multiply(result,a)
    return result

D=polynomial_multiply(polynomial_multiply(
    polynomial_pow([1,-1]+[0]*(ORDER-2),7),
    polynomial_pow([1,1]+[0]*(ORDER-2),2)),
    [1,1,1]+[0]*(ORDER-3))
num=[1,5,-8,8,13,-4,-10,-8,11,2,-5,2]
assert polynomial_multiply(D,Q)==num+[0]*(ORDER-len(num))
assert Q[:13]==[1,9,24,65,156,342,683,1272,2226,3708,5919,9120,13625]
print('VERIFY_OK: word enumeration n<=9, direct Eulerian profile enumeration n<=13, rational identity')
