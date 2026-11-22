"""Numerical diagnostics for the geometry of ellipse orthoptic sampling.

No numerical calculation substitutes for the analytic identities in RESULT.md.
Uses only the Python standard library.
"""
import cmath
import math

PI = math.pi
N = 32768
TOL_DERIV = 1.5e-5


def h(t, a, b):
    return math.hypot(a*math.cos(t), b*math.sin(t))


def angle(t, a, b):
    p = h(t, a, b)
    q = h(t+PI/2, a, b)
    z = complex(math.cos(t), math.sin(t))*complex(p,q)
    return cmath.phase(z)


def density(psi, c):
    return (1-c*math.cos(2*psi))/(2*PI*(1-2*c*math.cos(2*psi)+c*c))


def periodic_phase_diff(p1, p0):
    return (p1-p0+PI)%(2*PI)-PI


checks = 0
for a, b in [(1.0, 1.0), (1.1, 1.0), (2.0, 1.0), (5.0, 2.0), (20.0, 1.0)]:
    c = (a*a-b*b)/(a*a+b*b)
    R = math.hypot(a,b)
    dt=2*PI/N
    norm=0.0
    m2=0j
    m4=0j
    tv=0.0
    for j in range(N):
        theta=(j+0.5)*dt
        p=h(theta,a,b)
        v=h(theta+PI/2,a,b)
        q=complex(math.cos(theta),math.sin(theta))*complex(p,v)
        assert abs(abs(q)-R)<5e-13
        psi=cmath.phase(q)
        pred=density(psi,c)
        deriv=periodic_phase_diff(angle(theta+0.5e-5,a,b),angle(theta-0.5e-5,a,b))/1e-5
        assert abs(1/(2*PI*deriv)-pred)<TOL_DERIV
        checks+=2
        norm+=pred*dt
        m2+=cmath.exp(2j*psi)*dt/(2*PI)
        m4+=cmath.exp(4j*psi)*dt/(2*PI)
        tv+=abs(pred-1/(2*PI))*dt/2
    # Integrals in psi are computed separately, since theta is uniform.
    norm=0.0
    tv=0.0
    for j in range(N):
        psi=(j+0.5)*dt
        pred=density(psi,c)
        norm+=pred*dt
        tv+=abs(pred-1/(2*PI))*dt/2
    assert abs(norm-1)<5e-11
    assert abs(tv-math.asin(c)/PI)<5e-8
    assert abs(m2-c/2)<2e-4
    assert abs(m4-c*c/2)<2e-4
    checks+=4
    print(f"axes=({a:g},{b:g}) c={c:.9f} TV={tv:.9f} exact={math.asin(c)/PI:.9f} passed")

for c in [0.90,0.98,0.995,0.999]:
    delta=1-c
    for x in [-8,-3,-1,0,1,3,8]:
        scaled = delta*(1-c*c)/(2*PI*(1-2*c*math.cos(delta*x)+c*c))
        cauchy = 1/(PI*(1+x*x))
        # Local ratio tends to one as delta decreases; no unjustified fixed accuracy assertion.
        assert scaled>0 and abs(scaled-cauchy)<0.05
        checks+=1
    print(f"slender c={c:.3f}: local checks passed")

print(f"PASS {checks} deterministic checks")
