"""Deterministic mathematical consistency tests for a finite-interval cover law.
Run: python3 verify.py (Python standard library only).
"""
import math

N = 0

def test(ok, description):
    global N
    if not ok:
        raise AssertionError(description)
    N += 1

def terms(s, delta):
    # D = L = 1; k = 2s; r = k*k; location x = 1/2 + delta/k.
    k = 2.0*s
    r = k*k
    x = 0.5 + delta/k
    assert 0 < x < 1
    theta = r*math.exp(-s)
    return k, r, x, theta

def f(k, x, kind):
    if kind == 0: return math.cosh(k*x)/math.cosh(k)
    if kind == 1: return math.cosh(k*(1-x))/math.cosh(k)
    if kind == 2: return math.cosh(k*(x-0.5))/math.cosh(k/2)
    raise ValueError(kind)

def fp_r(k,x,kind):
    # Derivative with respect to r = k*k, from a different quotient differentiation.
    if kind == 0: a,b = x,1.0
    elif kind == 1: a,b = 1-x,1.0
    else: a,b = x-0.5,0.5
    return (a*math.sinh(k*a)*math.cosh(k*b) - b*math.cosh(k*a)*math.sinh(k*b))/(2*k*math.cosh(k*b)**2)

def moment1(k,r,x,kind):
    return (1/f(k,x,kind)-1)/r

def moment2(k,r,x,kind):
    p=f(k,x,kind)
    return 2*(1-p+r*fp_r(k,x,kind))/(r*r*p*p)

def shat(q,k,r,x,kind):
    v=f(math.sqrt(r+q), x, kind)
    return (1-v)/(q+r*v)

def exact_cover_mean(k,r,x):
    return moment1(k,r,x,0) + moment1(k,r,x,1) - moment1(k,r,x,2)

def expected_mean(delta):
    a=math.exp(delta); b=math.exp(-delta)
    return 1/a+1/b-1/(a+b)

def expected_second(delta):
    a=math.exp(delta); b=math.exp(-delta)
    return 2*(1/a**2+1/b**2-1/(a+b)**2)

def expected_shat(u,delta):
    a=math.exp(delta); b=math.exp(-delta)
    return 1/(u+a)+1/(u+b)-1/(u+a+b)

def exact_scaled_shat(u,s,delta):
    k,r,x,theta=terms(s,delta)
    return theta*(shat(u*theta,k,r,x,0)+shat(u*theta,k,r,x,1)-shat(u*theta,k,r,x,2))

for delta in [-2.,-1.,0.,0.5,1.,2.]:
    for s in [8.,12.,16.]:
        k,r,x,theta=terms(s,delta)
        vals=[f(k,x,j) for j in range(3)]
        test(0<vals[0]<vals[2]<1 and 0<vals[1]<vals[2]<1,'free-passage transform ordering')
        # Verify the singular excursion-hit amplitudes directly.
        expval=[math.exp(delta),math.exp(-delta),2*math.cosh(delta)]
        for j in range(3):
            test(abs(vals[j]/math.exp(-s)/expval[j]-1)<0.02,'rare-hit amplitude')
        m=theta*exact_cover_mean(k,r,x)
        q=theta**2*(moment2(k,r,x,0)+moment2(k,r,x,1)-moment2(k,r,x,2))
        test(abs(m-expected_mean(delta))<0.01,'limit mean')
        test(abs(q-expected_second(delta))<0.1,'limit second moment')
        test(q > m*m,'positive variance')
        for u in [0.25,1.,3.]:
            test(abs(exact_scaled_shat(u,s,delta)-expected_shat(u,delta))<0.002,'scaled survival resolvent')
        # Independent algebraic mean expression cited in prior literature.
        known_mean=(math.cosh(k)/math.cosh(k*x)+math.cosh(k)/math.cosh(k*(1-x))
                   -math.cosh(k/2)/math.cosh(k*(x-0.5))-1)/r
        test(abs(m-theta*known_mean)<2e-9,'published mean identity')
for s in [8.,12.,16.]:
    for delta in [0.25,1.,2.]:
        test(abs(exact_scaled_shat(1.5,s,delta)-exact_scaled_shat(1.5,s,-delta))<2e-12,
             'reflection symmetry')
# Independent limiting distribution test: inclusion-exclusion of two independent exponentials.
for delta in [-2.,0.,2.]:
    for t in [0.,0.2,1.,3.]:
        a,b=math.exp(delta),math.exp(-delta)
        cc=math.exp(-a*t)+math.exp(-b*t)-math.exp(-(a+b)*t)
        joint=1-(1-math.exp(-a*t))*(1-math.exp(-b*t))
        test(abs(cc-joint)<1e-14 and 0<=cc<=1+1e-14,'limiting survival probability')
# At the symmetric site: mean=3/2, variance=5/4, CV=sqrt(5)/3.
test(abs(expected_mean(0)-1.5)<1e-14,'symmetric mean')
test(abs(expected_second(0)-3.5)<1e-14,'symmetric second moment')
test(abs(math.sqrt(expected_second(0)-expected_mean(0)**2)/expected_mean(0)-math.sqrt(5)/3)<1e-14,'symmetric CV')
print(f'PASS {N} deterministic finite-parameter checks; numerical tests corroborate, not prove, the limiting law.')
