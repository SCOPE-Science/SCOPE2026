#!/usr/bin/env python3
"""Independent numerical and algebraic consistency tests for a polygonal Fourier radial cusp."""
import math
import mpmath as mp
mp.mp.dps=75
p=mp.mpf('1.5')
beta=2-p
coefficient=mp.pi/(mp.gamma(5-p)*mp.sin(mp.pi*p/2))

def triangle_fourier(r, x, y):
    ts=[mp.mpf(0), x,y]
    z=[]
    for i in range(3):
        d=mp.mpf(1)
        for j in range(3):
            if i!=j: d*=ts[i]-ts[j]
        z.append(1/d)
    return sum(z[i]*mp.exp(-1j*r*ts[i]) for i in range(3))/(1j*r)**2

def triangle_exact_spectral_moment(theta):
    # Exact evaluation of the radial Fourier integral from the simplex divided differences.
    ts=[mp.mpf(0), mp.sin(theta), -mp.cos(theta)]
    z=[]
    for i in range(3):
        d=mp.mpf(1)
        for j in range(3):
            if i!=j: d*=ts[i]-ts[j]
        z.append(1/d)
    return coefficient*sum(z[i]*z[j]*abs(ts[i]-ts[j])**(4-p)
                            for i in range(3) for j in range(i+1,3))

# Direct two-dimensional integral checks the vertex divided-difference formula.
for theta in (mp.mpf('0.13'),mp.mpf('0.28')):
    for r in (mp.mpf('1.7'),mp.mpf('3.8')):
        ux,uy=mp.sin(theta),-mp.cos(theta)
        direct=mp.quad(lambda xx: mp.exp(-1j*r*ux*xx)*
                       (1-mp.exp(-1j*r*uy*(1-xx)))/(1j*r*uy),[0,1])
        formula=triangle_fourier(r,ux,uy)
        assert abs(direct-formula) < mp.mpf('1e-55'),(direct,formula)
print('PASS: triangle Fourier transform matches direct integration at four settings')

# For an edge length 1, the exact limiting moment loss must be coefficient*angle^(2-p).
reference=triangle_exact_spectral_moment(mp.mpf('1e-32'))
errors=[]
for exponent in [2,3,4,5,6,7,8]:
    th=mp.power(10,-exponent)
    quotient=(reference-triangle_exact_spectral_moment(th))/th**beta
    errors.append(abs(quotient/coefficient-1))
    print('triangle cusp theta=1e-%d relative coefficient error=%s'%(exponent,mp.nstr(errors[-1],14)))
assert all(errors[j+1] < errors[j] for j in range(len(errors)-1))
assert errors[-1] < mp.mpf('0.0002')
print('PASS: exact triangle spectral moment converges to the universal facet coefficient')

# Independent square expression from the cited primary article.
d_p=mp.cos(mp.pi*p/2)*mp.gamma(p+1)*2**(1-p)/((4-p)*(3-p)*(2-p)*(1-p))
article_coefficient=8*d_p
universal_square_coefficient=(p/4)*2*(mp.mpf(2)**(4-p))*coefficient
assert abs(article_coefficient/universal_square_coefficient-1) < mp.mpf('1e-60')
print('PASS: independent published square radial coefficient agrees exactly')

# Exact Mellin identity for the Fourier-sinc attenuation.
J_numeric=mp.quad(lambda z: z**(-1-beta)*(1-(mp.sin(z)/z)**2),
                  [mp.mpf('1e-14'),mp.mpf('0.1'),1,10,100,1000])
J_numeric += mp.mpf(1000)**(-beta)/beta  # main analytic tail, sinc^2 correction negligible
J_exact=mp.pi*2**beta/(mp.gamma(3+beta)*mp.sin(mp.pi*beta/2))
assert abs(J_numeric/J_exact-1)<mp.mpf('2e-6'),(J_numeric,J_exact)
print('PASS: the universal Mellin integral agrees with its gamma closed form')

# An independent irregular trapezoid verifies that distinct, unequal parallel
# sides contribute additively, while cross-edge interference is subleading.
def polygon_exact_vertex_moment(vertices, theta):
    ux,uy=mp.sin(theta),-mp.cos(theta)
    n=len(vertices)
    projections=[ux*x+uy*y for x,y in vertices]
    ratios=[]
    for i in range(n):
        x1,y1=vertices[i]
        x2,y2=vertices[(i+1)%n]
        dx,dy=x2-x1,y2-y1
        ratios.append((ux*dy-uy*dx)/(ux*dx+uy*dy))
    weights=[ratios[i]-ratios[i-1] for i in range(n)]
    return coefficient*sum(weights[i]*weights[j]*abs(projections[i]-projections[j])**(4-p)
                           for i in range(n) for j in range(i+1,n))
trapezoid=[(mp.mpf('0'),mp.mpf('0')),(mp.mpf('2'),mp.mpf('0')),
           (mp.mpf('1.5'),mp.mpf('1')),(mp.mpf('0.5'),mp.mpf('1'))]
trapezoid_prediction=coefficient*(mp.mpf(2)**(4-p)+1)
trapezoid_reference=polygon_exact_vertex_moment(trapezoid,mp.mpf('1e-27'))
trapezoid_errors=[]
for exponent in range(2,7):
    theta=mp.power(10,-exponent)
    observed=(trapezoid_reference-polygon_exact_vertex_moment(trapezoid,theta))/theta**beta
    trapezoid_errors.append(abs(observed/trapezoid_prediction-1))
    print('trapezoid cusp theta=1e-%d relative error=%s'%(exponent,mp.nstr(trapezoid_errors[-1],14)))
assert all(trapezoid_errors[i+1]<trapezoid_errors[i] for i in range(4))
assert trapezoid_errors[-1]<mp.mpf('1e-7')
print('PASS: unequal parallel trapezoid facets have the predicted additive cusp')
