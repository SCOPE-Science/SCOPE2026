"""Numerical consistency checks for an off-apex metric-ball area theorem.
Standard-library Python; finite checks do not replace geometric proofs.
"""
import math

def exact(r, s, alpha):
    beta=alpha/2
    d=s*math.sin(beta)
    if r<=d: return math.pi*r*r
    cap=r*r*math.acos(d/r)-d*math.sqrt(max(0,r*r-d*d))
    if r<s: return math.pi*r*r-2*cap
    return (beta*r*r+s*s*math.sin(2*beta)/2
            +d*math.sqrt(r*r-d*d)+r*r*math.asin(d/r))

def polar_quadrature(r, s, alpha, n=200000):
    beta=alpha/2
    step=beta/n
    total=0.0
    for j in range(n):
        ang=(j+0.5)*step
        disc=r*r-(s*math.sin(ang))**2
        if disc<=0: continue
        root=math.sqrt(disc)
        hi=s*math.cos(ang)+root
        lo=max(0.0,s*math.cos(ang)-root)
        total+=(hi*hi-lo*lo)
    return total*step

def middle_analytic_continuation(r,s,alpha):
    d=s*math.sin(alpha/2)
    return math.pi*r*r-2*(r*r*math.acos(d/r)-d*math.sqrt(r*r-d*d))

if __name__=='__main__':
    checks=0
    for alpha in [math.pi/3,math.pi/2,2*math.pi/3,4*math.pi/5,0.39*math.pi]:
        s=1.37
        d=s*math.sin(alpha/2)
        for r in [0.35*d,d*.98,d*1.02,(d+s)/2,s*.99,s,s*1.01,1.7*s,3.5*s]:
            a=exact(r,s,alpha)
            b=polar_quadrature(r,s,alpha,n=30000)
            assert abs(a-b)<8e-5*max(1,a),(alpha,r,a,b)
            checks+=1
        for eps in [0.0002*d,0.00005*d]:
            deficit=math.pi*(d+eps)**2-exact(d+eps,s,alpha)
            coeff=(8/3)*math.sqrt(2*d)
            assert abs(deficit/(eps**1.5)/coeff-1)<0.005,('first contact',alpha,eps)
            checks+=1
        for eps in [0.0005*s,0.0002*s]:
            overlap=exact(s+eps,s,alpha)-middle_analytic_continuation(s+eps,s,alpha)
            jumpcoef=math.tan(alpha/2)
            assert abs(overlap/(eps*eps)/jumpcoef-1)<0.005,('second contact',alpha,eps)
            checks+=1
        alpha_recovered=2*math.asin(d/s)
        assert abs(alpha_recovered-alpha)<1e-12
        checks+=1
    print('OFF_APEX_CONE_BALL_CHECKS_OK',checks)
