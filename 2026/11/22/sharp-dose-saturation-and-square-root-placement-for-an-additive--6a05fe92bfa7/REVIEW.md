# Independent mathematical audit

## correctness

PASS

Variation of constants gives D_s(t)=g(t) before s and g(t)−min(Delta,g(s))exp(−b(t−s)) after it. The untreated sag peaks uniquely at t_c, with g''(t_c)=−abM. For 0<s<=t_c and positive dose, the post-pulse curve has its unique maximum after t_c: writing A=1+exp(bs)min(Delta,g(s))/K, the peak occurs at t_c+log(A)/(b−a) with height M A^(−a/(b−a)). Its height strictly decreases with s before t_c since exp(bs)min(Delta,g(s)) is the minimum of two strictly increasing functions there. The upstream supremum g(s) strictly increases to M. The continuous maxima cross once, giving strict global minimax; s=0 and s>=t_c have risk M, since g(0)=0 and the upstream limit is included. Full reset gives post-peak M exp(−as), yielding exactly s_star and Delta_star, with the crossing strictly before t_c. For s in [s_star,t_c) the pulse actually required for balancing is K exp(−bs)[(M/g(s))^((b−a)/a)−1]. It is strictly decreasing from Delta_star to zero and feasible (<=g(s)) precisely when g(s)>=M exp(−as). This verifies the branch, strict monotone shift and risk, and uniqueness at the critical dose; extra available dose is unused at full reset. Expanding this inverse dose formula at t_c−u and using K exp(−bt_c)=aM/(b−a) gives Delta=abM u²/2+O(u³), independently yielding both claimed asymptotics. At Delta=0 every location ties. I also checked the benchmark (a,b,L0)=(1,2,1): s_star=log(4/3), Delta_star=3/16. At Delta=0.1 put z=exp(−s); independent 65-digit decimal bisection of 20z³−20z²+7z−2 on [1/2,3/4] gives s≈0.349977832842958 and risk z−z²≈0.208096390775130, consistent with the source's stated approximations.

## originality

PASS

Credit prior work for the oxygen-sag model, additive impulse response setting, placing cost-optimal aerators at binding deficits, and balancing the upstream value with a downstream sag in the fixed-fraction model. The supported distinct result is the exact global capped fixed-available-dose phase diagram and its weak-dose law. The active-constraint placement and the post-peak formula alone are not new. In the fractional theorem an at-site reparameterization gives the same local peak, but not equality of the two risk functions over alternative sites; the additive-dose crossing, cap feasibility threshold, and inversion at zero dose need a separate comparison.

## value

PASS

A site-independent dose budget and inability to oxygenate beyond saturation are natural constraints absent from the constant-fraction formulation. The complete unique placement and risk profile distinguishes overprovision (exact no-improvement threshold) from near-zero sensitivity (a quantitative square-root movement), which can matter in using this classical baseline. The result is a mathematical benchmark, not an engineering prescription or a new general impulse-control method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
