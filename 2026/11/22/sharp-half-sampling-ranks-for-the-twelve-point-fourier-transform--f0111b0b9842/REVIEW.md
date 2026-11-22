# Scientific review: sharp half-sampling ranks for the twelve-point Fourier transform

## Correctness — PASS
For the finite abelian group statement, the normalized Fourier matrix is unitary, each restricted singular value is bounded by one, and its squared Frobenius norm is the ratio of the two support cardinalities to group order. Equality forces the two coordinate/Fourier projections to commute. Their off-diagonal block vanishes precisely when the Fourier transform of the column indicator is supported on the translation stabilizer of the row set, equivalently when the column set is periodic under the annihilator. The argument includes both directions, including rank integrality and zero-block necessity. At order twelve it forces the 76 disjoint parity/antipodal extremal pairs by subgroup-size divisibility.

The complete higher-rank census examines all 80-by-80 translation-orbit representative pairs over two distinct characteristic-zero-compatible finite-field reductions. Every minor of order at most six has fourth-degree cyclotomic absolute norm bounded by \(6^{12}=2{,}176{,}782{,}336\), whereas the two primes' product is \(1{,}001{,}050{,}033{,}561\). Thus simultaneous modular vanishing implies genuine complex vanishing. Independent C++17 and Python checks reproduce all 6,400 ranks, orbit weights, and histogram. Residual correctness risk is implementation error in both independent programs or a defect in the supplied algebraic proof; no independent audit was performed.

## Originality — PASS, with residual priority risk
Actual published-record searches for order-twelve six-by-six rank censuses, half-sampling Fourier failures, and subgroup-periodicity equality did not identify a covering result. Full texts of the closest existing published order-twelve fifth-order rank incidence, full-spark classification, and exact-support uncertainty findings were read and compared at the claim level. Their sampling sizes or invariants do not determine the six-by-six rank partition, all 76 extremal pairs, or the universal iff criterion.

The original Meshulam uncertainty paper supplies support bounds, Delvaux–Van Barel's rank-deficient Fourier-block work gives pertinent construction methods, and Bonami–Ghobber treat equality cases for support inequalities. These do not visibly state the complete theorem and census. A general Fourier-minor enumeration could contain unpublished or omitted refinements, and subgroup-block results could implicitly yield parts of the classification. Search failure is not proof of absolute historical priority.

## Value — PASS
Half-sampling a composite Fourier matrix is the natural boundary at which complete recovery often ceases to be automatic. Counting only zero determinants conceals how many independent directions disappear. Here the lowest possible rank is achieved in exactly 76 cases, and the full defect-depth distribution distinguishes rank-three, rank-four, and rank-five failures. The dual periodicity theorem explains the sharp boundary structurally for every finite abelian group, so this is not merely an incremental numerical census. The result does not give conditioning, general higher-rank distributions, or independent validation.

## Closest literature and limits
Meshulam, arXiv:math/0312407v1 (2003); Delvaux–Van Barel, KU Leuven Report TW477 (2006); Bonami–Ghobber, arXiv:1003.5060v1 (2010); complete fifth-order Fourier rank incidence at order 12 (2026-11-16); full-spark classification at order 12 and exact-support Fourier uncertainty profile at order 12 (2026-10-04). The aggregate vanishing-minor census in *A prime leaves no room for a comb* was considered; no dated, full six-frequency rank incidence claim was identified.

Self-review: passed. Independent audit: not yet performed.
