# Scientific assessment

**Correctness — PASS.** Both update multipliers have modulus below one, giving a finite second-moment stationary process. The conditional second moments solve an explicit two-state linear system with strictly positive determinant. The exact algebraic difference from the fixed-step variance and exact derivative of the Markov persistence parameter prove all strict and equality cases. The standalone checker passed 250 assertions (symbolic, exact rational, numerical recurrence). The infinite-dimensional quantifier over the parameter domain is discharged by the proof, not by numeric tests.

**Originality — PASS, with residual risk.** Gürbüzbalaban et al. (2023, arXiv:2302.05516) examine Markovian, cyclic and IID rate schedules through power-law tails and moment thresholds in stochastic regression; their inspected main and appendix results do not state the fixed-curvature, additive-noise exact stationary risk ordering or the persistence threshold. Goujaud et al. (2022, PMLR 151) address deterministic cyclical spectral convergence. Chen et al. (2021, arXiv:2111.06328) analyze constant-small-step stationary limits. The new contribution is an exact sharp ordering, not the classical method of Markov-modulated conditional moments. Equivalent step-switching parameterizations, broader covariance-theory coverage and exact-table possibilities were considered. A specialist prior publication may still have this explicit result.

**Value — PASS.** Alternating, IID and persistent two-rate learning schedules share identical per-step frequencies, average stepsize and oracle cost, yet can have sharply different stationary mean-square errors. The threshold \(h^2(1-\delta^2)>2\), the sharp repeat-probability boundary, and the independent monotonicity change at \(h=1\) give a natural complete classification for this benchmark and clarify how temporal ordering can overturn the usual IID stepsize-noise penalty. The claim is not extrapolated to nonlinear objectives or adaptive scheduling.

**Limitations.** Scalar fixed-curvature quadratic; fresh centered finite-variance gradient noise; symmetric two-state Markov stepsize chain; both steps individually stable. Convergence rates, higher-dimensional objectives and arbitrary noise correlations remain outside the proof.

**Primary comparisons.** https://arxiv.org/abs/2302.05516 ; https://proceedings.mlr.press/v151/goujaud22a.html ; https://arxiv.org/abs/2111.06328 .

Self-review: passed. Independent audit: not yet performed.
