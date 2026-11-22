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

# Exact finite verification

The first C++17 program (`verify_fwht.cpp`) enumerates all 1,546 matchings and computes every Walsh value by integer butterfly on 33,554,432 coordinates, then calculates the exact Fourier-support projection kernel. The second C++17 program (`verify_dp.cpp`) uses a disjoint combinatorial method: 376,992 multisets of five row signs with integer multiplicities and a 32-state used-column recursion. Their 187 signed histogram entries agreed exactly and matched `spectrum.csv`.

Checks: each program accounts for all 33,554,432 frequencies, 1,183,200 zeros, minimum positive multiplier modulus 2, 1,546 at the trivial frequency. The Fourier-support kernel has unnormalized absolute sum 25,902,311,232. The independent approach verifies the multiplier histogram, not the endpoint projection sum; the latter is determined exactly by the first full-group Walsh transform and the analytic averaging proof.

Limits: this is a finite exhaustive computation at one fixed board size, not a proof of a uniform-size formula. Independent external audit and validation have not been performed.
