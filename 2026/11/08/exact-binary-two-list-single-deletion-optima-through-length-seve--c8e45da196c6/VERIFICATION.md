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

Run `python3 checker.py` in the directory holding `checker.py` and `certificate.json`; no dependencies beyond Python 3 standard library.

The checker reconstructs every distinct exact-one-deletion output, checks codeword feasibility, independently recalculates the VT syndrome multiplicities, and recursively checks **both** children at every integer branch. A leaf proves infeasibility, a counting bound, or a rational dual inequality. The latter uses denominator 100000000 and tests all coefficients and costs with integers; every reported upper bound is strict below the next integer. The list-two tree at length seven has 103 nodes and 52 leaves. A separate capacity-one tree for length seven has 25 nodes and 13 leaves, verifying the known maximum 16 used in the structural comparison.

Observed checker replay: n=2: 3; n=3: 4; n=4: 7; n=5: 12; n=6: 19; n=7: 33; supporting capacity-one n=7: 16; `VERIFY_OK`. All six feasible codeword lists and the entire upper-proof forest are contained in the certificate. The test is exhaustive for these specified finite domains, not an exhaustive search of all longer codes. The independent audit is not performed.
