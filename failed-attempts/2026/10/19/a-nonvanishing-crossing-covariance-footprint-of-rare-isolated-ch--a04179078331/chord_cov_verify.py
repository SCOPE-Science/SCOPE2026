"""Exact-rational exhaustive checks of crossing/isolated-chord joint statistics.

Run: python chord_cov_verify.py
Standard-library only. Finite tests corroborate, but do not prove, all-n statements.
"""
from fractions import Fraction
from math import comb


def double_factorial(k):
    out = 1
    for t in range(k, 0, -2):
        out *= t
    return out


def analytic(n):
    assert n >= 2
    d = double_factorial(2*n-1)
    e_y = Fraction(0)
    e_z = Fraction(0)
    cov_y = Fraction(0)
    cov_z = Fraction(0)
    for r in range(n):
        s = n-1-r
        w = Fraction(double_factorial(2*r-1)*double_factorial(2*s-1), d)
        e_y += n*w
        cov_y -= Fraction(n,3)*w*(n-1+r*s)
        if r not in (0,n-1):
            e_z += n*w
            cov_z -= Fraction(n,3)*w*(n-1+r*s)
    e_s = Fraction(2*n,2*n-1)
    cov_s = -Fraction(n-1,3)*e_s
    assert e_y == e_s + e_z
    assert cov_y == cov_s + cov_z
    return e_y,e_s,e_z,cov_y,cov_s,cov_z


def matchings(remaining):
    if not remaining:
        yield ()
        return
    a = remaining[0]
    for i in range(1,len(remaining)):
        b=remaining[i]
        tail = remaining[1:i]+remaining[i+1:]
        for sub in matchings(tail):
            yield ((a,b),)+sub


def observed(n):
    total = 0
    sx=sy=ss=sz=sxy=sxs=sxz=0
    for chords in matchings(tuple(range(2*n))):
        total += 1
        degrees=[0]*n
        x=0
        for i in range(n):
            a,b=chords[i]
            for j in range(i+1,n):
                c,d=chords[j]
                cr = (a<c<b<d) or (c<a<d<b)
                if cr:
                    x+=1; degrees[i]+=1; degrees[j]+=1
        y=sum(d==0 for d in degrees)
        s=sum((b-a in (1,2*n-1)) for a,b in chords)
        z=y-s
        assert z>=0
        sx+=x;sy+=y;ss+=s;sz+=z
        sxy+=x*y;sxs+=x*s;sxz+=x*z
    den=Fraction(1,total)
    ex=sx*den
    ey=sy*den
    es=ss*den
    ez=sz*den
    cy=sxy*den-ex*ey
    cs=sxs*den-ex*es
    cz=sxz*den-ex*ez
    assert ex==Fraction(n*(n-1),6)
    return (ey,es,ez,cy,cs,cz),total


def main():
    grand_total=0
    for n in range(2,8):
        expected=analytic(n)
        actual,count=observed(n)
        assert expected==actual,(n,expected,actual)
        grand_total+=count
        print('n',n,'matchings',count,'covY',expected[3],'covZ',expected[5], 'PASS')
    print('ALL PASS: {} diagrams total'.format(grand_total))

if __name__=='__main__':
    main()
