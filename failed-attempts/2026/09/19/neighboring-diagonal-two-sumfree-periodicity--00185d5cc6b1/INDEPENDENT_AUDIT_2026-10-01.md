# Independent mathematical audit — SCOPE-20260919-00185d5cc6b1

Final disposition: **FAILED**.

## Correctness
**PASS** — The modular proof is correct. The residue set R modulo 5f+1 is sumfree, while the prefix interval Q satisfies Q+R=R-complement; the explicit finite transition blocks then give a greedy induction for the whole tail. Reading the gaps yields the claimed periods and density, with f=3 and f=4 handled by their exceptional cyclic words.

## Originality
**FAIL** — A September 17 published theorem, inspected in full, already proves the identical closed set formula, modulus 5f+1, minimal preperiod f+1, and minimal period f+2 for every f at least five. The van Berkel-Bosma primary paper was also read completely: it explicitly works out f=3,g=7 and Theorems 16-17 certify the conjectured period/preperiod data throughout the finite range containing f=3,4. Thus the only nominal extension beyond the prior infinite theorem is a pair of small boundary cases whose periodic behavior was already formally certified in the source paper.

### Equivalent formulations
The assigned theorem is the union of an already-published infinite theorem and two previously certified small boundary instances.

### Broader coverage
Together these prior results dominate the scientifically meaningful content of the assigned statement.

### Exact database or table
This is positive coverage evidence, not novelty inferred from search failure.

### Claim versus prior implication
No substantial current claim escapes prior implication/coverage.

## Value
**FAIL** — After removing the already-covered infinite family, the surviving content is only repackaging two small certified cases into the same residue formula. That does not constitute a motivated new classification or structural boundary under the value standard.

## Source inspections
- **Exact periodicity of the strict greedy 2-sumfree family S_{f,2f+1}** (https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-periodicity-of-greedy-2-sumfree-s-f-2f-plus-1--211ee0999b72): complete RESULT.md Assessment: EXACT_PRIOR_COVERAGE_FOR_F_AT_LEAST_5. Evidence: Same modulus, block formula, preperiod, period, and proof mechanism.
- **Periodicity conjectures for all 2-sumfree sequences** (https://arxiv.org/abs/2609.18522): complete 15-page primary preprint Assessment: SOURCE_CERTIFIES_SMALL_BOUNDARY_CASES. Evidence: Theorem 16 certifies period and preperiod predictions for f,d<=250 and Theorem 17 certifies periods through 500; f=3,g=7 is also explicitly worked out.

## Residual risks
- No correctness defect was found; rejection is prior coverage and lack of surviving value.
