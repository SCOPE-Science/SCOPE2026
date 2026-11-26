# Independent mathematical audit

## correctness

PASS

Reconstructed the argument for every initial point in the stated open Ω. In transformed coordinates x'=-qpx², q'=4x, p'=1-p+2εp² and ε'=ε²(4/q²-p). There are strict inward signs at p=1/2, p=2, q=3 and ε=1/10. On finite times x cannot reach zero since (1/x)'=qp, p is bounded, x is decreasing and q≤q0+4x0 t; positivity of ε then follows. These bounds also give global continuation. If q remained bounded, d log x/dq=-qp/4 would bound x away from zero, contradicting q'=4x and bounded q. Thus q→∞, while x→0 by x'≤−(3/2)x² and y=px²→0. A direct estimate giving the needed uniform tails is ε'≤−ε²/18: it gives ε(t)≤ε0/(1+ε0t/18) and ∫ε²≤18ε0. Write r=p−1. In r'+r=2εp², variation of constants and the L¹ norm of the exponential kernel give ||r||₂≤|r0|/√2+8||ε||₂. Hence (log J)'=−εr for J=x exp(q²/8) is absolutely integrable, proving a positive finite limit. Time shifts preserve that limit. The tail past T is bounded by ||ε||_{L²(T,∞)}||r||₂, uniformly small on compact initial-data sets, so finite-time continuous dependence gives continuity. With q0>3 fixed and p0=1, |log(L/[x0 exp(q0²/8)])|≤144ε0=O_{q0}(x0); since every L is positive but these values tend to zero, L is nonconstant. Integration of dt/dq=e^{q²/8}/(4J) gives t~e^{q²/8}/(Lq), by the endpoint asymptotic ∫^Q e^{s²/8}ds~4e^{Q²/8}/Q. Therefore tqx→1 and taking logarithms gives q²=8log t+4log log t+4log 8+8log L+o(1). The stable filter first implies p→1, and then the forcing is asymptotic to 2/t. In its convolution the part before t/2 is exponentially small; on later times the rescaled forcing is bounded, and at each fixed backward lag it tends to 2. Dominated convergence against the exponential kernel gives tr→2. Integrating (log J)'=−2/t²+o(t⁻²) from t to infinity gives the positive 2/t correction. These are analytic checks in physical time, with pointwise asymptotics. I inspected the frozen verify.py and recorded sample diagnostic, did not run that script, and did not complete an independent numerical trajectory check.

## originality

PASS

Best of knowledge for the continuous nonconstant scattering invariant on this specific escaping region and its state-resolved clock. The same-ODE leading-order companion covers trapping and the leading rates, and its exact proof identities give a short route to the pointwise refinements once supplemented with a convolution/tail argument. The novelty is not a new escaping cone or the leading clock, and the pointwise conclusions are close refinements, not independent phenomena. The uniform argument for dependence on initial state and nonconstancy is a substantive part of the surviving claim. Publication priority remains provisional, particularly against the 2019 originating paper.

## value

PASS

The explicit positive continuous invariant distinguishes escaping trajectories that are indistinguishable at leading order, via their finite physical-time height offset after subtraction of the universal log and log-log terms. It also quantifies how quickly the observable approaches its limit. This is useful original-time information in a studied quadratic family with an equilibrium line, independent of any claim of algebraic integrability or applicability outside Ω.

The dated certificate retains the supplied scientific assessment, sources and limitations.
