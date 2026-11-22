"""Numerical cross-checks for the orthogonal tricylinder directional-width law.

Requires numpy and scipy; run: python check_tricylinder_width.py.
All theorems require their analytic proofs, not these finite checks.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize
from scipy.stats import qmc

ROOT2 = math.sqrt(2.0)
RMAX = math.sqrt(1.5)
MID = 2.0 / math.sqrt(3.0)


def support(u):
    u=np.asarray(u,dtype=float)
    a,b,c=sorted(np.abs(u),reverse=True)
    if a>=b+c:
        return math.hypot(a,b+c)
    return (a+b+c)/ROOT2


def h_laws(phi):
    c=math.cos(phi)
    s=math.sin(phi)
    ss=c+s
    thetac=math.atan(1/ss)
    thetam=math.atan(1/c)
    hc=math.sqrt(1+2*c*s/(1+ss*ss))
    hm=(2*c+s)/math.sqrt(2*(1+c*c))
    return thetac,thetam,hc,hm,ss


def angle_cutoff(t,phi):
    if t<=1: return 0.0
    tc,tm,hc,hm,s=h_laws(phi)
    if t>=hm: return tm
    if t<=hc:
        v=(t*t-1)/math.sin(2*phi)
        return math.asin(math.sqrt(max(0.,min(1.,v))))
    angle=math.atan(s)-math.acos(max(-1.,min(1.,ROOT2*t/math.sqrt(1+s*s))))
    return min(tm,max(tc,angle))


def cdf(t):
    if t<=1: return 0.
    if t>=RMAX: return 1.
    f=lambda phi:1-math.cos(angle_cutoff(t,phi))
    val=quad(f,0,math.pi/4,epsabs=3e-10,epsrel=3e-10,limit=400,points=[0,math.pi/8,math.pi/4])[0]
    return 12/math.pi*val


def direct_support(u):
    def ineq(x):
        return np.array([1-x[0]**2-x[1]**2,1-x[0]**2-x[2]**2,1-x[1]**2-x[2]**2])
    constraints=[{'type':'ineq','fun':lambda x,j=j:ineq(x)[j]} for j in range(3)]
    opt=minimize(lambda x:-np.dot(u,x),np.asarray(u)*0.9,method='SLSQP',constraints=constraints,bounds=[(-1,1)]*3,options={'ftol':2e-13,'maxiter':300})
    if not opt.success and (np.max(-ineq(opt.x))>1e-8):
        raise AssertionError((u,opt.message,opt.x))
    return float(np.dot(u,opt.x))


def main():
    checks=0
    assert abs(cdf(RMAX)-1)<1e-14;checks+=1
    assert abs(cdf(1))<1e-14;checks+=1
    rng=np.random.default_rng(20261116)
    for _ in range(180):
        v=rng.normal(size=3);v/=np.linalg.norm(v)
        a=support(v)
        b=direct_support(v)
        assert abs(a-b)<1e-8,(v,a,b)
        checks+=1
    # Equal-area directions via Sobol's square to S^2 transformation.
    z=qmc.Sobol(d=2,scramble=True,seed=538).random_base2(18)
    zz=2*z[:,0]-1
    ang=2*math.pi*z[:,1]
    rr=np.sqrt(1-zz*zz)
    vectors=np.column_stack([rr*np.cos(ang),rr*np.sin(ang),zz])
    ss=np.sort(np.abs(vectors),axis=1)[:,::-1]
    aa,bb,cc=ss.T
    hh=np.where(aa>=bb+cc,np.sqrt(1+2*bb*cc),(aa+bb+cc)/ROOT2)
    for t in [1.01,1.03,1.07,1.1,1.15,MID,1.18,1.21,1.22,1.224]:
        exact=cdf(t)
        sim=np.mean(hh<=t)
        assert abs(exact-sim)<0.004,(t,exact,sim)
        checks+=1
    for t in [MID,1.16,1.18,1.19,1.20,1.21,1.22,1.224, RMAX]:
        expected=1-4*(1-t/RMAX)
        assert abs(cdf(t)-expected)<3e-9,(t,cdf(t),expected)
        checks+=1
    for t in np.linspace(1+1e-5,RMAX-1e-5,50):
        assert 0<=cdf(t)<=1
        checks+=1
    print('CDF samples:',[(t,round(cdf(t),9)) for t in [1.0001,1.001,1.01,1.05,1.1,MID,1.18,1.22]])
    print('lower ratios:',[(d, cdf(1+d)/(d*math.log(1/d))) for d in [1e-2,1e-3,1e-4,1e-5]])
    print('threshold survival',4*(1-MID/RMAX))
    print('TRICYLINDER_WIDTH_CHECKS_OK',checks)

if __name__=='__main__':main()
