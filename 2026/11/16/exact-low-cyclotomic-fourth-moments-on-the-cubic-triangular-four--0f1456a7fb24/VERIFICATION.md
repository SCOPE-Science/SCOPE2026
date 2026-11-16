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

# Reproducible verification

The claimed fourth-power moment values come from two finite Fourier coefficient sums derived by orthogonality. The attached C++17 certificate enumerates all \(q^7\) normalized arrays for each \(q\in\{1,2,3,4,6\}\), using exact Gaussian or Eisenstein integer arithmetic, and compares the two independent formulas for each. The attached Python standard-library checker reconstructs the minimum sets and their symmetry orbits.

Run from the directory of the extracted files:

```
c++ -O2 -std=c++17 verify.cpp -o verify
./verify
python3 orbit_check.py
```

Verified counts: \(1+128+2187+16384+279936=298636\) gauge representatives. In order \(q=1,2,3,4,6\), the exact minima were \(442,138,136,138,132\), and the normalized minimum counts were \(1,3,8,45,6\). The orbit checker established the complete disjoint orbit partitions, including sizes \(3,6,6,6,6,6,12\) in the quaternary case. All tests passed using the extracted package. No floating-point computation is needed or used for the stated conclusions.

The proof is exhaustive over precisely the named cyclotomic alphabets, not over arbitrary unit-circle coefficients. The certificate's reliability depends on inspecting and running the provided finite code; third-party independent audit has not been performed.
