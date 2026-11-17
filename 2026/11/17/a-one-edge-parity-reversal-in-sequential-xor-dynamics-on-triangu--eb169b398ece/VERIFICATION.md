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

The proof is analytic and covers every page count and single-visit scan. Independent checks were made by direct trajectory simulation for every schedule and every state at page counts one through five, and by an independently constructed binary-matrix rank calculation for every cyclic hub gap and page count one through forty on both graphs.

From an extracted package run `python3 verification/verify_exhaustive.py` and `python3 verification/verify_linear.py`. Successful expected outputs are embedded in `verification/exhaustive_output.txt` and `verification/linear_output.txt`. The first checker uses adjacency masks, the second uses basis transformations and Gaussian elimination in characteristic two. Neither enumerates unbounded graph sizes, so the proofs of the all-parameter claims rest on the symbolic update and rank argument in `RESULT.md`.

The central identity checks are the order-three, order-two and order-four parity cases, the rank-two fixed-point constraint, the rank-one second-iterate correction in the odd case, and the counts of labelled scans. Independent validation has not been performed.
