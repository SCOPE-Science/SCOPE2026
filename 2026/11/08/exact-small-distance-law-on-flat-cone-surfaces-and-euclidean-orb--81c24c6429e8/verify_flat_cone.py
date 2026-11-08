#!/usr/bin/env python3
"""Standalone numerical checks for the flat-cone short-distance identity.

Requires Python 3 standard library only. Numerical checks do not replace proof.
"""
from math import pi, sin, cos, tan, asin, acos, sqrt


def simpson(fun, lo, hi, n=800):
    assert n % 2 == 0
    h = (hi-lo)/n
    s = fun(lo)+fun(hi)
    for i in range(1,n):
        s += (4 if i&1 else 2)*fun(lo+i*h)
    return s*h/3


def angular_integrand(theta):
    eps = pi-theta
    if eps < .02:
        return 1/24+eps*eps/60+eps**4/252+eps**6/1350
    return (sin(theta)+(pi-theta)*cos(theta))/(8*sin(theta)**3)


def k_exact(alpha):
    phi = alpha/2
    return alpha/8*(1/tan(phi)+(pi-phi)/sin(phi)**2)


def k_angle_quad(alpha):
    return 2*alpha*simpson(angular_integrand, alpha/2, pi, 30000)


def ball_area_on_cone(u, phi):
    # Integrate the radial quadratic inequality in each angular direction.
    if u < 1:
        def f(t):
            z = sqrt(max(0,1-u*u*sin(t)**2))
            return (u*cos(t)+z)**2
        return simpson(f, 0., phi, 300)
    if u == 1:
        u=1-1e-12
        return ball_area_on_cone(u,phi)
    upper = min(phi,asin(1/u))
    def f(t):
        return 4*u*cos(t)*sqrt(max(0,1-u*u*sin(t)**2))
    return simpson(f, 0., upper, 300)


def k_radial_quad(alpha):
    phi=alpha/2
    max_u=1/sin(phi) if phi<=pi/2 else 1
    # Split integration at u=1, where the radial bounds change.
    def f(u):
        return alpha*u*(pi-ball_area_on_cone(u,phi))
    k=simpson(f,0,1,500)
    if max_u>1+1e-10:
        k+=simpson(f,1,max_u,500)
    return k


def lens_area(s,r):
    if s>=2*r:return 0.
    return 2*r*r*acos(s/(2*r))-.5*s*sqrt(max(0,4*r*r-s*s))


def run():
    for m in (2,3,4,6):
        alpha=2*pi/m
        ka=k_exact(alpha)
        kb=k_angle_quad(alpha)
        kc=k_radial_quad(alpha)
        print(f'cone_order={m}: closed={ka:.12f} angular={kb:.12f} radial={kc:.12f}')
        assert abs(ka-kb)<2e-9, (m,ka,kb)
        assert abs(ka-kc)<.003, (m,ka,kc)
    for alpha in (.9*pi,1.6*pi,1.96*pi):
        assert abs(k_exact(alpha)-k_angle_quad(alpha))<2e-8
    # On the square pillowcase, the average overlap of the two disks
    # is the convolution integral of two radius-r disk indicators.
    for r in (.12,.21,.34):
        lens_integral=simpson(lambda s:2*pi*s*lens_area(s,r),0,2*r,4000)
        assert abs(lens_integral-(pi*r*r)**2)<2e-8
    c=lambda m:k_exact(2*pi/m)
    signatures={'torus':0.,'(2,2,2,2)':4*c(2),'(3,3,3)':3*c(3),
                '(2,4,4)':c(2)+2*c(4),'(2,3,6)':c(2)+c(3)+c(6)}
    magnitudes=list(signatures.values())
    assert all(magnitudes[i]<magnitudes[i+1] for i in range(4))
    for label,value in signatures.items():print('signature',label,'positive_defect',f'{value:.12f}')
    print('FLAT_CONE_CHECK_OK angular=7 radial=4 pillowcase_convolutions=3 signatures=5')


if __name__=='__main__':run()
