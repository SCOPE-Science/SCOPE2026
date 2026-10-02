---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For a nontrivial normal p-subgroup P of G, the subgroup-fixed group algebra is local exactly when the centralizer of P is a p-group; in that local regime self-injectivity, Frobenius, and symmetry occur exactly when P is central, with a square-zero extension description under fixed-point-free outside action.

## Correctness — PASS

For normal P, non-singleton conjugation orbit sums span the Brauer kernel and the published normal-subgroup result makes that kernel nilpotent. Hence the semisimple quotient agrees with the centralizer group algebra, giving locality exactly for a p-group centralizer. In the local noncentral case, the full group sum and a nonzero socle submodule of the Brauer kernel provide independent socle contributions, excluding self-injectivity; the central case is a symmetric group algebra. Under fixed-point-free outside action, the nontrivial orbit sums are coset sums whose products vanish in characteristic p, giving the square-zero extension.

**Checked sources.** Assigned RESULT.md at tree 13d2662bbedb0878fc850fb82b2878b72b2dcb5f; Danz--Ellers--Murray 2013 full primary PDF; Allan 2011 full arXiv text

**Residual risks.** No correctness defect was found.

## Originality — FAIL

The load-bearing mechanisms are already published and the claimed classification is a routine combination of them. Danz--Ellers--Murray give the normal-p-subgroup Brauer quotient with nilpotent kernel. Allan proves non-self-injectivity for noncentral subgroup-fixed algebras in p-group algebras by the same two-dimensional-socle mechanism. Once the quotient makes the present algebra local, that socle argument transfers directly; the fixed-point-free square-zero formula is an elementary coset-orbit multiplication.

### Equivalent formulations

The locality and self-injectivity criteria are direct structural consequences of those published ingredients.

### Broader coverage

Allowing arbitrary ambient G adds no new nonstandard lemma once locality and the Brauer kernel are known.

### Exact database or table

Lack of identical wording does not establish novelty when prior implications are direct.

### Claim versus prior implication

These facts mechanically produce the classification. Under fixed-point-free action, orbit sums are coset sums and their products are multiples of the p-group order, so the extension formula is also routine.

**Checked sources.** https://doi.org/10.1017/S0013091512000077; https://arxiv.org/abs/1011.3559; published corpus search

**Residual risks.** The rejection is based on implication-level coverage, not failure to find identical wording.

## Value — FAIL

The packaged criterion is tidy, but after the published Brauer-kernel and socle results are combined, the remaining steps are standard radical/locality deductions and elementary orbit-sum multiplication. That is too routine for a separate mathematical gap.

**Checked sources.** Danz--Ellers--Murray 2013; Allan 2011

**Residual risks.** The result may remain useful as exposition.

## Limitations

- Normality of P is essential for the Brauer-kernel input.
- The self-injectivity classification is only asserted in the local regime.
- The square-zero description assumes fixed-point-free outside action.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
