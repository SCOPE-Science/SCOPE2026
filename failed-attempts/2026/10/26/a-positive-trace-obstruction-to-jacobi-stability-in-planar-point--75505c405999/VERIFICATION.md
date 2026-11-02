---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For k≥1 positive planar fixed masses outside singular centers, Hess(m_j/r_j)=m_j/r_j³(3u_j u_j^T−I_2), with trace m_j/r_j³ because trace(u_j u_j^T)=1. For the stated rotating model ddot z+2J dot z=∇U, the standard KCC convention gives P=Hess U−I_2. The centrifugal quadratic contributes +I_2 and cancels, leaving sum of mass Hessians. Therefore tr P=Σ m_j/r_j³>0 for every nonsingular configuration, and real symmetric P has at least one positive real eigenvalue, violating strict KCC Jacobi stability along any regular trajectory. Direct independent matrix calculations for one and three noncollinear centers agree in trace and positivity. This is a correct elementary trace identity; it does NOT establish physical linear/orbital instability or apply at singular centers.

## originality

FAIL

The primary 2021 Blaga–Blaga–Harko paper on Jacobi stability in the classical restricted three-body problem already writes the same P=Hess U−I and explicitly obtains the positive sum of inverse-cube contributions to the trace for positive point masses, with the no-Jacobi-stability conclusion for the two-center model. The purported arbitrary finite k result follows immediately by summing that already-established Hessian trace term by linearity; no new nonstandard hypothesis, exceptional boundary, proof mechanism or nontrivial extension is needed. Absence of the exact phrase “for arbitrary k” in the prior article cannot turn this routine corollary into an original scientific finding.

## value

FAIL

Although the KCC instability test is mathematically legitimate, its extension from two positive centers to any finite number is one line of linearity using the previously published trace identity. It gives no new motivated invariant, sharp threshold, conceptual mechanism, unexpected counterexample or hard finite classification. It is an elementary exercise in Hessian additivity, already qualitatively explained in the source and not a distinct valuable result. Correctness and longer quantifier range do not by themselves establish mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
