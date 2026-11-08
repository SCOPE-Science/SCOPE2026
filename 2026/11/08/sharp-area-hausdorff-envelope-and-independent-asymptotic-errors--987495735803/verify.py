"""Reproduce analytic identities for intersections of randomly rotated unit-incircle squares.
Python >=3.9; standard library only. No network requests.
"""
import math
import random

PI=math.pi
L=PI/2

def circle_gaps(angles):
    ordered=sorted(x % L for x in angles)
    return [ordered[i+1]-ordered[i] for i in range(len(ordered)-1)]+[L+ordered[0]-ordered[-1]]

def exact_scores(angles):
    gaps=circle_gaps(angles)
    return 4*sum(math.tan(d/2) for d in gaps), 1/math.cos(max(gaps)/2)-1

def clipped_area_and_radius(angles):
    polygon=[(-4.,-4.),(4.,-4.),(4.,4.),(-4.,4.)]
    for angle in angles:
        for k in range(4):
            t=angle+k*PI/2
            nx,ny=math.cos(t),math.sin(t)
            def sign(point): return nx*point[0]+ny*point[1]-1
            old=polygon
            polygon=[]
            for a,b in zip(old, old[1:]+old[:1]):
                da,db=sign(a),sign(b)
                if da <= 0: polygon.append(a)
                if (da < 0 and db > 0) or (da > 0 and db < 0):
                    r=da/(da-db)
                    polygon.append((a[0]+r*(b[0]-a[0]),a[1]+r*(b[1]-a[1])))
    area=abs(sum(x*y2-y*x2 for (x,y),(x2,y2) in zip(polygon,polygon[1:]+polygon[:1])))/2
    return area, max(math.hypot(x,y)-1 for x,y in polygon)

def s3_exact_moments(m):
    # Dirichlet(1,...,1) moments for fractions P_i, multiplied by L.
    denom6=math.prod(m+j for j in range(6))
    e_s3=6*L**3/((m+1)*(m+2))
    # E(sum P_i^3)^2 = [m*6! + m(m-1)*3!^2]/(m)_6.
    e_s3_sq=L**6*(720*m+36*m*(m-1))/denom6
    return e_s3, e_s3_sq-e_s3**2

# Analytic normalization and elementary two-square benchmark.
assert abs(exact_scores([0])[0]-4) < 1e-12
assert abs(exact_scores([0])[1]-(2**.5-1)) < 1e-12
assert abs(16*math.log(2)/PI-3.5301696024424256)<1e-12
assert abs(128*(1-math.log(2))/PI-(16*math.log(2)/PI)**2-0.040211189977289535) < 1e-12
for m in (2,3,4,12,100):
    es,v=s3_exact_moments(m)
    ref=72*L**6*(m-1)*(5*m+11)/((m+1)**2*(m+2)**2*(m+3)*(m+4)*(m+5))
    assert abs(v-ref) < 5e-10*max(1,ref), (m,v,ref)

rng=random.Random(515062)
max_area_error=0
max_radius_error=0
cases=0
for m in (1,2,3,5,10,20):
    for j in range(60):
        angles=[rng.uniform(0,L) for _ in range(m)]
        a,h=exact_scores(angles)
        a2,h2=clipped_area_and_radius(angles)
        ae=abs(a-a2); he=abs(h-h2)
        max_area_error=max(max_area_error,ae)
        max_radius_error=max(max_radius_error,he)
        assert ae<5e-9 and he<5e-9,(m,j,a,a2,h,h2)
        cases+=1

# Random-space asymptotics: variance and scaled extremes, non-proof diagnostics.
# Check sampling means for two and five rotations with exact expectations
for m in (2,5):
    nrep=80000
    sums=0
    for _ in range(nrep):
        angles=[rng.uniform(0,L) for j in range(m)]
        sums+=exact_scores(angles)[0]
    if m==2: assert abs(sums/nrep-16*math.log(2)/PI)<0.015
    else:
        # Direct high-accuracy numerical integration of the exact mean survival law
        N=120000;step=(PI/4)/N
        f=lambda t:(2*math.tan(t)/(math.cos(t)**2))*max(0,1-4*t/PI)**m
        integ=step*(f(0)+f(PI/4)+4*sum(f((2*k+1)*step) for k in range(N//2))+2*sum(f(2*k*step) for k in range(1,N//2)))/3
        predicted=PI+PI*integ
        assert abs(sums/nrep-predicted)<0.018,(sums/nrep,predicted)

# Variance prefactor of area is 10L^6; Gaussian variance influence 360.
# E[(E^3-18E+12)^2] = 6! - 36*4! + 24*3! +324*2! - 432*1! +144 = 360
influence_variance=math.factorial(6)-36*math.factorial(4)+24*math.factorial(3)+324*math.factorial(2)-432*math.factorial(1)+144
assert influence_variance==360
assert abs(10*L**6-5*PI**6/32)<1e-12
print('ROTATED_SQUARE_CHECK_OK independent_clipped_cases=%d max_area_error=%.3g max_hausdorff_error=%.3g dirichlet_moments=5' % (cases,max_area_error,max_radius_error))



def deterministic_envelopes(m,M):
    assert m>=2 and L/m-1e-12 <=M<L
    low=4*(math.tan(M/2)+(m-1)*math.tan((L-M)/(2*(m-1))))
    k=min(m,math.floor(L/M+1e-12))
    rem=max(0.,L-k*M)
    high=4*(k*math.tan(M/2)+math.tan(rem/2))
    return low,high

support_cases=0
for m in (2,3,4,6,11):
    for _ in range(120):
        gaps=circle_gaps([rng.uniform(0,L) for _ in range(m)])
        M=max(gaps)
        a=4*sum(math.tan(d/2) for d in gaps)
        low,high=deterministic_envelopes(m,M)
        assert low-1e-10<=a<=high+1e-10, (m,M,a,low,high)
        support_cases+=1
    # Construct all-equal remaining gaps: the lower envelope is attained.
    M=L*(1/m+(1-1/m)*0.39)
    low,_=deterministic_envelopes(m,M)
    eq_gaps=[M]+[(L-M)/(m-1)]*(m-1)
    assert abs(low-4*sum(math.tan(d/2) for d in eq_gaps))<1e-11
    # Upper envelope attained for M between L/m and L/(m-1).
    M=(L/m+L/(m-1))/2
    _,high=deterministic_envelopes(m,M)
    hot=[M]*(m-1)+[L-(m-1)*M]
    assert min(hot)>0 and abs(high-4*sum(math.tan(d/2) for d in hot))<1e-11
print('AREA_HAUSDORFF_ENVELOPE_OK support_cases=%d endpoint_constructions=%d' % (support_cases,10))
