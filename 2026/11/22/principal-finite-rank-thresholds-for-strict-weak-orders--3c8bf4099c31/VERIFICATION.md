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

# Reproducibility checks

Run `python3 weakorder_rank_verify.py` using the Python standard library after extracting this artifact beside the script. The saved `verification_output.txt` is the output of one executed run. The checker constructs every positive weak-order composition with at most eleven vertices and all induced marked count states, computes the direct one-point-extension game rank using a minimax over every abstract type and its possible host realizations, and compares it to the resource formula in RESULT.md. Independent tests compare the interval recurrence to canonical subsequence embeddings and run an additional 1,200 seeded random cases. It explicitly tests the two sharp smallest finite examples and the first six canonical size sums.

Successful run: `CHECK_OK`; 2,047 host profiles; 627,231 marked states; 1,200 random checks; canonical size list 1, 4, 11, 26, 57, 120.

This is finite corroboration of an all-size induction. It does not constitute independent proof checking, an exhaustive test of unbounded host sizes, or a certificate of historical novelty.
