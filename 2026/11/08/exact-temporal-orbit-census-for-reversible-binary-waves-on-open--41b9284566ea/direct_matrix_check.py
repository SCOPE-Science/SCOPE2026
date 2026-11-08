"""Exact bit-matrix checks for the reversible open-chain binary wave map."""
from math import gcd


def rows_for_map(n):
    return [((1 << (i-1)) if i else 0) ^ ((1 << (i+1)) if i+1<n else 0) ^ (1 << (n+i)) for i in range(n)] + [1 << i for i in range(n)]


def identity(d):
    return [1 << j for j in range(d)]


def product(left, right):
    return [xor_rows(r, right) for r in left]


def xor_rows(mask, matrix):
    accum = 0
    while mask:
        bit = mask & -mask
        accum ^= matrix[bit.bit_length()-1]
        mask ^= bit
    return accum


def power(A,t):
    z=identity(len(A))
    while t:
        if t & 1: z=product(z,A)
        A=product(A,A)
        t//=2
    return z


def rank(rows):
    pivots={}
    for row in rows:
        while row:
            k=row.bit_length()-1
            if k not in pivots:
                pivots[k]=row
                break
            row^=pivots[k]
    return len(pivots)


def two_valuation(x):
    a=0
    while x%2==0: x//=2; a+=1
    return a,x


def expected_nullity(n,t):
    a,u=two_valuation(n+1)
    b,v=two_valuation(t)
    h=gcd(u,v)
    return (h-1)*min(2**(a+1), 2**b)+min(2**(a+1)-2,2**b)


def divisors(k):
    return [j for j in range(1,k+1) if k%j==0]


def main():
    cases=0
    for n in range(2,33):
        A=rows_for_map(n)
        q=n+1
        for t in range(1,2*q+1):
            B=power(A,t)
            observed=2*n-rank([r ^ (1<<i) for i,r in enumerate(B)])
            assert observed==expected_nullity(n,t),(n,t,observed,expected_nullity(n,t))
            cases+=1
        assert power(A,2*q)==identity(2*n)
        for t in divisors(2*q)[:-1]:
            assert power(A,t)!=identity(2*n),(n,t)
    print(f'PASS: {cases} fixed-kernel rank comparisons for dimensions n=2..32')
    print('PASS: exact matrix order 2(n+1) for n=2..32')

if __name__=='__main__': main()
