#!/usr/bin/env python3
"""Check the path stable-extension pair-distance generating function.

Pure Python 3, standard library only; exact integer polynomial arithmetic.
The infinite identity follows from the displayed six-state transfer and
Cayley-Hamilton; finite brute force tests are additional checks.
"""
from itertools import permutations
from collections import Counter
from math import prod

# Polynomial z-coefficients; empty tuple is zero, (1,) is one.
def trim(a):
    a=list(a)
    while a and a[-1]==0: a.pop()
    return tuple(a)
def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a): return tuple(-v for v in a)
def mul(a,b):
    if not a or not b: return ()
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j]+=v*w
    return trim(c)
def scale(a,k): return trim([k*v for v in a])
Z=(); ONE=(1,); ZZ=(0,1)
# The matrix derived by swapping the two bit lanes of the paired word automaton.
Q=[[Z,Z,ONE,Z,Z,Z],
   [Z,Z,Z,Z,ZZ,Z],
   [Z,Z,Z,Z,Z,ONE],
   [Z,ONE,ONE,Z,Z,Z],
   [Z,Z,Z,ZZ,ZZ,Z],
   [ONE,(2,),ONE,Z,Z,Z]]
ALPHA=[1,2,1,0,0,0]
BETA=[1,0,0,1,0,1]

def reachable_coeffs(n):
    a=[(v,) if v else Z for v in ALPHA]
    out=[ONE]
    for k in range(1,n+1):
        a=[sum_polys(mul(a[i],Q[i][j]) for i in range(6)) for j in range(6)]
        out.append(sum_polys(scale(a[i],BETA[i]) for i in range(6)))
    return out

def sum_polys(ps):
    r=Z
    for p in ps:r=add(r,p)
    return r

def determinant_in_x():
    # Compute the determinant of I-xQ exactly over Z[z][x].
    ans=[Z for _ in range(7)]
    for perm in permutations(range(6)):
        inversions=sum(perm[i]>perm[j] for i in range(6) for j in range(i+1,6))
        terms=[ONE]
        for i,j in enumerate(perm):
            # Each factor is delta_ij - x Q_ij.
            updated=[Z]*(len(terms)+1)
            for d,p in enumerate(terms):
                if i==j:updated[d]=add(updated[d],p)
                updated[d+1]=add(updated[d+1],neg(mul(p,Q[i][j])))
            terms=updated
        for d,p in enumerate(terms):
            ans[d]=add(ans[d],p if inversions%2==0 else neg(p))
    return ans

# Numerator N(x,z) and denominator D(x,z) of the claimed rational series.
N=[ONE,add(ONE,neg(ZZ)),add(add(ONE,neg(ZZ)),scale(mul(ZZ,ZZ),2)),
   neg(add(ZZ,mul(ZZ,ZZ))),mul(ZZ,ZZ),neg(mul(ZZ,ZZ)),Z]
D=[ONE,neg(ZZ),(-1,),add(add((-1,),ZZ),neg(mul(ZZ,ZZ))),ZZ,
   neg(mul(ZZ,ZZ)),mul(ZZ,ZZ)]

def rational_coeffs(n):
    result=[]
    for k in range(n+1):
        rhs=N[k] if k<len(N) else Z
        for j in range(1,min(k,6)+1):rhs=add(rhs,neg(mul(D[j],result[k-j])))
        result.append(rhs)
    return result

def maximal_independent_masks(n):
    ans=[]
    for v in range(1<<n):
        if v&(v<<1):continue
        if any(not (v&(1<<i)) and not (i>0 and v&(1<<(i-1)))
               and not (i+1<n and v&(1<<(i+1))) for i in range(n)):continue
        ans.append(v)
    return ans

def brute(n):
    sets=maximal_independent_masks(n)
    d=Counter((a^b).bit_count() for a in sets for b in sets)
    return trim([d[k] for k in range(n+1)]),len(sets)

def main():
    assert determinant_in_x()==D, ('Incorrect exact characteristic determinant',determinant_in_x())
    mat=reachable_coeffs(42)
    rat=rational_coeffs(42)
    assert mat==rat, 'transfer and exact rational identity disagree'
    total=0
    for n in range(0,17):
        direct,count=brute(n)
        total+=count*count
        assert direct==mat[n],(n,direct,mat[n])
        assert sum(direct)==count*count
        if n>=2: assert direct[-1]==2
        if n>=4: assert direct[1]==0
    print('VERIFY_OK exact determinant and 43 generating coefficients; 17 direct lengths;',total,'ordered pairs')
    print('D coefficients:',D)
    print('N coefficients:',N[:6])
    print('n=8:',mat[8]);print('n=12:',mat[12])

if __name__=='__main__':main()
