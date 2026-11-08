"""Standalone exact checks for three-marker Abelian-square diversity.
Run: python3 verify.py. Python standard library only.
Finite tests support, but do not replace, the all-length proof.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb
from fractions import Fraction

@lru_cache(None)
def H(A, B, g):
    assert min(A, B, g) >= 0
    return sum(max(0, min(A, B + delta) - max(0, delta) + 1)
               for delta in range(-g, g + 1, 2))

def predicted(a, b, c, d):
    p = H(a, c, b) + H(b, d, c)
    if b == c:
        p -= H(min(a, b), min(c, d), b)
    return max(a, b, c, d) // 2 + p

def direct(w):
    out = set()
    for i in range(len(w)):
        for k in range(1, (len(w) - i)//2 + 1):
            x, y = w[i:i+k], w[i+k:i+2*k]
            if x.count('1') == y.count('1'):
                out.add(x+y)
    return len(out)

checked = 0
for n in range(3, 27):
    for inds in combinations(range(n), 3):
        w = ['0'] * n
        for i in inds:
            w[i] = '1'
        a = inds[0]
        b = inds[1] - inds[0] - 1
        c = inds[2] - inds[1] - 1
        d = n - inds[2] - 1
        assert predicted(a, b, c, d) == direct(''.join(w)), (w, a,b,c,d)
        checked += 1
print('DIRECT_DISTINCT_AB_SQUARES_OK', checked)

# Independent formal power-series arithmetic checks of the rational formula.
N = 23

def conv(A, B):
    return [sum(A[j]*B[i-j] for j in range(i+1)) for i in range(N)]
def add(*L):
    return [sum(A[i] for A in L) for i in range(N)]
def scale(A,c): return [c*x for x in A]
def shift(A,k): return [0]*k + A[:N-k] if k<N else [0]*N
def invminus(k): return [int(i%k == 0) for i in range(N)]
def invplus(k): return [(-1)**(i//k) if i%k==0 else 0 for i in range(N)]
def prod(*L):
    result=[1]+[0]*(N-1)
    for x in L: result=conv(result,x)
    return result
pm1=invminus(1); pp1=invplus(1)
Z=prod(pm1,pm1,pm1,pm1,add(*[
    scale(shift(invminus(2*j),2*j),(-1)**(j+1)*comb(4,j))
    for j in range(1,5)]))
F=prod(add([1]+[0]*(N-1),shift([1]+[0]*(N-1),2)),
       pm1,pm1,pm1,invminus(2),invminus(2),invminus(2))
U=prod(pm1,pm1,add(invminus(2),scale(shift(invminus(3),1),-2),shift(invminus(4),2)))
V=prod(pp1,pp1,add(invplus(2),scale(shift(invminus(3),1),2),shift(invplus(4),2)))
O=scale(prod(pm1,pm1,add(U,V)),Fraction(1,2))
GF=add(Z,scale(F,2),scale(O,-1))
for m in range(N):
    brute_sum=sum(predicted(a,b,c,m-a-b-c) for a in range(m+1)
                   for b in range(m-a+1) for c in range(m-a-b+1))
    assert GF[m] == brute_sum, (m,GF[m],brute_sum)
print('RATIONAL_ALL_LENGTH_GF_OK',N)
# Independent rational evaluation of the Dirichlet moment expression.
E_AB=Fraction(1,20)
E_AminusG_sq=Fraction(1,20)
E_AminusBminusG_sq=Fraction(1,40)
E_J=E_AB-(2*E_AminusG_sq-2*E_AminusBminusG_sq)/2
assert E_J == Fraction(1,40)
print('LIMITING_MEAN_OK', E_J)
