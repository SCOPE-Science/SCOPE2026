---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The pure-death transition chain has independent Geom(p_k) holding times and mean Σ1/p_k, variance Σ(1-p_k)/p_k². Under Σ(p_k-k/M)<=B, strict convexity of Σ1/p_k and KKT derivative -1/p_k² yield unique clipped water-filling p_k=max(k/M,c); budget function is continuous and increasing, with upper cap c<1. Writing K≈Mc yields K~sqrt(2BM), c~sqrt(2B/M), leading mean M[1/2 log M +1 -1/2 log(2B)+o(1)], and variance two equal leading tail contributions totaling sqrt(2/B) M^(3/2). Geometric third absolute moments sum O_B(M²), yielding Lyapunov CLT on scale M^(3/4). Independently checked exact rational M=100,B=1/2 threshold c=21/200 and budget, and strict local convex comparison; source verifier was inspected but was not taken as an all-M proof.

## originality

PASS

Classical unbiased coupon-collector waiting times, convex water filling, and stochastic rounding bias theory are prior facts. The complete optimal calibration law with a fixed statewise TV budget and its unusual halved logarithmic mean and Gaussian M^(3/4) transition remain distinct best-of-knowledge claims.

## value

PASS

Optimizing a finite aggregate budget of signed rounding bias is a natural exact resource-allocation question. Its unique policy produces a nontrivial change both to the leading absorption-time scale and the limit distribution, offering a precise benchmark for quantized-descent models beyond a routine KKT calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
