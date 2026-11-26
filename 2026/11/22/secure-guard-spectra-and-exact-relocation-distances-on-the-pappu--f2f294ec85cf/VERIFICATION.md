---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The finite certificates test the two size polynomials on the labelled 18-vertex Pappus incidence graph. `python3 verify.py` uses cached closed-neighborhood unions for every one of the 262144 masks, tests each required feasible swap, and checks inclusion-minimality by single deletions. `c++ -std=c++17 -O2 independent_check.cpp -o check && ./check` computes domination directly for each proposed swap and verifies the same polynomials. The success markers are `PAPPUS_SECURE_VERIFY_OK` and `INDEPENDENT_DIRECT_SWAP_OK`, respectively.

The move graph and automorphism outputs are ancillary checks on the minimum class, which also occurs as the all-singleton sector of weak Roman optima. They do not establish originality, and the weight-eight overlap provides no certificate for the higher-cardinality coefficients. The exhaustive all-mask tests, not the overlap or the symmetry data, certify the complete spectra.
