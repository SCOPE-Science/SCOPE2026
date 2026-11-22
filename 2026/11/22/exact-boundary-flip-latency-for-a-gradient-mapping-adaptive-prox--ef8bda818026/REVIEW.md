# Scientific review

## Correctness — PASS

The projection of a radial point is a scalar clipping, so a saturated reversal is equivalent to \(\lambda\eta/S_k\ge2\). Each full reversal travels exactly \(2R\), multiplying the accumulator by \(Q=\sqrt{1+4R^2/\eta^2}\). This gives the precise integer count including the equality case. Thereafter \(\lambda\eta/S_k<2\) remains true as the accumulator increases, so the ball projection never acts again. A telescoping difference-of-squares inequality bounds the accumulator, yielding a uniform contraction factor strictly below one. The reciprocal-log expansion proves the \(\eta^2\log\eta\) asymptotic. Finite recurrence checks and exact-rational threshold certificates passed; they do not replace the proof. The scope includes all finite positive dimensions, strictly positive parameters and boundary initializations.

## Originality — PASS, qualified

The motivating algorithm and convergence theory are due to Wang and Yurtsever (arXiv:2605.05944, Algorithm 1, Sections 3–4 and Appendix E). Ene, Nguyen and Vladu (arXiv:2007.08840, Appendix A) present a related movement-normalized constrained AdaGrad+ update. The published result *Automatic boundedness for deterministic gradient-mapping accumulation* removes a boundedness hypothesis for the same algorithm, but its theorem and proof do not count initial antipodal boundary steps or derive their sharp large-gain coefficient. Searches of related mathematical records found different stepsize and projection phenomena, but no same-statement or stronger covering claim. The near-equivalence of the scalar accumulation recurrences is acknowledged: the proposed contribution is the exact objective-plateau complexity, not the recurrence or general convergence.

## Value — PASS

An explicitly solvable strongly convex constrained problem reveals an arbitrarily long initial interval of zero objective progress as the free gain increases, despite eventual geometric convergence and a one-step fixed-stepsize solution. The exact floor law and leading constant distinguish finite-iteration startup latency from asymptotic convergence; they are useful for gain selection and for interpreting parameter-uniform complexity statements. This is not a claim that standard gain choices or other constrained objectives exhibit the same delay.

## Limitations and closest literature

The result is restricted to an isotropic quadratic, a Euclidean-ball constraint and a boundary start, with deterministic full gradients, exact arithmetic and projection. The sharp large-gain plateau is a constructed family, not a universal lower bound. Related scalar AdaGrad+ representations may conceal equivalent observations, and further historical comparison could change priority. There is no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
