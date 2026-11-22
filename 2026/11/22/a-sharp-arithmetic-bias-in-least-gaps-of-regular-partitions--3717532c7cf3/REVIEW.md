# Scientific review: arithmetic bias in least regular-partition gaps

## Correctness — PASS

The exact shifted-count identity follows by removing \(r\) mandatory copies of every smaller eligible part. Its quadratic-plus-residue expression is checked algebraically. The regular-partition Rademacher expansion supplies a coefficient asymptotic with a controlled \(N^{-1/2}\) correction and an \(O(N^{-1})\) remainder; this precision is essential for the second-order quotient. Taylor subtraction at \(m\) and \(m-1\) gives the signed \(\ell-2s\) coefficient. A growing \(n^{1/4}\sqrt{\log n}\) cutoff and shifted Euler--Maclaurin summation make the class-probability expansion rigorous. The exact verifier checks 7,851 enumeration identities and 30 finite-scale asymptotic comparisons. Finite checks do not establish the limits.

## Originality — PASS, with residual risk

Priya--Bhowmick--Meher, arXiv:2611.07871v1, Proposition 2.2 and the published joint least-gap study already imply the exact single-gap law and leading Rayleigh limit. These are explicitly treated as prior results. Agarwal--Garg--Maji, arXiv:2511.05907v1, supply the underlying exact partition coefficients. The evaluated contribution is neither of those individual inputs but the **sharp, class-dependent \(n^{-1/4}\) bias and strict eventual ordering** for every fixed \(\ell\ge3\). Inspected relevant sources did not state it; the cited older exact formulas could support an implicit earlier derivation, which remains the main priority risk. Searches did not certify uniqueness.

## Mathematical value — PASS

The probability of the first multiplicity deficiency in a regular partition has an arithmetic bias not visible at the Rayleigh scale: a complete, explicit descending hierarchy across allowed residue classes. The result supplies exact first-order separation, establishes a sign change of the local correction at the middle residue, and turns weak equidistribution into a quantitative prediction for every fixed modulus and multiplicity threshold. The phenomenon is a natural refinement of a recently studied partition invariant, rather than an arbitrary numerical slice. Its analytic ingredients are classical; the value is the sharp newly identified bias, not a new general asymptotic method.

## Closest literature and limits

The nearest published statement is *Joint least-multiplicity-gap laws for regular partitions* (November 2026), which gives exact joint survivors and the Rayleigh limit, but does not resolve nonleading residue-class asymmetry. The main motivating source is Priya--Bhowmick--Meher (2026-11-05). The Rademacher exact formula of Agarwal--Garg--Maji (2025) is a critical classical-style input. Unindexed or implicitly equivalent derivations, and earlier smallest-gap literature, remain residual priority risks. Parameters are fixed; no finite threshold for ordering is asserted.

Self-review: passed. Independent audit: not yet performed.
