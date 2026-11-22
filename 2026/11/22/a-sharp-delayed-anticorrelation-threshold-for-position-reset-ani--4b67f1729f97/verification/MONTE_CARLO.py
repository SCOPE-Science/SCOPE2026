import numpy as np
import math
rng=np.random.default_rng(1729)
N=180000; M=130; F=160
r=4.; q=.2; D=1.; delta=.98
ang0=rng.uniform(-math.pi,math.pi,N)
age=rng.exponential(1/r,N)
ang=ang0.copy(); timestep=age/M
xx=np.zeros(N);yy=np.zeros(N);xy=np.zeros(N)
for _ in range(M):
    c=np.cos(2*ang); ss=np.sin(2*ang)
    xx+=2*(D+delta*c)*timestep
    yy+=2*(D-delta*c)*timestep
    xy+=2*delta*ss*timestep
    ang+=np.sqrt(2*q*timestep)*rng.normal(size=N)
base_xy=xx*yy+2*xy*xy

def predicted(t):
    v=4*D*D/r**2+4*delta**2/(r*(r+4*q));a=2*delta**2/(r+4*q)
    return math.exp(-r*t)*(v-a*math.expm1((r-4*q)*t)/(r-4*q))
print('lag=0',float(np.mean(base_xy)-np.mean(xx)*np.mean(yy)),predicted(0))
for lag in (.2,.6,1.0):
    ang=ang0.copy(); step=lag/F
    lastage=rng.exponential(1/r,N)
    noreset=lastage>=lag
    integral=np.zeros(N)
    for j in range(F):
        loc=(j+.5)*step
        frac=np.clip((loc-(lag-lastage))/step+.5,0,1)
        integral += 2*(D-delta*np.cos(2*ang))*step * frac
        ang += math.sqrt(2*q*step)*rng.normal(size=N)
    y2now=integral+noreset*yy
    prod=xx*integral+noreset*base_xy
    val=np.mean(prod)-np.mean(xx)*np.mean(y2now)
    print('lag=',lag,'conditional MC=',round(float(val),5),'exact=',round(predicted(lag),5),'error=',round(float(val-predicted(lag)),5))
    assert abs(val-predicted(lag))<0.03
print('MC checks passed')
