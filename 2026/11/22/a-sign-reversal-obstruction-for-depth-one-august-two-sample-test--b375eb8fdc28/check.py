"""Exact arithmetic checks for the depth-one AUGUST sign-reversal theorem.

Requires Python 3.9+ standard library only. Run: python check.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def scale(a, c):
    return trim([x*c for x in a])


def mul(a, b):
    out = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def pow_poly(a, n):
    v = [F(1)]
    for _ in range(n):
        v = mul(v, a)
    return v


def derivative(a):
    return trim([a[i]*i for i in range(1,len(a))] or [F(0)])


def integral01(a):
    return sum((x/F(i+1) for i,x in enumerate(a)), F(0))


def compose(a, b):
    v = [F(0)]
    for c in a[::-1]:
        v = add(mul(v,b),[c])
    return v


def evaluate(a, x):
    t = F(0)
    for c in a[::-1]:
        t = t*x+c
    return t


def bernstein_coefficients_cubic_on(a, lo, hi):
    v = compose(a,[lo, hi-lo])
    v = v + [F(0)]*(4-len(v))
    return [sum((v[k]*F(comb(j,k),comb(3,k))
                 for k in range(j+1)),F(0)) for j in range(4)]


def exact_rank_statistic(xloc, m, n):
    xs=set(xloc)
    ys=set(range(m+n))-xs
    def h_reference(k, ref_size):
        a = comb(ref_size-k,3) if ref_size-k>=3 else 0
        b = k*comb(ref_size-k,2) if ref_size-k>=2 else 0
        return F(2*(a+b), comb(ref_size,3))-1
    sx = sum((h_reference(sum(y<x for y in ys),n) for x in xs),F(0))/m
    sy = sum((h_reference(sum(x<y for x in xs),m) for y in ys),F(0))/n
    return -sx*sy


def all_checks():
    checks=0
    h=[F(1),F(0),F(-6),F(4)]
    Q=[F(0),F(1157,700),F(243,700),F(-5),F(4)]
    dQ=derivative(Q)
    assert evaluate(Q,F(0))==0 and evaluate(Q,F(1))==1;checks+=2
    assert integral01(dQ)==1;checks+=1
    assert dQ==[F(1157,700),F(243,350),F(-15),F(16)];checks+=1
    pieces=[(F(0),F(1,2)),(F(1,2),F(3,4)),(F(3,4),F(1))]
    expected=[ [F(1157,700),F(619,350),F(111,175),F(1,4)],
              [F(1,4),F(81,1400),F(149,2800),F(1361,2800)],
              [F(1361,2800),F(2573,2800),F(501,280),F(2343,700)] ]
    for (lo,hi),exp in zip(pieces,expected):
        b=bernstein_coefficients_cubic_on(dQ,lo,hi)
        assert b==exp and min(b)>0, (lo,hi,b,exp)
        checks+=len(b)+1
    A=integral01(mul(h,dQ))
    B=integral01(compose(h,Q))
    assert A==F(1,250),(A,B);checks+=1
    assert B==F(45549381047,5150145000000),B;checks+=1
    assert -A*B==F(-45549381047,1287536250000000);checks+=1
    assert A>0 and B>0;checks+=2
    var_h=integral01(mul(h,h))
    assert integral01(h)==0 and var_h==F(17,35);checks+=2
    # Under the null, uniform pooled labels give all compositions equally.
    for m,n in [(3,3),(3,4),(4,3),(4,4),(4,5),(5,4),(5,5),(5,6),(6,6)]:
        total=sum((exact_rank_statistic(xs,m,n)
                   for xs in combinations(range(m+n),m)),F(0))
        avg=total/F(comb(m+n,m))
        target=F(17*(m+n+1),35*m*n)
        assert avg==target,(m,n,avg,target)
        checks+=1
    # Symbolic decomposition for arbitrary perturbation Q=u+psi.
    # Since h(u+psi) is cubic, the identity is exact.
    u=[F(0),F(1)]; psi=add(Q,scale(u,-1))
    # a(Q) = 12 * integral u(1-u) psi(u) du.
    a2=12*integral01(mul(mul(u,add([F(1)],scale(u,-1))),psi))
    assert a2==A;checks+=1
    rhs=(-A+12*integral01(mul(add(u,[F(-1,2)]),mul(psi,psi)))
         +4*integral01(pow_poly(psi,3)))
    assert rhs==B;checks+=1
    # One fixed reference y: 2 E median(y,U,V)-1 = -h(y)/3.
    # E median = integral_0^y (1-t^2)dt + integral_y^1 (1-t)^2dt.
    Em=[F(1,3),F(0),F(1),F(-2,3)]
    assert add(scale(Em,2),[F(-1)])==scale(h,F(-1,3));checks+=1
    # Finite overlap kernel cross-moment. For two shared comparison
    # observations, condition on x<y and integrate the two quadratic factors.
    # 2 * int_0^1 int_0^y (1-2x^2)*(1-4y+2y^2) dx dy.
    first=[F(0), F(1),F(0),F(-2,3)]
    second=[F(1),F(-4),F(2)]
    assert 2*integral01(mul(first,second))==F(-17,45);checks+=1
    # One shared comparison gives -Var(h)/3; two shared give -17/45.
    assert -var_h/3==F(-17,105);checks+=1
    print(f'PASS: {checks} independent exact identities/checks')
    print('Q coefficients:', [str(x) for x in Q]);print('A=',A,'B=',B,'limit=',-A*B)
    print('Null variance for h(U):', var_h)

if __name__=='__main__':
    all_checks()
