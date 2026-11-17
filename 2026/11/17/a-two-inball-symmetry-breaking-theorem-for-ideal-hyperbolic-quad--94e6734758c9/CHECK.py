import math,random
from scipy.optimize import differential_evolution
for c in [1/math.sqrt(2), .75,.8,.85,.95,.999]:
 s=math.sqrt(1-c*c);u0=(c*c-s*s)/c
 def k(x,y):
  if abs(x)>=c or abs(y)>=s:return 0.0
  den=math.sqrt(1-x*x-y*y)
  return min((c-abs(x))/s,(s-abs(y))/c)/den
 sol=differential_evolution(lambda z:-k(*z),[(-c+.000001,c-.000001),(-s+.000001,s-.000001)],tol=1e-11,popsize=18,seed=2931,maxiter=800)
 kp=1/math.sqrt(4*c*c-1)
 assert abs(-sol.fun-kp)<5e-7,(c,sol.fun,kp)
 assert abs(abs(sol.x[0])-u0)<5e-5,(c,sol.x,u0)
 assert abs(sol.x[1])<5e-5,(c,sol.x)
 for z in range(12000):
  x=(2*random.random()-1)*c;y=(2*random.random()-1)*s
  assert k(x,y)<=kp+1e-12
 print(f'c={c:.6f}, opt={sol.x}, sinh(inradius)={-sol.fun:.10f}, predicted={kp:.10f}')
print('IDEAL_QUADRILATERAL_INBALL_CHECKS_OK')
