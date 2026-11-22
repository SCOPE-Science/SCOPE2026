"""Independent numerical checks for the projection-hole law of a spherical ring.
Uses ordinary Python + numpy/scipy only; numerical tests are diagnostic, not a proof.
"""
import math
import numpy as np
from scipy.integrate import quad


def formula_area(R,a,theta):
    h=math.sqrt(R*R-a*a)
    c=math.cos(theta)
    s=math.sin(theta)
    if c <= 0 or h*s >= a*c:
        return 0.0
    t=h*s/(a*c)
    return 2*c*a*a*(math.acos(t)-t*math.sqrt(1-t*t))


def independent_area(R,a,theta):
    h=math.sqrt(R*R-a*a)
    c=math.cos(theta)
    s=math.sin(theta)
    ymax2=a*a-h*h*(s/c)**2
    if ymax2 <= 0:
        return 0.
    ymax=math.sqrt(ymax2)
    return 4*quad(lambda y: c*math.sqrt(a*a-y*y)-s*h,0,ymax,epsabs=1e-12)[0]


def ray_occupancy(R,a,theta,p,y):
    r2=R*R-p*p-y*y
    if r2 < 0: return False
    if y*y>=a*a:return True
    return abs(p)*math.cos(theta)+math.sin(theta)*math.sqrt(r2) >=math.sqrt(a*a-y*y)-1e-13


def central_hole(R,a,theta,p,y):
    h=math.sqrt(R*R-a*a)
    c=math.cos(theta)
    s=math.sin(theta)
    if abs(y)>=a or p*p+y*y>=R*R:return False
    return abs(p)+s*h < c*math.sqrt(a*a-y*y)-1e-13


def run():
    count=0
    rng=np.random.default_rng(20261116)
    for R,a in [(1.,0.17),(1.,0.5),(1.,0.8),(1.,0.99),(2.7,1.9)]:
        h=math.sqrt(R*R-a*a)
        critical=math.atan2(a,h)
        for ratio in [0,0.05,0.3,0.5,0.9,0.999,1,1.01,1.1]:
            theta=min(critical*ratio,math.pi/2-0.000001)
            x=formula_area(R,a,theta)
            y=independent_area(R,a,theta)
            assert abs(x-y)<1e-8*max(1,R*R),(R,a,ratio,x,y)
            count+=1
            # All points in putative bounded hole are absent in exact ray test.
            for p,z in zip(rng.uniform(-R,R,150),rng.uniform(-R,R,150)):
                if central_hole(R,a,theta,p,z):
                    assert not ray_occupancy(R,a,theta,p,z)
                count+=1
        # critical constant, verified using progressively small angles
        if a/R<0.95:
            C=(8*math.sqrt(2)/3)*R*R*math.sqrt(a/h)
            errors=[]
            for eta in [0.0006,0.0003,0.00015,0.000075]:
                q=formula_area(R,a,critical-eta)/eta**1.5
                errors.append(abs(q/C-1))
                count+=1
            assert errors[-1]<errors[0] and errors[-1]<0.001,(R,a,errors)
        assert abs(formula_area(R,a,0)-math.pi*a*a)<1e-12
        assert abs(formula_area(R,a,critical))<1e-11
        count+=2
    # Isotropic hole probability from uniform cos(theta) by quadrature of indicator.
    for R,a in [(1.,0.15),(1.,0.55),(1.,0.94)]:
        h=math.sqrt(R*R-a*a)
        prob=quad(lambda t: float(t>h/R),0,1,points=[h/R])[0]
        assert abs(prob-(1-h/R))<1e-12
        count+=1
    print(f'PASSED {count} numerical diagnostic assertions; analytic proof independent')

if __name__=='__main__':run()
