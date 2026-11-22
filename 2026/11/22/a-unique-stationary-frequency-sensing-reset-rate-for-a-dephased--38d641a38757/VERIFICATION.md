---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

- Reconstruct the stationary Bloch vector from the specified generator, then use its full-rank property to derive the one-qubit symmetric-logarithmic-derivative QFI.
- Differentiate the dimensionless rational QFI. The exact positive prefactor multiplied by the degree-six \(P(u,t)\) provides the global sign test.
- Verify \(P(u,0)=-(u-1)(u+1)^3(2u+1)^2\) and \(P(b,b^2-1)=b^5(b-1)(b+1)^2\). For fixed \(t\ge0\), exactly one positive zero follows from one coefficient sign change and opposite endpoint signs.
- The included standalone Python checker uses SymPy for symbolic identities and NumPy/SciPy for an independent stationary reset-age quadrature and density-matrix SLD linear solve. It tests 45 distinct physical parameter triples and eight optimum examples. The checker output must read PASS. Actual symbolic and numerical checker execution succeeded for the embedded code prior to packaging.
- Computations do not replace the analytic global statement. No experimental implementation, resource-normalized advantage, independent specialist audit or full priority certification is claimed.
