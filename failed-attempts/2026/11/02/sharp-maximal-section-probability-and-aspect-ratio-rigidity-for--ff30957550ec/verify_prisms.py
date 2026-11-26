"""Independent edge-intersection checks of the maximal-section probability of right regular even-gon prisms."""
import math
import numpy as np

def law(m, h):
    x=math.sin(math.pi/(2*m))
    y=math.sin(math.pi/m)
    t=1/math.sqrt(1+h*h)
    return (2*m/math.pi)*(2*math.asin(x*t)-math.asin(y*t))

def classify_direct(m,h,n,seed):
    g=np.random.default_rng(seed).standard_normal((n,3))
    th=np.arange(2*m)*math.pi/m
    pr=np.outer(g[:,0],np.cos(th))+np.outer(g[:,1],np.sin(th))
    above=pr+h*g[:,2,None]
    below=pr-h*g[:,2,None]
    nv=(above*below<0).sum(axis=1)
    nv+= (above*np.roll(above,-1,axis=1)<0).sum(axis=1)
    nv+= (below*np.roll(below,-1,axis=1)<0).sum(axis=1)
    return nv

for m,h in [(2,2**-.5),(3,5**.5/2),(4,1),(5,1.3),(8,.8),(12,2.5)]:
    num=classify_direct(m,h,220000,m+175)
    assert np.all((num>=4)&(num<=2*m+2)&(num%2==0)), (m,np.unique(num))
    obs=np.mean(num==2*m+2);exact=law(m,h)
    print('m/h',m,h,'direct',obs,'theory',exact,'error',abs(obs-exact))
    assert abs(obs-exact)<.0042
    hstar=math.sqrt(3*math.cos(math.pi/(2*m))**2-1)
    assert law(m,hstar)>=max(law(m,hstar*.97),law(m,hstar*1.03))

# Direct deterministic sign-combinatorics over a fine grid, not the integral derivation.
for m in range(2,13):
    for phi in np.linspace(.0003,math.pi/(2*m)-.0003,24):
        dots=np.cos(phi-np.arange(2*m)*math.pi/m)
        distinct=sorted(set(np.round(np.abs(dots),12)))
        # take second-highest and highest among antipodal pairs
        vals=np.sort(np.abs(dots[:m]))
        a,b=vals[-2],vals[-1]
        for t in [a-.001, (a+b)/2, b+.001]:
            if t<0 or (t<=a and t>=b):continue
            pos=dots+t
            neg=dots-t
            nv=np.sum(pos*neg<0)+np.sum(pos*np.roll(pos,-1)<0)+np.sum(neg*np.roll(neg,-1)<0)
            assert (nv==2*m+2)==(a<t<b), (m,phi,t,nv,a,b)

for m in (3,6,10,30,100):
    h=math.sqrt(3*math.cos(math.pi/(2*m))**2-1)
    approx=math.pi**2/(6*math.sqrt(3)*m*m)
    print('asymptotic m',m,'exact',law(m,h),'leading',approx,'ratio',law(m,h)/approx)
print('ALL_CHECKS_PASSED')
