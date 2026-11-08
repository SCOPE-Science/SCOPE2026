"""Independent finite checks for endpoint one-wildcard universal partial words.

Only Python's standard library is required. Run: python3 verify.py
The infinite-order formulas are established by the accompanying proof, not by tests.
"""
from fractions import Fraction
from itertools import product


def expected(n, k):
    if k == 1:
        return 2 ** (2 ** (n - 1) - n + 1)
    if n == 2:
        return 0
    if n == 3:
        return 2
    return ((2 ** (n - 2) - (-1) ** n) // 3) * 2 ** (2 ** (n - 1) - 2 * n + 2)


def direct(n, k):
    length = 2 ** n + n - k - 1
    count = 0
    for bits in product('01', repeat=length - 1):
        word = ''.join(bits[:k-1]) + '*' + ''.join(bits[k-1:])
        covered = set()
        good = True
        for i in range(length - n + 1):
            window = word[i:i+n]
            for bit in ('01' if '*' in window else '0'):
                value = window.replace('*', bit)
                if value in covered:
                    good = False
                    break
                covered.add(value)
            if not good:
                break
        if good and len(covered) == 2**n:
            count += 1
    return count


def determinant_int(a):
    """Fraction-free exact Bareiss determinant."""
    a = [row[:] for row in a]
    n = len(a)
    if not n:
        return 1
    previous = 1
    sign = 1
    for k in range(n-1):
        if not a[k][k]:
            swap = next((j for j in range(k+1,n) if a[j][k]),None)
            if swap is None:
                return 0
            a[k],a[swap] = a[swap],a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = a[i][j]*pivot - a[i][k]*a[k][j]
                assert num % previous == 0
                a[i][j] = num//previous
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def second_prefix(n):
    sequence = ''.join('01'[j%2] for j in range(n))
    sequence = sequence[:-1] + ('1' if sequence[-1]=='0' else '0')
    return '0*' + sequence


def tree_count(n):
    """Compute rooted trees after deleting the five fixed prefix edges.

    For n >= 4 root r stays in the residual graph and an initial 0 prefix is fixed.
    """
    prefix = second_prefix(n)
    q = 2**(n-1)
    used = set()
    for i in range(3):
        window = prefix[i:i+n]
        for bit in ('01' if '*' in window else '0'):
            used.add(int(window.replace('*',bit),2))
    assert len(used)==5
    root = int(prefix[0:n-1].replace('*','0'),2)
    # The removed source 0* (with 0 completion) fixes the root of the residual trail.
    r = root
    c = int(('01'*n)[:n-1],2)
    assert r!=c
    remaining = [(e>>1,e%(q)) for e in range(2*q) if e not in used]
    vertices = [v for v in range(q) if v not in (r,c)]
    index = {v:i for i,v in enumerate(vertices)}
    minor = [[0]*len(vertices) for _ in vertices]
    for x,y in remaining:
        if x in index:
            minor[index[x]][index[x]]+=1
            if y in index:
                minor[index[x]][index[y]]-=1
    return determinant_int(minor)


def green(n):
    m=n-1
    C=('01'*n)[:m]
    a='0'+C[:-1]
    b='1'+C[:-1]
    r='0'+a[:-1]
    assert len(set([C,a,b,r]))==4
    def S(x,y):
        return sum((Fraction(1,2**j) for j in range(m)
                    if x[j:]==y[:m-j]),Fraction())
    def K(x,y):
        return (S(x,y)-S(r,y)-S(x,r)+S(r,r))/2
    points=[C,a,b]
    rows=[[K(x,y) - (int(i==j and i>0))
           for j,y in enumerate(points)] for i,x in enumerate(points)]
    det=(rows[0][0]*(rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1])
         -rows[0][1]*(rows[1][0]*rows[2][2]-rows[1][2]*rows[2][0])
         +rows[0][2]*(rows[1][0]*rows[2][1]-rows[1][1]*rows[2][0]))
    return det

if __name__=='__main__':
    for n in (2,3,4):
        for k in (1,2):
            observed=direct(n,k)
            assert observed==expected(n,k), (n,k,observed,expected(n,k))
            print('DIRECT',n,k,observed)
    for n in range(4,8):
        t=tree_count(n)
        assert 2*t==expected(n,2), (n,t,expected(n,2))
        print('TREE',n,t)
    for n in range(4,13):
        ratio=green(n)
        required=Fraction(2**(n-2)-(-1)**n,3*2**(n-1))
        assert ratio==required,(n,ratio,required)
        print('GREEN',n,ratio)
    print('VERIFY_OK')
