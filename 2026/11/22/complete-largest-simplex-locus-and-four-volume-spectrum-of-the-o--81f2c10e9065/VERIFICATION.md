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
# Verification record

Run `python3 verify_pentagon_simplex.py` (Python 3 standard library only). It verifies the four exact levels and multiplicities among all \(\binom{10}{5}=252\) vertex subsets, all 50 extremal vertex configurations, every same-oriented-volume single replacement and forbidden simultaneous pair, and all 75 moving-vertex families. The expected output contains four `PASS` lines; every assertion was observed to succeed.

An independent direct-coordinate numerical determinant sweep verified each level to absolute error less than \(10^{-12}\); a separate convex-hull computation matched the quoted containing volume. Numerical checks are corroborative. The proof for all interior simplex vertices is the analytic separately-affine determinant and equality-of-convex-averages argument in `RESULT.md`.

The first-public source is the 2026-11-10 version of arXiv:2611.14674. The source paper's objective is the four-volume of the containing polytope, not the contained simplex maximum. The checked literature and a related nine-vertex simplex-spectrum record do not imply the ten-vertex optimizer graph. Broader historical priority remains provisional; independent audit is not performed.
