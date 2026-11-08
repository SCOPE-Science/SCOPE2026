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

# Verification of the wheel-majority temporal classification

The finite verifiers are standalone, need no third-party libraries, and implement distinct checks.

1. Compile and run `verify_orbits.cpp` using `c++ -std=c++17 -O2 verify_orbits.cpp -o verify_orbits && ./verify_orbits`. This traverses all labelled configurations at rim lengths three through nineteen, applies the actual open-neighbor synchronous majority rule twice, and counts fixed points and genuine period-two configurations by whether the hub changes.
2. Run `python3 verify_generating.py`. This constructs the displayed cyclic-run polynomial from integer binomial coefficients and counts hub-flipping cycles by coefficient threshold. It independently scans every binary rim string at each length and tests the two-step occupied-neighbor criterion and strict hub inequalities. It also independently enumerates valid cyclic component strings through length fifteen to check the run-polynomial total.

The complete standard outputs are included in `orbits_output.txt` and `generating_output.txt`; rows share the columns `n`, fixed configurations, period-two configurations, hub-flipping primitive cycles, hub-preserving primitive cycles. The programs agree on all tested lengths and the generating verifier ends in `RUN_POLYNOMIAL_OK`. These exhaustive finite tests are checks, not an argument for arbitrarily large \(n\). The infinite result relies on the explicit proofs in `RESULT.md`.

No independent audit or independent formal certification is asserted.
