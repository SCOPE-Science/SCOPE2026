"""Independent multinomial-type enumeration of two-periodic majority patterns.
Run: python3 verify_types.py
"""
from math import comb, factorial


def majority(n, ones, retained):
    return int(2*ones > n or (2*ones == n and retained == 1))


def valid_pair(n, counts):
    # counts[2*a+b] counts sites with old hub a, next hub b.
    k = counts[2] + counts[3]
    ell = counts[1] + counts[3]
    for code,c in enumerate(counts):
        if not c:
            continue
        a, b = code//2, code%2
        if majority(n,k-a+b,a) != b:
            return False
        if majority(n,ell-b+a,b) != a:
            return False
    return True


def total(n):
    f = factorial(n)
    all_periodic = fixed = 0
    for a00 in range(n+1):
        for a01 in range(n-a00+1):
            for a10 in range(n-a00-a01+1):
                a11=n-a00-a01-a10
                row=(a00,a01,a10,a11)
                if valid_pair(n,row):
                    ways = f//(factorial(a00)*factorial(a01)*factorial(a10)*factorial(a11))
                    all_periodic += ways
                    if a01 == 0 and a10 == 0:
                        fixed += ways
    return fixed,all_periodic-fixed


def expected(n):
    if n%2 == 0:
        b=comb(n,n//2)
        return (b+2,b*(b-1))
    r=(n-1)//2
    return (2,2*n*comb(n-1,r)+2*comb(n,r))


def main():
    checks=0
    for n in range(2,61):
        actual=total(n)
        assert actual == expected(n),(n,actual,expected(n))
        checks+=1
    for n in (2,3,4,5,6,7,8,9,10,15,16,29,30,59,60):
        print('n=%d fixed=%d primitive2=%d' % ((n,)+expected(n)))
    print('MULTINOMIAL_OK %d graph orders' % checks)

if __name__ == '__main__':
    main()
