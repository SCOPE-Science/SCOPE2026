# Self-review

**Correctness — PASS.** The exact transformed-ratio derivative is nonpositive after an integrable logistic upper correction, forcing every positive trajectory into the prey-only boundary. Logistic comparison then proves global convergence. Exact reciprocal-predator and prey-error identities yield the inverse-time laws and an integrable remainder after logarithmic subtraction. Symbolic and numerical checks were replayed from `check.py`. The proof applies to the precise positive-data, monotone-ratio hypothesis; the script is supplementary evidence, not infinite certification.

**Originality — PASS within the inspected evidence.** The 2021 original model paper and the 2022 extinction analysis were inspected in accessible full-text versions. Both state equilibrium invasion conditions or Lambert-W extinction analysis, but neither inspected statement covers the exact global neutral-threshold theorem or its signed logarithmic coefficient. The nearest indexed exponential ratio-dependent result concerns the collision of two *extinction* directions, requiring an equation incompatible with the monotone-ratio hypothesis. Analogous logarithmic corrections in other models do not imply this coefficient. Search incompleteness and unindexed equivalent work remain residual risks.

**Mathematical value — PASS.** The predator's invasion threshold is neutral, so conventional exponential stability predictions give no extinction clock; the exact \(t^{-1}\) law and the first signed logarithmic term resolve the rate for **all** positive starting states in a structurally meaningful parameter region. The cancellation at \(a=\alpha/2\) changes the reciprocal-time renormalization from logarithmically divergent to finite. The result does not purport to identify the maximal globally attracting region.

**Limitations.** The inequality \(a\leq\alpha d\) is sufficient and tied to monotonicity of a precise ratio-response function; stronger global parameter coverage is not proved. Neither delayed dynamics nor stochastic effects are addressed. Publication priority is provisional until wider independent literature scrutiny.

Self-review: passed. Independent audit: not yet performed.
