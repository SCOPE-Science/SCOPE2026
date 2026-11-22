# Self-review

**Correctness — PASS.** The stationary convolution and trajectory-reversal entropy identity are explicitly reconstructed from the published starting equations [1, Eqs. (4), (9), (10)]. The all-tail theorem follows by dominated convergence under the written log-density growth and moment conditions. The exact integer-power formula follows by binomial expansion and known Laplace moments; every coefficient is positive, which proves monotonicity, not merely numerical evidence. The standard-library checker verifies normalization, exact coefficients, and endpoint cases. No result from a finite parameter grid is used as an infinite proof.

**Originality — PASS (qualified).** The general resetting entropy-production functional and its Gaussian/exponential specializations are firmly prior [1], and the broader stochastic-thermodynamics setup is prior [2]. The reviewed final claim is the **asymptotic all-tail phase diagram and all-rate even-power monotonicity**, not the functional. Searches in published findings and primary literature for stretched-exponential reset-tail entropy scaling, quartic/super-Gaussian resetting entropy, and rate-dependent Gaussian/Laplace comparisons found no explicitly dominating theorem. The transformation is a consequence of the general functional identity, however, so broader implicit coverage remains the main originality risk; priority is not independently certified.

**Value — PASS.** Fixing the reset-location variance isolates the *tail shape* as the determinant of whether more infrequent resetting reduces or exacerbates path-wise irreversibility. The sharp \(p=2\) boundary and exact all-rate super-Gaussian monotonicity provide mathematically controlled design and interpretation constraints, not an arbitrary parameter slice. The paradoxical divergent rare-reset limit is realized by a smooth positive finite-variance quartic density; its full formula is exact.

**Closest prior literature and residual risks.** Mori et al. [1] directly imply the entropy functional for arbitrary reset distributions and solve exponential/Gaussian examples; that framework is not claimed as new. Bressloff [2] provides general stochastic-calculus methods, but access to its complete article was restricted; no unsupported full-text noncoverage claim is used. Physical reset-actuator work and finite return times could alter experimental interpretation.

Self-review: passed. Independent audit: not yet performed.

References: [1] https://arxiv.org/abs/2211.15372; [2] https://doi.org/10.1088/1751-8121/ad8495.
