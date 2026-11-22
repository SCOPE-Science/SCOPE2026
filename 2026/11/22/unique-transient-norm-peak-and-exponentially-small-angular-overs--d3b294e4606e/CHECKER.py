"""Reproducible finite checks for the affine Fock semigroup norm-envelope theorem.

These checks corroborate the analytical proof; finite samples are not a proof of
uniqueness or the infinite asymptotics.
"""
import math
import cmath

checks = 0

def ck(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def scaled_stationary(t, k):
    q = math.exp(-t)
    theta = k * t
    return (1.0 + q*q)*math.cos(theta) + k*(1.0-q*q)*math.sin(theta)-2.0*q

def excess(t, k):
    q = math.exp(-t)
    return 2.0*q*(q-math.cos(k*t))/(1.0-q*q)

def stationary(m, k):
    lo = (m+0.5)*math.pi/k
    hi = (m+1.5)*math.pi/k
    ck(((-1)**m)*scaled_stationary(lo,k)>0, 'left stationary sign')
    ck(((-1)**m)*scaled_stationary(hi,k)<0, 'right stationary sign')
    for _ in range(100):
        mid=(lo+hi)/2
        if ((-1)**m)*scaled_stationary(mid,k)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

for k in (0.1,0.2,0.5,1.0,2.0,5.0):
    roots = [stationary(m,k) for m in range(8)]
    for m, r in enumerate(roots):
        ck(r>0 and (m+.5)*math.pi/k<r<(m+1.5)*math.pi/k, 'stationary location')
        ck(((-1)**m)*excess(r,k)>0, 'alternating extrema')
        if m:
            ck(r>roots[m-1], 'ordered stationary times')
    for i in range(1,3001):
        t=(4*math.pi/k)*i/3001
        ck(excess(t,k) <= excess(roots[0],k)+2e-12, 'global peak sampled')
    for m in range(1,8):
        theta_0=math.pi/2 + math.atan(k) + m*math.pi
        t_0=theta_0/k
        if t_0 < 550:
            predicted=2*((-1)**m)*k/math.sqrt(1+k*k)*math.exp(-t_0)
            if abs(predicted)>1e-60:
                ratio=excess(roots[m],k)/predicted
                ck(abs(ratio-1)<max(0.6,10*math.exp(-t_0)), 'far-time asymptotics')

for k in (0.04,0.05,0.08,0.1,0.15):
    peak=stationary(0,k)
    scale=(2*k/math.e)*math.exp(-math.pi/(2*k))
    ck(abs(excess(peak,k)/scale-1)<0.025, 'small-angle overshoot')
    ck(abs(peak-(math.pi/(2*k)+1))<0.02, 'small-angle peak time')

# Check the coherent-state conjugation formula on polynomial test functions.
for a,b,z in ((0.3+0.2j,0.7-0.5j,0.1+0.4j),(-0.5+0.1j,0.3+0.6j,-0.2+0.7j), (0j,0.7j,0.8-0.2j)):
    d=1-abs(a)**2
    u=-b/d
    v=a.conjugate()*b/d
    def f(w): return 1+0.4*w+0.2*w*w
    def U(x, fun, w): return cmath.exp(-abs(x)**2/2+w*x.conjugate())*fun(w-x)
    lhs=U(v,lambda w: U(u,f,a*w),z)
    rhs=math.exp(-abs(b)**2/(2*d))*f(a*z+b)
    ck(abs(lhs-rhs)<1e-12, 'unitary conjugation identity')
print('PASS', checks, 'finite diagnostic checks')
