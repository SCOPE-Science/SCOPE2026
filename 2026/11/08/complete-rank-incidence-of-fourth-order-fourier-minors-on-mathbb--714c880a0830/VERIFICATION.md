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

# Verification and scope

Run `python3 checker.py` and `python3 alt_checker.py` from the directory containing these files. The Python standard library is the sole dependency. It checks all five affine orbits over \(\mathbb F_5^2\), the disjoint complete partition of all \(12650\) four-point index sets, and all \(63250\) representative-by-column pairs; these imply the result for all \(160022500\) ordered pairs by affine invariance. A determinant is evaluated as the integer coefficient vector of a fifth-root sum, and zero is tested exactly by divisibility by the fifth cyclotomic polynomial. All subminors needed to prove each complete complex rank are evaluated; no floating-point threshold is used. The final completion marker is `F5_FOURTH_ORDER_FOURIER_MINORS_EXACT_PASS`.

The finite enumeration establishes the finite claim exactly but gives neither an independent validation nor a theorem for a general prime \(p\). The separate `alt_checker.py` affine-normal-form calculation gives matching orbit-by-orbit and global singular counts and concludes `F5_INDEPENDENT_ORBIT_SINGULARITY_CHECK_PASS`. No external certification is represented.
