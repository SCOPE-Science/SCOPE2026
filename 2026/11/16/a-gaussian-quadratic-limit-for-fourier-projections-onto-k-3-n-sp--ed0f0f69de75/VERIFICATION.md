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
The independent **computational formulas** (not an independent mathematical review) are embodied in `check_k3n.py`.

For each integer from \(1\) through \(5\), the program identifies all spanning trees by an acyclicity-and-connectivity criterion, applies the full Walsh–Hadamard transform, and tests each coefficient against both a direct combinatorial tree-degree enumeration and a separate exact rational Schur formula. It compares the full absolute first moment with the independently updated integer-weighted random-walk distribution, extended exactly through \(n=16\). It verifies the eight-step tilt normalization and covariance entries using rational arithmetic.

Observed exact endpoint norms for \(n=1,2,3,4,5\) are respectively \(1\), \(9/4\), \(801/128\), \(183/16\), and \(23715/1024\). Tree counts are respectively \(1,12,81,432,2025\). For \(n=16\), the independently computed dimensionless normalized ratio is approximately \(0.603243320016\), compared with the proven limiting value approximately \(0.609475708249\). These values are not asserted to be monotone or to give an error bound.

Actual execution concludes with `K3N_SIGNED_TREE_FOURIER_AND_TILT_DP_PASS`. The universal asymptotic is supported by the exact signed identity, central limit theorem, uniform-integrability estimate, and Gaussian moment calculation in `RESULT.md`, not merely by finite experiments. The external scientific review remains not performed.
