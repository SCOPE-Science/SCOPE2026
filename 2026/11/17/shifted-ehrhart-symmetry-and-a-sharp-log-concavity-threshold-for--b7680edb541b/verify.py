#!/usr/bin/env python3
"""Exact arithmetic checks for a weighted directed five-cycle simplex."""
import math

def compositions(total, count):
    if count == 1:
        yield (total,)
        return
    for head in range(total + 1):
        for rest in compositions(total - head, count - 1):
            yield (head,) + rest

def count_lattice_points(weight, dilate):
    # Inverse of I + weight*S has numerator I-w*S+w^2*S^2-w^3*S^3+w^4*S^4.
    result = 0
    for coordinates in compositions((weight + 1) * dilate, 5):
        if all(sum((-weight)**r * coordinates[(j-r)%5] for r in range(5)) >= 0
               for j in range(5)):
            result += 1
    return result

def expected(weight):
    A = math.comb(weight, 4) if weight >= 4 else 0
    B = weight * (weight-1) * (11*weight*weight+5*weight+6) // 24
    return (1, A, B, B, A)

def main():
    total = 0
    for weight in range(2,10):
        L1 = count_lattice_points(weight,1)
        L2 = count_lattice_points(weight,2)
        h = expected(weight)
        assert L1-5 == h[1], (weight,L1,h)
        assert L2-5*L1+10 == h[2], (weight,L2,h)
        assert sum(h) == weight**4-weight**3+weight**2-weight+1
        assert h[1] == h[4] and h[2] == h[3]
        total += 4
    for weight in range(2,61):
        h = expected(weight)
        log_concave = all(h[j]*h[j] >= h[j-1]*h[j+1] for j in range(1,4))
        assert log_concave == (weight>=7), weight
        total += 1
    print('VERIFY_OK',total,'exact tests')

if __name__ == '__main__':
    main()
