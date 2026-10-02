# Independent mathematical audit — 2026-10-01

## Final claim

A single Schur target is additively epsilon-isometrically universal for separable Banach spaces

## Correctness — PASS

PASS. The construction is valid. The gauge given by the maximum of the identity and square-root functions is nontrivial, so Kalton's theorem gives the Schur property for the associated Lipschitz-free space. Banach-Mazur embeds every separable real Banach space isometrically into C([0,1]). Scaling the canonical metric embedding gives the exact distance formula used in the record, hence additive error at most epsilon with equality on a pair at distance epsilon. The lower distance bound gives injectivity and a one-Lipschitz inverse. Godefroy-Kalton linearization then excludes exact metric embeddings of non-Schur domains into the Schur target.

## Originality — FAIL

FAIL. Sun and Zhang's full 2026 paper proves the same gauged Lipschitz-free construction for a fixed separable Banach domain and explicitly states Kalton's theorem for every pointed metric space. Their proof uses no Hilbert-specific ingredient in the approximate-isometry construction; the Hilbert choice is needed only for the non-Schur obstruction. Taking the domain in their construction to be the classical Banach-Mazur universal space C([0,1]), and then restricting the resulting maps to isometric copies of arbitrary separable Banach spaces, mechanically yields the audited fixed universal target. Thus the universal quantifier change is a direct corollary of the primary construction plus a classical theorem.

### equivalent_formulations

Searches: single Schur target additive epsilon-isometry all separable Banach spaces; universal target Lipschitz-free Schur epsilon-isometries

Evidence: The exact published-record search returned the audited record, while Sun-Zhang gives the fixed-domain construction with a theorem valid for arbitrary pointed metric spaces.

Reasoning: Replacing the fixed domain by a universal separable Banach host is equivalent to the audited universal-target formulation after restriction to subspaces.

### broader_coverage

Searches: Sun-Zhang 2026 full text; Kalton gauged Lipschitz-free Schur theorem; Banach-Mazur C([0,1]) universal theorem

Evidence: Sun-Zhang's Theorem 1.5 and proof give the exact additive distance formula; their Theorem 2.1 quotes Kalton for every pointed metric space; Banach-Mazur gives a common host for all separable Banach spaces.

Reasoning: Together these prior results directly cover the audited construction and its quantifiers.

### exact_database_or_table

Searches: published mathematical record semantic search for universal Schur additive epsilon target

Evidence: No older record with the exact headline was found.

Reasoning: The exact-title absence is immaterial because the theorem is mechanically implied by the inspected primary proof and classical universality.

### claim_vs_prior_implication

Searches: Sun-Zhang proof formula for exact epsilon-isometry; Banach-Mazur universal embedding theorem

Evidence: The Sun-Zhang construction works for any chosen separable metric/Banach domain once the universal Schur theorem is invoked; selecting C([0,1]) gives one target and Banach-Mazur supplies every separable Banach domain inside it.

Reasoning: No new nonstandard lemma is needed beyond composing and restricting the prior constructions.

## Scientific value — FAIL

FAIL. The statement is mathematically meaningful, but the claimed contribution is obtained by a direct substitution of a classical universal host into an already published construction and then restricting to its subspaces. Under the required value bar, that is a routine synthesis rather than a distinct motivated gap or structural theorem.

## Source inspections

- **Longfa Sun and Yipeng Zhang, epsilon-isometries without isometric embeddings** — https://arxiv.org/abs/2609.13937. Material read: Full five-page preprint, including Theorems 1.1, 1.5 and 2.1 and the complete construction/proof. Assessment: COVERING_BY_MECHANICAL_GENERALIZATION. Evidence: The exact distance formula and Schur construction are already proved, and the quoted Schur theorem applies to every pointed metric space; choosing a universal separable Banach host yields the audited target.
- **Robert H. Lohman, An Embedding Theorem for Separable Locally Convex Spaces** — https://doi.org/10.4153/CMB-1971-023-1. Material read: Theorem/bibliographic context for the classical isometric embedding of separable Banach spaces into C([0,1]). Assessment: CLASSICAL_COMPONENT_OF_COVERAGE. Evidence: This supplies the universal host needed to turn the Sun-Zhang construction into the audited fixed-target statement.

## Limitations and residual risks

The theorem is correct over the real scalars, but its universal-target conclusion is a direct synthesis of the 2026 fixed-pair construction with the classical Banach-Mazur universal embedding into C([0,1]). It therefore fails the originality criterion and, under the value standard used here, is too close to a substitution into an existing construction to qualify as a separate scientific finding.

- No correctness defect was found; the rejection is for originality and scientific value.
- The theorem is stated over real scalars, matching the classical host and linearization framework used.

## Disposition

**failed**
