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

# Mathematical and computational verification

The proof reconstructs normalized cyclic ambiguity, derives an exact geometric-progression expression, localizes minimizers through a radial mismatch estimate, solves the parity-constrained phase equations, and uses irrational rotations for matching sharp upper subsequences. Limits and exact quantifiers are stated in `RESULT.md`.

Execute `python geometric_parity_checker.py` with Python 3 and NumPy. Direct computation of the original cyclic self-ambiguity agrees with the closed identity on all 4,899 pairs of indices for dimensions 2 through 24 within the programmed floating-point tolerances. Four full finite-dimensional minimum searches and four chosen high-dimensional near-resonance tests also passed. Observed output begins `CHECK_OK direct_coefficients=4899 finite_minima=4 near_resonances=4` and prints constants approximately 0.844069907041 and 1.067673364263.

This numerical test is not an exhaustive certificate for all dimensions; the exact inequalities, irrationality and subsequence claims follow from the analytic proof. Scientific originality assessment has bibliographic uncertainty, and no independent mathematical audit is represented or claimed.
