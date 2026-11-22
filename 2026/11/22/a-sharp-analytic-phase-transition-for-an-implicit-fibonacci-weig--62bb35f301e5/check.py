from fractions import Fraction

def coefficients(q, N):
    a = [1] + [0]*N
    for degree in range(1, N+1):
        s = [Fraction(0)]*(degree+1)
        for m in range(1, degree+1):
            reach = degree-m
            base = [q**m+1]+a[1:reach+1]
            poly = [1]+[0]*reach
            for _ in range(m):
                nxt = [0]*(reach+1)
                for i, u in enumerate(poly):
                    if u:
                        for j, v in enumerate(base[:reach+1-i]):
                            nxt[i+j] += u*v
                poly = nxt
            for j, u in enumerate(poly):
                s[m+j] += Fraction(u, m)
        value = sum(j*s[j]*a[degree-j] for j in range(1, degree+1))/degree
        assert value.denominator == 1
        a[degree] = int(value)
    return a

def main():
    tests = 0
    for q in (0, 1, 2, 3):
        a = coefficients(q, 8)
        for n in range(1, len(a)):
            if q == 0:
                expect = sum(a[k]*a[n-1-k] for k in range(n))
                assert a[n] == expect
            if q == 1:
                expect = a[n-1] + sum(a[k]*a[n-1-k] for k in range(n))
                assert a[n] == expect
            if q >= 2:
                assert n*a[n] >= q**(n*n)
                assert a[n] <= 2*6**n*q**(n*n)
            tests += 1
    assert coefficients(2, 5)[1:] == [3, 20, 329, 22584, 7938470]
    print('IMPLICIT_EXPONENTIAL_PHASE_CHECK_OK', tests)

if __name__ == '__main__':
    main()
