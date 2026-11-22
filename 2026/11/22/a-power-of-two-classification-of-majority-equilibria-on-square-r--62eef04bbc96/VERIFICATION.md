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

The all-order result is established by the row/column inequalities, nested-support proof, precise corner test, and two-branch bijection in `RESULT.md`. All computations below are supplementary checks, not an extrapolation to arbitrary size.

Run `python3 code/verify_rook.py` with Python 3 (standard library only) from the package root to reproduce `outputs/verification.json`. The checker constructs the two-branch recursive families for sizes one through ten; enumerates and directly checks all Ferrers partitions up to size eight; uses independent vertex-by-vertex strict majority with ties retained to examine all 16, 512 and 65,536 possible boards of sizes two, three and four; and independently tests 20,000 random boards of size five under recorded seed 23117. It computes orbit-stabilizer labelled counts for ten sizes and confirms equivalence between the geometric and direct tests in the exhaustively checked sizes. The full direct enumeration totals 66,064 configurations.

The calculated labelled counts, including the previously known \(302\) at size four, agree with all checks. No verification is asserted beyond those actually executed; the higher-size theorem relies on its exact combinatorial proof. No independent review or external replication is claimed.
