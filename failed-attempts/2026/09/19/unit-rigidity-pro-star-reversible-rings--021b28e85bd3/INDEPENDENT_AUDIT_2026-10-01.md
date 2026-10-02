# Independent mathematical audit — 2026-10-01

**Record:** SCOPE-20260919-021b28e85bd3 — Unit rigidity characterizes pro-star-reversible rings
**Disposition:** FAILED

## Final claim assessed

The record states the exact unit-group characterization of pro-\(*\)-reversibility and its local/clean/division consequences, but explicitly as an alternate proof of an earlier published theorem.

## Correctness — PASS

The alternate proof is mathematically correct. Pro-\(*\)-reversibility forces every unit to be self-adjoint by applying the projection condition to an inverse pair. Conversely, in a \(*\)-reversible ring with all units fixed, centrality of \(p=ab\), the lifted inverse unit in the \(p\)-corner, and the complementary zero-product argument give \(b^*a=p\). The listed consequences follow as in the earlier theorem.

## Originality — FAIL

The package itself records decisive prior coverage: the earlier same-day record unit-group-criterion-pro-star-reversibility--dcd6bac06405 was committed before this record and proves the exact same iff criterion and the stronger identity \(b^*a=p\), with the same clean/semiperfect/division consequences. The 2026-09-18 semiperfect-rigidity record is earlier still for unit rigidity and several class-specific corollaries. An alternate proof and consequence re-packaging do not create a distinct final mathematical claim.

## Scientific value — FAIL

As a separate research finding, the record does not fill a new mathematical gap: it is deliberately an alternate proof and expository consequence package for an already-published exact theorem. The proof may be pedagogically useful, but under the audit value standard that is not a new validated finding.

## Originality comparison details

### Equivalent formulations

The theorem statements coincide after notation normalization.

Searches:
- Resultary semantic search: pro-star-reversible rings unit group fixed by involution exact criterion star-reversible

Evidence:
- Resultary returns the earlier exact criterion and describes this record as a later alternate proof.

### Broader coverage

The earlier same-day result directly dominates the current final claim.

Searches:
- 2026/09/19/unit-group-criterion-pro-star-reversibility--dcd6bac06405 full RESULT.md
- 2026/09/18/pro-star-reversible-semiperfect-rigidity--8cd8850c47f1 full RESULT.md

Evidence:
- The earlier same-day record proves the full general equivalence, stronger identity, and principal consequences; the previous-day record already contains unit rigidity and semiperfect/local collapse.

### Exact database or table

The database evidence is corroborative; the decisive comparison is theorem implication and publication order.

Searches:
- Resultary query listed above

Evidence:
- The published index places the exact-criterion record before this later alternate-proof record and also returns the earlier semiperfect result.

### Claim versus prior implication

The current theorem is an exact covered restatement with an alternate proof.

Searches:
- direct theorem-by-theorem comparison of the two full RESULT.md files

Evidence:
- The earlier theorem is the same equivalence for every unital \(*\)-ring and includes \(b^*a=p\) plus clean/semiperfect/division consequences.

## Source inspections

### Unit groups exactly detect pro-star-reversibility

- Identifier: 2026/09/19/unit-group-criterion-pro-star-reversibility--dcd6bac06405
- Trigger: Direct exact prior claim
- Material read: Full RESULT.md
- Method: Read-only repository inspection at frozen commit
- Assessment: COVERING
- Evidence: States the same iff theorem, stronger identity, and overlapping consequences.

### Pro-star reversibility collapses on semiperfect rings

- Identifier: 2026/09/18/pro-star-reversible-semiperfect-rigidity--8cd8850c47f1
- Trigger: Earlier structural predecessor
- Material read: Full RESULT.md
- Method: Read-only repository inspection
- Assessment: PARTIAL_COVERAGE
- Evidence: Contains unit rigidity and local/semiperfect/domain consequences.

## Limitations and residual risks

- Scientific rejection is solely originality/value; the mathematics of the alternate proof is correct.
