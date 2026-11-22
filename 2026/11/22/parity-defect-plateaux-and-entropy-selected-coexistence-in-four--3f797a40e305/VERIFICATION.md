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

Compile `verify.cpp` using a C++17 compiler and run it from a directory containing that source file. The program enumerates the full four-color configuration space separately for \(n=6,7,8,9\), counts every monochromatic graph edge and every favored vertex, and constructs the sectorwise exact minima and degeneracies before evaluating field-dependent minima. It tests the formula at \(0,1,2,3,n,n+1\) and at half-integer fields on both sides of critical values where applicable, and also directly enumerates the cycle independence sets. The recorded execution concluded in `ALL_ENUMERATION_CHECKS_PASSED`.

The proof in `RESULT.md` is an analytic all-size proof. Finite-state tests do not certify untested sizes or independent scientific validation. The last field transition is size-dependent; the density statement concerns uniform samples from the zero-temperature critical ground configurations at precisely \(H/J=2\).
