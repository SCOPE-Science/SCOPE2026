#!/usr/bin/env python3
"""Exact bounded corroboration of modular hyper-ary partition distributions."""

def population_matrix(b, r):
    P = ((1, 0, b-1, 0),
         (0, 1, 1, 0),
         (0, 0, b-2, 2),
         (1, 1, b-2, 0))
    counts = [1, 0, 0, 0]
    for _ in range(r):
        counts = [sum(counts[i]*P[i][j] for i in range(4))
                  for j in range(4)]
    return counts[0]+counts[2]+counts[3]


def hyper_values(b, size):
    a = [0]*size
    a[0] = 1
    for n in range(1, size):
        q, t = divmod(n, b)
        a[n] = a[q]+a[q-1] if t == 0 else a[q]
    return a


def digit_step(b, digit, pair):
    x, y = pair
    if digit == 0:
        return (x+y, y)
    if digit == 1:
        return (x, x+y)
    return (x, x)


def run():
    checks = 0
    for b in range(2, 12):
        size = min(150000, b**8)
        a = hyper_values(b, size)
        assert a[0] == 1
        for n in range(size):
            assert a[n] >= 1
            checks += 1
            if n > 0:
                x, y = a[n], a[n-1]
                for digit in range(b):
                    n2 = b*n+digit
                    if n2+1 < size:
                        assert (a[n2], a[n2-1]) == digit_step(b, digit, (x,y))
                        checks += 1
        count_levels = []
        for r in range(0, 24):
            count_levels.append(population_matrix(b,r))
            if b**r <= size:
                assert count_levels[-1] == sum(x % 3 != 0 for x in a[:b**r])
                checks += 1
            lhs = count_levels[-1]
            def aseq(j): return count_levels[j] if j >= 0 else 0
            if r == 0:
                rhs = 1
            elif r == 2:
                rhs = 1
            elif r == 3:
                rhs = -4
            else:
                rhs = 0
            assert (lhs - b*aseq(r-1) + aseq(r-2) +
                    (b-6)*aseq(r-3) + 4*aseq(r-4)) == rhs
            checks += 1
        if b >= 3:
            for q in range(2, 13):
                L = q+1
                for x in range(q):
                    for y in range(q):
                        state = (x,y)
                        for d in [2]+[0]*(q-1)+[2]:
                            state = digit_step(b,d,state)
                        assert state == (q*x,q*x)
                        checks += 1
                for r in range(0, 7):
                    if b**r > size:
                        break
                    nonzero = sum(x % q != 0 for x in a[:b**r])
                    m = r // L
                    upper = b**(r-L*m)*(b**L-1)**m
                    assert nonzero <= upper
                    checks += 1
    print('VERIFY_OK', checks)

if __name__ == '__main__':
    run()
