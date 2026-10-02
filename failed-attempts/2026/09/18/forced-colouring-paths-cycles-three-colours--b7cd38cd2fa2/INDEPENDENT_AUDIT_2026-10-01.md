---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For three colours, the forced-colouring functions of every path and cycle have the displayed closed coefficient formulas obtained from independent sets of tight vertices; together with the two-colour and high-colour regimes this determines the forced-colouring function of every path and cycle.

## Correctness — PASS

The forcing characterization was reconstructed: on a path or cycle an initially uncoloured vertex can be forced with three colours only when both neighbours are already coloured distinctly, so the omitted set must be independent (and avoids path endpoints); conversely an independent set of tight vertices is forced immediately. Encoding a proper 3-colouring by ±1 increments over Z_3 yields the path count by j disjoint equality constraints. On a cycle, replacing each constrained adjacent sign pair by its effective sign leaves a length n-j sign sequence with sum zero mod 3, counted by the roots-of-unity filter as (2^{n-j}+2(-1)^{n-j})/3 before the initial-colour factor. The inspected brute-force script independently matches all coefficients through n=8.

**Checked sources.** Assigned RESULT.md at tree 68bc3da3b2c39a228ee6507152782edda0d1861d; artifacts/verify.py blob 2ab40427e9df30a742767bf15e315961182a6a52; published maximum-degree-two record dated 2026-09-17; G. E. Farr, arXiv:2609.17108

**Residual risks.** No correctness defect was found; the rejection is prior coverage.

## Originality — FAIL

A published record dated 2026-09-17 states exactly the same path and cycle formulas, with the same weighted-Fibonacci path recurrence and cycle coefficient, and strengthens them to every graph of maximum degree at most two by multiplicativity. That record predates this 2026-09-18 package, so the audited claim is directly covered.

### Equivalent formulations

The prior record is not merely equivalent under an alias; it literally states the same mathematical formulas and a stronger family conclusion.

### Broader coverage

This is decisive stronger coverage.

### Exact database or table

The relevant exact-database check is the published-result corpus itself; it contains the exact theorem.

### Claim versus prior implication

The assigned final claim is an immediate special case of the earlier theorem.

**Checked sources.** published maximum-degree-two record dated 2026-09-17; https://arxiv.org/abs/2609.17108

**Residual risks.** No residual risk can reverse the direct prior-coverage finding.

## Value — FAIL

The formulas are mathematically natural and correct, but as a claimed new result this package duplicates a stronger theorem already published the preceding day. The required value standard for a new narrow result excludes a known/mechanically implied answer.

**Residual risks.** This is a scientific rejection of duplicate coverage, not a statement that the formulas themselves are uninteresting.

## Limitations

- The structural lemma is specific to maximum degree two.
- The finite exhaustive artifact through order eight is corroborative and is not the proof.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
