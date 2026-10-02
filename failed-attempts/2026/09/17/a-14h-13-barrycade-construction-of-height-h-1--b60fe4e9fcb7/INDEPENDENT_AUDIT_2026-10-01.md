# Independent mathematical audit — SCOPE-20260917-015

Audit date: 2026-10-01 (UTC) UTC.
Disposition: **failed**.

## Correctness
**PASS** — The three-skip lemma was checked algebraically: for k<i only three of the nine new/old joint equalities can have d>x_k, yielding x_{h-1}<=6h-7 and L<=14h-13. A fresh implementation constructed the rows exactly from the proof and, for every h=2,...,14, verified that all surviving rows are permutations of [14h-13] and all proper-prefix-sum sets are pairwise disjoint. These finite checks corroborate, rather than replace, the all-h proof.

## Originality
**FAIL** — A later primary preprint, Binięda--Dębski--Gutowski--Milewski, 'How to Construct High Barrycades' (arXiv:2609.24373, 21 September 2026), states a construction for every height r>=1 of order 2r+3. Substituting r=h-1 gives order 2h+1, which is strictly smaller than 14h-13 for every h>=2 and therefore strictly dominates the final existence/asymptotic claim.

### Equivalent formulations
The terminology and object are identical, so the implication comparison requires no reduction beyond renaming the height variable.

### Broader coverage
Putting r=h-1 in the later theorem yields 2h+1, strictly better than 14h-13 for all h>=2.

### Exact database or table check
No finite database comparison is needed because a stronger universal theorem decisively covers the claim.

### Claim versus prior implication
The final claim is a strict corollary of later stronger coverage, so originality fails regardless of independent correctness.

## Value
**FAIL** — Although the three-skip observation is mathematically sound, the final claim being assessed is now a much weaker all-height construction than a published later construction on the identical object. As filed, it no longer closes a meaningful current gap or supplies a competitive boundary.

## Source inspections
- **How to Construct High Barrycades** (https://arxiv.org/abs/2609.24373): STRONGER COVERAGE. Primary arXiv abstract and theorem-level statement in the bibliographic record. For every height r>=1 the paper states a Barrycade of order 2r+3.
- **Finite and infinite barrycades** (https://arxiv.org/abs/2609.18476): PARENT SOURCE. The source relationship and public construction scale described in the package were compared with the later stronger theorem. Provides the earlier explicit framework that the audited three-skip argument improves, but is superseded by the later 2r+3 result.

## Residual risks
- Only the later paper's primary arXiv abstract/theorem statement was available through the current retrieval path, but that statement is already logically decisive because it explicitly gives the stronger all-height order.
- The failed disposition is due to later coverage/value, not a detected correctness defect in the 14h-13 construction.

The accompanying JSON file records the four structured originality checks, source inspections, checked sources, and residual risks.
