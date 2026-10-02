# Independent audit — 2026-10-01

## Record

A two-point property spectrum for tense Grzegorczyk extensions

## Final claim

On Chen–Takahashi's single computable family \(L(c)\) of tense Grzegorczyk extensions, the seven properties tabularity, local tabularity, FMP, decidability, elementarity, canonicity, and Kripke completeness have vector \((1,1,1,1,1,1,1)\) exactly for reachable configurations and \((0,0,0,0,0,0,0)\) otherwise; consequently every fixed Boolean separator of those endpoints is undecidable on the promised family.

## Correctness

**PASS** — The source construction gives the two cases needed. For reachable configurations, Lemma 0.4.32 identifies \(L(c)\) with the fixed tabular logic, and the source's property corollary supplies all seven positive properties. For non-reachable configurations, Lemmas 0.4.34 and 0.4.35 give Kripke incompleteness and undecidability. The remaining listed properties each imply Kripke completeness in the source's Corollary 0.4.2 proof, so none can hold in the non-reachable case. A Boolean function that takes different values at the two endpoint vectors therefore decides reachability or its complement on this family.

Risk: No behavior on the other \(126\) Boolean vectors is needed because the construction never realizes them.

## Originality

**FAIL** — The Chen–Takahashi primary full text was inspected at the exact reduction lemmas and Theorem 0.4.1. Lemma 0.4.32 gives the reachable equality with the fixed logic; Lemmas 0.4.34–0.4.35 give simultaneous Kripke incompleteness and undecidability off the reachable set; and Theorem 0.4.1 explicitly uses this same single computable map for every property satisfying the endpoint hypotheses. Corollary 0.4.2 lists exactly the seven properties. Thus the two-point vector is just the joint reading of one published proof, and the Boolean-separator statement is a mechanical truth-table corollary of those same two endpoints. Resultary found no separate earlier SCOPE theorem, but direct implication from the primary source is decisive.

Risk: There is no access uncertainty: the relevant primary theorem and lemmas were read in full.

### Equivalent formulations

Those are precisely the two endpoint vectors after applying the source's property implications.

### Broader coverage

The source's parametrized theorem is broader than treating the seven coordinates one by one.

### Exact database or table

Database exactness cannot overcome direct primary-source implication.

### Claim versus prior implication

Taking all seven properties together and applying a Boolean separator is a mechanical corollary.

## Value

**FAIL** — Although recognizing the common reduction can be expositorily useful, the submitted contribution adds no new mathematical mechanism, boundary, or classification beyond the source proof. The synchronized vector and Boolean closure are immediate repackagings of the already published endpoint reduction, so they do not clear the value bar as an independent mathematical gap.

Risk: This does not diminish the value of the underlying Chen–Takahashi undecidability construction.

## Source inspections

- **Most properties are undecidable even in NExt Grz_t** (arXiv:2608.30816v1): Full primary HTML around Corollary 0.4.2, Lemmas 0.4.32, 0.4.34, 0.4.35, and Theorem 0.4.1 Assessment: COVERING. Evidence: The same computable family collapses reachable configurations to one fixed logic and makes non-reachable members both Kripke-incomplete and undecidable; Theorem 0.4.1 uses those endpoints for every property satisfying the listed implication condition, and Corollary 0.4.2 lists all seven properties.

## Residual risks

- No residual source-access risk affected the disposition.

## Disposition

Failed: the submitted claim does not survive all three axes and is preserved as a failed attempt.
