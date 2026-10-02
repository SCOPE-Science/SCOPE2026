# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260911-084`

## Correctness — PASS

The direct proof is correct. Each prime event has measure 4/(p+1); the prime sum diverges. Fourier support restricts pairwise common frequencies for distinct primes to the relation pk=qj, and the stated coefficient bounds give a summable double-overlap error. Consequently the Chung-Erdos lower bound for every tail tends to one, so the prime limsup has full measure. The committed verifier correctly checks finite ledger values and the conservative summable-error constant, while the measure-one conclusion is analytic rather than finite.

## Originality — FAIL

Allen, Hauke-Treuer and Ramírez proved in May 2026 the full inhomogeneous Khintchine theorem in dimension two for every fixed shift and every function psi:N->[0,infinity), with no monotonicity assumption. Setting psi(q) equal to the inverse square root of q+1 on primes q>=1000 and psi(q)=0 on composites gives exactly the audited prime-denominator limsup, and the divergence of the prime reciprocal sum triggers their measure-one case. The audited theorem is therefore a direct special case of stronger prior work.

### equivalent_formulations

Searches: Resultary: prime denominator simultaneous approximation the two-dimensional torus shift full measure psi(q) equal to the inverse square root of q+1 Chung Erdos Fourier overlap; inhomogeneous Khintchine dimension two arbitrary psi prime-supported

Evidence: Resultary's exact hit was the audited record, but the primary-literature search found arXiv:2605.19582, which is broader and predates it.

Reasoning: The audited prime restriction is exactly represented by an arbitrary approximation function supported only on primes.

### broader_coverage

Searches: Allen-Hauke-Treuer-Ramírez, The inhomogeneous Khintchine Theorem in dimension two, arXiv:2605.19582

Evidence: Theorem 1.1 covers every psi:N->[0,infinity) and every gamma in the real plane, with full measure iff sum the square of psi(q) diverges.

Reasoning: This strictly dominates the fixed shift and prime-supported psi in the audited record.

### exact_database_or_table

Searches: prime-denominator exact table/database

Evidence: Inapplicable: the decisive prior coverage is a general measure theorem, not a finite table.

Reasoning: No database comparison is needed once a stronger theorem directly implies the claim.

### claim_vs_prior_implication

Searches: Theorem 1.1 of arXiv:2605.19582 applied to a prime-supported psi

Evidence: Define psi-star(q) equal to the inverse square root of q+1 for primes q>=1000 and 0 otherwise. Then the corresponding limsup set is the audited limsup and the series of squared psi-star values=sum_p 1/(p+1)=infinity.

Reasoning: The prior theorem yields measure one immediately, so the audited final claim is a corollary.

### source_inspections

- **The inhomogeneous Khintchine Theorem in dimension two** — https://arxiv.org/html/2605.19582v1. Trigger: Same dimension, inhomogeneous shift, arbitrary nonmonotone approximation function. Material read: Full accessible arXiv HTML introduction and Theorem 1.1, including definition of the inhomogeneous approximable set. Method: Primary-source full-text inspection. Assessment: DECISIVE COVERAGE: the audited prime-supported statement is a direct specialization. Evidence: Theorem 1.1 states measure one for any fixed gamma when the series of squared psi values diverges, with no monotonicity requirement.
- **Assigned prime-ubiquity verifier** — 2026/09/11/084/artifacts/verify_prime_ubiquity.py. Trigger: Correctness of the record's independent Fourier/Chung-Erdos proof. Material read: Complete source file. Method: Line-by-line package inspection and algebraic check of the overlap bound. Assessment: Supports correctness but cannot restore originality. Evidence: The code checks the prime mass ledger, Fourier coefficient bounds, summable tail constant and Chung-Erdos ratio.

### checked_sources

- Resultary exact-object search
- Allen-Hauke-Treuer-Ramírez arXiv:2605.19582v1
- assigned verify_prime_ubiquity.py

### residual_risks

- None material to the coverage decision: the stronger theorem was submitted on 2026-05-19, before the audited record.

## Scientific value — FAIL

The fixed shift and prime-supported approximation function are mathematically natural, but the exact measure-one conclusion is now mechanically implied by a stronger prior theorem that allows arbitrary shifts and arbitrary nonmonotone functions. A second proof with an explicit overlap constant is useful exposition, not a new exact invariant or boundary under the required value bar.

## Limitations

- Scientific rejection is originality/value based, not correctness based.
- The audited elementary proof remains a valid alternative derivation.
- RESULT names output/artifacts/verify_prime_ubiquity.py, while the actual audited file is artifacts/verify_prime_ubiquity.py.

## Disposition

**FAILED — not a validated finding.**
