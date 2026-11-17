---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The shared iid Gaussian query matrix G gives rowwise diagonal error delta_i=sum_{j != i}A_ij (g_i.g_j)/||g_i||². Conditional variance uses E[1/chi_q²]=1/(q-2); distinct-row covariances vanish except the reciprocal pair, whose angular-square expectation is 1/q. Summing yields Var(E)=||A_off||_F²/(q-2)+(2/q)sum_{i<j}A_ij A_ji = 2(q-1)/(q(q-2))||S_off||_F²+2/(q(q-2))||K||_F². For A_q=[[0,a],[-a+kappa/sqrt(q),0]], the iid coordinate-pair vector (g_r h_r,h_r²-g_r²) has covariance diag(1,4); joint CLT and LLN denominators give qE⇒Z(kappa+2aW), independent normal Z,W. Characteristic function follows by conditioning. Checked exact rational skew formulas for q=3..14; no finite test substituted for the limit proof.

## originality

PASS

Best-of-knowledge survival of precise final claim after source-by-source implication comparison, with listed risks; no worldwide priority certification. Marginal error bounds and the original diagonal-estimator expansion do not determine the joint trace variance because the same Gaussian probes couple different reconstructed coordinates. This coupling is evaluated explicitly, and the critical product-normal limit requires a joint CLT of inner product with norm-difference, not implied by individual t marginals.

## value

PASS

A sharp, useful trace-risk identity beyond marginal diagonal reconstruction error bounds, revealing order q^-2 skew cancellation and a genuinely non-Gaussian near-skew critical window. Matters for probabilistic trace uncertainty with shared sketches and nonsymmetric inputs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
