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

# Reproducibility and verification

Run `python3 verify.py` with the supplied standalone standard-library script. It performs exhaustive 0–1 knapsack Fibonacci-partition counts for every \(0\le n<121393\), independently evaluates the Zeckendorf-gap state formula at every such index, checks all 25 exact fixed-value histograms at each Fibonacci cutoff through \(L=24\), and verifies the displayed \(k=12\) polynomial and ensuing affine counts.

The exact infinite statement relies on the algebraic termination argument, the strict growth of the first state coordinate and coefficient extraction from the rational series in `RESULT.md`. The finite computations are corroboration, not a proof over unbounded indices. Mathematical priority and correctness remain open to external expert audit.

Self-review: passed. Independent audit: not yet performed.
