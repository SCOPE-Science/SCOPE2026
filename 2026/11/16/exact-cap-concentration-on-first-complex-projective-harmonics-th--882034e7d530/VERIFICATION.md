---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For d>=3, trace-zero bidegree-(1,1) harmonics identify H_1 with trace-zero matrices of dimension d^2-1 and global L2 inner product tr(AB*)/[d(d+1)]. U(d-1) splits into axial, off-diagonal cross and tangential sectors of dimensions 1,2(d-1),d(d-2). With Y=1-|u_1|^2~Beta(d-1,1) and E[Y^k 1_{Y<=s}]=(d-1)s^(d-1+k)/(d-1+k), the scalar restriction ratios give exactly s^(d-1)(1-2t+d^2 t^2), s^d(1+dt), s^(d+1). Direct algebra yields axial-cross=(d+1)t(dt-1)s^(d-1), the other two gaps >0, so the sole top switch is t=1/d and the tangential mode is always the bottom. Fixed-volume s=v^(1/(d-1)) gives dt->-ln(v), yielding stated limits. Independent symbolic sector-moment recomputation confirmed the identities; the original rational verifier tests 42 parameter cases, not all dimensions.

## originality

PASS

Resultary similarity search located this record itself and projective-space analogues on distinct projective fields or second harmonic bands; Jaming–Speckbacher derives general homogeneous-space concentration inequalities but not exact first complex-projective eigenspace eigenvalue ordering. Holomorphic Toeplitz/Bergman symbol operators act on another space. No identified prior statement directly implies all three explicit first-band concentration branches and unique t=1/d exchange.

## value

PASS

The exact spectrum and extremal transition of projective cap observation are intrinsic to the first Laplace band, with sharp observability/conditioning and an e^-1 high-dimensional volume transition. It answers a natural continuous spectral concentration question with nontrivial representation decomposition and sharp parameter boundary, not a reparametrization of a known numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
