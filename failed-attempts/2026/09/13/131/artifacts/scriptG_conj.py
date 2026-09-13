"""Script G: structural-stability distance check: ||f-A||_{C^1} explicit bound.
C^0 part + derivative part with exact integer arithmetic where possible."""
import math
Aop=3.246979603717467
alp,bet=2*math.pi*0.03,2*math.pi*0.02
C0=Aop*math.sqrt(0.03**2+0.02**2)
C1=Aop*math.hypot(alp,bet)
print(f"C0 dist <={C0:.4f}, C1 deriv <={C1:.4f}, total C1 <={C0+C1:.4f}")
print("quadratic products for D2f bounds:")
print("  D2S entries: 0.03*(2pi)^2 =",0.03*(2*math.pi)**2," 0.02*(2pi)^2 =",0.02*(2*math.pi)**2)
print("  ||D2f|| <= ||A||*max =",Aop*0.03*(2*math.pi)**2)
