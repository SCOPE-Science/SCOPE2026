# Independent mathematical audit — SCOPE-20260930-7d41886b0b65
Audit date: 2026-10-01 (UTC) UTC.
Disposition: **failed**.

## Final claim
For the model companion \(T_3^*\) of the universal theory of groups of exponent dividing \(3\), the explicit bounded non-amalgamation theorem makes the model companion effectively axiomatizable; joint embedding makes it complete; hence its first-order theory is decidable.

## Correctness
Status: **PASS**.

The derivation is mathematically sound. The exponent-three source gives an explicit finite witness bound for non-amalgamation. Local finiteness and the explicit size of free exponent-three Burnside groups make the finite obstruction set and finite amalgamability decidable. Direct products give joint embedding of the universal class, and a model companion of a joint-embedding universal theory is complete. A complete computably enumerable theory is decidable by dovetailing proofs of a sentence and its negation.

## Originality
Status: **FAIL**.

Originality fails by implication. Burris, “Decidable Model Companions” (1989), Theorem 1.7 proves decidability from decidable universal theory plus the recursively bounded obstruction property, Lemma 2.2 proves decidability of the universal theory for locally finite finitely axiomatizable universal classes in a finite language, and Theorem 2.3 combines them: such a class has a decidable model companion exactly when its existentially closed class has a recursively bounded obstruction property. The 2026 exponent-three paper supplies precisely an explicit recursive bounded-obstruction theorem. Therefore the audited decidability conclusion is a direct specialization of Burris’s pre-existing general criterion even if the exact exponent-three application had not been written down.

### Equivalent formulations
- Search/source: Stanley Burris, Decidable Model Companions, Math. Logic Quarterly 35 (1989), 225-227, DOI:10.1002/malq.19890350305
- Search/source: Yawara Ishida, Ryosuke Mizuno, Kota Takeuchi, Existence of a Model Companion for Groups of Exponent 3, arXiv:2609.30061v1
- Evidence: Burris Theorem 2.3 states the general locally-finite criterion whose specialization is the audited conclusion.
- Reasoning: The exact group-specific wording is absent, but the theorem is covered by a general criterion plus the new source’s hypotheses.

### Broader coverage
- Search/source: Burris 1989, Theorem 2.3
- Search/source: Ishida-Mizuno-Takeuchi 2026, bounded obstruction theorem
- Evidence: The general theorem applies to locally finite finitely axiomatizable universal finite-language classes and is strictly broader than the exponent-three instance.
- Reasoning: This is decisive broader coverage.

### Exact database or table
- Search/source: Published-record semantic corpus
- Search/source: Targeted literature search for exponent-three model companion decidability and recursively bounded obstruction
- Evidence: No exact database row was needed because a broader primary theorem already determines the outcome.
- Reasoning: The exact-table check is inapplicable as a novelty rescue: implication by a published general theorem is sufficient for coverage.

### Claim versus prior implication
- Search/source: Burris 1989, Theorems 1.7 and 2.3
- Search/source: Ishida-Mizuno-Takeuchi 2026, Fact 2.6 and quantitative bounded-obstruction theorem
- Evidence: The 2026 source makes the obstruction bound recursive; Burris 1989 then yields decidability.
- Reasoning: The audited claim is mechanically implied by the conjunction of the source theorem and the older general decidability criterion, so originality fails.

### Source inspections
- **Decidable Model Companions** (DOI:10.1002/malq.19890350305): trigger — the package itself cites Burris as a general decidability precedent; material read — complete three-page article, including Theorem 1.7, Lemma 2.2, and Theorem 2.3; method — authorized institutional full-text inspection after open-access routes did not provide the article; assessment — DECISIVE_BROADER_COVERAGE; evidence — Theorem 2.3 says a locally finite finitely axiomatizable universal class in a finite language has a decidable model companion iff its existentially closed class has the recursively bounded obstruction property.
- **Existence of a Model Companion for Groups of Exponent 3** (arXiv:2609.30061v1): trigger — primary source of the new model-companion and bounded-obstruction theorem; material read — full accessible text around Fact 2.6 and the quantitative bounded-obstruction construction; method — lawful arXiv full-text inspection; assessment — SUPPLIES_HYPOTHESIS_OF_PRIOR_GENERAL_THEOREM; evidence — The source supplies an explicit finite witness bound for non-amalgamation in exponent-three groups, making the relevant obstruction bound recursive.

## Value
Status: **FAIL**.

Value fails under the stated bar once prior implication is taken seriously. After the 2026 source establishes an explicit recursive bounded obstruction for the locally finite finite-language exponent-three class, Burris’s Theorem 2.3 gives decidability directly. The remaining completeness and proof-enumeration observations are standard. The package is a correct and useful corollary, but not a distinct motivated research gap.

## Checked sources
- Yawara Ishida, Ryosuke Mizuno, Kota Takeuchi, Existence of a Model Companion for Groups of Exponent 3, arXiv:2609.30061v1.
- Stanley Burris, Decidable Model Companions, Math. Logic Quarterly 35 (1989), 225-227, DOI:10.1002/malq.19890350305.

## Residual risks
- No correctness defect was found; rejection is scientific coverage/value, not access or transport failure.

The audit distinguishes finite reproducibility checks from proofs of infinite statements and makes no claim beyond the final claim above.
