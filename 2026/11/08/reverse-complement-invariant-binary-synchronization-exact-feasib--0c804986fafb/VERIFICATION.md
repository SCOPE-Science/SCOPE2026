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

# Reproducibility checks and limits

The two included standalone source programs test the same binary reverse-complement and prefix/suffix definitions using distinct representations. Run `python verify.py`; then run `g++ -O2 -std=c++17 verify_independent.cpp -o verify_independent` followed by `./verify_independent`.

The Python program compares the direct orbit test to the unbordered/antipalindromic criterion for all binary words through length fourteen, checks exact finite exclusions through nine, tests the long-form witness through length eighty, and enumerates several finite guard families through length thirty-two, including their predicted counting lower bounds, closure, and uniqueness of the marker. The independently written C++ program enumerates every indexed binary word through length nine, reconstructs all four overlap comparisons using integer masks, and counts the reverse-complement orbits. The observed results are `DIRECT_ALL_CHECKS_OK` and `INDEPENDENT_INTEGER_OK`.

These are finite tests only. The universal existence statement and the asymptotic rate claim rely on the explicit combinatorial proof in RESULT.md. No independent scientific audit or exhaustive literature-priority certification was performed.
