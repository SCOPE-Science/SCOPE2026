"""Independent finite checks for weighted Bergman radial row Hankel blocks."""
from fractions import Fraction as Q
import mpmath as mp

checks = 0
for n in range(1, 90):
    # Uniform disk: the squared-radius beta(n+1, 1) moments.
    e = lambda j: Q(n+1, n+j+1)
    q = Q(n+2,n+1)
    g11 = q*(e(2)-e(1)**2)
    g12 = q*(e(3)-e(1)*e(2))
    g22 = q*(e(4)-e(2)**2)
    det = g11*g22-g12*g12
    assert g11 > 0 and det > 0
    checks += 2
    # For t,t^2 the smaller branch limit has constant 2/sqrt(5).
    # This determinant and trace are exact finite beta moments.
    assert det == Q(4, (n+3)**3*(n+4)**2*(n+5))
    checks += 1

mp.mp.dps = 65
for s in [mp.mpf(1), mp.mpf('2.5')]:
    n = 300
    beta = mp.beta(s, n+1)
    def expect(f):
        return mp.quad(lambda u:f(u)*u**(s-1)*(1-u)**n,[0,1])/beta
    h1=lambda u: 1-u
    h2=lambda u: (1-u)*mp.exp(-u)
    m1,m2=expect(h1),expect(h2)
    q=mp.mpf(n+s+1)/(n+1)
    a=q*(expect(lambda u:h1(u)**2)-m1*m1)
    b=q*(expect(lambda u:h1(u)*h2(u))-m1*m2)
    c=q*(expect(lambda u:h2(u)**2)-m2*m2)
    eig=mp.eigsy(mp.matrix([[a,b],[b,c]]),eigvals_only=True)
    top=mp.sqrt(eig[1]); bottom=mp.sqrt(eig[0])
    lead=mp.sqrt(5*s)
    second=3*mp.sqrt(s*(s+1)/2)/mp.sqrt(5)
    assert abs(n*top/lead-1)<mp.mpf('0.04')
    assert abs(n*n*bottom/second-1)<mp.mpf('0.07')
    checks += 2
print(f'PASS {checks} finite exact-rational and high-precision assertions')
