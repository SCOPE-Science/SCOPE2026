"""Reproducibility checks for singular boundary sampling on the circle.
Run: python CHECK.py. All random samples are seeded.
These checks are finite corroboration, not proof of limiting assertions.
"""
import math
import numpy as np

rng=np.random.default_rng(20261103)

def sample_angles(n,alpha):
    u=rng.uniform(-1.0,1.0,n)
    return np.sort(math.pi*np.sign(u)*np.abs(u)**(1/(alpha+1)))

def defects(theta):
    gaps=np.diff(np.r_[theta,theta[0]+2*math.pi])
    area=float(np.sum((gaps-np.sin(gaps))/2))
    h=float(1-np.cos(np.max(gaps)/2))
    # Exact for circle, with all gaps shorter than pi.
    assert np.max(gaps)<math.pi
    return h,area,gaps

# Deterministic geometric checks: chord area and sagitta.
for m in [6,9,15,32,100]:
    theta=np.arange(m)*2*math.pi/m-math.pi
    h,a,g=defects(theta)
    expected_a=math.pi-m/2*math.sin(2*math.pi/m)
    expected_h=1-math.cos(math.pi/m)
    assert abs(a-expected_a)<1e-12
    assert abs(h-expected_h)<1e-12

# Cubic and quadratic local geometry constants.
for d in [0.08,0.04,0.02,0.01]:
    hd=1-math.cos(d/2)
    ad=(d-math.sin(d))/2
    assert abs(hd/(d*d)-1/8)<0.0001
    assert abs(ad/(d**3)-1/12)<0.0001

# Exact Poisson local process sampling via its integrated intensity.
alpha=1.0
c=(alpha+1)/(2*math.pi**(alpha+1))
R=160.0

def poisson_gap_functionals():
    # Gamma arrival clock on each positive/negative ray.
    out=[]
    for sign in [-1,1]:
        z=[]; t=0.0
        while True:
            t+=float(rng.exponential())
            x=((alpha+1)*t/c)**(1/(alpha+1))
            if x>R: break
            z.append(sign*x)
        out.extend(z)
    pts=np.sort(out)
    gaps=np.diff(pts)
    return np.max(gaps)**2/8, np.sum(gaps**3)/12

pH=[];pA=[]
for _ in range(300):
    h,a=poisson_gap_functionals()
    pH.append(h);pA.append(a)
# Finite-window truncation: the area functional omits the tail beyond R.
qH=[];qA=[]
for _ in range(300):
    theta=sample_angles(12000,alpha)
    h,a,_=defects(theta)
    qH.append(h*12000**(2/(alpha+1)))
    qA.append(a*12000**(3/(alpha+1)))
assert abs(np.median(pH)-np.median(qH)) < 2.5
assert abs(np.median(pA)-np.median(qA)) < 15.0

# Bulk phase: compare scaled mean with exact predicted constant.
alpha=0.25
c=(alpha+1)/(2*math.pi**(alpha+1))
expected=4*math.pi**3/((1-2*alpha)*(alpha+1)**2)
vals=[]
for _ in range(150):
    th=sample_angles(25000,alpha)
    _,a,_=defects(th)
    vals.append(a*25000**2)
assert abs(np.mean(vals)-expected)/expected < 0.07

# Critical-phase constant is from integration of curvature/f^2.
alpha=0.5
c=(alpha+1)/(2*math.pi**(alpha+1))
critical=2/(3*c*c)
assert abs(critical-36.74817976924424)<1e-10
print('SINGULAR_SAMPLING_OK circle_shapes=5 local_expansions=4 poisson_pairs=300 bulk_trials=150')
print('poisson_medians',np.median(pH),np.median(pA),'finite_medians',np.median(qH),np.median(qA))
print('bulk_mean',np.mean(vals),'bulk_prediction',expected,'critical_coefficient',critical)
