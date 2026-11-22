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

# Exact verification
Run `python3 verify.py` using a standard Python 3 interpreter; the script has no external dependencies. The script was executed on the embedded source and printed three `PASS` lines. It constructs the opposite-parity interior diagonals, tests pair crossings by endpoint interleaving, independently enumerates noncrossing quadrangulations for six, eight and ten sides, and compares their cardinalities against 3, 12 and 55. It checks all 256 octagon frequencies two ways, from geometrical quadrangulations and graph cuts, including the signed spectrum, cancellation-support counts and first crossing-pair threshold. It computes a complete integer Walsh transform of the nonzero frequency mask, the projection-kernel coefficient distribution, and exactly 944 as the sum of absolute unnormalized kernel coefficients. The decagon check covers all 32,768 characters and exhibits an attained smallest-magnitude multiplier of one.

The graph isomorphism is explicit in the proof; the integral computation verifies its complete adjacency list. The statement that all projections have norm at least 59/16 follows from translation averaging, independently of the computer. Limits: all computational checks apply to the finite sizes in the claim; no full large-polygon spectrum or external validation is asserted.
