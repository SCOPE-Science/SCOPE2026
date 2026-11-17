#!/usr/bin/env python3
"""Independent exact-rational moment checks for complete-bipartite stable-set polytopes.

Uses a uniform random linear extension of the two-level poset and moments of
uniform order statistics. Requires only Python 3 standard library.
"""
from fractions import Fraction as F
from math import factorial


def rank_moments(a,b):
    n=a+b
    D=(n+1)*(n+2)
    rx=list(range(1,a+1)); rz=list(range(a+1,n+1))
    def ex(r): return F(r,n+1)
    def second(r,s): return F(min(r,s)*(max(r,s)+1),D)
    def y(r): return 1-ex(r)
    def yz(r,s):return 1-ex(r)-ex(s)+second(r,s)
    def avg(seq, func):return sum((func(x) for x in seq),F(0))/len(seq)
    def avgoff(seq, func):return sum((func(x,y) for x in seq for y in seq if x!=y),F(0))/(len(seq)*(len(seq)-1))
    mx=avg(rx,ex); my=avg(rz,y)
    x2=avg(rx,lambda r:second(r,r))
    y2=avg(rz,lambda r:yz(r,r))
    xx=avgoff(rx,second)
    yy=avgoff(rz,yz)
    xy=sum((ex(r)-second(r,s) for r in rx for s in rz),F(0))/(a*b)
    return mx,my,x2,y2,xx,yy,xy


def beta_moments(a,b):
    n=a+b; D=(n+1)*(n+2)
    return (F(a+1,2*(n+1)), F(b+1,2*(n+1)),
            F((a+1)*(a+2),3*D),F((b+1)*(b+2),3*D),
            F((a+1)*(a+2),4*D),F((b+1)*(b+2),4*D),
            F((a+1)*(b+1),4*D))


def spectral_parts(a,b):
    n=a+b; D=(n+1)**2*(n+2)
    ca=F((a+1)*(a+2),12*(n+1)*(n+2))
    cb=F((b+1)*(b+2),12*(n+1)*(n+2))
    A=F((a+1)*(a*a+4*a*b+3*a+2*b+2),12*D)
    B=F((b+1)*(b*b+4*a*b+3*b+2*a+2),12*D)
    # off-diagonal is -sqrt(a*b)*W; only its square is rational.
    W=F((a+1)*(b+1),4*D)
    C2=a*b*W*W
    return ca,cb,A,B,C2


def verify_one(a,b):
    r=rank_moments(a,b)
    assert r==beta_moments(a,b), (a,b,r,beta_moments(a,b))
    mx,my,x2,y2,xx,yy,xy=r
    ca,cb,A,B,C2=spectral_parts(a,b)
    assert x2-xx==ca and y2-yy==cb
    assert (x2-mx*mx)+(a-1)*(xx-mx*mx)==A
    assert (y2-my*my)+(b-1)*(yy-my*my)==B
    assert a*b*(xy-mx*my)**2==C2
    n=a+b
    assert A-ca==F(a*b*(a+1),4*(n+1)**2*(n+2))
    assert B-cb==F(a*b*(b+1),4*(n+1)**2*(n+2))
    det=(A-ca)*(B-ca)-C2
    expected=F(a*b*(a+1)*(b*b-a*a-3*a-3),48*(n+1)**3*(n+2)**2)
    assert det==expected
    other=(A-cb)*(B-cb)-C2
    other_expected=F(a*b*(b+1)*(a*a-b*b-3*b-3),48*(n+1)**3*(n+2)**2)
    assert other==other_expected
    assert A*B-C2==F((a+1)*(b+1)*(2*a*b+a+b+2),72*(n+1)**2*(n+2)**2)
    if a<=b:
        # lambda+ exceeds both ca and cb; the lower eigenvalue is
        # below ca exactly when det(M-ca I) is negative.
        assert (det<0)==(b-a<=1)
        assert det!=0
        assert other<0
    if a==b:
        s=a
        assert A==B
        assert C2==F(s*s*(s+1)**4,16*(2*s+1)**4*(2*s+2)**2)
        off=F(s*(s+1)**2,4*(2*s+1)**2*(2*s+2))
        assert A+off==F(1,12)
        assert A-off==F(s*s+s+1,12*(2*s+1)**2)


def main():
    checked=0
    for a in range(2,16):
        for b in range(2,16):
            verify_one(a,b)
            checked+=1
    # Independent symbolic-sign boundary over a much larger integer range.
    signs=0
    for a in range(2,301):
        for difference in range(0,30):
            b=a+difference
            N=b*b-a*a-3*a-3
            assert (N<0)==(difference<=1)
            signs+=1
    print(f'BIPARTITE_STABLE_COVARIANCE_CHECKS_PASSED exact_rank_and_beta_profiles={checked} threshold_sign_tests={signs}')

if __name__=='__main__':
    main()
