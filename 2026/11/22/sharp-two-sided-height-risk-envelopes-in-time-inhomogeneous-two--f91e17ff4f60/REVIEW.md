# Self-review

## Correctness — PASS

The precise claim is the equality between all marginal height laws under deterministic independent time-varying nearest-or-penultimate attachment schedules and all shifted sums of exactly \(r=\lfloor n/2\rfloor\) independent Bernoulli variables, followed by the sharp two-sided convex-order and variance envelope at each feasible mean. The proof first derives \(H_n=D_n\) and the exact depth generating-polynomial recurrence; the reversed recurrence is the continuant of a real symmetric weighted path matrix. Spectral \(\pm\beta\) pairing gives the negative-root factorization, including a compactness argument for boundary probabilities. A deterministic odd/even attachment schedule realizes **every** Bernoulli factor vector, establishing the converse rather than merely a bound. Direct discrete convexity and pairwise equalization prove both envelope directions, with schedules achieving both endpoints and continuous interpolation attaining every intermediate variance.

The included exact-rational checker independently enumerated finite attachment histories and returned `PASSED 67354 exact assertions`; no finite enumeration is offered as an infinite proof. The spectral and convexity arguments establish the universal quantifiers, including zero/one attachment probabilities. The claimed independent summands represent the **law**, not the actual temporal increments.

## Originality — PASS under inspected evidence

Tang, Wang and Wu (2026, arXiv:2607.02916) study topological ends, trunk/branches and walk collisions in the homogeneous parent-choice model; their inspected main theorems and Sections 1–3 do not classify finite-horizon height laws under arbitrary deterministic temporal inhomogeneity. A related published fixed-parameter height/leaf Gaussian limit and a fixed-parameter Brownian distance-field limit were compared in their complete scientific manuscripts: neither states the finite distributional attainable-family converse or fixed-mean two-sided envelope. Dekking and Kong (arXiv:1102.3613, Proposition 4.2) give negative-real-rooted generating functions for homogeneous antipersistent Markov occupation sums, which can cover the *homogeneous* height law by an equivalent increment chain; that coverage is acknowledged and excluded from the novelty claim. Wagner's weighted matching-polynomial theory (arXiv:0803.1659) provides the underlying root-location tool, and the classical Hoeffding theorem as reviewed by Tang and Tang (arXiv:1908.10024, Theorem 2.1) gives the upper convex bound once an independent-Bernoulli representation is available. Their general theorems are not presented as new. The newly compared implication is the exact characterization **of this tree model's attainable laws, in both directions**, including explicit realizability of the lower and upper risk bounds with constrained mean.

No indexed or directly inspected relevant manuscript was identified that states or logically implies that full model-specific classification without first establishing the special attachment-to-path-polynomial correspondence and converse construction. More general, unindexed results may subsume it; independent priority assessment remains outstanding.

## Value — PASS

The full family of finite-horizon height distributions is a natural complete invariant of independently controlled two-predecessor growth. It answers a non-asymptotic design question: at a prescribed expected height, the worst and best possible convex height risks, including variance, are **both feasible**, not merely abstract bounds. The result quantifies exactly which apparent dependence from temporally variable attachments can be replicated by independent Bernoulli increments, and supplies constructive schedules realizing all such laws. This is more informative than a single scalar moment, an arbitrary finite example, or a special case of a stationary Gaussian limit.

## Limitations and closest literature

No adaptive policy, longer memory, joint observable or finite-sample tail-pointwise domination is claimed. Closest texts are arXiv:2607.02916 (the model), arXiv:1102.3613 (homogeneous Markov occupation real zeros), arXiv:0803.1659 (matching-polynomial root theory), and arXiv:1908.10024 (the classical binomial convex-order inequality). Historical uniqueness is not proved and the independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
