import sympy as S
from scipy.optimize import brentq
import numpy as np
A=S.symbols('A', positive=True)
mu0,muS,xi,d=S.symbols('mu0 muS xi d', positive=True)
w=1/(A+1); s0=2*w; k=xi*A/2
s=(1+S.sqrt(1+(A*A-1)*d*d))/(A+1)
# Taylor: for sigmoid m(z)=mu0+muS*(1+tanh(k*(z-w)))
# d'=d*(1-s-2mu0) + s*muS*(tanh(k*(s-s0+d)/2)-tanh(k*(s-s0-d)/2)) - d*muS*(2+tanh(k*(s-s0+d)/2)+tanh(k*(s-s0-d)/2))
X=k*(s-s0)/2
Y=k*d/2
# expand polynomial in d; explicit up to cubic
s2=(A-1)/2
linear=S.factor(1-s0-2*(mu0+muS)+s0*muS*k)
cubic=S.factor(-s2-s0*muS*k**3/12)
xi_c=S.solve(linear,xi)[0]
print('linear:',linear,'xi_c:',xi_c,'cubic:',cubic)
assert S.simplify(linear-(A-1)/(A+1)+2*(mu0+muS)-muS*xi*A/(A+1))==0
assert S.simplify(cubic+ (A-1)/2+muS*A**3*xi**3/(48*(A+1)))==0
# numerical near bifurcation with A=2, mu0=1/3, muS=1/6, xi_c=6
AF=2.;m0=1/3;ms=1/6;xic=6.
from math import exp, sqrt,tanh

def station(dval, x):
 ss=(1+sqrt(1+(AF**2-1)*dval**2))/(AF+1)
 uu=(ss+dval)/2; vv=(ss-dval)/2
 m=lambda z:m0+ms*(1+tanh(x*AF*(z-1/(AF+1))/2))
 return (1-ss)+ (ss*(m(uu)-m(vv))/dval-(m(uu)+m(vv)))
for delta in [0.1,0.01,0.001]:
 x=xic+delta; pred=sqrt((ms*AF/(AF+1))*delta/((AF-1)/2+ms*AF**3*xic**3/(48*(AF+1))))
 root=brentq(lambda z:station(z,x),1e-6,0.15)
 ss=(1+sqrt(1+(AF**2-1)*root**2))/(AF+1)
 u=(ss+root)/2;v=(ss-root)/2
 mp=lambda z: ms*(x*AF/2)/(np.cosh(x*AF*(z-1/(AF+1))/2)**2)
 m=lambda z:m0+ms*(1+tanh(x*AF*(z-1/(AF+1))/2))
 # full Jacobian
 J=np.array([
 [1-2*u-AF*v-m(v), -AF*u-u*mp(v), m(u), v*mp(u)],
 [-AF*v-v*mp(u), 1-2*v-AF*u-m(u), u*mp(v),m(v)],
 [m(u),v*mp(u),1-2*v-AF*u-m(u),-AF*v-v*mp(u)],
 [u*mp(v),m(v),-AF*u-u*mp(v),1-2*u-AF*v-m(v)]
 ])
 eig=np.linalg.eigvals(J)
 print(delta,'d=',root,'pred=',pred,'ratio=',root/pred,'eig=',sorted(np.real(eig),reverse=True))
 assert 0.8<max(eig.real) / (.3333) <1.1
