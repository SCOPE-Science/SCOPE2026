"""Standalone integer check for three-class relational group quotients.

Elements of a product of cyclic groups are lexicographically ordered tuples.
In a witness mask, bit i-1 marks the i-th nonzero tuple as belonging to A.
"""
from itertools import product
from fractions import Fraction

WITNESSES = {
    (13,): 0x7c4, (15,): 0x1d26, (17,): 0xaee,
    (19,): 0x2538f, (21,): 0xfdb0, (23,): 0x20cf15,
    (25,): 0x315e91, (5,5): 0xd7dc7,
    (27,): 0x10ac7f, (3,9): 0x20d5674,
    (3,3,3): 0xcd3143, (29,): 0xfa58e05,
    (31,): 0x11b1c967, (33,): 0x2d8950fa,
    (35,): 0x3e0d9aa83,
}

def table(factors):
    elements = list(product(*(range(m) for m in factors)))
    lookup = {x: i for i, x in enumerate(elements)}
    return [[lookup[tuple((a[j]+b[j]) % factors[j]
                          for j in range(len(factors)))]
             for b in elements] for a in elements]

def cells(n, mask):
    a = [i for i in range(1,n) if (mask >> (i-1)) & 1]
    b = [i for i in range(1,n) if not ((mask >> (i-1)) & 1)]
    return [{0}, set(a), set(b)]

def products(T, P):
    return [{T[a][b] for a in X for b in Y}
            for X,Y in ((P[1],P[1]),(P[1],P[2]),(P[2],P[2]))]

def universal(T, mask):
    P = cells(len(T),mask)
    return bool(P[1] and P[2]) and all(len(s)==len(T) for s in products(T,P))

def dimensionality_direct(T, P):
    # D1 and the original quantified D2 from the definition, not merely
    # the three-product coverage shortcut.
    n=len(T)
    if P[0]!={0} or len(P)!=3 or any(not X for X in P): return False
    if set().union(*P)!=set(range(n)):return False
    if sum(len(X) for X in P)!=n:return False
    idx={a:i for i,X in enumerate(P) for a in X}
    for a in range(n):
        for b in range(n):
            s=T[a][b]
            A,B=P[idx[a]],P[idx[b]]
            for target in P[idx[s]]:
                if not any(T[x][y]==target for x in A for y in B):
                    return False
    return True

def brute_no_universal(factors):
    T=table(factors); n=len(T)
    count=0
    for mask in range(1<<(n-1)):
        count+=universal(T,mask)
    assert count==0, (factors,count)
    return 1<<(n-1)

def check_witnesses():
    for factors,mask in WITNESSES.items():
        T=table(factors)
        P=cells(len(T),mask)
        assert universal(T,mask), factors
        assert dimensionality_direct(T,P),factors
    return len(WITNESSES)

def analytic_tail():
    # Exact rational union bound at n=33; monotonic on odd n >= 33.
    n=33; k=(n-3)//2
    error=2*n*Fraction(3,4)**k+n*Fraction(1,2)**k
    assert error<1, error
    for n in range(35,99,2):
        prior=2*(n-2)*Fraction(3,4)**((n-5)//2)+(n-2)*Fraction(1,2)**((n-5)//2)
        current=2*n*Fraction(3,4)**((n-3)//2)+n*Fraction(1,2)**((n-3)//2)
        assert current<prior
    return str(error)

if __name__=='__main__':
    assert brute_no_universal((9,))==256
    assert brute_no_universal((3,3))==256
    assert brute_no_universal((11,))==1024
    count=check_witnesses()
    print('THREE_CLASS_DIMENSIONALITY_OK',count,'finite witnesses',
          1536,'small-colourings checked','tail_n33',analytic_tail())
