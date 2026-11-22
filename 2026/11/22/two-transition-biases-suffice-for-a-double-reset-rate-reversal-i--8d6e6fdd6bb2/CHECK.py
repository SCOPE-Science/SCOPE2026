"""Exact finite rational verification for a two-valued birth-death reset response.

Run with Python 3 and its standard library: python3 CHECK.py.
The all-parameter inequalities are established in RESULT.md; this file
verifies the displayed exact continuants and a Sturm root-count certificate.
"""
from fractions import Fraction as R


def strip(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [R(0)] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return strip(c)


def scale(a, c):
    return strip([v * c for v in a])


def multiply(a, b):
    c = [R(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b): c[i+j] += v*w
    return strip(c)


def derivative(a):
    return strip([R(i)*a[i] for i in range(1, len(a))] or [R(0)])


def value(a, x):
    z = R(0)
    for v in reversed(a): z = z*x + v
    return z


def divrem(a, b):
    a, b = strip(a), strip(b)
    assert b != [0]
    if len(a) < len(b): return [R(0)], a
    q = [R(0)]*(len(a)-len(b)+1)
    r = list(a)
    while r != [0] and len(r) >= len(b):
        d = len(r)-len(b)
        c = r[-1]/b[-1]
        q[d] += c
        for j, v in enumerate(b): r[j+d] -= c*v
        r = strip(r)
    return strip(q), r


def sturm(a):
    out = [strip(a), derivative(a)]
    while out[-1] != [R(0)]:
        rem = divrem(out[-2],out[-1])[1]
        if rem == [0]: break
        out.append(scale(rem,-1))
    return out


def signs_at(a, x):
    return [int((v>0)-(v<0)) for poly in a if (v := value(poly,x)) != 0]


def changes(seq):
    return sum(u != v for u,v in zip(seq,seq[1:]))


def continuant(p, lo, hi):
    old, prev = [R(1)], [R(1)]
    for j in range(lo,hi+1):
        if j == lo:
            cur = [R(1)]
        else:
            cur = add(prev, [R(0)] + scale(old, -p[j-2]*(1-p[j-1])))
        old, prev = prev, cur
    return prev


def solve(a, b):
    n = len(b)
    A = [list(row)+[b[i]] for i,row in enumerate(a)]
    for k in range(n):
        i = next(i for i in range(k,n) if A[i][k])
        A[i],A[k] = A[k],A[i]
        v = A[k][k]
        A[k] = [u/v for u in A[k]]
        for i in range(n):
            if i != k:
                v = A[i][k]
                A[i] = [A[i][j]-v*A[k][j] for j in range(n+1)]
    return [row[-1] for row in A]


def direct_response(p,s):
    n=len(p)
    A = [[R(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        if j>0: A[j][j-1]-=s*(1-p[j])
        if j<n-1: A[j][j+1]-=s*p[j]
    left=[R(0)]*n;left[0]=s*(1-p[0])
    right=[R(0)]*n;right[-1]=s*p[-1]
    u=solve(A,left)[4]
    v=solve(A,right)[4]
    return u/(u+v)


def main():
    e=R(1,20)
    p=[1-e,e,1-e,e,1-e,e,1-e,1-e,e,e,e]
    H=continuant(p,1,4)
    T=continuant(p,6,11)
    assert H == [R(1),-R(723,400),R(130321,160000)]
    assert T == [R(1),-R(419,400),R(399,8000),-R(6859,64000000)]
    XH=add(H,[R(0)]+derivative(H))  # not used: derivative of xH follows below
    # F=(H+xH')T-xHT'
    F=add(multiply(add(H, [R(0)]+derivative(H)),T),scale([R(0)]+multiply(H,derivative(T)),-1))
    P=[R(25600000000),-R(92544000000),R(109747200000),-R(43678112000),R(1035002523)]
    assert F == scale(P,R(1,25600000000))
    K=e*(1-e)
    for s in [R(1,10),R(1,4),R(1,2),R(3,4),R(9,10),R(99,100),R(1)]:
        x=s*s
        formula=value(T,x)/(value(T,x)+K*x*value(H,x))
        assert formula == direct_response(p,s)
    seq=sturm(P)
    at0=signs_at(seq,R(0));at1=signs_at(seq,R(1))
    assert at0 == [1,-1,1,-1,1]
    assert at1 == [1,1,-1,1,1]
    assert changes(at0)-changes(at1) == 2
    assert value(P,R(13,20))>0>value(P,R(33,50))
    assert value(P,R(87,100))<0<value(P,R(22,25))
    # Uniform sign bound: for 0<e<=3/50, g is increasing and g(3/50)<8.
    E=R(3,50)
    g=lambda t:105*t+t*t*(468-1413*t)+2106*t**4+2187*t**6+243*t**8
    assert g(E) == R(301054212401823,39062500000000)
    assert g(E)<8
    print('Exact continuants, 7 independent resolvents, Sturm root count,')
    print('two rational root brackets, and uniform parameter bound: PASS')
    print('Sturm variations on [0,1]:', changes(at0), changes(at1))


if __name__=='__main__': main()
