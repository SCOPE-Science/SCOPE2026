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

Reproduce the finite checks with `python3 verify.py`. The script is self-contained and uses only Python's standard library. It computes exact fourth-order Gaussian and spherical coordinate moments for two- and three-factor Kronecker products, testing identity and rank-one PSD matrices. It verifies 52 exact-rational identities and the identity/Bell-projector benchmark values. The script does not infer infinite tails from finite experiments: the proof in `RESULT.md` obtains the logarithmic limit using matching chi-square upper and lower bounds.

Scientific reproducibility depends on the displayed definitions, including the factor variances \(\mathbb E G_jG_j^\mathsf T=I\), the sphere scaling \(\sqrt{n_j}\), the natural coupling, and fixed \(m\). No external numerical dataset, private path or proprietary package is required. Exponential moments at their critical boundary, efficient evaluation of the product-state radius, and publication priority have not been independently validated.
