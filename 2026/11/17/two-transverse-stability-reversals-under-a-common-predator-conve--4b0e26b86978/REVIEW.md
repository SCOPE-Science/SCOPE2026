# Scientific review

## Correctness — PASS

The positive equilibrium follows from a nonsingular constant coefficient matrix; its exact positive existence interval is \(3/7<t<703/175\). The exact Jacobian coefficients and the identity \(AB-C=Q/(7925540864t^3)\) are recomputed by symbolic differentiation and determinant expansion in `check.py`. The numerator of \(B\) has a strictly negative cubic discriminant, unique negative real root, and hence remains positive throughout the feasible interval. Descartes' rule and three disjoint rational sign brackets isolate every positive root of \(Q\) and prove exactly two are feasible. The Routh–Hurwitz test and implicit differentiation prove opposite transverse imaginary crossings. Numerical root values are illustrations, not proof. At a boundary the nonlinear equilibrium stability is undecided.

## Originality — PASS within examined evidence

The 2026 Huang–Yang primary full-text paper explicitly gives the eight-parameter two-prey–one-predator system and its general cubic Routh–Hurwitz criteria. Those antecedents are credited rather than claimed. Its introduction, the local-stability theorem, stability tables and discussion were read for the stronger specific statement of **two** crossings under one common predator-conversion factor with a fixed prey interaction matrix; that explicit parameter-path phase diagram was not identified. Braza's 2003 two-Hopf result is for Holling–Tanner, not the unsaturated three-population Lotka–Volterra competition ODE. Smith's 1982 result addresses two predators and one prey. A published three-species antagonistic-loop reentrance result varies a reciprocal antagonistic link, unlike the moving-equilibrium conversion-efficiency sweep here. Search results do not guarantee novelty; especially older Lotka–Volterra bifurcation literature remains a risk.

## Mathematical value — PASS

Two opposite oscillatory stability changes along a **single positive coexistence branch** occur in the standard unsaturated autonomous three-species ecological ODE, without delay, spatial coupling, seasonal switching or specially tuned higher-order response terms. The calculation gives exact global parameter ordering, both transversality signs and perturbation robustness, making the specific ecological parameter mechanism accessible for future nonlinear or global analysis. It is not a routine single-point linear stability exercise: the complete algebraic parameter scan is proved and the second stability restoration is nontrivial.

## Closest sources and remaining limits

The Huang–Yang paper covers general equilibrium stability conditions, not an explicitly determined single-sweep double-transition theorem in the inspected sections. The Braza paper was available as a bibliographic abstract, not full text. A record of reentrance for antagonistic three-species links was available as a published summary, not complete source text. These access restrictions limit historical-priority confidence, but the models and parameter mechanisms in the descriptions differ in mathematically relevant ways. Nothing here proves a nonlinear Hopf branch or classifies global attractors.

Self-review: passed. Independent audit: not yet performed.
