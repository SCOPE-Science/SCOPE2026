---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

Conjugate-linear isometric involutions on \(C^1[0,1]\) generate generalized bi-circular idempotents for arbitrary distinct unit phases and can be non-bicircular; pointwise conjugation gives an explicit non-antipodal counterexample to the dichotomy in arXiv:2609.18967v1, with corrected semilinear criteria for the mixed and conjugate forms.

## Correctness — PASS

For a conjugate-linear involution \(T\), expanding \(P_1=(T-\lambda_2I)/(\lambda_1-\lambda_2)\) while conjugating scalars shows \(P_1^2=P_1\); \(P_2=I-P_1\) is complementary and \(\lambda_1P_1+\lambda_2P_2=T\). For pointwise conjugation and phases \(1,i\), the projections reduce on \(u+iv\) to explicit real-linear lines, and the phase \(1,-1\) sends the constant \(i\) to \(2-i\), so it is not an isometry. The block calculation for Form IV gives \(T^2=I\) exactly when \(\phi^2=\mathrm{id}\) and \(eta(t)\overline{eta(\phi(t))}=1\). These computations are direct and independently reconstruct the counterexample.

**Sources.** current RESULT.md at archived record; arXiv:2609.18967 abstract; earlier published SCOPE RESULT dated 2026-09-17 at blob 55d84683dd506d89ae305329d1010fe66b4e5a2b

**Residual risks.** No correctness defect was found.

## Originality — FAIL

A published SCOPE record dated 2026-09-17, two days before this package, already proves pointwise-conjugation counterexamples on the same \(C^1[0,1]\) norm for every pair of distinct unit phases, explicitly treats Forms III and IV, proves non-bicircularity, and identifies the phase-squared correction in the other forms. The current record's abstract conjugate-involution lemma and more systematic block criteria are elementary repackagings/extensions of that already-published mechanism. This is decisive prior coverage independent of the unresolved 2019 corrigendum comparison.

### Equivalent formulations

The earlier result uses the same norm, objects, arbitrary phase pairs, and semilinear conjugation mechanism.

### Broader coverage

The older corrigendum is a residual coverage risk, but it is not needed because the 2026-09-17 published SCOPE theorem already covers the core claim.

### Exact database or table

This is direct database coverage, not merely a failed search.

### Claim versus prior implication

The current abstract lemma \(T^2=I\) is the immediate semilinear generalization of that mechanism and does not rescue originality of the final claim.

**Checked sources.** earlier SCOPE 2026-09-17 frozen RESULT.md; arXiv:2609.18967; Botelho--Miura 2019 corrigendum; published-result corpus search

**Residual risks.** The exact 2019 corrected proposition was not read, but that uncertainty cannot reverse the direct 2026-09-17 coverage.

## Value — FAIL

Correcting a false current dichotomy is worthwhile, but this package is not the first such correction in the published corpus: the same norm, arbitrary-phase conjugation family, non-bicircularity, and semilinear diagnosis were already present two days earlier. The additional abstract lemma is a short formal generalization and does not constitute a separate motivated gap under the value standard.

**Sources.** earlier SCOPE 2026-09-17 record; current source abstract

**Residual risks.** The blockwise exposition is useful, but duplicate/elementary refinement does not satisfy the scientific value bar.

## Limitations

- The claim concerns the source v1 statements as written.
- The 2019 Botelho--Miura corrigendum is additional older prior art whose full proposition remained inaccessible in this run.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
