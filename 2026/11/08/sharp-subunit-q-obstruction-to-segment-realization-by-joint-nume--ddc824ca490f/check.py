"""Exact algebraic checks for the sharp subunit-q segment approximation law.

The universal Hilbert-space inequalities are proved analytically in RESULT.md;
finite checks here test only the explicit algebra and extremal ellipse.
Run with: python check.py
"""
from fractions import Fraction as Q

checks = 0

def verify(condition, label):
    global checks
    assert condition, label
    checks += 1

# Rational points on the unit circle: r^2+s^2=1, 0<r,s<1.
triples = [(3,4,5), (5,12,13), (8,15,17), (7,24,25),
           (20,21,29), (9,40,41), (12,35,37), (11,60,61)]
lengths = [Q(1,1), Q(2,1), Q(3,2), Q(11,7), Q(17,4)]
for a,b,c in triples:
    r, s = Q(a,c), Q(b,c)
    verify(r*r+s*s==1, 'unit-circle parameters')
    scale=1/(1+s)
    verify(scale*(1+s)==1, 'optimal scale')
    verify(1-scale==s*scale, 'Hausdorff balance')
    verify(0<scale<1, 'admissible extremal scale')
    for L in lengths:
        eps=L*s/(2*(1+s))
        verify(2*eps==s*(L-2*eps), 'sharp lower bound equality')
        verify(eps == L/2 * (1-scale), 'segment-to-ellipse distance')
        verify(eps == L/2 * scale*s, 'ellipse-to-segment distance')
        verify(0<eps<L/4, 'strict subunit positive separation')
    # Parameterized ellipse: z = r*u + s*sqrt(1-u^2)*exp(i*theta).
    # Choosing rational u and theta allows exact checking that
    #   Re(z)^2 + Im(z)^2/s^2 <= 1.
    points=[(Q(0),Q(1)),(Q(1),Q(0)),(Q(-1),Q(0))]
    for aa,bb,cc in triples:
        points += [(Q(aa,cc),Q(bb,cc)), (Q(-aa,cc),Q(bb,cc))]
    circle=[(Q(1),Q(0)),(Q(-1),Q(0)),(Q(0),Q(1)),(Q(0),Q(-1))]
    for aa,bb,cc in triples:
        circle += [(Q(aa,cc),Q(bb,cc)),(Q(aa,cc),-Q(bb,cc))]
    for u,v in points:
        verify(u*u+v*v==1, 'circle point u,v')
        for co,si in circle:
            verify(co*co+si*si==1, 'circle phase')
            xx = r*u + s*v*co
            yy = s*v*si
            verify(xx*xx + yy*yy/(s*s) <=1, 'ellipse exact containment')
            verify(-1<=xx<=1, 'horizontal semimajor')
            verify(-s<=yy<=s, 'vertical semiminor')
print('SUBUNIT_Q_SEGMENT_CHECK_OK', checks, 'exact rational assertions')
