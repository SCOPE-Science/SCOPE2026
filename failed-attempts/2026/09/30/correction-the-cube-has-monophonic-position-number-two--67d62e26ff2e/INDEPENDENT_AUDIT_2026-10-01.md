---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

The published statement that the three-dimensional cube has monophonic position number four is false: in fact \(\operatorname{mp}(Q_n)=2\) for every \(n\ge1\), and a direct coordinate construction places every three cube vertices on one induced path.

## Correctness — PASS

After translating one selected vertex to the empty set, write the other two as \(A,B\) and split coordinates into \(A\setminus B\), \(B\setminus A\), and \(A\cap B\). If one set is nested in the other, a geodesic contains all three. Otherwise, delete shared coordinates then private coordinates on the first half and add the other private coordinates then shared coordinates on the second half. Every nonzero vertex on opposite halves differs in at least one coordinate of each private block, so no cross-half chord exists. Thus every triple lies on an induced path and \(\operatorname{mp}(Q_n)=2\). The actual verifier exhaustively checks all triples through \(Q_7\), but the coordinate proof is infinite.

**Checked sources.** assigned RESULT.md and verify.py at tree e01bf02093b960c41633bc5db8462b4b2c43572a; Thomas--Chandran--Tuite--Di Stefano 2024 full public article text; Chandran--Klavžar--Neethu--Tuite 2026 Cartesian-product theorem

**Residual risks.** No correctness defect was found.

## Originality — FAIL

The corrected numerical formula is already a direct corollary of the later published Cartesian-product inequality \(\operatorname{mp}(G\square H)\le\max\{\operatorname{mp}(G),\operatorname{mp}(H)\}\): iterating from \(K_2\) gives \(\operatorname{mp}(Q_n)=2\). The earlier source does explicitly print the incompatible claim that the cube has monophonic position number four. Identifying that contradiction is useful, but under implication-level originality the mathematical theorem itself is covered.

### Equivalent formulations

The direct coordinate theorem and the product-theorem corollary have the same numerical implication.

### Broader coverage

It dominates the numerical part of the final claim for all dimensions.

### Exact database or table

Absence of an erratum does not make the already implied numerical identity original.

### Claim versus prior implication

This mechanically proves the complete hypercube formula without the record's coordinate construction.

**Checked sources.** https://doi.org/10.1016/j.dam.2023.02.021; https://doi.org/10.1007/s40314-026-03901-3; Resultary semantic search

**Residual risks.** No prior explicit erratum was found; this does not change implication-level coverage.

## Value — PASS

The false cube value is used as a sharpness witness in the defining paper, so explicitly reconciling it with the later product theorem and supplying a direct elementary certificate removes a meaningful literature error. The record fails originality, not motivation.

**Checked sources.** Thomas et al. 2024; Chandran et al. 2026

**Residual risks.** The correction does not identify a replacement sharpness example for the cubic bound.

## Limitations

- The numerical formula is already a corollary of a later Cartesian-product theorem.
- The contribution is a literature correction and direct proof, not an uncovered numerical invariant.
- The broader sharpness of the cubic-graph bound is not settled.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
