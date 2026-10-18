import math
import numpy as np
from scipy import special, optimize

def cdf(x,theta):
    z=x/theta
    return 1.0-0.5*(1.0+math.exp(2.0*z))*math.exp(-math.expm1(z))

def logpdf(x,theta):
    z=x/theta
    return -math.log(2.0*theta)+2.0*math.log(math.expm1(z))+z-math.expm1(z)

for theta in (0.5,1.0,2.3):
    for x in (0.05,0.3,1.0,2.0,4.0):
        g=math.expm1(x/theta)
        assert abs(cdf(x,theta)-special.gammainc(3.0,g)) < 4e-14

for theta in (0.7,1.0,2.0):
    for u in (0.01,0.2,0.5,0.8,0.99):
        g=special.gammaincinv(3.0,u)
        q=theta*math.log1p(g)
        assert abs(cdf(q,theta)-u) < 3e-13

x=np.array([0.41,0.73,1.05,1.46,2.18],dtype=float)
n=len(x)

def ll(theta,s):
    return sum(logpdf(float(v),theta) for v in s)
def F(theta,s):
    return np.array([cdf(float(v),theta) for v in np.sort(s)])
def mps(theta,s):
    ff=F(theta,s); d=np.diff(np.r_[0.0,ff,1.0]); return np.mean(np.log(d))
def ls(theta,s,weighted=False):
    ff=F(theta,s); i=np.arange(1,len(s)+1,dtype=float); t=i/(len(s)+1.0)
    w=np.ones_like(i) if not weighted else 1.0/(i*(len(s)-i+1.0))
    return np.sum(w*(ff-t)**2)
def cvm(theta,s):
    ff=F(theta,s); i=np.arange(1,len(s)+1,dtype=float); t=(2*i-1)/(2*len(s))
    return 1/(12*len(s))+np.sum((ff-t)**2)
def ad(theta,s):
    ff=F(theta,s); i=np.arange(1,len(s)+1,dtype=float)
    return -len(s)-np.sum((2*i-1)*(np.log(ff)+np.log(1-ff[::-1])))/len(s)

theta=1.17
for c in (0.37,2.0,5.5):
    y=c*x
    assert abs(ll(c*theta,y)-(ll(theta,x)-n*math.log(c))) < 3e-12
    assert abs(mps(c*theta,y)-mps(theta,x)) < 3e-13
    assert abs(ls(c*theta,y)-ls(theta,x)) < 3e-13
    assert abs(ls(c*theta,y,True)-ls(theta,x,True)) < 3e-13
    assert abs(cvm(c*theta,y)-cvm(theta,x)) < 3e-13
    assert abs(ad(c*theta,y)-ad(theta,x)) < 3e-13

def opt(fun,s,b=(0.05,10.0)):
    return optimize.minimize_scalar(lambda th: fun(th,s),bounds=b,method="bounded",
                                    options={"xatol":1e-12}).x
base_ml=opt(lambda th,s:-ll(th,s),x)
base_ls=opt(ls,x)
cscale=2.0
scaled_ml=opt(lambda th,s:-ll(th,s),cscale*x)
scaled_ls=opt(ls,cscale*x)
assert abs(scaled_ml/cscale-base_ml)<2e-6
assert abs(scaled_ls/cscale-base_ls)<2e-6

def second(fun,t,h):
    return (fun(t+h)-2*fun(t)+fun(t-h))/(h*h)
cinfo=2.5
I0=-second(lambda th:ll(th,x),theta,2e-5)
Ic=-second(lambda th:ll(th,cinfo*x),cinfo*theta,5e-5)
assert abs(Ic/(I0/cinfo**2)-1)<3e-5

print("VERIFY_OK")
print("ML_base",format(base_ml,".12f"))
print("ML_scaled_over_c",format(scaled_ml/cscale,".12f"))
print("LS_base",format(base_ls,".12f"))
print("LS_scaled_over_c",format(scaled_ls/cscale,".12f"))
print("information_ratio",format(Ic/(I0/cinfo**2),".12f"))
