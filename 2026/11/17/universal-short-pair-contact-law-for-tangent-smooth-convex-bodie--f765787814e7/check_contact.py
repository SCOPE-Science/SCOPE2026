"""Reproduce independent quadratures for tangent-disk contact asymptotics.

Requires scipy and numpy. Run: python check_contact.py
"""
from math import sqrt, asin, pi
from scipy.integrate import quad
from scipy.special import beta


def overlap_unit_disks(distance):
    """Exact area shared by unit disks separated by distance <= 2."""
    if distance >= 2:
        return 0.0
    z = sqrt(max(0.0, 1.0 - distance * distance / 4.0))
    return 2.0 * (asin(z) - distance * z / 2.0)


def independent_two_disk_probability(radius):
    """Integrate the exact translate-overlap formula, not the local proof."""
    def integrand(t):
        smax = min(sqrt(max(0.0, 1.0 - t*t)),
                   sqrt(max(0.0, 4.0*t/radius - t*t)))
        val = quad(lambda s: overlap_unit_disks(
            sqrt((2.0-radius*t)**2+(radius*s)**2)),
            0.0, smax, epsabs=3e-13, limit=150)[0]
        return 2.0 * radius**2 * val / pi**2
    return quad(integrand, 0.0, 1.0, epsabs=4e-13, limit=200)[0]


def crossover(lam, k=1.0):
    if lam >= 1:
        return 0.0
    return 8/(3*sqrt(k))*quad(
        lambda h: (h-lam)**1.5 * sqrt(max(0.0,1-h*h)),
        lam, 1.0, epsabs=1e-12)[0]


def main():
    C = 4*beta(1.25,1.5)/(3*pi*pi)
    volume = crossover(0.0)
    assert abs(volume - 4*beta(1.25,1.5)/3)<1e-9
    assert abs(C-volume/pi**2)<1e-9
    ratios=[]
    for r in (0.30,0.15,0.07,0.03):
        p = independent_two_disk_probability(r)
        ratio=p/(C*r**3.5)
        ratios.append(ratio)
        print(f"radius={r:.3f} probability={p:.12g} scaled_coefficient={p/r**3.5:.10f} ratio={ratio:.8f}")
    assert all(0.9 < a < 1.03 for a in ratios)
    assert all(ratios[i] < ratios[i+1] for i in range(len(ratios)-1))
    print('limiting_coefficient',format(C,'.12g'))
    for lam in (0.,.2,.6,.9,.98):
        v=crossover(lam)
        print(f'lambda={lam:.2f} crossover={v:.12g}')
        assert v >= 0
    assert all(crossover(a)>crossover(b) for a,b in ((0,.2),(.2,.6),(.6,.9),(.9,.98)))
    for p in (1,2,3):
        moment = quad(lambda h: h**(1.5+p)*sqrt(1-h*h),0,1)[0]/quad(
            lambda h: h**1.5*sqrt(1-h*h),0,1)[0]
        expected=beta(1.25+p/2,1.5)/beta(1.25,1.5)
        assert abs(moment-expected)<1e-10
    print('TANGENT_CONTACT_QUADRATURE_AND_BETA_CHECKS_OK')


if __name__=='__main__':
    main()
