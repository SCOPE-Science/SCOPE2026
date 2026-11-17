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

The actual assigned proof diagonalizes the unit complete-graph Laplacian L0=nI−J together with mutually orthogonal rank-one edge projectors P_e=(e_a−e_b)(e_a−e_b)^T/2 for disjoint exceptional edges. Each modified edge has eigenvalue λ_e=n−2+2t_e. Nonexceptional offdiagonals are (1−F(nh))/n>0 and exceptional endpoint entries are 6h Q/[D_n D_λ] with Q=λ[n²−(n−2)λ]h²+12λh+24t, D_s=s²h²+6sh+12. The only possible sign change is the leading coefficient, equivalent to t≤2(n−1)/(n−2) for n≥3. If violated Q has exactly one positive root, giving an eventual negative transition; other exceptional edges do not interfere. F(hL) is positive definite and stochastic, so diagonals remain positive; n=2 handled separately. Independently derived symbolic difference of the exceptional transition and claimed rational formula was identically zero.

## originality

PASS

Targeted Resultary and primary literature comparison found method-wide rational absolute-monotonicity and sharp weighted split-graph thresholds, but not an exact independent-per-edge all-step criterion for arbitrary matching defects in K_n. The splitting/complete-multipartite theorem concerns a uniform clique edge orbit, not freely heterogeneous disjoint matching edges. This is best-of-knowledge; hidden specialized graph-kernel results remain a priority risk.

## value

PASS

A sharp per-edge conductance-tolerance threshold under arbitrarily many noninteracting sparse defects is a natural robust positivity question for network heat integration. Exact no-recovery crossing laws and the independence from other edge weights provide reusable structural information, not merely a test for tiny graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
