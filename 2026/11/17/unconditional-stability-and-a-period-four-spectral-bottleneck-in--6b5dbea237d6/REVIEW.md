# Independent mathematical audit

## correctness

PASS

The positive fixed-point equation (r+2b)t²+(v−2a)t−u=0 has one positive root by negative constant and positive leading coefficient. Set D=v+(2b+r)t=u/t+2a, α=(a−bt)/D, ω=rt/D. Algebra gives −1/2<α<1/2 and 0<ω<1. Jacobian is companion [[α,−ω,α],[1,0,0],[0,1,0]], P(λ)=λ³−αλ²+ωλ−α. The four exact strict cubic Jury conditions reduce to |α|<1, 1−2α+ω>0, 1+2α+ω>0, 1−ω>0. All hold without monotonicity restrictions. For a period-two alternating sequence A,B the subtraction factor (A−B)[v+2a+r(A+B)]=0 rules out distinct positive values. For ε=r^(−1/2), t=√u ε+(a−v/2)ε²+O(ε³), α=aε/√u+O(ε²), ω=1−v ε/√u+O(ε²). The simple limiting polynomial λ(λ²+1) and implicit perturbation give λ±=±i(1−v ε/(2√u))+O(ε²) and λ0=a ε/√u+O(ε²), hence the asserted spectral radius and coefficient independence. Two independent choices of u,v,a,b with r=4,10^4,10^6 gave strict ρ<1; scaled gaps converge toward v/(2√u) (0.50037 vs 0.5 in the first case at 10^6; 0.4571 vs 0.4472 in the second). Finite samples are diagnostic only.

## originality

PASS

Best-of-knowledge PASS for all-positive-parameter local Schur stability together with universal period-two absence and sharp r→∞ period-four spectral gap, while fully crediting earlier equal-outer-lag rational recurrence and its sufficient global-attractor regimes.

## value

PASS

The exact all-parameter local sink/no-two-cycle rigidity combined with a sharp singular relaxation law identifies a nontrivial spectral bottleneck: no finite-parameter local destabilization occurs, yet strong delayed inhibition drives damping to zero and nearly four-step oscillation. This distinction matters for analysis of delayed rational recurrences, without suggesting a nonlinear period-four attractor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
