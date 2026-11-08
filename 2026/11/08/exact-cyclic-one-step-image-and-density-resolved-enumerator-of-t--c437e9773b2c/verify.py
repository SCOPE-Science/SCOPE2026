"""Standalone exact checks for the Rule 184 one-step ring image theorem.

Uses only Python's standard library. Execute: python3 verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def update_184(bits):
    n = len(bits)
    return tuple(int((bits[(i-1) % n] and not bits[i]) or
                     (bits[i] and bits[(i+1) % n])) for i in range(n))


def update_226(bits):
    n = len(bits)
    return tuple(int((bits[(i+1) % n] and not bits[i]) or
                     (bits[i] and bits[(i-1) % n])) for i in range(n))


def avoids(bits):
    n = len(bits)
    return all(tuple(bits[(i+j) % n] for j in range(4)) != (1, 1, 0, 0)
               for i in range(n))


def closed_coefficient(n, k):
    value = sum(
        (Fraction((-1) ** s * n, n-3*s) * comb(n-3*s, s) *
         comb(n-4*s, k-2*s)
         for s in range(min(n//4, k//2) + 1)
         if k-2*s <= n-4*s), Fraction(0)
    )
    assert value.denominator == 1
    return value.numerator


def local_defects():
    defects = set()
    for a,b,c,d,e in product(range(2), repeat=5):
        y = (a,b,c,d,e)
        def g(i):
            return int((y[i+1] and not y[i]) or (y[i] and y[i-1]))
        z = int((g(1) and not g(2)) or (g(2) and g(3)))
        if z != c:
            defects.add(y)
    assert defects == {
        (0,1,1,0,0),(1,1,0,0,0),(1,1,0,0,1),(1,1,1,0,0)
    }


def polynomial_add(A,B,sign=1):
    C=A.copy()
    for m,c in B.items():
        C[m]=C.get(m,0)+sign*c
        if C[m]==0:del C[m]
    return C


def polynomial_mul(A,B):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            key=(i+k,j+l)
            C[key]=C.get(key,0)+a*b
    return {mon:c for mon,c in C.items() if c}


def det_symbolic_8():
    # Rows/columns indexed by three-bit words abc, and bcd respectively.
    matrix=[[{} for _ in range(8)] for __ in range(8)]
    for r in range(8):
        a,b,c=((r>>2)&1,(r>>1)&1,r&1)
        for d in (0,1):
            if (a,b,c,d)==(1,1,0,0):continue
            col=4*b+2*c+d
            matrix[r][col][(1,d)]=-1  # minus z u**d
        matrix[r][r][(0,0)]=1
    cache={}
    def determinant_rows(r, remaining):
        if r==8:return {(0,0):1}
        key=(r,remaining)
        if key in cache:return cache[key]
        result={}
        for position,col in enumerate(remaining):
            a=matrix[r][col]
            if not a:continue
            smaller=determinant_rows(r+1,remaining[:position]+remaining[position+1:])
            result=polynomial_add(result,polynomial_mul(a,smaller),
                                  1 if position%2==0 else -1)
        cache[key]=result
        return result
    result=determinant_rows(0,tuple(range(8)))
    assert result=={(0,0):1,(1,0):-1,(1,1):-1,(4,2):1},result


def main():
    local_defects()
    det_symbolic_8()
    counts=[]
    for n in range(1,17):
        images={update_184(w) for w in product(range(2),repeat=n)}
        allowed={w for w in product(range(2),repeat=n) if avoids(w)}
        assert images==allowed, n
        assert all(update_184(update_226(w))==w for w in allowed),n
        by_weight=Counter(map(sum,images))
        assert [by_weight[k] for k in range(n+1)] == [closed_coefficient(n,k) for k in range(n+1)],n
        counts.append(len(images))
    assert counts==[2,4,8,12,22,40,72,132,242,444,816,1500,2758,5072,9328,17156],counts
    # Independent local necessity certificate via labeled pair graph.
    matrices=[[[0]*4 for _ in range(4)] for _ in range(2)]
    for a,b,c in product(range(2),repeat=3):
        bit=int((a and not b) or (b and c))
        matrices[bit][2*a+b][2*b+c]=1
    def matmul(A,B):
        return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    product_1100=matmul(matmul(matmul(matrices[1],matrices[1]),matrices[0]),matrices[0])
    assert product_1100==[[0]*4 for _ in range(4)]
    print('VERIFY_OK: five-bit local certificate, symbolic determinant, labeled graph exclusion,')
    print('           16 cyclic lengths by exhaustive images and exact weight coefficients')


if __name__=='__main__':
    main()
