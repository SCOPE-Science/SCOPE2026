"""Check two-site breakthrough identifiability and the exact alias identity.

Only standard-library Python is required. The analytic proof is in RESULT.md.
"""
import math
import random

TAU = 1e-9
N = 0

def close(a, b, tol=TAU):
    global N
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)
    N += 1

def c(x, t, xi, D, v, k, M, tau):
    if t <= tau:
        return 0.0
    s = t-tau
    return M / math.sqrt(4*math.pi*D*s) * math.exp(-(x-xi-v*s)**2/(4*D*s)-k*s)

def alias(x0, x1, xi, D, v, k, M):
    assert xi < x0 < x1 and D > 0 and v > 0 and k >= 0 and M > 0
    p, L = x0-xi, x1-x0
    q = L/(2*p+L)
    eta = x0 + p*q
    return eta, D*q*q, v*q*q, k+(1-q*q)*v*v/(4*D), M*q*math.exp(v*(eta-xi)/(2*D))

def fingerprints(x, times, obs, tau):
    # Recover log K, A, B from F(s)=log(C*sqrt(s))=log K-A/s-B*s.
    ss = [t-tau for t in times]
    yy = [math.log(y*math.sqrt(s)) for y,s in zip(obs, ss)]
    # Multiply by s: -A+log(K)*s-B*s*s, quadratic interpolation.
    # divided differences on an arbitrary triple of distinct positive times
    s0,s1,s2=ss
    z0,z1,z2=[s*y for s,y in zip(ss,yy)]
    d01=(z1-z0)/(s1-s0)
    d12=(z2-z1)/(s2-s1)
    quadratic=(d12-d01)/(s2-s0)
    linear=d01-quadratic*(s0+s1)
    constant=z0-linear*s0-quadratic*s0*s0
    return -constant, -quadratic, math.exp(linear) # A, B, K

def recover_upstream(x0, x1, times, c0, c1, tau):
    A0,B0,K0=fingerprints(x0,times,c0,tau)
    A1,B1,K1=fingerprints(x1,times,c1,tau)
    close(B0,B1,tol=1e-7)
    r=math.sqrt(A1/A0)
    assert r > 1
    xi=(r*x0-x1)/(r-1)
    D=(x0-xi)**2/(4*A0)
    rho=2*math.log(K1/K0)/(x1-x0)
    v=D*rho
    k=B0-rho*rho*D/4
    M=K0*math.sqrt(4*math.pi*D)*math.exp(-rho*(x0-xi)/2)
    return xi,D,v,k,M

def recover_three(xlocs, times, obs, tau):
    vals=[fingerprints(x,times,ys,tau) for x,ys in zip(xlocs,obs)]
    xs=xlocs
    aa=[z[0] for z in vals]
    d01=(aa[1]-aa[0])/(xs[1]-xs[0])
    d12=(aa[2]-aa[1])/(xs[2]-xs[1])
    alpha=(d12-d01)/(xs[2]-xs[0])
    beta=d01-alpha*(xs[0]+xs[1])
    D=1/(4*alpha)
    xi=-beta/(2*alpha)
    rho=2*math.log(vals[1][2]/vals[0][2])/(xs[1]-xs[0])
    v=D*rho
    k=vals[0][1]-D*rho*rho/4
    M=vals[0][2]*math.sqrt(4*math.pi*D)*math.exp(-rho*(xs[0]-xi)/2)
    return xi,D,v,k,M

rng = random.Random(1192105)
for _ in range(150):
    x0=rng.uniform(-0.8,0.8)
    L=rng.uniform(0.4,1.7)
    x1=x0+L
    p=rng.uniform(0.2,1.4)
    xi=x0-p
    D=rng.uniform(0.4,2.0)
    v=rng.uniform(0.1,1.0)
    k=rng.uniform(0.2,1.1)
    M=rng.uniform(0.5,2)
    tau=rng.uniform(-0.4,0.4)
    alt=alias(x0,x1,xi,D,v,k,M)
    assert x0<alt[0]<x1 and alt[1]>0 and alt[2]>0 and alt[3]>=0 and alt[4]>0
    N+=5
    for x in (x0,x1):
        for dt in (0.1,0.3,0.8,1.3,2.0,3.2):
            close(c(x,tau+dt,xi,D,v,k,M,tau),c(x,tau+dt,*alt,tau),tol=1e-10)
    times=[tau+z for z in (0.5,1.4,3.3)]
    obs=[[c(x,t,xi,D,v,k,M,tau) for t in times] for x in (x0,x1)]
    rr=recover_upstream(x0,x1,times,*obs,tau)
    for aa,bb in zip(rr,(xi,D,v,k,M)):
        close(aa,bb,tol=5e-8)
    x2=x1+rng.uniform(0.4,1.3)
    obs3=obs+[[c(x2,t,xi,D,v,k,M,tau) for t in times]]
    rr=recover_three((x0,x1,x2),times,obs3,tau)
    for aa,bb in zip(rr,(xi,D,v,k,M)):
        close(aa,bb,tol=5e-8)

# Exact calibrated-mass collision: two distinct releases retain M=1.
v=1.5*math.log(3)
alt=alias(0,1,-1,1,v,1,1)
close(alt[0],1/3)
close(alt[1],1/9)
close(alt[2],math.log(3)/6)
close(alt[3],1+0.5*math.log(3)**2)
close(alt[4],1)
for x in (0,1):
    for t in (0.2,0.6,1,2,4):
        close(c(x,t,-1,1,v,1,1,0),c(x,t,*alt,0),tol=1e-11)
print(f"PASS {N} checks")
