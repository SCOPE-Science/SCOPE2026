import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from delta import Delta, r, eu, es, lam, mu, apply_B
# Symbolic K(x): derive series for mixed derivative.
# For f_k(y) = r(B^k y), D2 term: let v_u=B^k eu=lam^k eu, v_s=B^k es=mu^k es (with wrap, derivatives same)
# mixed deriv of compensated sum: sum_{k>=0} dr terms... Let's just compute K formula by differentiating r analytically.
# dr(x) = 2pi*(0.04 cos(2pi x1), -0.03 sin(2pi x2)); D2r[v,w] = -(2pi)^2 (0.04 sin(2pi x1) v1 w1 + 0.03 cos(2pi x2) v2 w2)... check: d2/dx1^2 = -(2pi)^2*0.04 sin; d2/dx2^2 = -(2pi)^2*0.03 cos.
# term for quadrilateral Q_k(x)= r(B^k(x+aeu+bes))-r(B^k(x+aeu))-r(B^k(x+bes))+r(B^k x)
# d2/(da db)|0 = D2r(B^k x)[B^k eu, B^k es] = -(2pi)^2 [0.04 sin(2pi (B^k x)_1) lam^k mu^k eu1 es1 + 0.03 cos(2pi (B^k x)_2) lam^k mu^k eu2 es2]
# since lam*mu=1, lam^k mu^k = 1! So K(x) = sum_{k in Z} g(B^k x) where g(y) = -(2pi)^2[0.04 sin(2pi y1) eu1 es1 + 0.03 cos(2pi y2) eu2 es2], with convergence factors? But wait sum over k of conjugated terms: forward sum k>=0 converges? Each term O(1) — NOT summable! Need compensation: Delta has stable holonomy form with subtraction; mixed derivative should converge because individual D2 terms don't decay... Hmm.
# Actually check: forward temporal function H_s: sum r(B^k xu)-r(B^k x) terms have first-deriv in a direction decaying? mixed derivative: D2r(B^k x)[lam^k eu, mu^k es]: lam^k*mu^k=1 so each O(1)?? That diverges!
# Resolution: Delta as defined double-sums; mixed partial needs care: the compensating terms make each fixed-(a,b) summand O(lam^{-k}) etc but derivative in a brings factor lam^k. So formal termwise mixed derivative diverges; K(x) must be defined via summation-by-parts / Livsic coboundary. But numerics show K finite (~O(1)). Let's verify scaling: Delta(x,h,h)/h^2 at decreasing h.
x = np.array([0.13,0.71])
for h in [0.02,0.01,0.005,0.002,0.001]:
    print(h, Delta(x,h,h,N=16)/h**2, Delta(x,h,-h,N=16)/h**2)
# So K exists. The resolution: sum formula must be grouped; termwise differentiation invalid.
# Standard formula: Delta's Taylor: Delta = (1/2) c(x) a b + ..., c from derivative of temporal holonomy (Anosov cocycle), computed via convergent series with contraction on appropriate bundle (derivative of unstable holonomy along stable etc).
# Let's test the two-sided decomposition convergence empirically per-side.
x = np.array([0.13,0.71]); a=b=0.01
for N in [4,8,12,16,24,32]:
    fwd = sum(r(apply_B((x+a*eu)%1.0,k))-r(apply_B((x+a*eu+b*es)%1.0,k))-r(apply_B(x,k))+r(apply_B((x+b*es)%1.0,k)) for k in range(N+1))
    bwd = sum(r(apply_B(x,-j))-r(apply_B((x+a*eu)%1.0,-j))+r(apply_B((x+a*eu+b*es)%1.0,-j))-r(apply_B((x+b*es)%1.0,-j)) for j in range(1,N+1))
    print(N, fwd, bwd, fwd+bwd)
