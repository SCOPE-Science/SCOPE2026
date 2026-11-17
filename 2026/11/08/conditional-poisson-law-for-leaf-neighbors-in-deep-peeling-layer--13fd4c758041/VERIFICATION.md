---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For fixed peeling depth h≥2, away from negligible root boundary, survival through h rounds equals rooted fringe height≥h. Yule fringe representation with Exp(1) age makes original leaf-child category Poi(a(t)), a=1−e^{−t}, independent of a child branch reaching height≥h−1 by Poisson thinning. This gives exact B_h and Q_h mixture; fixed-size fringe truncation plus bounded differences provides a.s. empirical frequencies. Generation-h expectation ≤t^h/h!, while earliest-child Gamma(h,1) yields B_h≥2^{−h}; splitting ages at h/10 gives TV≤e^{−h/10}+0.1(e/5)^h. Independent quadrature finds B_2≈0.28171808 and rank-one conditional at h=2≈0.53101872, h=12≈0.63029848, corroborating the formulas; no joint n,h limit is asserted.

## originality

PASS

The specific Yule Poisson leaf-child intensity and marginal peeling-layer recursion are known; their nontrivial conditional coupling across all h and uniform high-layer total-variation bound were not established by the inspected primary rank/layer or fringe-tree papers. Best-of-knowledge original joint invariant survives, with possible implicit-specialization risk.

## value

PASS

Leaf proximity and peeling depth are two natural but distinct tree centrality measures. The conditional full leaf-child distribution and sharp asymptotic contrast between unconditional e^{−1} and deep-layer 1−e^{−1} give a meaningful structural dependency, beyond known marginal frequencies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
