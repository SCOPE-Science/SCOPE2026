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

# Mathematical verification
The primary proof independently checks (i) Fock diagonal Gaussian moments, (ii) an analytic-half-plane pole obstruction for a finite sum of geometric eigenvalue sequences, (iii) exact bounded Gaussian symbols for allowed powers, (iv) uniqueness by Gaussian Hermite density, and (v) irrational/rational orbit densities. The determinant step is distinctness of \((1+it)^k\) for different nonnegative integer \(k\), which follows from \(|1+it|>1\).

The companion `CHECK.py` tests bounded finite identities, selected pole separations and rational-angle orbit counts. Its finite assertions are diagnostics and cannot establish the analytic or equidistribution steps. The formula includes the boundary \(\operatorname{Re}((1+it)^k)=1\), where the unique Gaussian symbol has modulus one rather than decaying. No computer-assisted infinite proof, independent audit, or external certification is claimed.
