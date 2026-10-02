---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For a connected complete multipartite graph of order \(N\), the mixed metric dimension is \(N\) with at least two singleton parts, \(N-2\) for complete bipartite graphs with both parts at least three, and \(N-1\) otherwise; this contradicts the all-parameter formula stated by Hayat--Khan--Zhong.

## Correctness — PASS

The case proof is sound. With at least two universal vertices, every proper landmark set has a vertex/incident-edge collision, forcing all \(N\) vertices. With exactly one universal vertex, two omitted vertices cause a collision and omitting the unique universal vertex gives an \(N-1\) resolver. With no singleton parts and at least three parts, prior edge-metric dimension gives the \(N-1\) lower bound and omitting one vertex mixed-resolves. In the bipartite case, Kelenc et al.'s exact theorem gives \(N-1\) when a part has size two and \(N-2\) when both parts are at least three. The inspected exhaustive checker agrees on all 58 part types through order eight.

**Checked sources.** assigned RESULT.md and verify.py at tree eaa313e7b49f392548d441568f8b166f66429cd1; Kelenc--Kuziak--Taranenko--Yero 2017 full arXiv text; Hayat--Khan--Zhong 2022 full HTML; Ghalavand--Klavžar--Tavakoli 2023; Peterin--Yero edge-metric complete multipartite theorem

**Residual risks.** No correctness defect was found.

## Originality — FAIL

The corrected piecewise answer is mechanically recoverable from published results that predate this record. Kelenc et al. already give the exact complete-bipartite cases and their general criterion \(\operatorname{mdim}(G)=|V(G)|\) iff every vertex has a maximal neighbour. The universal-vertex cases are also explicitly treated by Ghalavand--Klavžar--Tavakoli. For multipartite graphs with no singleton parts and at least three parts, the published edge-metric value \(N-1\) gives the lower bound while Kelenc's maximal-neighbour criterion rules out \(N\), forcing equality. Thus the replacement formula is a synthesis/corollary of prior theorems, even though the 2022 paper states a conflicting formula.

### Equivalent formulations

The audited cases are equivalent to partitioning complete multipartite graphs by singleton count and number of parts, then applying those prior theorems.

### Broader coverage

Together these stronger prior statements force the remaining \(N-1\) case.

### Exact database or table

A missing correction entry does not restore originality because the mathematical answer is already implied by published theorems.

### Claim versus prior implication

Under the audit rule, a correction whose numerical theorem is already mechanically implied is covered.

**Checked sources.** https://arxiv.org/abs/1611.04292; https://doi.org/10.3390/math10111815; https://doi.org/10.1007/s40314-023-02351-5; Peterin--Yero 2020; Resultary semantic search

**Residual risks.** The literature correction itself may not have been explicitly published before this record, but the exact mathematical values are already forced.

## Value — PASS

Documenting a false published all-parameter formula and giving a clean replacement is scientifically useful, especially because the error affects multiple parameter ranges. The rejection is originality, not lack of practical or expository value.

**Checked sources.** Hayat--Khan--Zhong 2022; Kelenc et al. 2017; Peterin--Yero 2020

**Residual risks.** The corrected formula is largely a synthesis of known results rather than a new invariant computation.

## Limitations

- Finite simple connected complete multipartite graphs only.
- The edge-metric correction is prior work and not part of the originality claim.
- The rejection is implication-level prior coverage, not a correctness defect.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
