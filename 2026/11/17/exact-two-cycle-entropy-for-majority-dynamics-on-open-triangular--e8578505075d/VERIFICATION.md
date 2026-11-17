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

The finite exact vector identities and transfer-to-dynamics bijection are specified in `RESULT.md`. `verify.py` is a complete standard-library Python 3 checker for both integer annihilator identities and generating function numerators. Its output appears in `verification-output.txt`. `direct.cpp` is a separate microscopic implementation of the synchronous majority update, and `direct-output.txt` records exhaustive comparisons over \(2\le n\le7\). Reproduce with `python3 verify.py` and `g++ -O3 -std=c++17 direct.cpp -o direct && ./direct`.

The transfer certificate evaluates all finite local transition cases and the full integer row-vector residual, then uses the resulting polynomial identity to establish a recurrence for *arbitrary* length. The direct exhaustive dynamics check is corroboration, not a substitute for the infinite argument. The numerical root value is not a rigorous stand-alone root certificate; the proof supplies real intervals and root separation. The classification covers initially recurrent configurations, not their larger basins. Independent audit has not yet been performed.
