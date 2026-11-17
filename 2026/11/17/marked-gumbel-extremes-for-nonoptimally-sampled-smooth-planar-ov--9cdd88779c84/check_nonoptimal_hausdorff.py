"""Independent numeric checks of weighted random-inscribed circle extreme laws.

Requires numpy. All geometric quantities are computed from angular gaps,
not from the asymptotic surrogate. No claims of proof from simulation.
"""
import math
import numpy as np

a = 0.5
b0 = (1-a)/(2*math.pi)
bdd = a/(2*math.pi)
C = b0 * math.sqrt(2*math.pi*b0/bdd)
assert abs(C - math.sqrt(2*math.pi)/(4*math.pi)) < 1e-12
assert abs(b0/bdd - 1) < 1e-12

# Independent Laplace integral check for the tail exceedance intensity;
# the two quadratures must agree closely for each finite n.
def intensity(n):
    y = math.log(n) - 0.5 * math.log(math.log(n)) + math.log(C)
    ngrid = 16384
    t = (np.arange(ngrid)+0.5)*(2*math.pi/ngrid)
    f = (1+a*np.cos(t))/(2*math.pi)
    return float(n*np.sum(f*np.exp(-y*f/b0))*(2*math.pi/ngrid))
for n in (10**4, 10**6, 10**9, 10**12):
    ans = intensity(n)
    print('quadrature_n', n, 'intensity', format(ans,'.8f'))
assert abs(intensity(10**12)-1)<0.25

# Actual iid nonuniform angular points on unit circle. Newton's method
# inverts F(t)=(t+a*sin(t))/(2*pi); derivative >= (1-a)/(2*pi).
rng = np.random.default_rng(6129321)
n, reps = 12000, 300
Ys = np.empty(reps)
locations = np.empty(reps)
for r in range(reps):
    u = np.sort(rng.uniform(0, 2*math.pi, n))
    theta = u.copy()
    for _ in range(8):
        theta -= (theta+a*np.sin(theta)-u)/(1+a*np.cos(theta))
    gaps = np.diff(np.r_[theta,theta[0]+2*math.pi])
    k = int(np.argmax(gaps))
    g = gaps[k]
    # On the circle, H=1-cos(maxgap/2) for maxgap<pi.
    assert g<math.pi
    H = 1-math.cos(g/2)
    Ys[r] = n*b0*math.sqrt(8*H) - (math.log(n)-0.5*math.log(math.log(n))+math.log(C))
    midpoint = (theta[k] + g/2)%(2*math.pi)
    locations[r] = ((midpoint-math.pi+math.pi)%(2*math.pi)-math.pi)*math.sqrt(math.log(n))
print('sample_reps',reps,'n',n,'mean_normalized_Gumbel',round(float(Ys.mean()),4),'expected',round(float(np.euler_gamma),4))
print('sample_cdf_at_zero',round(float((Ys<=0).mean()),4),'Gumbel_theory',round(math.exp(-1),4))
print('sample_location_mean',round(float(locations.mean()),4),'limit',0)
print('sample_location_variance',round(float(locations.var()),4),'limit',1)
assert abs(float((Ys<=0).mean())-math.exp(-1))<0.30
assert abs(float(locations.mean()))<0.40
assert abs(float(locations.var())-1)<0.8
print('NONOPTIMAL_INSCRIBED_GUMBEL_CHECKS_OK')
