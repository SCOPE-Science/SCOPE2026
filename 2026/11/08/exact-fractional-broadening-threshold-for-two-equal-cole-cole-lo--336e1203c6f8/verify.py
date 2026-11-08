#!/usr/bin/env python3
"""Standalone numerical and exact-integer consistency checks for a two-component Cole-Cole loss profile."""
import math

COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def close(a, b, tol=2e-10):
    return abs(a-b) <= tol * max(1.0,abs(a),abs(b))

def parameters(alpha, log_r):
    theta = math.pi * alpha / 2
    c = math.cos(theta)
    a = alpha * log_r / 2
    d = math.cosh(a)
    return theta,c,a,d

def critical(alpha):
    c = math.cos(math.pi*alpha/2)
    d = (c + math.sqrt(c*c+8))/2
    return 2*math.acosh(d)/alpha

def direct_loss(alpha, log_r, s, strength=1.0):
    # Evaluate the original two fractions with t=(omega*tau)^alpha.
    theta,c,a,_ = parameters(alpha,log_r)
    total=0.0
    for t0 in (s-a,s+a):
        t=math.exp(t0)
        total += strength*math.sin(theta)*t/(1+2*c*t+t*t)
    return total

def direct_derivative(alpha, log_r,s):
    # Independent differentiation of the uncombined original loss fractions.
    theta,c,a,_=parameters(alpha, log_r)
    total=0.0
    for t0 in (s-a,s+a):
        t=math.exp(t0)
        total += math.sin(theta)*t*(1-t*t)/(1+2*c*t+t*t)**2
    return total

def reduced_loss(alpha, log_r, s):
    theta,c,a,d = parameters(alpha,log_r)
    y=math.cosh(s)
    return math.sin(theta)*(d*y+c)/(y*y+2*c*d*y+c*c+d*d-1)

def root_y(alpha, log_r):
    _,c,_,d=parameters(alpha,log_r)
    disc=(d*d-1)*(d*d-c*c)
    return (math.sqrt(disc)-c)/d

for alpha in (0.12,0.2,0.35,0.5,0.75,1.0):
    log_r_star=critical(alpha)
    theta,c,a_star,D=parameters(alpha,log_r_star)
    check(close(D*D-c*D-2, 0,1e-13),"threshold quadratic")
    check(close((D+c)*(D*D-c*D-2),0,1e-13),"derivative factorization")
    for f in (0.15,0.55,0.95,1.0,1.05,1.3,2.0):
        lr=f*log_r_star
        theta,c,a,d=parameters(alpha,lr)
        # Finite frequency grid covers central plateau, shoulders, and tails.
        for s in (-5.,-2.,-1.,-0.4,0.,0.4,1.,2.,5.):
            check(close(direct_loss(alpha,lr,s),reduced_loss(alpha,lr,s),2e-12),"raw Cole-Cole vs hyperbolic reduction")
            check(close(direct_loss(alpha,lr,s),direct_loss(alpha,lr,-s),1e-13),"reflection symmetry")
        # At the center the exact valley/maximum height is known.
        check(close(direct_loss(alpha,lr,0),math.sin(theta)/(d+c),1e-12),"center value")
        if f < 1:
            for h in (0.02,0.25,1.,3.):
                check(direct_loss(alpha,lr,h)<direct_loss(alpha,lr,0),"single-peak global maximum")
        if f > 1:
            ystar=root_y(alpha,lr)
            check(ystar>1,"outer maximum exists")
            sp=math.acosh(ystar)
            check(abs(direct_derivative(alpha,lr,sp))<1e-12,"analytical root of raw derivative")
            check(direct_loss(alpha,lr,sp)>direct_loss(alpha,lr,0),"central minimum")
            check(direct_derivative(alpha,lr,0.5*sp)>0,"outward rising branch")
            check(direct_derivative(alpha,lr,sp+1)<0,"outer falling branch")
        if f == 1:
            check(abs(direct_derivative(alpha,lr,0))<1e-13,"central quartic stationary")
            check(direct_loss(alpha,lr,0.15)<direct_loss(alpha,lr,0),"center still maximum at threshold")

# Global monotonicity of the physical time-ratio threshold in the Cole-Cole exponent.
a_list=[0.12,0.2,0.35,0.5,0.75,1.0]
check(all(critical(a_list[i])>critical(a_list[i+1]) for i in range(len(a_list)-1)),"decreasing separation threshold")
check(close(math.exp(critical(1)),3+2*math.sqrt(2),1e-13),"exact Debye endpoint")
for alpha in (0.5, 0.75, 1.0):
    lr=critical(alpha)
    _,c,a,D=parameters(alpha,lr)
    for epsilon in (1e-3,1e-4,1e-5):
        log_r=lr+epsilon
        _,_,_,d=parameters(alpha,log_r)
        s=math.acosh(root_y(alpha,log_r))
        asymp=math.sqrt(math.sqrt(c*c+8)*(d-D))
        check(abs(s/asymp-1)<0.002,"square-root critical branch")
    for log_extra in (12,16,22):
        test_lr=lr+log_extra/alpha
        _,_,_,dt=parameters(alpha,test_lr)
        expected=2*math.sin(math.pi*alpha/2)*math.exp(-alpha*test_lr/2)
        actual=direct_loss(alpha,test_lr,0)
        check(abs(actual/expected-1)<0.04,"large-separation notch decay")

print('VERIFY_OK checks='+str(COUNT))
