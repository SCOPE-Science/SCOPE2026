# Scientific review

## Correctness
**PASS.** The proof specifies the rational-base digit convention and relies on the published \((9,4)\) Toeplitz first-difference identity. Periodic approximants of period \(9^m\) leave an exceptional density at most \(|v|(4/9)^m\) for factor \(v\). Since \(4\) is invertible modulo \(9^m\), this bound remains valid on the source index progressions required by residue conditioning. Consequently the nine-residue recurrence is valid, strictly decreases word length above two, and yields exact rational answers. The conversion from marked boundaries to run indices includes the normalization \(F(1)=2/5\). The exact fraction checker verifies all 25 outputs, and independent direct base-digit construction agrees with the first 200,000 Toeplitz differences. Finite checks are not substituted for the infinite proof.

## Originality
**PASS under searched-source comparison, with residual priority uncertainty.** The closest source, Cassaigne–Espinoza–Rigo–Stipulanti, arXiv:2602.21895, provides the vital Toeplitz representation and one-letter frequencies, but its inspected theorem statements and surrounding discussion did not provide an all-order exact run-pattern formula or the evaluated adjacent-run matrix. Dekking, arXiv:2301.13563, studies the sibling base-digit convention and does not imply the stated matrix. Targeted mathematical-record searches for Toeplitz gap/run matrices, aliases, finite-frequency tables, and the exact template found no covering statement; unindexed equivalent calculations remain possible. The result is a new derived characterization, not a claim of discovery of the Toeplitz structure.

## Value
**PASS.** This solves a natural, complete infinite family of local observables: distributions of arbitrarily long blocks of maximal-run lengths. The concrete transition matrix identifies eight impossible ordered transitions, nonuniform exact marginals, and the mean run length. These capture structure beyond symbol frequencies, in a numeration-defined word whose frequency behavior motivated the source paper. The all-order recursive construction is meaningful despite being enabled by the prior Toeplitz representation, and does not assert an unrelated downstream theorem.

## Closest literature and risks
The primary mathematical assumption is Proposition 11 in arXiv:2602.21895. The adjacent matrix is a further finite deduction, and the all-order formula uses regularity and arithmetic-progression equidistribution. A previous unindexed computation, or a broad Toeplitz-frequency theorem implicitly subsuming the rationality component, may restrict priority; this does not amount to locating the exact claimed run statistics. Independent scientific review has not occurred.

Self-review: passed. Independent audit: not yet performed.
