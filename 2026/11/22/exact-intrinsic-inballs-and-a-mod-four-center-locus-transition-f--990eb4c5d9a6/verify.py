"""Exact finite checks for the cycle-midpoint polytope formulas.

All linear algebra below uses rational integers/Fractions, not floating sampling.
The loop tests finite sizes; the accompanying proof establishes the theorem for all n.
"""
from fractions import Fraction as F
from math import gcd


def rank(rows):
    a = [[F(x) for x in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0]); r = 0
    for c in range(n):
        p = next((i for i in range(r,m) if a[i][c]), None)
        if p is None: continue
        a[r],a[p] = a[p],a[r]
        f = a[r][c]; a[r] = [x/f for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [a[i][j]-f*a[r][j] for j in range(n)]
        r += 1
        if r == m: break
    return r


def normal_norm_squared(n, omitted):
    if len(omitted) == 1:
        heights = [F(1-n if k in omitted else 1) for k in range(n)]
    else:
        m = n//2
        heights = [F(1-m if k in omitted else 1) for k in range(n)]
    p = [F(0)]
    for k in range(n-1): p.append(heights[k] - p[-1])
    if n%2:
        t = (heights[-1]-p[-1])/2
    else:
        assert heights[-1] == p[-1], (n, omitted)
        t = -sum(((-1)**k)*p[k] for k in range(n))/n
    z = [p[k] + ((-1)**k)*t for k in range(n)]
    assert all(z[k]+z[(k+1)%n] == heights[k] for k in range(n))
    assert sum(z) == 0
    if not n%2: assert sum(((-1)**k)*z[k] for k in range(n)) == 0
    return F(4*(n-1),n) *sum(u*u for u in z)


def main():
    tests = 0
    for n in range(3, 27):
        if n%2:
            expected=(n-1)**2 * (n+1)
            for i in range(n):
                assert normal_norm_squared(n,(i,)) == expected
                tests+=1
        else:
            m=n//2
            squared = []
            tangent=[]
            for i in range(0,n,2):
                for j in range(1,n,2):
                    d=min((j-i)%n,(i-j)%n)
                    q=normal_norm_squared(n,(i,j))
                    assert q == (n-1)*(d*(n-d)-1), (n,i,j,d,q)
                    tests+=1
                    squared.append(q)
            maxq=max(squared)
            assert maxq == (n-1)*(m*m-(1 if m%2==0 else 0)-1)
            for i in range(0,n,2):
                for j in range(1,n,2):
                    if normal_norm_squared(n,(i,j))==maxq:
                        tangent.append((i,j))
            assert len(tangent) == (n if m%2==0 else m), (n,tangent)
            # Zero-sum coefficient gauge and every tangent support equality.
            rows=[[1]*n]
            for i,j in tangent:
                v=[0]*n;v[i]=v[j]=1;rows.append(v)
            # The coefficient map has kernel the alternating vector.
            center_dim=(n-rank(rows))-1
            assert center_dim == (0 if m%2==0 else m-1), (n,center_dim)
            tests+=3
    # The normalized odd/even inradii follow by inverse square root of max norm.
    print(f'PASS: {tests} exact facet-normal, shell, contact, and center-rank checks for 3 <= n <= 26')
    print('The finite checker does not certify the infinite-parameter theorem.')

if __name__=='__main__': main()
