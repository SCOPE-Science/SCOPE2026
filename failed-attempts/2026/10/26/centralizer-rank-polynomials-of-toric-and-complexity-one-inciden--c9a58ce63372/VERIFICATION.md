---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Fix the diagonal vertex labels. On every edge with unequal labels the commutation equation uniquely solves for b's arrow coefficient given the vertex values of b. For equal labels this arrow coefficient is free; precisely those edges S with nonzero arrow coefficient in a impose equalities on b's vertex values. Consequently dim C_A(a)=m−|D|+n−r(S), where D consists of unequal-label edges and r(S)=n−k_G(S) over every finite field. Weight each active equal edge by q−1, and each remaining edge by 1 if equal or qz if unequal. Expanding the latter as qz+(1−qz)1_equal and counting equality assignments on S∪T gives exactly the displayed double sum. Dividing by q^c removes the only dependence on n beyond r(E). In a forest the vertex differences and edge coefficients are independent parameters once root labels are fixed, with one zero-rank pair and q²−1 rank-one pairs per edge. On a cycle the provisional independent-edge contribution is the trace of the transfer matrix power, with eigenvalues P_q(z) and 1−z; only S containing the whole cycle overcounts rank by one, requiring all its labels equal and coefficients nonzero. Correcting the q(q−1)^ell such choices gives the stated term, and pendant edges supply independent P_q(z) factors. This includes isolated vertices and the edgeless case; the invariant counts elements, not distinct adjoint operators. No uploaded code was executed; the universal proof, not the finite output, establishes correctness.

## originality

FAIL

Earlier Resultary record 38b9edb44d0d (2026-10-12) proves the full elementwise adjoint-rank polynomial, normalized graphic-matroid invariance and forest law for radical-square-zero quivers on arbitrary finite simple graphs over all finite fields. The height-at-most-two incidence algebra is exactly its specialization to the oriented Hasse graph. The new double sum is inclusion–exclusion in the earlier flat formula, and the single-cycle law is a mechanical simplification of that same full histogram. The decisive overlap is not just a commuting-pair count and is not based on unavailable literature.

## value

FAIL

The full histogram is a natural invariant, but it had already been computed in a strictly broader setting. The unicyclic expression is a convenient simplification using one circuit and the standard two-eigenvalue cycle transfer matrix, not a missing exact invariant beyond the earlier general formula. The alternative inclusion–exclusion and tree examples do not leave a distinct mathematical gap relative to that result. No repaired finding is justified on the evidence reviewed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
