#!/usr/bin/env python3
from itertools import combinations

def bits(mask, n):
    return [i for i in range(n) if (mask >> i) & 1]

def construct_path(n, x, y, z):
    """Return an induced path of Q_n containing distinct x,y,z."""
    A = x ^ z
    B = y ^ z
    if A == 0 or B == 0 or A == B:
        raise ValueError("x, y, z must be distinct")

    P = A & ~B
    Q = B & ~A
    R = A & B

    if P == 0:
        # A is contained in B: 0 -> A -> B is geodesic.
        v = 0
        path = [v]
        for i in bits(A, n):
            v ^= 1 << i
            path.append(v)
        for i in bits(Q, n):
            v ^= 1 << i
            path.append(v)
    elif Q == 0:
        # B is contained in A: 0 -> B -> A is geodesic.
        v = 0
        path = [v]
        for i in bits(B, n):
            v ^= 1 << i
            path.append(v)
        for i in bits(P, n):
            v ^= 1 << i
            path.append(v)
    else:
        # A -> 0 -> B.  On the left flip R before P; on the
        # right flip Q before R.
        v = A
        path = [v]
        for i in bits(R, n):
            v ^= 1 << i
            path.append(v)
        for i in bits(P, n):
            v ^= 1 << i
            path.append(v)
        assert v == 0
        for i in bits(Q, n):
            v ^= 1 << i
            path.append(v)
        for i in bits(R, n):
            v ^= 1 << i
            path.append(v)
        assert v == B

    return [v ^ z for v in path]

def is_induced_path(path):
    if len(path) != len(set(path)):
        return False
    for i in range(len(path) - 1):
        if (path[i] ^ path[i + 1]).bit_count() != 1:
            return False
    for i in range(len(path)):
        for j in range(i + 2, len(path)):
            if (path[i] ^ path[j]).bit_count() == 1:
                return False
    return True

def main():
    total = 0
    for n in range(1, 8):
        vertices = range(1 << n)
        for x, y, z in combinations(vertices, 3):
            path = construct_path(n, x, y, z)
            assert x in path and y in path and z in path
            assert is_induced_path(path)
            total += 1
    assert total == 388620
    print("VERIFY_OK dimensions=1..7 triples=388620")

if __name__ == "__main__":
    main()
