"""Direct numerical checks for square-grid disk-coverage boundary asymptotics.
Scientific calculations are in the companion proof; this program tests finite geometry.
"""
import math
import numpy as np
from scipy.integrate import quad

A=1-math.sqrt(3)/4-math.pi/6
assert 0<A<0.05
# Area of a single missing-site hole for a disk of radius R<1,
# integrating its first-quadrant component.
def single_hole_area(R):
    d=1-R
    s=(1-math.sqrt(2*R*R-1))/2
    f=lambda x:1-math.sqrt(max(0,R*R-x*x))
    h=lambda x:math.sqrt(max(0,R*R-(1-x)**2))
    return 4*(quad(f,0,d,epsabs=1e-13)[0]+quad(lambda x:f(x)-h(x),d,s,epsabs=1e-13)[0])

def boundary_coefficients(R,N=600000):
    # Angle midpoint enumeration on the surviving circle of the origin.
    t=(np.arange(N)+.5)*2*math.pi/N
    x,y=R*np.cos(t),R*np.sin(t)
    counts=np.zeros(N,np.int8)
    for i in range(-2,3):
        for j in range(-2,3):
            if (i,j)==(0,0):continue
            if i*i+j*j>4*R*R+1e-10:continue
            counts+=((x-i)**2+(y-j)**2<=R*R+1e-13)
    # (1-q)*sum_m R*measure{m}*q^m ; note b2=alpha2-alpha1
    alpha1=2*math.pi*R*(counts==1).mean()
    alpha2=2*math.pi*R*(counts==2).mean()
    return alpha1,alpha2-alpha1

for d in (0.1,0.05,0.02,0.01,0.005):
    R=1-d
    area=single_hole_area(R)
    b1,b2=boundary_coefficients(R)
    print(f'delta={d:.5f} single_hole_area/delta²={area/d**2:.9f} boundary_linear/delta={b1/d:.9f} boundary_quadratic={b2:.9f}')
    assert abs(area/(d*d)-4)<2.0*d
    assert abs(b1/d-8)<8*d
b1,b2=boundary_coefficients(1)
assert abs(b1)<0.0002
assert abs(b2-4*math.pi/3)<0.0004
# Classification of vertex-failure patterns inside one unit square at R=1.
N=1600
u=(np.arange(N)+.5)/N
x=u[:,None];y=u[None,:]
counts=((x*x+y*y<=1).astype('int8')+((1-x)**2+y*y<=1).astype('int8')+
       (x*x+(1-y)**2<=1).astype('int8')+((1-x)**2+(1-y)**2<=1).astype('int8'))
a2=(counts==2).mean()
assert abs(a2-4*A)<0.001
assert (counts==1).sum()==0
print('critical area q2 coefficient',a2,'exact',4*A)
print('critical boundary q2 coefficient',b2,'exact',4*math.pi/3)
print('SQUARE_COVERAGE_TWO_SCALE_CHECK_OK')
