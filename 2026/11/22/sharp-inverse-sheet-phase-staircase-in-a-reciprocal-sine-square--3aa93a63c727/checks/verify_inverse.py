"""Standalone numerical checks for exact inverse-sheet equations.

Only Python standard library is required. This is finite corroboration;
for the all-target theorem see the analytic proof in RESULT.md.
"""
import math

PI = math.pi


def inverse_phases(v, a, b):
    theta = math.asin(math.sqrt(v))
    upper = b * PI + a
    result = []
    for k in range(math.ceil(upper / PI) + 3):
        for z in (k * PI + theta, (k + 1) * PI - theta):
            if 0 < z <= upper + 1e-12:
                result.append(z)
    return result


def root(c, a):
    return 2*a / (c + math.sqrt(c*c + 4*a*a/(PI*PI)))


def enum_fiber(a, b, u, v, eps):
    alpha = math.asin(math.sqrt(u))
    out = []
    for z in inverse_phases(v, a, b):
        lower = max(eps, (z-b*PI)/a)
        upper = min(1., z/a)
        if lower > upper + 1e-13: continue
        if lower <= 0: continue
        tlo = a*PI/upper + z/PI-a*upper/PI
        thi = a*PI/lower + z/PI-a*lower/PI
        for delta in (alpha, PI-alpha):
            for m in range(math.floor((tlo-delta)/PI)-2, math.ceil((thi-delta)/PI)+3):
                c = m + delta/PI-z/(PI*PI)
                x = root(c,a)
                y = (z-a*x)/(b*PI)
                if eps-1e-12 <= x <= 1+1e-12 and -1e-12<=y<=1+1e-12:
                    out.append((x,y,z,delta,m))
    return out


def predicted_count_crossings(a,b,u,v,eps):
    # Independent count from the monotone phase traversed on each allowed x-interval.
    alpha=math.asin(math.sqrt(u))
    total=0
    for z in inverse_phases(v,a,b):
        low=max(eps,(z-b*PI)/a)
        high=min(1.,z/a)
        if low>high+1e-13: continue
        low=max(low,1e-14)
        minphase=a*PI/high+z/PI-a*high/PI
        maxphase=a*PI/low+z/PI-a*low/PI
        for delta in (alpha,PI-alpha):
            lower=math.ceil((minphase-delta)/PI-1e-11)
            upper=math.floor((maxphase-delta)/PI+1e-11)
            total+=max(0,upper-lower+1)
    return total


def k_formula(b,v):
    tau=math.asin(math.sqrt(v))/PI
    # integer-part boundary expression
    return max(0,math.floor(b-tau+1e-13)+1)+max(0, math.floor(b+tau+1e-13))


def verify():
    n=0
    for a in (0.7,1.0,1.9):
        for b in (0.2,0.5,0.83,1.3,2.1):
            for u in (0.25,0.6):
                for v in (0.25,0.5,0.75):
                    for eps in (0.2,0.08,0.03):
                        roots=enum_fiber(a,b,u,v,eps)
                        expected=predicted_count_crossings(a,b,u,v,eps)
                        assert len(roots)==expected, (a,b,u,v,eps,len(roots),expected)
                        for x,y,z,d,m in roots:
                            assert abs(math.sin(a*PI/x+b*y)**2-u)<1e-8
                            assert abs(math.sin(b*PI*y+a*x)**2-v)<1e-12
                            # determinant of DF, nonzero for interior targets
                            determinant=-a*b*(1+PI*PI/(x*x))*math.sin(2*(a*PI/x+b*y))*math.sin(2*(b*PI*y+a*x))
                            assert abs(determinant)>1e-9
                            n+=1
    for b in (1/6,1/2,5/6,1,1.4):
        for v in (0.25,0.75):
            theta=math.asin(math.sqrt(v))
            z=[p for p in inverse_phases(v,1,b) if p<=b*PI+1e-12]
            assert k_formula(b,v)==len(z), (b,v,k_formula(b,v),len(z))
    # At exact half-period and full-period phase thresholds the band is included.
    assert k_formula(1/6,.25)==1
    assert k_formula(5/6,.25)==2
    assert k_formula(.5,.75)==1
    # The asymptotic coefficient is checked across three orders of cutoff.
    for b,v in ((0.2,0.25),(0.2,0.75),(0.5,0.75),(1.3,0.4),(2.1,0.7)):
        k=k_formula(b,v)
        for eps in (0.01,0.005,0.002):
            N=len(enum_fiber(1.0,b,0.3,v,eps))
            assert abs(N-2*k/eps)<50, (b,v,eps,N,k)
    print(f"PASS: {n} regular inverse points; 270 independent total-count cases; threshold and asymptotic cases")


if __name__=='__main__': verify()
