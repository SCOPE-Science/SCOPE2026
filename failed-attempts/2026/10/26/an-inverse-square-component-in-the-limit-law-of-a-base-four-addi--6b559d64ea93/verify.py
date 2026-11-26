"""Exact finite checks for a base-four additive-complement limiting law.

This verifies finite identities and rational Cantor-gap CDF enclosures.
It does not purport to prove infinite convergence or bibliographic novelty.
Standard library only; run with Python 3.9+.
"""
from bisect import bisect_right
from fractions import Fraction


def prefixes(k):
    return sorted(sum(((v >> j) & 1) * (4 ** j) for j in range(k))
                  for v in range(1 << k))


def cylinder_gaps(k):
    """Return exact gaps (integer scaled endpoints, exact c) at depth k.

    All physical endpoints are divided by 3*4**k. Each returned c is
    the exact product F(u)G(u) on the full gap, not an approximation.
    """
    aa = prefixes(k)
    bb = [2*a for a in aa]
    intervals = sorted([(3*a, 3*a+1) for a in aa] +
                       [(3*b, 3*b+2) for b in bb])
    merged = []
    for a,b in intervals:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a,b))
    scale = 3 * (4**k)
    assert merged[0][0] == 0 and merged[-1][1] <= scale
    raw = [(x[1],y[0]) for x,y in zip(merged,merged[1:])
           if x[1] < y[0]]
    if merged[-1][1] < scale:
        raw.append((merged[-1][1],scale))
    ae = [3*a+1 for a in aa]
    be = [3*b+2 for b in bb]
    gaps = []
    for a,b in raw:
        # Entire depth-k cylinders to the left count their full measure.
        fa = bisect_right(ae,a)
        gb = bisect_right(be,a)
        c = Fraction(fa*gb,4**k)
        assert c > 0 and 0 <= a < b <= scale
        gaps.append((a,b,c))
    unresolved = Fraction(scale-sum(b-a for a,b,_ in gaps),scale)
    assert 0 <= unresolved <= Fraction(1,2**k)
    return gaps,unresolved,scale


def cdf_lower(k,t):
    """Rational certified CDF lower approximation at t>0."""
    gaps,tail,scale = cylinder_gaps(k)
    area = Fraction(0)
    for a,b,c in gaps:
        low,high = Fraction(a,scale),Fraction(b,scale)
        area += max(Fraction(0),high-max(low,c/t))
    assert Fraction(0) <= area <= 1-tail
    return area,tail


def finite_cdf(k,t):
    aa=prefixes(k)
    bb=[2*a for a in aa]
    n=4**k
    num=0
    for j in range(1,n+1):
        prod=bisect_right(aa,j)*bisect_right(bb,j)
        if j==n:
            prod=(len(aa)+1)*len(bb)
        if prod * t.denominator <= j*t.numerator:
            num+=1
    return Fraction(num,n)


def test_unique_and_ratio(k):
    aa=prefixes(k)
    bb=[2*a for a in aa]
    bset=set(bb)
    n=4**k
    for t in range(n):
        assert sum(1 for a in aa if 0 <= t-a in bset)==1
        counta=bisect_right(aa,t)
        countb=bisect_right(bb,t)
        assert counta*countb >= t+1
    assert aa[-1]*3 == n-1
    assert bb[-1]*3 == 2*(n-1)


def test_macro_gaps(k):
    gaps,tail,scale=cylinder_gaps(k)
    lookup={(Fraction(a,scale),Fraction(b,scale)):c
            for a,b,c in gaps}
    for j in range(k):
        four=4**j
        left1,right1=Fraction(1,3*four),Fraction(1,2*four)
        left2,right2=Fraction(2,3*four),Fraction(1,four)
        assert lookup[(left1,right1)]==Fraction(1,2*four)
        assert lookup[(left2,right2)]==Fraction(1,four)
    # Both families together occupy 2/3 of Lebesgue space in the limit.
    finite_mass=sum(Fraction(1,2*4**j) for j in range(k))
    assert finite_mass == Fraction(2,3)*(1-Fraction(1,4**k))


def main():
    for k in range(1,7):
        test_unique_and_ratio(k)
    for k in range(1,9):
        test_macro_gaps(k)
        for t in [Fraction(11,10),Fraction(5,4),Fraction(7,5)]:
            low,tail=cdf_lower(k,t)
            assert low <= 1 and low+tail<=1
            # The two explicit macro families alone contribute this much.
            macro = 2*(1-Fraction(1,4**k))*(1-1/t)
            assert low >= macro
    k=8
    vals=[]
    for t in [Fraction(11,10),Fraction(5,4),Fraction(7,5)]:
        low,tail=cdf_lower(k,t)
        vals.append(f't={t}: lower={low} upper={low+tail}')
    sample=finite_cdf(6,Fraction(5,4))
    print('VERIFY_OK unique_representation=4096_at_depth6 exact_macro_gaps=all_depths_1_to_8')
    print('CANTOR_CDF_ENCLOSURES depth8 '+ ' | '.join(vals))
    print(f'FINITE_EMPIRICAL_CDF depth6 threshold=5/4 value={sample} (not infinite certificate)')


if __name__=='__main__':
    main()
