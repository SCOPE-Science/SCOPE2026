"""Outward-rounded interval verification of scale-free Platonic section means.
Requires mpmath. Uses its interval arithmetic for the full closed expression.
"""
from mpmath import iv
iv.dps=65
pi=iv.pi
sqrt=iv.sqrt
one=iv.mpf(1)
phi=iv.sqrt(5)
solids=[('tetra',4,3,sqrt(6)/12),('cube',6,4,one/2),('octa',8,3,sqrt(6)/6),('dodeca',12,5,sqrt(250+110*sqrt(5))/20),('icosa',20,3,sqrt(3)*(3+sqrt(5))/12)]
values=[]
for name,F,p,h in solids:
 c=pi/p;a=one/(2*iv.tan(c));tt=iv.tan(c)
 x=a*tt/sqrt(h*h+a*a)
 I=a*iv.ln(x+sqrt(1+x*x))+h*iv.atan2(h*tt,sqrt(h*h+a*a*(1+tt*tt)))
 mean=F*h*p/2*(I-h*c)
 area=F*p*a/2
 volume=area*h/3
 normalized=mean/(volume**(iv.mpf(2)/3))
 values.append(normalized)
 print(name,'mean',str(mean)[:110],'normalized',str(normalized)[:120])
bounds=[('1.141336','1.141338'),('1.190037','1.190040'),('1.193400','1.193403'),('1.205385','1.205388'),('1.206447','1.206450')]
for val,(lo,hi) in zip(values,bounds):
 assert iv.mpf(lo)<val<iv.mpf(hi),f'Uncertified bracket: {val}'
for i in range(4):
 assert values[i]<values[i+1],f'Uncertified comparison: {i}' 
print('CERTIFIED_STRICT_NORMALIZED_ORDER_OK')
