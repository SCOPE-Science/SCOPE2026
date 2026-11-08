"""Standalone exact arithmetic checks for cyclic Rule 50 at two time steps.

Run with Python 3: python check.py. No third-party libraries.
"""
from itertools import permutations


def local(a, b, c):
    return (1 - b) * (a | c)


def two_local(bits):
    return local(*(local(*bits[i:i+3]) for i in range(3)))


def matrix_multiply(A, B):
    size = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(size))
             for j in range(size)] for i in range(size)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def get_matrices():
    M = [[[0]*16 for _ in range(16)] for _ in range(2)]
    for i in range(16):
        state = [(i >> (3-j)) & 1 for j in range(4)]
        for bit in (0, 1):
            symbols = state + [bit]
            j = ((i << 1) & 15) | bit
            M[two_local(symbols)][i][j] += 1
    return M


def polynomial_multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def det_i_minus_zK(K):
    n = len(K)
    out = [0]*(n+1)
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        coeff = [1]
        for i, j in enumerate(perm):
            coeff = polynomial_multiply(coeff, [int(i == j), -K[i][j]])
        for j,v in enumerate(coeff):
            out[j] += (-1)**inversions * v
    return out


def step(word, n):
    mask=(1 << n)-1
    left=((word << 1)&mask) | (word >> (n-1))
    right=(word >> 1) | ((word & 1) << (n-1))
    return (~word) & (left|right) & mask


def brute_counts(n):
    counts=[0]*(1 << n)
    for source in range(1 << n):
        mid=step(source,n)
        dest=step(mid,n)
        counts[dest]+=1
    return counts


def matrix_power(A,m):
    R=identity(len(A))
    while m:
        if m&1:
            R=matrix_multiply(R,A)
        m//=2
        if m:
            A=matrix_multiply(A,A)
    return R


def main():
    M0,M1=get_matrices()
    B=matrix_multiply(M0,M1)
    expected_rows={
        0:[1], 1:[4,5,6,7], 4:[0,1], 5:[4,5,6,7],
        7:[12,13], 9:[4,5,6,7], 12:[0,1],
        13:[4,5,6,7], 15:[12,13]
    }
    actual_rows={i:[j for j,c in enumerate(row) if c]
                 for i,row in enumerate(B) if any(row)}
    assert actual_rows == expected_rows
    assert all(c in (0,1) for row in B for c in row)
    K=[[0,1,0,0],[0,1,1,1],[1,1,0,0],[0,1,1,0]]
    assert det_i_minus_zK(K)==[1,-1,-2,-2,-1]
    recurrence=[4,1,5,13,29]
    for m in range(1,41):
        a=trace(matrix_power(K,m))
        if m<=4:
            assert a==recurrence[m]
        else:
            b=sum(co*trace(matrix_power(K,m-i))
                  for i,co in enumerate((1,2,2,1),1))
            assert a==b
        if m<=12:
            assert a==trace(matrix_power(B,m))
    for m in range(1,10):
        n=2*m
        counts=brute_counts(n)
        even_pattern=sum(1 << j for j in range(0,n,2))
        odd_pattern=((1 << n)-1) ^ even_pattern
        a=trace(matrix_power(K,m))
        assert counts[0]==2, (n,'zero',counts[0])
        assert counts[(1 << n)-1]==0, (n,'one',counts[-1])
        assert counts[even_pattern]==counts[odd_pattern]==a, (n,'alternating')
    print('VERIFY_OK: all transfer rows, 4x4 determinant, 40 recurrence terms, 12 graph traces, exhaustive even rings 2..18')


if __name__ == '__main__':
    main()
