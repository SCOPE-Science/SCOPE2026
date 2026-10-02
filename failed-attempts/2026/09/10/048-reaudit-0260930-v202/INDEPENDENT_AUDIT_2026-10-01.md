# Fresh audit — SCOPE-20260910-048

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For a nonzero homogeneous sextic \(F\) over an infinite characteristic-zero field, the apolar Artinian Gorenstein algebra has a general linear multiplication operator with largest Jordan block of length seven; hence a requested longest block of at most six is impossible.

## Correctness

**PASS** — The proof is the direct Macaulay-dual identity \(L^6\circ F=6!F(a)\). Since a nonzero sextic is nonzero on a nonempty Zariski-open set of points \(a\), a general linear form satisfies \(L^6\neq0\), while socle degree six gives \(L^7=0\). Thus the nilpotency index and largest Jordan block are exactly seven. The archived verifier source reproduces the identity on sample sextics, but the symbolic argument itself is decisive.

Residual risk: The statement requires characteristic not dividing \(6!\) and an infinite field; the package properly restricts to characteristic zero.

## Originality

**FAIL** — The claimed phenomenon is mechanically implied by the standard Macaulay-dual description of graded Artinian Gorenstein algebras and the general Jordan-type framework. Costa–Gondim explicitly develop Jordan type for graded Artinian Gorenstein algebras and exhibit the same top block of length socle-degree-plus-one in low socle degrees; the displayed sextic identity is the routine generalization. The record therefore does not isolate a new mathematical fact even if the exact sentence for degree six is not separately tabulated.

Residual risk: The exact degree-six wording was not located verbatim, but originality fails because the conclusion is a direct standard-theory consequence rather than because of title matching.

### Originality checks

**equivalent_formulations**

Searches: Resultary socle degree 6 apolar Jordan block 7; Jordan type graded Artinian Gorenstein general linear form.

Evidence: https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE048; B. Costa and R. Gondim, The Jordan type of graded Artinian Gorenstein algebras, https://arxiv.org/abs/1811.02072.

Reasoning: The exact degree-six phrasing is an instance of the standard top-degree Jordan-chain phenomenon in the general framework.

**broader_coverage**

Searches: general Jordan type of Artinian Gorenstein algebras; Macaulay duality socle degree top multiplication.

Evidence: https://arxiv.org/abs/1811.02072; N. Altafi, A. Iarrobino, P. Macías Marques, Jordan type of an Artinian algebra, a survey, https://arxiv.org/abs/2307.00957.

Reasoning: General theory covers arbitrary socle degree and multiplication by a linear form; the degree-six case is obtained by evaluating the top power against the dual generator.

**exact_database_or_table**

Searches: Resultary exact degree-six query; Costa–Gondim low-socle Jordan tables.

Evidence: Low-socle tables exhibit the top block with length socle-degree-plus-one; no separate degree-six table is needed for implication..

Reasoning: Absence of a row with the exact number seven does not establish novelty when a stronger general mechanism implies it.

**claim_vs_prior_implication**

Searches: Macaulay dual top multiplication and Jordan type literature.

Evidence: For a dual generator of degree \(d\), \(L^d\circ F=d!F(a)\), so a general \(L\) has nilpotency index \(d+1\)..

Reasoning: The prior framework plus the standard apolar action directly implies the final claim, so the record is covered as a special case.

### Source inspections

- **Assigned RESULT.md** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/048/RESULT.md. Trigger: Exact claim/proof. Material read: Full Macaulay-dual identity and limitations. Method: direct file inspection. Assessment: SUPPORTS_CORRECTNESS. Evidence: The identity proves the stated impossibility in characteristic zero.
- **verify_disproof.py** — https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/10/048/artifacts/verify_disproof.py. Trigger: Corroborating computation. Material read: Full source, including conjugate partition and test sextics. Method: direct source inspection. Assessment: SUPPORTS_CORRECTNESS. Evidence: The computation corroborates, but is not needed for the general proof.
- **The Jordan type of graded Artinian Gorenstein algebras** — https://arxiv.org/abs/1811.02072. Trigger: Highly relevant same invariant/framework. Material read: General framework and low-socle Jordan-type results, including the top block of length socle-degree-plus-one. Method: primary full-text inspection. Assessment: COVERS_BY_GENERAL_MECHANISM. Evidence: The degree-six statement is a routine instance of the standard top-degree chain.
- **Jordan type of an Artinian algebra, a survey** — https://arxiv.org/abs/2307.00957. Trigger: Broader survey of same invariant. Material read: Definitions and generic Jordan-type/multiplication-map framework. Method: primary full-text inspection. Assessment: BROADER_COVERAGE. Evidence: Confirms this is standard Jordan-type structure rather than an isolated new invariant.

## Value

**FAIL** — Once Macaulay duality is fixed, the proof is a one-line top-degree evaluation and nilpotency observation. It corrects an impossible target clause but does not yield a motivated new boundary, structural lemma, or independent exact invariant beyond a routine consequence of the definitions.

Residual risk: The correction can still be useful diagnostically, but diagnostic usefulness is below the shared mathematical-value threshold for a validated finding.

## Overall disposition

**FAILED**
