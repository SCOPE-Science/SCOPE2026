---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For minimal \(\tau\)-tilting-infinite algebras with radical square zero, the sink-source affine-Dynkin classification yields the stated complete unfaithful-brick classification: a projective-line family in Kronecker, exactly \(n^2\) unfaithful bricks on an alternating affine \(n\)-cycle, and only nonsincere unfaithful bricks in affine tree types; hence nondistributivity is equivalent to infinitely many unfaithful bricks in this subclass.

## Correctness — PASS

Mousavand--Paquette reduce the radical-square-zero minimal case to path algebras of sink-source affine Dynkin quivers. On a tree, a zero arrow in a sincere representation disconnects the support and forces decomposition, so every sincere brick has all arrows nonzero and, with no parallel arrows, zero annihilator. On an alternating affine cycle, a nonsincere brick has a proper connected Dynkin \(A\)-support and is the unique thin interval module on that support; a sincere unfaithful brick can have exactly one zero arrow, giving the unique sincere \(A_n\)-module for each deleted edge. This counts \(n(n-1)+n=n^2\). For Kronecker, an annihilator line gives the unique sincere \(A_2\)-module over the quotient and hence the projective-line family. The distributivity conclusion follows from the parallel-arrow ideal family versus finitely many vertex/arrow-block ideal choices in the no-parallel cases.

**Checked sources.** assigned RESULT.md at frozen tree bef6341799a2f896d986dd1182eeafbca8cba640; Mousavand--Paquette 2023 full open-access article; standard finite/affine Dynkin quiver representation facts; Jans finite-ideal criterion

**Residual risks.** No correctness defect was found.

## Originality — FAIL

The record's load-bearing classification is a routine corollary package of the published radical-square-zero reduction and textbook Dynkin representation theory. Mousavand--Paquette explicitly reduce the subclass to sink-source affine path algebras, note the one-parameter affine brick families and the unfaithful regular Kronecker family, and pose the nondistributivity question. Once that reduction is in hand, connected-support classification for proper affine-cycle/tree subquivers and the elementary annihilator calculation mechanically give the stated finite counts and faithful/sincere dichotomy.

### Equivalent formulations

The audited theorem does not introduce a new class of algebras; it enumerates annihilator behavior inside the already-classified affine quiver cases.

### Broader coverage

These standard representation-theoretic facts are broad enough to supply the cycle/tree classification mechanically.

### Exact database or table

Absence of a separately tabulated count does not establish novelty because the count is a direct enumeration of connected intervals plus deleted-edge sincere modules.

### Claim versus prior implication

Under the required implication standard, the final theorem is covered even though the source paper poses a broader question rather than printing this restricted corollary.

**Checked sources.** https://doi.org/10.1017/nmj.2022.28; https://doi.org/10.2307/1969899; Resultary semantic search

**Residual risks.** The exact \(n^2\) count may not have been printed elsewhere, but it is mechanically forced by the published classification plus standard interval-module facts.

## Value — FAIL

Answering the broader published question is well motivated, but in this radical-square-zero slice the asserted answer and exact counts are routine consequences of the source's affine-Dynkin reduction and textbook representation theory. Under the common value bar, an elementary enumeration of an already structurally classified subclass does not constitute a separate worthwhile gap.

**Checked sources.** Mousavand--Paquette 2023 full text; standard Dynkin quiver classification

**Residual risks.** The result remains useful as an exposition of how the broader question behaves in the easiest classified subclass.

## Limitations

- The statement concerns only the radical-square-zero minimal \(\tau\)-tilting-infinite subclass.
- The ambient field is algebraically closed.
- The rejection is implication-level scientific coverage, not a correctness or access failure.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
