"""Independent labelled-diagram verification of two-point type counts.

The age consists of finite 1,2,3 metrics forbidding triangles 111 and 122
(the nonmetric triangle 113 is automatically excluded).
"""
from itertools import product


def triangle_ok(a, b, c):
    x, y, z = sorted((a, b, c))
    return z <= x + y and (x, y, z) not in {(1, 1, 1), (1, 2, 2)}


def direct(d, n):
    old = list(product((1, 2, 3), repeat=n))
    good = [u for u in old if all(triangle_ok(u[i],u[j],d) for i in range(n) for j in range(i+1,n))]
    return len(good), tuple(sum(all(triangle_ok(u[i],v[i],c) for i in range(n)) for u in good for v in good) for c in (1,2,3))


def formulas(d, n):
    if d == 2:
        return 2**(n+1)-1, (3*3**n-2*2**n, 2*4**n+2*3**n-4*2**n+1, 3*4**n+3**n-4*2**n+1)
    assert d == 3
    term3 = n*(n-1)*3**(n-2) if n>=2 else 0
    term4 = n*(n-1)*4**(n-2) if n>=2 else 0
    return 2**n+n*2**(n-1), (3**n+2*n*3**(n-1)+term3, 4**n+3*n*4**(n-1)+term4, 4**n+4*n*4**(n-1)+4*term4)

if __name__=='__main__':
    for n in range(1,7):
        for d in (2,3):
            expected=formulas(d,n)
            observed=direct(d,n)
            assert observed==expected, (d,n,observed,expected)
            print('diagram n=%d d=%d unary=%d channels=%s' % (n,d,*observed))
    for n in range(2,201):
        a=formulas(2,n)[1]; b=formulas(3,n)[1]
        aa=sum(a); bb=sum(b)
        assert a[0]*bb>b[0]*aa, n
        assert b[2]*aa>a[2]*bb, n
    for n in range(2,6):
        a=formulas(2,n)[1]; b=formulas(3,n)[1]
        aa=sum(a); bb=sum(b)
        print('stochastic cross-product n=%d short=%d long=%d' % (n,a[0]*bb-b[0]*aa,b[2]*aa-a[2]*bb))
    assert formulas(2,1)==formulas(3,1)
    print('ALL_DIRECT_DIAGRAM_AND_STOCHASTIC_TESTS_PASS')
