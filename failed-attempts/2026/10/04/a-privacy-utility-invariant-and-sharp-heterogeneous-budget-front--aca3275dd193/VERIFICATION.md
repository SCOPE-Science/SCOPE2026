---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Independent canonical noises give total log-noise \(N(V/2,V)\) with \(V=\sum_k\Delta_k^2/\mu_k^2\). Disjoint adjacency gives product log sensitivity \(\Delta_{\max}\), so the sharp equal-variance Gaussian shift parameter is \(\Delta_{\max}/\sqrt V\). Hence \(2L\mu_{\rm prod}^2=\Delta_{\max}^2\), and the cap frontier is exactly the scalar constraint \(V\ge\max\{V_0,T\}\), attained by lowering one \(\mu_k\) if needed.

## originality

FAIL

Kuang–Gang–Xia already prove the same sharp product mechanism for a common budget and separately define the blockwise canonical Gaussian mechanism/general aggregation for heterogeneous parameters. Their product proof depends only on maximum log sensitivity and the summed independent Gaussian variance, so replacing the common variance terms by \(\Delta_k^2/\mu_k^2\) mechanically yields the assigned heterogeneous formula. The invariant and budget frontier are then immediate algebra.

## value

FAIL

After the source theorem, the heterogeneous law is a direct variance substitution and the frontier is a one-variable monotone optimization; it is useful bookkeeping but not a distinct research gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
