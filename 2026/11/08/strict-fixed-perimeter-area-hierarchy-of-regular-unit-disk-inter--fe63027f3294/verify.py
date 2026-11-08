"""Independent numerical checks for the area formula of regular disk intersections.

Pure standard-library Python. These tests are supplementary to the analytic proof.
"""
import math

PI=math.pi

def parameters(m,u):
    assert isinstance(m,int) and m>=2 and 0<u<PI
    return math.sin(u/m)/math.sin(PI/m)

def area_formula(m,u):
    return PI-u-m*math.sin(u/m)*math.sin((PI-u)/m)/math.sin(PI/m)

def radial_area(m,u,N=8192):
    t=parameters(m,u)
    total=0.0
    for k in range(N):
        angle=2*PI*(k+0.5)/N
        radial=1e100
        for j in range(m):
            theta=angle-2*PI*j/m
            c=math.cos(theta)
            root=t*c+math.sqrt(max(0.0,1-t*t*(1-c*c)))
            radial=min(radial,root)
        total+=radial*radial
    return PI*total/N

checks=0
for m,u in [(2,.2),(3,.3),(4,1.2),(7,2.1),(13,2.5)]:
    af=area_formula(m,u)
    aq=radial_area(m,u)
    assert abs(af-aq)<3e-7,(m,u,af,aq)
    assert abs(af-(PI-u))<PI
    checks+=3
for u in [.03,.5,1.0,2.0,3.05]:
    A=[area_formula(m,u) for m in range(2,46)]
    for a,b in zip(A,A[1:]):
        assert a<b,(u,a,b)
        checks+=1
    assert A[-1]<(PI-u)**2/PI
    assert abs(A[0]-(PI-u-math.sin(u)))<1e-12
    checks+=2
for u in [.2,.7,1.6,2.7]:
    c=u*u*(PI-u)**2/(3*PI)
    for m in [60,100,140]:
        defect=(PI-u)**2/PI-area_formula(m,u)
        assert abs(defect*m*m/c-1)<0.002,(m,u,defect*m*m/c)
        checks+=1
for m in [3,4,7,11]:
    for u in [.02,.03]:
        difference=area_formula(m,u)-area_formula(2,u)
        leading=math.cos(PI/m)/math.sin(PI/m)*u*u/m
        assert 0.94<difference/leading<1.06
        checks+=1
for m in [2,3,5,9]:
    P=0.01
    u=PI-P/2
    measured=area_formula(m,u)
    leading=P**3/48 if m==2 else math.cos(PI/m)/math.sin(PI/m)*P*P/(4*m)
    assert abs(measured/leading-1)<.025
    checks+=1
print('DISK_HIERARCHY_CHECKS_OK',checks)
