"""Reproducible finite checks for an exact two-point square-residue census.
No external packages needed. Finite checks supplement the proof, not certify all cases.
"""
from math import isqrt


def chi(a, p):
    a %= p
    if not a:
        return 0
    return 1 if pow(a, (p - 1)//2, p) == 1 else -1


def S(p, m, a):
    assert m >= 1 and 0 <= a <= m
    return 1 + sum((p-1)//2 * p**(m-2*j-1)
                   for j in range((m+1)//2) if a <= 2*j < m)


def U(p, m, t):
    return sum((p-1)//2*p**(m-2*j-1)
               for j in range((m+1)//2) if 2*j < t and 2*j < m)


def A(p, m, h):
    h %= p**m
    if h == 0:
        return S(p, m, 0)
    t = 0
    while h % p == 0:
        h //= p
        t += 1
    u = h % p
    initial = U(p, m, t)
    if t % 2:
        return initial
    N = (p - 3 - chi(u,p) - chi(-u,p))//4
    return (initial + p**(m-t-1)*N
            + (chi(-u,p) == 1)*S(p,m-t,1)
            + (chi(u,p) == 1)*S(p,m,t+1))


def is_prime(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))


def check_prime_power(p, m, full=False):
    n = p**m
    squares = {x*x % n for x in range(n)}
    assert len(squares) == S(p,m,0), (p,m,'size')
    shifts = range(n) if full else sorted({0,1,2,3,n-1,n//2,n//3,p,p*p,p*p+1}
                                          | {k*n//113 for k in range(114)})
    ct = 0
    for h in shifts:
        h %= n
        measured = sum(((x+h)%n) in squares for x in squares)
        expected = A(p,m,h)
        assert measured == expected, (p,m,h,measured,expected)
        ct += 1
    return ct


def sq(n):
    return {x*x % n for x in range(n)}


def factor(n):
    out = []
    p = 2
    while p*p <= n:
        if n%p == 0:
            m = 0
            while n%p==0:
                n//=p; m+=1
            out.append((p,m))
        p+=1
    if n>1:out.append((n,1))
    return out


def main():
    total=0
    for p in [3,5,7,11,13,17,19,23,29]:
        for m in range(1,6):
            n=p**m
            if n>5000:
                continue
            total += check_prime_power(p,m,full=(n<=400))
    for n in [15,21,33,35,45,63,75,77,99,105,135,175,225,275,315,495]:
        vals=sq(n)
        fac=factor(n)
        assert all(p%2 and is_prime(p) for p,m in fac)
        for h in range(n):
            measured=sum(((v+h)%n) in vals for v in vals)
            expected=1
            for p,m in fac:
                expected*=A(p,m,h)
            assert measured==expected,(n,h,measured,expected)
            total += 1
    for p in [5,13,17,29,37,41,53,61,73,89,97,101]:
        for m in range(1,7):
            q=p**m
            s=S(p,m,1)
            square_shift=q//p*(p-5)//4+2*s  # p^{m-1}*(p-5)/4
            nonsquare_shift=q//p*(p-1)//4
            assert (square_shift>nonsquare_shift)==(m==1), (p,m)
            assert (square_shift<nonsquare_shift)==(m>=2), (p,m)
            total += 1
    print('PASS; exact shift comparisons and phase-inequality checks:',total)
    print('Sample p=5, m=1,2,3,4:')
    for m in range(1,5):
        print(m, A(5,m,1),A(5,m,2))

if __name__=='__main__':
    main()
