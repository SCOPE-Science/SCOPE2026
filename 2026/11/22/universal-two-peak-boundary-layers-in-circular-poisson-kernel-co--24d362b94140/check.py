"""Independent finite diagnostics for a two-peak circular Poisson approximation formula.

Requires Python 3 and mpmath >= 1.2. The mathematical proof is in RESULT.md;
these numerical tests do not assert global optimality or infinite-range statements.
"""
import mpmath as mp

mp.mp.dps = 65
checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def P(r, theta):
    return (1 - r*r)/(1 - 2*r*mp.cos(theta) + r*r)

def J(r, a, t, phi):
    return P(r*t, phi-a) + P(r*t, phi+a) - (1+t*t)/(1-t*t)

def normsq(r,a):
    return (P(r*r, 0) + P(r*r, 2*a))/2

for rr,tt,aa,pp in [('0.35','0.52','0.4','0.2'),('0.68','0.27','0.9','0.5'),('0.78','0.64','1.1','0.8')]:
    r,t,a,phi = map(mp.mpf,(rr,tt,aa,pp))
    lhs=mp.quad(lambda th:P(r,th-a)*P(t,th-phi), [-mp.pi, 0, mp.pi])/(2*mp.pi)
    check(abs(lhs-P(r*t,phi-a))<mp.mpf('1e-34'), 'Poisson convolution')
    full=mp.quad(lambda th:((P(r,th-a)+P(r,th+a))/2-P(t,th-phi))**2, [-mp.pi,0,mp.pi])/(2*mp.pi)
    check(abs(full-(normsq(r,a)-J(r,a,t,phi)))<mp.mpf('1e-30'),'squared-error identity')

for aa in ['0.3', '0.7', '1.2']:
    a=mp.mpf(aa)
    for rr in ['0.01','0.025','0.05']:
        r=mp.mpf(rr)
        t=mp.findroot(lambda x:mp.diff(lambda u:J(r,a,u,0),x), (r*mp.cos(a)*mp.mpf('0.9'),r*mp.cos(a)*mp.mpf('1.1')))
        check(t>0,'positive small-radius fit')
        check(abs(t/r-mp.cos(a))<mp.mpf('0.02'),'small-radius first-order scale')
        check(mp.diff(lambda x:J(r,a,x,0),t,2)<0,'small-radius radial curvature')
        check(mp.diff(lambda x:J(r,a,t,x),0,2)<0,'small-radius angular curvature')

kstar=1+mp.sqrt(2)
hstar=3-2*mp.sqrt(2)
errstar=2*mp.sqrt(2)-mp.mpf('2.5')
for aa in ['0.3','0.7','1.2']:
    a=mp.mpf(aa)
    C=(2+mp.sqrt(2))**4*mp.sin(2*a)/(4*(1-mp.cos(2*a))**2)
    errors=[]
    for dd in ['0.01','0.005','0.0025']:
        delta=mp.mpf(dd)
        r=1-delta
        def obj(k,h):
            return J(r,a,1-k*delta,a+h)
        near=mp.findroot((lambda k,h:mp.diff(lambda v:obj(v,h),k),lambda k,h:mp.diff(lambda v:obj(k,v),h)),(kstar,-C*delta**4),tol=mp.mpf('1e-52'))
        k,h=near
        check(k>0 and 1-k*delta>0,'valid radius')
        check(h<0,'inward angular displacement')
        check(abs(k-kstar)<mp.mpf('0.15'),'universal depth coefficient')
        check(abs(h/delta**4/C+1)<mp.mpf('0.10'),'fourth-order shift coefficient')
        scaled_gain=delta*(obj(k,h)-1)
        check(abs(scaled_gain-hstar)<mp.mpf('0.03'),'optimal gain coefficient')
        scaled_error=delta*(normsq(r,a)-obj(k,h))
        check(abs(scaled_error-errstar)<mp.mpf('0.035'),'error coefficient')
        errors.append(abs(k-kstar))
    check(errors[2]<errors[1],'depth converges with decreasing boundary distance')

print('PASS:',checks,'finite diagnostics; no numerical test substitutes for the proof.')
