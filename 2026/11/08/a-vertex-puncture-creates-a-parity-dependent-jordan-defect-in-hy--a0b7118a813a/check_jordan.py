"""Exact rank and polynomial-identity checks for neighbor-sum on a punctured cube.

No dependencies beyond Python 3; all matrices are represented as binary integer rows.
The same ranks hold over every characteristic-two extension field.
"""

def rank(rows):
    pivots = {}
    for r in rows:
        while r:
            pivot = r.bit_length() - 1
            if pivot in pivots:
                r ^= pivots[pivot]
            else:
                pivots[pivot] = r
                break
    return len(pivots)


def multiply(X, Y):
    out = []
    for row in X:
        z = 0
        while row:
            low = row & -row
            z ^= Y[low.bit_length() - 1]
            row ^= low
        out.append(z)
    return out


def add(X, Y):
    return [x ^ y for x, y in zip(X, Y)]


def punctured(d):
    n = (1 << d) - 1
    out = []
    for i in range(1, n + 1):
        r = 0
        for k in range(d):
            j = i ^ (1 << k)
            if j != 0:
                r |= 1 << (j - 1)
        out.append(r)
    return out


def full_cube(d):
    n = 1 << d
    return [sum(1 << (i ^ (1 << k)) for k in range(d)) for i in range(n)]


def main():
    for d in range(2, 9):
        N = 1 << d
        B = punctured(d)
        BB = multiply(B, B)
        BBB = multiply(BB, B)
        I = [1 << i for i in range(N - 1)]
        A = full_cube(d)
        assert rank(add(A, [((d & 1) << i) for i in range(N)])) == N // 2
        if d % 2 == 0:
            assert rank(B) == N // 2
            assert rank(BB) == 1
            assert BBB == [0] * (N - 1)
            assert rank(A) == N // 2
            j3, j2 = 1, N // 2 - 2
            assert 3*j3 + 2*j2 == N - 1
            print(f'd={d}, vertices={N-1}: nilpotent J3(0)^{j3} + J2(0)^{j2}; ranks=(%d,1,0)' % rank(B))
        else:
            assert rank(B) == N - 2
            b = sum(1 << (j - 1) for j in range(1, N) if j.bit_count() == 1)
            assert BB == [I[i] ^ (b if ((b >> i) & 1) else 0) for i in range(N - 1)]
            assert BBB == B
            C = add(B, I)
            assert rank(multiply(B, C)) == N // 2 - 1
            print(f'd={d}, vertices={N-1}: J1(0) + J2(1)^{N//2-1}; ranks(B,B^2,B(B+I))=({rank(B)},{rank(BB)},{rank(multiply(B,C))})')
    print('PASS: matrix ranks and polynomial identities for d=2..8')

if __name__ == '__main__':
    main()
