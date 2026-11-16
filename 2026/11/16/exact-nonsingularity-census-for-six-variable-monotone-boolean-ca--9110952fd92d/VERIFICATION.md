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

The attached C++17 file is a standalone finite certificate. Compile with `g++ -O3 -std=c++17 monotone6_spectral_census.cpp -o monotone6_spectral_census` and run `./monotone6_spectral_census`. The completed run printed the exact success marker `MONOTONE_SIX_EXACT_WALSH_CENSUS_PASS`, the total 7,828,354, and each of the twelve even-invertible weight strata.

The verifier constructs all monotone truth tables using exact pointwise cofactor order, checks dimensions one through five for absence of even nonsingular cases, and independently computes each six-variable Walsh multiplier two ways: the full integer butterfly and a direct character sum of both five-variable cofactors. All 64 Fourier values are compared for every one of the 7,828,354 functions. It then checks the support parity, nonzero minimum multiplier, total census and weight strata. All integer values fit in signed 32-bit arithmetic; the truth-mask encoding uses unsigned 64-bit words.

This is an exhaustive algorithmic argument, not an assertion that sampled data prove a result. The verifier has not been reproduced by an independent human auditor. Historical-priority verification is bounded.
