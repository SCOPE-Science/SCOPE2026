#!/usr/bin/env python3
"""Independent finite-direction numerical checks for the stated convex-geometric formulas.
No finite check replaces the proof for all polygon orders and angles.
"""
import math

PI = math.pi


def data(n):
    alpha = PI/n
    c, s = math.cos(alpha), math.sin(alpha)
    vertices = [(math.cos(2*PI*j/n), math.sin(2*PI*j/n)) for j in range(n)]
    polar_vertices = [(math.cos((2*j+1)*PI/n)/c,
                       math.sin((2*j+1)*PI/n)/c) for j in range(n)]
    return alpha, c, s, vertices, polar_vertices


def direct_supports(theta, vertices, polar_vertices):
    ux, uy = math.cos(theta), math.sin(theta)
    # Projection onto the line perpendicular to u; take length of its image.
    projections = [(-uy*x + ux*y) for x, y in vertices]
    projected_length = max(projections)-min(projections)
    polar_support = max(ux*x+uy*y for x,y in polar_vertices)
    return projected_length, polar_support


def exact_values(n):
    alpha = PI/n
    c, s = math.cos(alpha), math.sin(alpha)
    lam_zer = 2*c
    if n % 4 == 2:
        return lam_zer, 0.0, 0.0, lam_zer, 0.0
    a = alpha+s*c
    lam = 2*c*(s+alpha*c)/a
    residual = 4*n*s*s*(alpha*alpha-s*s)/a
    normalized = s*s*(alpha*alpha-s*s)/a**2
    return lam, residual, normalized, lam_zer, 2*(1-c)


def check(n, count=10000):
    alpha,c,s,vertices,polar_vertices = data(n)
    l2,e2,relative,linf,einf=exact_values(n)
    h1_sq=h2_sq=cross=0.0
    maxerr=0.0
    for i in range(count):
        theta = 2*PI*(i+0.5)/count
        h1,h2 = direct_supports(theta,vertices,polar_vertices)
        h1_sq += h1*h1; h2_sq += h2*h2; cross += h1*h2
        maxerr=max(maxerr,abs(h1-linf*h2))
    for theta in (0.0, alpha):
        h1,h2 = direct_supports(theta,vertices,polar_vertices)
        maxerr=max(maxerr,abs(h1-linf*h2))
    factor=2*PI/count
    h1_sq*=factor; h2_sq*=factor;cross*=factor
    best_l2=cross/h2_sq
    best_e2=h1_sq-cross*cross/h2_sq
    assert abs(l2-best_l2)<3e-5,(n,l2,best_l2)
    assert abs(e2-best_e2)<3e-5,(n,e2,best_e2)
    assert abs(relative-e2/h1_sq)<2e-6,(n,relative,e2/h1_sq)
    assert abs(maxerr-einf)<2e-5,(n,maxerr,einf)
    if n%4==0:
        for t in (0.03,0.18,0.37,0.55,0.79,0.96):
            r=2*c*c+2*(1-c*c)*t
            u=math.atan(c*(2-r)/(s*r))
            cdf=1-u/alpha
            # Empirical cumulative distribution with uniform direction samples.
            count_less=0
            for j in range(5000):
                theta=2*PI*(j+0.5)/5000
                h1,h2=direct_supports(theta,vertices,polar_vertices)
                count_less += (h1/h2 <=r)
            assert abs(cdf-count_less/5000)<0.004,(n,r,cdf,count_less/5000)
    print(f'N={n}: direct support/polar integrals, CDF and optimal scales agree')


if __name__ == '__main__':
    for n in (4,6,8,10,12,16,20):
        check(n)
    # Asymptotic constants are tested independently of raw quadrature.
    for n in (256,512,1024):
        a=PI/n
        lam,E,D2,lam_inf,H=exact_values(n)
        assert n%4==0
        assert abs(E/((2*PI**5)/(3*n**4))-1)<1e-3,(n,E)
        assert abs(math.sqrt(D2)/(PI**2/(2*math.sqrt(3)*n**2))-1)<1e-3
        assert abs(H/(PI**2/n**2)-1)<1e-3
    print('Asymptotic scales agree. All independent numerical checks passed.')
