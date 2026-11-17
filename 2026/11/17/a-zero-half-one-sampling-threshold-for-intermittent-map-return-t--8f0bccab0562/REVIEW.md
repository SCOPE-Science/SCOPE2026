# Self-review

**Correctness — PASS.** The exact first-return law follows from the source's right-branch linearization and inverse iterates. Coupling to a power of a shifted exponential variable is exact. The mean-scale asymptotic, gamma tilted law and CLT, truncation variance, and three-part critical decomposition prove the stated convergence for all fixed sampling exponents. `verify.py` numerically tests identities and finite analytic bounds, not an infinite proof.

**Originality — PASS (with priority risk).** Li (arXiv:2611.06416v1) treats macroscopic return-time spectra along individual orbits, not independently restarted return-mean estimation at the parameter/sample-size double limit. The shifted-exponential law is deducible from its inverse branches and is explicitly credited; the three-regime empirical convergence requires additional rare-event and gamma asymptotics. Published-record comparisons include general thin-tail near-maxima and small-Weibull-shape results. A more general unindexed triangular-array theorem might imply the result.

**Mathematical value — PASS.** First-return means are natural recurrence invariants, but severe intermittency makes naive independent-seed estimation unreliable. Identifying exactly how exponentially growing sample counts restore consistency, including the one-half boundary, provides a concrete, parameter-uniform threshold rather than merely a finite example.

Limitations: independence of sampled initial seeds, no claim for successive returns in one orbit; fixed sampling exponent, and no independent certification. The closest original literature and the uninspected Pakes full text are described in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
