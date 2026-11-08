"""Exact symbolic-word transfer and last-visit counting checks; no external packages."""
from math import gcd


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def trace_power(T, power):
    n = len(T)
    P = [[int(i == j) for j in range(n)] for i in range(n)]
    B = T
    while power:
        if power & 1:
            P = matmul(P, B)
        B = matmul(B, B)
        power >>= 1
    return sum(P[i][i] for i in range(n))


def transfer():
    M = [[0]*4 for _ in range(4)]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                if a == b or b == c:
                    M[2*a+b][2*b+c] = 1
    return M


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def e(n):
    return (2,1,-1,-2,-1,1)[n%6]


def count_last_by_first_repeat(n):
    m = n-2
    total = 0
    for mask in range(1 << max(0, m-2)):
        a = [1] + [(mask >> i) & 1 for i in range(max(0, m-2))] + ([1] if m>=2 else [])
        assert len(a) == m
        first_equal = next((j for j in range(m-1,0,-1) if a[j-1] == a[j]), None)
        good = first_equal is None or a[first_equal] == 1
        total += int(good)
    return 2*total


def mobius(n):
    res=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0:return 0
            res=-res
        p+=1
    return -res if n>1 else res


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


if __name__ == '__main__':
    T=transfer()
    for n in range(1,101):
        expected=lucas(n)+e(n)
        actual=trace_power(T,n)
        assert expected==actual,(n,expected,actual)
        cycles={d:sum(mobius(d//v)*(lucas(v)+e(v)) for v in divisors(d))//d for d in divisors(n)}
        assert all(c>=0 for c in cycles.values())
        assert sum(d*count for d,count in cycles.items()) == expected
        if n<=16:
            actual_last=count_last_by_first_repeat(n) if n>=3 else None
            if n>=3:
                assert actual_last==((1 << (n-2))+(2 if n%2==0 else 4))//3
    print('PASS: transfer traces and exact periodic-orbit Möbius counts for n=1..100')
    print('PASS: independent first-repeat count for latest-entry population n=3..16')
    print('T=',T)
