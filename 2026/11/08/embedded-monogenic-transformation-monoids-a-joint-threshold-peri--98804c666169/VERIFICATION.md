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

Run `python3 verify.py` with a Python 3 standard-library interpreter. There are no third-party dependencies, downloaded datasets, random seeds, or network connections.

The verifier counts permutations of each exact order with a cycle-decomposition recurrence and Möbius inversion; counts forest parent assignments by distance layers; independently enumerates all functions on sets of sizes 1 through 6; computes the sets of actual powers of every function; and compares the exact joint counts of generated embedded monoids and their generator fibers. It separately enumerates permutations up to degree 6 to test the cycle recurrence. Expected totals of distinct embedded submonoids are `1, 4, 26, 237, 2842, 42488` for degrees 1 through 6. Each test prints `CHECK_OK` and the completed program prints `VERIFY_OK`.

This is a finite reproducibility check, not a proof for arbitrary degree. The all-degree result depends on the separately written bijective counting argument and elementary inequality. Neither this document nor the program claims external or independent mathematical verification.
