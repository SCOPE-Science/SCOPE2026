# Independent mathematical audit — SCOPE-20260920-0347171537ea

Final disposition: **FAILED**.

## Correctness
**PASS** — Generalized Dixmier averaging sends every closed ideal into itself under the center-valued trace, so the trace descends. Central quotient classes lift centrally modulo the ideal by the same averaging argument. For a descended-trace-zero class, subtracting the center-valued trace gives a trace-zero lift and the uniform parent-algebra theorem makes that lift one commutator. The converse, exact distance, trace-factorization, general 2K estimate, and the reduced-product K estimate then follow.

## Originality
**FAIL** — The arbitrary-quotient theorem is mechanically implied by the uniform trace-zero commutator theorem plus classical Dixmier averaging and center lifting. Moreover, a September 18 published result already gives the exact single-commutator kernel, distance and quotient structure, and universal K bound for norm reduced products, so the package's reduced-product and matrix-corona portion is direct prior coverage. The remaining arbitrary-ideal step is a short quotient lift.

### Equivalent formulations
The arbitrary quotient statement is the same kernel theorem after classical trace descent and lifting.

### Broader coverage
The prior ingredients jointly dominate the final claim.

### Exact database or table
Positive partial coverage plus direct implication for arbitrary ideals is decisive.

### Claim versus prior implication
The main theorem is a routine quotient corollary of the prior results.

## Value
**FAIL** — The quotient formulation is useful, but after the parent-algebra theorem the proof is a direct subtract-the-central-trace lift combined with classical averaging; the most distinctive reduced-product consequences were already published earlier. No nonroutine scientific remainder survives.

## Source inspections
- **Single commutators and trace rigidity in norm reduced products of finite von Neumann algebras** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-single-commutators-trace-rigidity-norm-reduced-products--66c3e3c26339): complete published RESULT.md Method: published-record full-text inspection. Assessment: EXACT_PRIOR_COVERAGE_OF_REDUCED_PRODUCT_PART. Evidence: Proves the exact single-commutator kernel, closed-linear quotient, trace rigidity, and universal K bound for norm reduced products.
- **A uniform commutator bound in finite von Neumann algebras** (https://arxiv.org/abs/2609.16932): primary abstract and theorem statement; direct full-text opening was unavailable in this run Method: primary record inspection. Assessment: STRONGER_PARENT_ALGEBRA_INPUT. Evidence: States that every center-valued-trace-zero element is one commutator with a universal norm-product bound.

## Checked sources
- https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-single-commutators-trace-rigidity-norm-reduced-products--66c3e3c26339
- https://arxiv.org/abs/2609.16932

## Residual risks
- No correctness defect is asserted; rejection is implication-based coverage and routine value.
- The parent theorem's full text was not accessible through the web route used, but the rejection relies on its explicit theorem statement plus the complete prior reduced-product result.
