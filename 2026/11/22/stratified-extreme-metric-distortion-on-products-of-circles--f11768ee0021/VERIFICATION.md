---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Folded angular differences are independent uniform on [0,π]. The squared ratio is a positive weighted average of the squared one-circle arc/chord factors, which increase strictly to (π/2)². It tends to 1 at the all-zero corner and reaches π/2 exactly on the other 2^d−1 corners, so all sufficiently high exceedances are localized there. Expanding at antipodal set A gives deficit F=L+O(L²) with L=Σ_{j∈A}r_j²s_j/(2S_A)+Σ_{i∉A}(π²−4)r_i²y_i²/(16πS_A); all coefficients are positive at fixed radii. In a small fixed neighborhood, F<ε is thus squeezed by L<ε±O(ε²). The volumes of these model sets scale exactly with exponent (d+|A|)/2. The squared-coordinate substitution and beta integral give c_A as stated, with a relative O(ε) error, so a singleton's next error cannot contribute to the second coefficient (including d=2). The AM–GM equality case is exactly equal radii. On singleton corners, rescaled model contributions have simplex density proportional to the product of inverse square roots of the coincident-coordinate contributions; adding slack gives Dirichlet(1,1/2,…,1/2,1). The squeeze implies the same law for the true exceedance and either exact or leading slack. Singleton corner weights are proportional to r_j^d, and the labelled ratios plus diameter determine the scale. All claims are for fixed positive radii and the specified embedding.

## originality

PASS

Available sources share ingredients, statistics in other geometries, or intrinsic-distance observables on flat tori. No inspected statement gives the claimed two corner orders, labelled inverse proportions and conditional simplex law for the specified orthogonal product embedding. Credit the corner tail and defect law rather than classical metric formulas or the Clifford torus itself.

## value

PASS

The second term reflects a genuinely different antipodal stratum rather than a correction to the most likely stratum. The coefficients measure geometric imbalance, identify equal radii uniquely, and recover labelled shape information from rare events. The conditional defect profile gives more than an endpoint exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
