---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

A positive equilibrium forces b_i>0 or an incoming link at each node. For any c>0 either rational activating or inhibiting link satisfies h(cs)/h(s) between min(c,c^-1) and max(c,c^-1); this gives forward invariance of the history-dependent positive box. In logarithmic coordinates, integrate the partial derivatives of (-d_i x_i+b_i+sum h_ij)/x_i along the geometric interpolation to the equilibrium. The exact diagonal coefficient is ∫(b_i+sum h_ij(z_j))/z_i ds, while off-diagonal coefficients are ∫z_j h_ij'(z_j)/z_i ds. The identity s|h'(s)|=h(s)-h(s)^2/a implies A_i−sum|C_ij|≥δ_r>0 and sum|C_ij|≤B_r on the invariant box. A weighted sup norm, first-crossing comparison with delayed terms and η+B_r(exp(ητ)−1)<δ_r give |log(x_i(t)/bar x_i)|≤r exp(−ηt) for t≥0. This also proves uniqueness of the strictly positive equilibrium. Independent rational checks of both derivative signs and example rates passed; finite samples are not the proof.

## originality

PASS

The positive-equilibrium-conditional topology-free global convergence for positive delayed histories strengthens the inspected Sontag delayed theorem, whose hypothesis includes a strongly connected graph, while retaining the same Michaelis–Menten family. Its explicit history-dependent exponential rate and reducible-network application are a mathematically specified extension; neither the undelayed topology-free theorem nor structural/local delay theory directly implies the delayed conclusion in the inspected statements. General contraction/functional differential-equation results could nevertheless furnish another proof, so originality is qualified.

## value

PASS

Removing strong-connectivity from arbitrary-delay global attraction is a structural stabilization theorem: reducible biochemical networks are natural and excluded by the existing delayed strong-connectivity hypothesis. It gives a nontrivial explicit rate under an easily interpretable positive-equilibrium assumption, beyond local or finite tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
