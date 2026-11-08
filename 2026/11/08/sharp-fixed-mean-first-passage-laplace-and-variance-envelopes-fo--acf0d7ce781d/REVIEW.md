# Scientific review: fixed-mean distributed Brownian resetting

## Correctness — PASS

The renewal equation is recomputed from a successful Brownian attempt and a competing independent exponential reset. The inversion of its first-passage transform, the mean and variance derivatives, and both strict convexity arguments are explicit in `RESULT.md`. Jensen and the chord inequality hold for *every* admissible probability law, making the continuum optimization exact rather than experimentally extrapolated. Equality cases and the distance-law uniqueness theorem follow by strict convexity and Laplace-transform uniqueness. The exact two-site witness is independently checked by substituting its weights into the mean and variance expressions. `verify.py` supplies deterministic numerical checks and is not used as an infinite proof. The proof assumes fixed known Brownian diffusivity and Poisson rate, equal initial/reset laws, and a positive compact distance interval for bounds.

## Originality — PASS, qualified

The closest source, Méndez–Flaquer-Galmés–Campos (arXiv:2401.01125v1, Sec. II.A and Eq. (16)), already derives the correct full averaged survival transform and Eq. (60) the unoptimized variance. Its prose erroneously promotes equality of a *single* value \(I(r)\) to equality of the entire function \(I(r+s)\); the present exact two-site example disproves the associated full-statistics claim without disputing their correct equations or mean-equivalent point construction. No fixed-mean sharp all-frequency envelope, global extremizer classification, or iff reset-distance identifiability is stated in the material inspected. Julián-Salgado–Dagdug–Boyer (arXiv:2311.11897v1) optimize reset rates for two locations rather than the unrestricted fixed-mean distribution; Toledo-Marín–Boyer (arXiv:2206.14387v1) treat mean first passage and information/entropy. Searches of public mathematical-research records of the source title, equivalence aliases, Poisson distributed-reset variance and fixed-mean transform bounds returned no record implying this precise result. A generic discrete memoryless-catastrophe variance envelope is a near conceptual analogue but does not cover the Brownian spatial all-frequency class; its full text was unavailable in these checks. These comparisons support a qualified original contribution, not a proof of global publication priority. An unindexed general convex-order theorem could subsume the bounds.

## Mathematical value — PASS

The literature explicitly treats a reset site with the same mean as physically statistically equivalent. The new result provides a strict counterexample with a computable nonzero variance gap, identifies the complete information erased by a single first-passage mean, and gives sharp error/envelope bounds across *all* temporal Laplace frequencies and variance at that same mean. The optimizers are physically natural: a precisely controlled single-distance reset versus a randomized two-endpoint protocol. This is an interpretation and experimentally relevant identifiability/variability boundary for the exact process, not an arbitrary finite parameter slice. No statistical estimation guarantees or stochastic-order implication are claimed.

## Residual limitations

Novelty remains conditional on accessible literature and research records. The precise result does not cover non-Poisson clocks, nonidentical initial distributions, or data of finite precision. The existing source's long-time approximate mean-universality statement is not contradicted as an asymptotic approximation; the distinction concerns exact full distributions and variance.

Self-review: passed. Independent audit: not yet performed.
