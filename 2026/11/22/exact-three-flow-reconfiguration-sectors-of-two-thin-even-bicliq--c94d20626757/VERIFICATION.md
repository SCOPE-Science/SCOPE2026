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

Run `python3 verify_flow.py` with Python 3 standard library; expected final line `VERIFY_OK`.

The program checks: (1) all 27 characters of the order-three roots-of-unity filter using exact Eisenstein-integer pairs, with multiplicities 1 for 36, 14 for 9, and 12 for zero; (2) independent integer dynamic-programming totals for the first ten parameter values; (3) sector polynomial formulas for all values through 29; (4) exact construction and 2-by-2-switch search of the state graphs for left-shore sizes two and four with t from one through four; (5) exact matching of independently enumerated component sizes and counts of isolated states.

The unrestricted proof relies on binary-matrix margin feasibility and interchange connectivity, not on a finite-state extrapolation. No external certification, review or independent verification has been performed.
