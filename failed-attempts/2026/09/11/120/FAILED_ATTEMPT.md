# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Triviality of the 2x2 interchanger holonomy loop in Gray-categories
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1012
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Higher Category Theory
- **Method:** polygraph rewriting with critical-pair coherence analysis and string-diagram normalization

## Problem

Decide triviality of the 2x2 interchanger loop in Gray-categories. In the free Gray-category on four generating 2-cells forming a compatible 2x2 grid, let L be the cyclic composite of four whiskered interchangers and inverses around the grid. Determine with a logged ledger whether L equals the identity 3-cell or exhibit an explicit Gray-category witness with nontrivial holonomy.

## Attempted claim

In the free Gray-category on a compatible 2x2 grid of distinct generating 2-cells, the cyclic four-interchanger loop composite L equals the identity 3-cell on the common composite 2-cell pasting.

## Research outcome

Proved the 2x2 interchanger holonomy loop trivial: explicit grid, disjoint-peak lemma, logged contraction L=id, machine-checked VERIFY_OK.

## Why this attempt failed

Failed axes: originality, value.

originality: ADMISSION_DEFECT: admission audit_preflight decisive_checks claimed no covering theorem and no equivalent formulation, but the headline L=id is a direct mechanical instance of the textbook strict 2-category interchange/Godement law in the hom 2-category G(P,R). nLab strict 2-category states (beta' o beta)(alpha' o alpha)=(beta' alpha') o (beta alpha) from functoriality of comp. Instantiating with Phi=id_V0, Phi'=beta, Psi=alpha, Psi'=id_U1 yields the disjoint-peak lemma verbatim, and the loop cancellation is then pure invertibility. No prior source states the 2x2 loop verbatim, but STANDARD fails mechanically-implied claims even without verbatim restatement. Hence the finite cyclic implication is not new beyond axioms. Fused live search found only general interchange/coherence context and no exact 2x2 ledger, confirming the only covering prior is the stronger textbook interchange law itself. value: ADMISSION_DEFECT: admission triviality_preflight claimed no single axiom contracts the loop and real cyclic confluence work is needed, but the submitted proof contracts it with one textbook axiom (strict middle-four) plus invertibility in a few lines, i.e. a textbook exercise unfolding the definition of hom 2-category. Per STANDARD reject textbook restatements and mechanically-implied results even if correct and new verbatim. The narrow-invariant rescue does not apply because that clause requires the value not be mechanically implied, whereas here it is. Neither a reusable cycle lemma beyond interchange nor a holonomy obstruction is contributed; downstream engines learn only that disjoint 3-cells commute, already in every 2-category text.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Proved for the canonical minimal disjoint-segment 2x2 commutator loop with fixed interchanger orientations; does not cover larger grids, overlapping non-disjoint interchanger peaks, alternative chirality conventions beyond the fixed one, or weak tricategories prior to Gray strictification. The verifier is a term-level replay of the equational proof, not an independent search of the free model.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
