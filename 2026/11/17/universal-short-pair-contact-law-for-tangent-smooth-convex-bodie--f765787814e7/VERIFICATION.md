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

# Computational verification and limits

Run `python check_contact.py` from the extracted package with the SciPy dependency specified in `requirements.txt`.

The checker uses the exact intersection area of two unit disks after a relative translation, integrating over distance-deficit coordinates, so its geometry is independent of the boundary-graph Jacobian proof. It checks the normalization of the predicted contact-volume integral, three positive moments of the squared horizontal mark, and monotonicity of the gap crossover. For thresholds \(r=0.30,0.15,0.07,0.03\), respectively, the normalized probability ratios approach one as \(0.93745625,0.96877509,0.98543840,0.99376128\). The checker finished with `TANGENT_CONTACT_QUADRATURE_AND_BETA_CHECKS_OK`.

The mathematical proof is analytical, via localized coordinate changes and dominated convergence. The numerical quadratures are not exhaustive symbolic certificates, nor are they an independent mathematical audit. This package makes no claim about a general quantitative error bound, nonquadratic contact or definitive historical priority.
