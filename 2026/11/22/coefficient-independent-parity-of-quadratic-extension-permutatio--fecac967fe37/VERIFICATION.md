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

# Verification record

The full algebraic proof is provided in `RESULT.md`. For finite replay, execute `python3 verify_parity.py` under Python 3 without third-party packages. The checker constructs five explicit quadratic prime-field extensions and tests every coefficient and specified exponent range. It reports 1,251 permutation instances with 707 even and 544 odd, and confirms the coefficient lemma for all observed permutations. It also rejects non-permutations by exact image cardinality rather than presuming them permutations. These computations are finite spot tests; they neither exhaust arbitrary prime powers nor certify an infinite theorem. No independent audit has been performed.
