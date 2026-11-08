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

The proof gives all-horizon results by exact full-branch Markov paths, not by numerical extrapolation. The four-cell adjacency matrix is stated in `RESULT.md`. It has \((2(n+1))\) length-\(n\) admissible paths and exactly two with each first-inner-cell entrance time; each path has initial Lebesgue mass \(1/(5\,2^{n-1})\). Its terminal path-count row is \((1,n,n,1)\). A two-cell graph proves the exact comparison hole law. Inverse-branch contraction proves the limits of conditional spatial measures.

Run `python3 verify_escape.py` in the same directory using Python 3 and its standard-library `fractions` module. It independently enumerates exact preimage interval unions of the safe region for \(n=1,\ldots,25\) at both holes, without deriving them from the claimed path-count formula. It additionally computes graph powers, enumerates all legal first-entrance-time paths, checks each terminal weight and exact total-variation formula. Output observed from the submitted program:

`VERIFY_OK independent_exact_interval_horizons=1..25 matrix_terminal_initial=1..25 conditional_TV=1..25`

No limit theorem or global all-\(n\) assertion is inferred solely from those finite tests. Historical-priority checks remain provisional, and independent scientific audit is not performed.
