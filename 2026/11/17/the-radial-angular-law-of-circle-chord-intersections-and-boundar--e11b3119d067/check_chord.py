import numpy as np
from scipy.integrate import simpson
rng=np.random.default_rng(314159)
N=600000
T=rng.uniform(0,2*np.pi,(N,4))
mid=(T[:,0]+T[:,1])/2
mid2=(T[:,2]+T[:,3])/2
a=mid%np.pi; b=mid2%np.pi
p=np.cos((T[:,1]-T[:,0])/2)*np.where(mid>=np.pi,-1,1)
q=np.cos((T[:,3]-T[:,2])/2)*np.where(mid2>=np.pi,-1,1)
s=np.sin(b-a)
x=(p*np.sin(b)-q*np.sin(a))/s
y=(q*np.cos(a)-p*np.cos(b))/s
R=np.hypot(x,y)
D=(b-a)%np.pi
C=R<1
assert abs(np.mean(C)-1/3)<.004
print('P(cross)',C.mean())
# Unconditional angle: beta 2 2 in angle/pi
print('cross angle mean cos2', np.mean(np.cos(2*D[C])), 'expected',-3/np.pi**2)
# radial bin angular histogram compared with quadrature f(delta;r)
NA=2001
al=np.linspace(0,np.pi,NA)
nd=np.linspace(.01,np.pi-.01,35)
for rad in [.25,.65,.9]:
 A=1/np.sqrt(1-rad**2*np.cos(al)**2)
 j=np.array([simpson(A/np.sqrt(1-rad**2*np.cos(al+d)**2),x=al) for d in nd])
 f=rad**2*np.sin(nd)*j/(2*np.pi*(-np.log1p(-rad*rad)))
 sel=C & (np.abs(R-rad)<.05)
 obs=np.mean(np.cos(2*D[sel]))
 moment=simpson(f*np.cos(2*nd),x=nd)
 # approximates endpoints .01 omitted (negligible)
 print('r=',rad,'sample_count',sum(sel),'obs cos2',obs,'pred approx',moment,'density area',simpson(f,x=nd))
# conditional angle at radial shell near boundary, predicted nearly uniform
for cutoff in [.9,.97,.99]:
 sel=C&(R>cutoff)
 m=np.mean(np.cos(2*D[sel]));n=sum(sel)
 print('R>',cutoff,'n',n,'mean cos2',m,'uniform limit=0')
print('CHORD_JOINT_RADIAL_ANGLE_DIAGNOSTIC_OK')
