"""Reproduce exact derivative certificates for cubic spherical Dirichlet caps.
Run: python checker.py (requires sympy and scipy). This is supplementary finite
arithmetic verification; the paper's all-dimensional inequalities are proved analytically.
"""
import sympy as sp
from scipy.integrate import quad
from math import sqrt
s,d=sp.symbols('s d',real=True)
c=1/(d+2)
g=[9*(1-s)*(s-c)**2,
   s*(2+c-3*s)**2+(d-2)*(s-c)**2,
   (1-s)*(1+2*(d-4)*s+9*s*s),
   3*(d+3*s)*(1-s)**2]
D=[18*(d-1)*(d+1)/(d*(d+2)**2*(d+4)),
   6*(d-1)*(d+1)**2/(d*(d+2)**2*(d+4)),
   3*(d-1)*(d+1)**2/(d*(d+2)*(d+4)),
   3*(d-1)*(d+1)**2*(d+3)/(d*(d+2)*(d+4))]
Q={
 (0,1):-d*(d+4)*((d+2)*s-1)*(3*(d+2)*s-(2*d+5))/(6*(d-1)*(d+1)**2),
 (0,2):d*(d+4)*(1-s)*(3*(d+2)*s-1)/(6*(d+1)**2),
 (0,3):d*(d+4)*(1-s)*((d**3+4*d*d+7*d+6)*s+d*d-3)/(2*(d-1)*(d+1)**2*(d+3)),
 (1,2):d*(d+4)*(9*(d+2)*s*s+(d*d-8*d-23)*s+(d+6))/(6*(d-1)*(d+1)**2),
 (1,3):d*(d+4)*((d*d-10*d-21)*s+9*(d+2)*s*s+5*d+6)/(6*(d-1)*(d+1)*(d+3)),
 (2,3):d*(d+2)*(d+4)*(1-s)*(2*d+9*s-3)/(3*(d-1)*(d+1)**2*(d+3))
}
checks=0
# Exact moment normalizations on S^{d-1}; beta moment E[z^{2j}]=(1/2)_j/(d/2)_j.
for k in range(4):
 p=sp.Poly(g[k],s)
 average=sum(coeff*sp.rf(sp.Rational(1,2),mon[0])/sp.rf(d/2,mon[0]) for mon,coeff in p.terms())
 assert sp.cancel(average-D[k])==0
 checks+=1
for (i,j),q in Q.items():
 identity=(1-d*s)*q+2*s*(1-s)*sp.diff(q,s)+(g[i]/D[i]-g[j]/D[j])
 assert sp.cancel(identity)==0,(i,j)
 checks+=1
# Check the all-dimensional polynomial positivity proof's finite subrange.
for nd in range(3,11):
 discr=(nd*nd-8*nd-23)**2-36*(nd+2)*(nd+6)
 assert discr<0
 checks+=1
# Independent quadrature against exact boundary-gap certificate for multiple dimensions/regions.
for nd in [3,4,5,7,11,18]:
 Z=quad(lambda z:(1-z*z)**((nd-3)/2),0,1,epsabs=2e-12)[0]
 lambdas=[]
 for a in [0.07,0.19,0.4,0.62,0.85,0.97]:
  lambdas=[]
  for k in range(4):
   val=quad(lambda z:(1-z*z)**((nd-3)/2)*float(g[k].subs({d:nd,s:z*z})),a,1,epsabs=1e-12)[0]
   lambdas.append(val/(Z*float(D[k].subs(d,nd))))
  for (i,j),q in Q.items():
   exact=float(q.subs({d:nd,s:a*a}))*a*(1-a*a)**((nd-1)/2)/Z
   assert abs(exact-(lambdas[i]-lambdas[j]))<3e-10,(nd,a,i,j,exact,lambdas)
   checks+=1
print(f'PASS: {checks} exact and independent numerical checks')
