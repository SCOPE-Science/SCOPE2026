from fractions import Fraction
from math import comb, sqrt

def expected_os_two_point(x, y, p):
    q = Fraction(1, 1) - p
    h = y - x
    out = []
    for j in range(1, 5):
        prob_high = sum(Fraction(comb(4,k),1) * p**k * q**(4-k) for k in range(0,j))
        out.append(x + h * prob_high)
    return out


def expected_os_discrete(xs, ps, n=4):
    cum = []
    total = 0.0
    for p in ps:
        total += p
        cum.append(total)
    ans = []
    for j in range(1, n+1):
        prev = 0.0
        val = 0.0
        for x,F in zip(xs,cum):
            cdf = sum(comb(n,k)*(F**k)*((1-F)**(n-k)) for k in range(j,n+1))
            val += x*(cdf-prev)
            prev = cdf
        ans.append(val)
    return ans

# Boundary family: every rational two-point parent produces equality, and
# the reconstruction formulas recover its probability and support.
boundary_cases = 0
for p in [Fraction(1,5), Fraction(1,4), Fraction(1,3), Fraction(2,5),
          Fraction(1,2), Fraction(3,5), Fraction(2,3), Fraction(3,4), Fraction(4,5)]:
    for h in [Fraction(3,2), Fraction(2,1), Fraction(7,3)]:
        x = Fraction(-5,3)
        y = x + h
        beta = expected_os_two_point(x,y,p)
        a,b,c = beta[1]-beta[0], beta[2]-beta[1], beta[3]-beta[2]
        assert 9*a*c == 4*b*b
        pr = sqrt(float(c)) / (sqrt(float(a)) + sqrt(float(c)))
        hr = (sqrt(float(a)) + sqrt(float(c)))**4 / (4*sqrt(float(a*c)))
        xr = float(beta[0]) - float(a)**1.5/(4*sqrt(float(c)))
        yr = float(beta[3]) + float(c)**1.5/(4*sqrt(float(a)))
        assert abs(pr-float(p)) < 2e-13
        assert abs(hr-float(h)) < 2e-12
        assert abs(xr-float(x)) < 2e-12
        assert abs(yr-float(y)) < 2e-12
        boundary_cases += 1

# Strict interior: the first two generator moments implied by the three
# EOS gaps admit a continuum of explicit two-atom generators.
strict_cases = 0
for a,b,c in [(2.0,2.0,2.0),(1.0,1.0,1.0),(1.0,0.5,3.0),(4.0,2.0,2.0),(3.0,1.0,5.0)]:
    assert 9*a*c > 4*b*b
    S = 3*a + 4*b + 3*c
    m = (3*c + 2*b)/S
    s2 = 3*c/S
    v = s2 - m*m
    assert 0 < v < m*(1-m)
    lo, hi = v/(1-m), m
    for frac in [0.2,0.4,0.6,0.8]:
        u = lo + frac*(hi-lo)
        r = m-u
        s = m+v/u
        w = v/(u*u+v)
        assert 0 < r < s < 1
        assert 0 < w < 1
        mm = w*r + (1-w)*s
        vv = w*(r-mm)**2 + (1-w)*(s-mm)**2
        assert abs(mm-m) < 2e-14
        assert abs(vv-v) < 2e-14
        # Construct the normalized three-point parent induced by this generator.
        d1 = w/(r*(1-r))
        d2 = (1-w)/(s*(1-s))
        z0 = -(1-r)*d1 - (1-s)*d2
        z1 = z0+d1
        z2 = z1+d2
        masses = (r, s-r, 1-s)
        assert all(t > 0 for t in masses)
        assert abs(sum(masses)-1) < 2e-14
        assert abs(masses[0]*z0 + masses[1]*z1 + masses[2]*z2) < 3e-13
        # The source normalization has scale lambda=S/12 and location equal to
        # the average of the four expected order statistics.
        beta = [0.0, a, a+b, a+b+c]
        center = sum(beta)/4.0
        scale = S/12.0
        parent_x = [center+scale*z0, center+scale*z1, center+scale*z2]
        got = expected_os_discrete(parent_x, masses)
        assert max(abs(g-t) for g,t in zip(got,beta)) < 3e-11, (a,b,c,u,got,beta)
        strict_cases += 1

print(f"VERIFY_OK boundary_cases={boundary_cases} strict_generators={strict_cases}")
