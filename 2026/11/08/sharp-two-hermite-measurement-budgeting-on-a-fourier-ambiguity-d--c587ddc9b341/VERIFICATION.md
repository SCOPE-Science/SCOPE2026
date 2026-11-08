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

The attached `CHECK.py` derives and tests the radial ambiguity identities using numerical integration and verifies the critical-point algebra independently with SymPy. It then compares the analytic optimum to direct one-dimensional optimization for multiple radii, tests the nontrivial \(T=4\) benchmark, and checks large-radius asymptotics. The analytic proof, not this finite test list, supports the all-radius conclusion. The least-squares norm applies to pointwise Fourier-transformed squared-intensity errors; no independent scientific audit has been performed.
