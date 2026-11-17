# Self-review

## Correctness — PASS
A full proof is in RESULT.md. The finite reducing Jacobi paths are derived from the two tensor factors, without assuming norm convergence. Even total degrees yield constant edges \(ab/2\). Odd degrees yield the bidiagonal singular-value matrix \(A I+B L\), \(A=a^2/2\), \(B=b^2/2\). The difficult case \(A<B\) is resolved by interlacing: all but at most the smallest singular value are at least \(B-A\), and the smallest is at most \(A<ab\). Bulk Weyl vectors with disjoint reflected supports prove every proposed spectral interval occurs in each parity sector and in its Fredholm essential spectrum. A nilpotent strictness argument excludes norm attainment. Positive weights, endpoint overlap, equal weights, and the gap threshold are covered. The numerical checker tests 20,804 finite matrix assertions but is not used as an infinite-dimensional proof.

## Originality — PASS, qualified
Garcia–O'Loughlin–Yu solve the uniform-weight case (2023). Tian–Wang–Zhu analyze convergent-weight norms (2025). Yang–Zhang supply a general finite-degree algorithm for point eigenvalues (2025), and this finite decomposition is **not new**. The explicit full **and essential** spectrum of permanently alternating positive weights, its three-band threshold, and nonattained sharp norm are not stated in the inspected primary texts and are not implied by the indexed one-spike result. Searches compare mathematical hypotheses and consequences, not titles alone. Earlier unindexed periodic special cases remain a real bibliographic risk.

## Mathematical value — PASS
The problem is motivated by the published weighted-shift tensor spectral question. It gives an exact, natural two-parameter nonconvergent classification with a sharp topology change from one to three spectral bands at \(1+\sqrt2\). It also quantifies the strict norm loss relative to \(\|S\|^2\) and proves both symmetry sectors share the full Fredholm essential spectrum. This is more than restating a finite characteristic polynomial or making a routine scalar substitution; the proof requires a uniform finite-block exclusion and reflection-symmetric bulk Weyl sequence construction.

## Risks and limits
An older periodic Jacobi/tensor spectral result not found by the searches may contain an equivalent special case. The comparison with the one-spike published record used its indexed summary rather than its full text. The only new claim is the stated two-factor period-two full and essential spectral classification, not the known finite-block algorithm. Independently sourced mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
