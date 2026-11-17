"""Verify stable exact side-angle integration against the odd-gon crossover law."""
import math
from scipy.integrate import quad

def h_and_f(m,u):
 a=math.pi/m; x=a*u
 C=1/(2*m*math.tan(a)); T=math.tan(a)
 h=0.5+C*((math.tan(x+a)-math.tan(x)-T) if u<0 else (math.tan(x-a)-math.tan(x)+T))
 # Twice the side-coordinate density; integration applies an outer factor 1/2
 return h,2*a*m*C/(math.cos(x)**2) # integrates from -1 to 1 to 2

def ratio(m,n):
 # Q / (n * 2**(1-n)) = integral of f angular * (2h)^(n-1)
 return .5*sum(quad(lambda u: h_and_f(m,u)[1]*math.exp((n-1)*math.log(2*h_and_f(m,u)[0])),l,r,epsabs=1e-12,epsrel=1e-12)[0] for l,r in [(-1,0),(0,1)])

def limiting(t):
 return quad(lambda u: math.cosh(t*math.pi**2*u*(1-u)),0,1,epsabs=1e-12)[0]

def main():
 for t in [0.05,0.25,1,2,4]:
  print('tau',t,'limit',limiting(t))
  for m in [5,7,11,19,31]:
   n=max(3,round(t*m**3))
   val=ratio(m,n)
   print(m,n,round(val,10),'relative',round(val/limiting(t),9),'m2error',round((val-limiting(t))*m*m,5))
 for m in [5,7,13,29]:
  for u in [-1,-.7,-.5,0,.3,.5,.9,1]:
   h,f=h_and_f(m,u)
   g=u*(u+1) if u<0 else u*(1-u)
   assert abs(m**3*(2*h-1)-math.pi**2*g)<100/m**2
  assert abs(quad(lambda u:h_and_f(m,u)[1],-1,1)[0]-2)<1e-11
 print('REGULAR_POLYGON_PARITY_CROSSOVER_OK')
if __name__=='__main__':main()
