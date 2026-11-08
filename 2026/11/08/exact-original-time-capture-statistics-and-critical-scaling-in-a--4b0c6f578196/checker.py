"""Exact-rational consistency checks for the max-plus capture-time theorem.

Run: python3 checker.py
Only the Python 3 standard library is required.
The proof is analytic; these finite checks independently test its formulas.
"""
from fractions import Fraction as Q


def h(x, b, m):
    return b - max(Q(0), m*x)


def step(x, y, b, m):
    return y, h(x, b, m)


def scalar_capture(x, b, m):
    d = (1-m)*b
    for j in range(200):
        if x in (b, d):
            return j
        x = h(x, b, m)
    raise AssertionError('point did not reach scalar attracting pair')


def plane_capture(x, y, b, m):
    d = (1-m)*b
    for j in range(400):
        if x in (b, d) and y in (b, d):
            return j
        x,y = step(x, y, b, m)
    raise AssertionError('point did not reach four-cycle')


def interval(n, b, m):
    c = b/(1+m)
    a,z = -c, b-c
    if n % 2 == 1:
        a,z = -z, -a
    return c+a/m**n, c+z/m**n


def new_pmf(j, r):
    return ((1-r)*r**(j-2)*(1-r**(j-2)),
            (1-r)*r**(j-2)*(1-r**(j-1)))


def exact_tests():
    count = 0
    for m in [Q(6,5),Q(3,2),Q(2),Q(5,2),Q(4)]:
        r = 1/m
        for b in [Q(1),Q(5,3)]:
            c = b/(1+m)
            d = (1-m)*b
            assert h(c,b,m)==c and h(b,b,m)==d and h(d,b,m)==b
            for n in range(1,20):
                left,right=interval(n,b,m)
                assert right-left==b/m**n
                if n>=2:
                    pl,pr=interval(n-1,b,m)
                    assert pl <= left < right <= pr
                # On the inverse-branch interval: h^n remains positive.
                mid=(left+right)/2
                u=mid
                for _ in range(n):
                    u=h(u,b,m)
                    assert u>0
                count+=1
            # Test exact first-capture original-step parity on a rational grid.
            for i in range(1,84):
                x=b*Q(i,89)
                if x==c:
                    continue
                qx=scalar_capture(x,b,m)
                for j in range(1,84):
                    y=b*Q(j,89)
                    if y==c:
                        continue
                    qy=scalar_capture(y,b,m)
                    n=plane_capture(x,y,b,m)
                    assert n==2*max(qx,qy)-(qx>qy),(m,b,i,j,qx,qy,n)
                    count+=1
            # Finite exact sum matches residual tail (max of two geometric variables).
            for k in range(2,25):
                total = sum(sum(new_pmf(j,r)) for j in range(2,k+1))
                assert total == (1-r**(k-1))**2
                # For threshold N<=2k, both scalar times <=k.
                count+=1
    print('PASS:',count,'exact-rational identity, interval and orbit checks')

if __name__=='__main__':
    exact_tests()
