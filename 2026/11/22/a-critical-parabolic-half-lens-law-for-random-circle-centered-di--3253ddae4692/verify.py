"""Independent reproducibility checks for the circular ball-intersection boundary layer.

Python standard library only. Numerical checks are diagnostics, not the proof.
"""
from math import pi, sin, cos, sqrt, isclose
from random import Random


def area_lens_unit(delta):
    # Positive only for a containing arc with length pi-delta.
    return delta - sin(delta)


def score(s, b, divisions=1024):
    # Circular-gap score with stable numerical evaluation near b=1.
    h = s / (2*divisions)
    a2 = (b-1)*(b+1)
    def fn(i):
        t = i*h
        c = cos(t)
        root = sqrt(c*c+a2)
        if c > 0:
            rho = a2/(root+c) if a2 else 0.0
        else:
            rho = root-c
        return rho*rho
    accum = fn(0)+fn(divisions)
    for i in range(1,divisions):
        accum += (4 if i&1 else 2)*fn(i)
    return accum*h/3


def area_from_gaps(angles, b):
    angles = sorted(x%(2*pi) for x in angles)
    gaps = [angles[i+1]-angles[i] for i in range(len(angles)-1)]
    gaps.append(2*pi+angles[0]-angles[-1])
    return sum(score(s,b,divisions=32768 if s>3 else (1024 if s>1 else 64)) for s in gaps)


def area_direct_polar(angles, b, n_grid=65536):
    # Independent area formula from all original disks, no gap decomposition.
    h = 2*pi/n_grid
    a2 = (b-1)*(b+1)
    total=0.0
    for j in range(n_grid):
        phi=(j+0.5)*h
        r=float('inf')
        for theta in angles:
            c=cos(phi-theta)
            root=sqrt(c*c+a2)
            radius= a2/(root-c) if c<0 and a2 else (root+c if c>=0 else 0.0)
            r=min(r,radius)
        total += 0.5*r*r*h
    return total


def H(gamma, q):
    return (q**3+(q*q+8*gamma)**1.5)/12 + gamma*q


def run():
    rng=Random(20261121)
    count=0
    for n in [3,4,7,12]:
        for k in range(14):
            a=sorted(rng.random()*2*pi for _ in range(n))
            gaps=[a[j+1]-a[j] for j in range(n-1)]+[a[0]+2*pi-a[-1]]
            d=max(gaps)-pi
            exact=area_lens_unit(d) if d>0 else 0.0
            scorearea=area_from_gaps(a,1.0)
            assert abs(exact-scorearea)<1e-7,(n,k,exact,scorearea)
            count+=1
    print('B_EQUALS_ONE_GAP_CHECKS',count)
    count=0
    for L in [.7,1.6,2.5,3.01]:
        for b in [1,1.002,1.04]:
            angles=[-L/2,-.32*L,0,.21*L,L/2]
            ag=area_from_gaps(angles,b)
            ap=area_direct_polar(angles,b,8192)
            tol=3e-6 if b>1 else 2e-6
            assert abs(ag-ap)<tol,(L,b,ag,ap,abs(ag-ap))
            count+=1
    print('INDEPENDENT_POLAR_CASES',count)
    q=pi
    for gamma in [0,0.5,2]:
        estimates=[]
        for n in [40,80,160,320]:
            delta=q/n
            L=pi-delta
            # Even-spaced interior centers, with two arc endpoints fixed.
            angles=[-L/2+L*k/(n-1) for k in range(n)]
            area=area_from_gaps(angles,1+gamma/n**2)
            estimates.append((n,n**3*area))
        target=H(gamma,q)
        # Convergence is checked quantitatively by progressively tighter errors.
        diffs=[abs(v-target) for _,v in estimates]
        assert diffs[3]<diffs[0]*0.45, (gamma, target, estimates)
        assert diffs[-1]<0.4, (gamma,target,estimates)
        print('CROSSOVER',gamma,'target',f'{target:.10f}', 'samples',[(n,round(v,7)) for n,v in estimates])
    # Independent beta gap law and rare-event probability via simulated circle spacings.
    n=5
    trials=30000
    event=0
    surv=0
    for _ in range(trials):
        angles=sorted(rng.random()*2*pi for _ in range(n))
        gaps=[angles[j+1]-angles[j] for j in range(n-1)]+[angles[0]+2*pi-angles[-1]]
        big=max(gaps)
        if big>pi:
            event+=1
            if big-pi>pi/4:
                surv+=1
    event_emp=event/trials
    survival_emp=surv/event
    event_true=n/2**(n-1)
    survival_true=(3/4)**(n-1)
    assert abs(event_emp-event_true)<.014,(event_emp,event_true)
    assert abs(survival_emp-survival_true)<.027,(survival_emp,survival_true)
    print('CIRCULAR_SPACING_LAW',event_emp,event_true,survival_emp,survival_true)
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':run()
