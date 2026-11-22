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

The direct checker reconstructs the orientation-compatible generator order and applies adjacent max/min comparators. It tests the exact stabilization time against the independently computed orientation-height formula, all binary-block threshold times, and cumulative tridiagonal transfer counts. Exhaustive orientations were checked for \(3\le n\le11\), plus 840 seeded examples up to \(n=60\). Both minimum-power formulas and the total number of orientations were verified for \(3\le n\le30\). See `CHECKER.py` and `CHECKER_OUTPUT.txt` for exact reproducible commands and recorded checks.

The proof of the all-size formula is mathematical, not based on extrapolation: thresholding and grid-crossing precedence reduce the problem to a telescoping recurrence; independence of orientation signs yields the transfer matrices; Donsker's invariance principle gives the weak limit. Empirical checks cannot establish historical novelty or furnish an independent audit.

Run with `python3 CHECKER.py` in an environment providing Python 3 standard libraries only.
