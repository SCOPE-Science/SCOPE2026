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

Run `python3 verify.py` from this directory, with Python 3. The program requires no external libraries and directly computes individual payoffs before and after every cross-team exchange for 155 parameter settings and 9,588 labeled assignments. It compares the resulting classifications with the formulas in RESULT.md, verifies exact labeled-binomial counts, and tests the two minimum-size distinctions.

The proof in RESULT.md is infinite in the integer parameters; these computations are bounded validation checks and are not claimed to prove the infinite theorem. No third-party validation was undertaken.
