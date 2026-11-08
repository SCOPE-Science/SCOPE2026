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

The analytical proof uses finite-group character orthogonality, norm-one idempotents, arbitrary target decomposition in the full group algebra, explicit \(k\)-fold factor construction, and norm-one extensions of finite-subgroup characters. These give matching \(\varepsilon^s\) bounds and do not rely on finite enumeration.

Execute `python3 checks/check_finite_moduli.py`. The file uses only Python standard-library exact fractions and the XOR convolution law on \((\mathbb Z/2\mathbb Z)^3\); expected output `EXACT_FINITE_CONVOLUTION_MODULI_OK 201`. It tests Fourier idempotents, zero-multiplicity cases, exact product reconstruction and perturbations outside the generating subgroup. These 201 tests do not certify the proof for arbitrary groups or arbitrary inputs. No independent audit has been performed.
