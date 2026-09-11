from decimal import Decimal, getcontext
getcontext().prec=50
import mpmath as mp
mp.mp.dps=50
# S(u,v)=1/u+1/v+v+u*v; minimize over u,v>0
f=lambda u,v: 1/u+1/v+v+u*v
# solve: v=1/u^2, u^4-u-1=0
g=lambda u: u**4-u-1
# find root >1
root=mp.findroot(g,1.22)
print("u*=",root)
v=1/root**2
print("v*=",v)
Smin=f(root,v)
print("Smin=",Smin)
print("rho_exc=Smin=",Smin)
# twisted distribution: weights proportional to step*e^{<a,s>} where a=(log u, log v)
import math
a=mp.log(root); b=mp.log(v)
print("a=",a,"b=",b)
steps=[(-1,0),(0,-1),(0,1),(1,1)]
Z=sum(mp.e**(a*sx+b*sy) for sx,sy in steps)
print("Z=",Z)
probs=[mp.e**(a*sx+b*sy)/Z for sx,sy in steps]
print(probs, sum(probs))
# twisted mean should be 0
mx=sum(p*sx for p,(sx,sy) in zip(probs,steps))
my=sum(p*sy for p,(sx,sy) in zip(probs,steps))
print("mean:",mx,my)
# twisted covariance
exx=sum(p*sx*sx for p,(sx,sy) in zip(probs,steps))-mx**2
eyy=sum(p*sy*sy for p,(sx,sy) in zip(probs,steps))-my**2
exy=sum(p*sx*sy for p,(sx,sy) in zip(probs,steps))-mx*my
print("cov:",exx,eyy,exy)
r=exy/mp.sqrt(exx*eyy)
print("r=",r)
theta=mp.acos(-r)
print("theta=arccos(-r)=",theta)
print("pi/theta=",mp.pi/theta)
# Denisov-Wachtel excursion exponent for zero-drift quadrant: alpha=-1-pi/theta? check convention e_n~C rho^n n^{-1-pi/(2beta)}... let's report p=pi/arccos(-r)
print("p=",mp.pi/mp.acos(-r))
# also correlation of ORIGINAL (zero-drift-normalized) for reference
# original cov computed earlier: [[1/2,1/4],[1/4,11/16]]
r0=(mp.mpf(1)/4)/mp.sqrt(mp.mpf(1)/2*mp.mpf(11)/16)
print("r0=",r0,"p0=",mp.pi/mp.acos(-r0))
