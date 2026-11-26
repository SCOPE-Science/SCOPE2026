# Independent mathematical audit

## correctness

PASS

At fixed search parameters the assumed exit flux gives h(L−ε)=(rq/D)ε+o(ε). Rescaling the OU backward equation with the stated K, Z_K and V_K gives F''+(1−z/K)F'=sF with boundary values 1 and 0. At s=0 the splitting ratio is the integral from z to K of exp(−v+v²/(2K)) divided by the integral from 0 to K of the same integrand. For K≥1 the denominator is at least 1−e^(−1), and the numerator is bounded by 2e^(−z/2). The same bound holds for s≥0 by killing/discount comparison. The integrating-factor equation gives compact derivative bounds from the bounded values of F at two separated sites; the resulting local limit uniquely solves F''+F'=sF with F(0)=1 and decay at infinity (the latter matters at s=0). Thus F=exp(−a_s z), a_s=(1+sqrt(1+4s))/2. Near L one may dominate the rescaled integral by a constant times z exp(−z/2); away from L the exponential bound times the finite mass of h is negligible even after multiplication by K². Integration gives rL²q/(DK²) times (u+a_s)^−2. Paths starting below 0 cannot succeed on return. The conditional hitting-time transform is exp(−z(a_s−1)), with mean z and variance 2z, so the limit mixture has mean 2 and variance 6. The eventual return-success fraction is P(E_K)/(q+P(E_K)), not the per-cycle rare-event probability. The finite BVP and MFPT scripts in the frozen package were inspected, not executed; the asymptotic decision is analytic.

## originality

PASS

The distinct content is the flux-normalized joint law of the boundary-layer starting gap and conditioned successful duration in the stiff-return limit. The protocol, renewal formulas, finite-strength splitting law and drifted-Brownian first-passage transform are antecedents, not priority claims. No separate inspected statement covers the joint selection and time limit together.

## value

PASS

For this target-visible protocol the theorem quantifies a rare detection channel that total mean completion times can hide. It identifies both the inverse-square frequency and the coupled entrance-gap and duration scales from the local flux alone, not from a fitted Brownian example or a typical-return approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
