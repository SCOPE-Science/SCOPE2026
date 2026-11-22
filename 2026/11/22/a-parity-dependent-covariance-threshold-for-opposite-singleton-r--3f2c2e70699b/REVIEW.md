# Scientific review

## Correctness — PASS
All claims use the stationary two-state chain with flip probability \(0<p<1\), linear observations, and \(n\ge3\). The proof supplies a complete lag-by-lag joint probability calculation, finite geometric-sum reduction, strict step-two identity, derivative-based uniqueness, monotone threshold ordering, and moving-boundary asymptotics. An separately implemented full weighted enumeration for lengths 3–12 at five exact rational probabilities agreed with the formula and mean; the checker completed 11,174 deterministic assertions including root-bisection tests. The finite checker is corroboration rather than an all-size proof. The analytic equalities and inequalities cover all integer lengths and real interior probabilities.

## Originality — PASS (provisional historical assessment)
The closest preexisting general work is Rukhin's Markov pattern-correlation matrix framework (2006/2007), which can recover pattern covariances but does not state the finite odd/even sign law or its threshold asymptotic in inspected sections. Mytalas–Zazanis (2013), whose author-posted text was examined, gives run-count central limit and asymptotic covariance formulas, principally for success runs, not the finite opposite-colour singleton classification. Exact fixed-composition binary-word studies address a different law. Research-record searches for the symmetric Markov \(010/101\) covariance, parity threshold, and asymptotic constant did not show a covering statement; this is not a proof of historical uniqueness. The irreducible novelty is the complete sign phase and critical scale, not standard covariance computation. Residual risks include a buried equivalent specialization in the general pattern literature and the limited material accessed from older Russian-language work.

## Value — PASS
Enclosed singleton runs are basic clustering and alternation diagnostics. Their opposite-colour covariance is a natural input to joint run tests; its strict dependence on sample-length parity is surprising, and the exact unique thresholds distinguish near-deterministic alternation from every fixed interior Markov regime. The monotone boundary and its sharp \(1/n\) scale are structural, not arbitrary small-parameter tables. They make the finite-sample sign usable without evaluating the full pattern-count distribution.

## Limits
The result does not claim a new general Markov pattern covariance method, a multivariate CLT, or claims for asymmetric transitions, nonstationary starts or circular words. No independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
