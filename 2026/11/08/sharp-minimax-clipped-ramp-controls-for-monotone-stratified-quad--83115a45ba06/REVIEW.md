# Scientific review: minimax clipped-ramp controls for monotone stratified quadrature

## Correctness — PASS

The final theorem is an equality over **all** fixed deterministic, square-integrable, mean-zero stratum controls and all bounded nondecreasing integrands, with independent uniform within-stratum draws. The unit-step reduction follows from the nonnegative Stieltjes representation of monotone functions and convexity of the squared centered-estimator norm. Averaging the exact unit-step risk over a uniformly selected stratum and a central local jump supplies a lower bound, whose Hilbert-space square completion has a unique equality point. The clipped-ramp candidate has a flat maximum over precisely that central interval, so it attains the lower bound. Every dependence on \(n\), each local coordinate, and the variance normalization has been reconstructed. A standalone standard-library rational verifier passed 3,217 assertions; no finite sample is used as an infinite-dimensional proof. Unproved: more general adaptive or coupled estimator classes.

## Originality — PASS, with recorded precedence risks

The central motivating paper of Basak, Bect and Vazquez (arXiv:2203.00423, PDF pp. 3–6, Theorems 3.1 and 4.1) gives separate results for unstratified linear-control sampling and uncorrected independent stratification. The current theorem concerns the missing joint, unrestricted stratumwise additive-control optimization, establishes its clipped nonlinear optimizer, proves uniqueness, and gives a different sharp constant. Bayne and Chakraborty (arXiv:1804.01197, PDF pp. 1–5) combine generic controls and stratification for molecular integrals but not the bounded-monotone universal minimax problem. Chopin and Gerber (arXiv:2210.01554, PDF pp. 1–3 and abstract) assume smoothness and use numerical derivatives, so their higher-order guarantees do not cover the discontinuous unit-step worst cases. Published mathematical-research semantic searches found general control/stratified sampling and bounded-variance results, but no comparable exact theorem. This is best-knowledge originality rather than a proof of universal precedence. An equivalent result in older numerical integration or optimal-recovery literature remains a genuine risk; Novak's 1992 paper was identified but its entire primary text was not fully inspected.

## Value — PASS

The missing design problem is natural: a bounded monotone risk integrand has neither derivatives nor a known shape beyond its order, yet its integral is estimated from one observation per fixed stratum. A preselected correction must improve the **worst case** without data-dependent tuning. The theorem characterizes the unique optimal control in an infinite-dimensional admissible family, including clipping rather than just a best scalar coefficient, and supplies a sharp finite-sample gain. At two points the worst-case variance falls from \(1/16\) to \(7/192\), about 41.7 percent below uncorrected stratification and below the global linear-control benchmark \(1/24\). It does not change the leading \(n^{-2}\) variance rate, nor establish unrestricted unbiased quadrature optimality; those limitations are material rather than concealed.

## Closest literature and limits

- S. Basak, J. Bect, E. Vazquez, *Integration of bounded monotone functions*, arXiv:2203.00423 (2022), especially Theorems 3.1 and 4.1; same integrand class, different estimator classes.
- M. G. Bayne, A. Chakraborty, *Composite control-variate stratified sampling*, arXiv:1804.01197 (2018); generic hybrid method for molecular integrals, no matching minimax statement.
- N. Chopin, M. Gerber, *Higher-order Monte Carlo through cubic stratification*, arXiv:2210.01554 (2022); smoothness and derivative-based control construction rather than bounded-monotone uniform-risk optimization.
- E. Novak, *Quadrature formulas for monotone functions*, Proc. AMS 115 (1992); relevant wider randomized/adaptive complexity, not established as covering the fixed additive-control claim. Primary full-text comparison remains incomplete.

Self-review: passed. Independent audit: not yet performed.
