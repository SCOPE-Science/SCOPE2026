---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For any finite Kraus refinement, Gregoratti--Werner's optimal qubit feedback formula reduces to \(F_{\mathrm{corr}}=\tfrac12+\tfrac12\sum_k|\det B_k|\). Writing every refinement as an isometric remixing of a minimal pair and Takagi-diagonalizing its determinant quadratic gives \(s_1-s_2\le\sum_k|\det B_k|\le s_1+s_2\). The two-outcome unitary path in the package reaches both bounds and varies continuously, hence fills the interval. The amplitude-damping and dephasing specializations and the provided deterministic verifier are consistent with these identities.

## originality

FAIL

The interval endpoints are established concurrence roofs in disguise. Normalize the channel's Choi matrix by two. Finite Kraus representations are exactly finite pure-state ensemble decompositions of that rank-two two-qubit state by the HJW theorem, and for a Kraus branch the ensemble-weighted pure-state concurrence is \(|\det B_k|\). Wootters' two-qubit concurrence therefore gives the minimum average as \(s_1-s_2\), while Laustsen--Verstraete--van Enk explicitly prove that concurrence of assistance is the maximum over all right-unitary decompositions and equals the sum of the Takagi singular values, here \(s_1+s_2\). Gregoratti--Werner already identify the corrected qubit fidelity with the same determinant sum. Thus both fidelity endpoints follow directly from established results; connected two-outcome remixing then gives the interval by a routine continuity argument.

## value

FAIL

The channel-language synthesis is pedagogically useful, but under the audit bar it does not constitute an independent mathematical gap: the objective is Gregoratti--Werner's, and its extrema are the standard concurrence and concurrence-of-assistance roofs of the rank-two Choi state. The remaining full-interval statement follows from a simple continuous two-outcome remix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
