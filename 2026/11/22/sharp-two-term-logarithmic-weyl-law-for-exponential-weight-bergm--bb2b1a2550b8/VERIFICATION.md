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

The exact monomial eigenvalue identity follows from radial integration, not from numerical experiments. A one-variable Laplace expansion at the unique saddle gives the fixed-parameter logarithmic moment coefficient, and strict likelihood-ratio monotonicity converts the \(O(k^{-1/2})\) logarithmic error to an \(O(1)\) degree cutoff error. The exact homogeneous-degree multiplicities then give the two-term counting law and sharp jump remainder. The small Schatten exponent formula follows by integrating the counting function.

Reproduction: install the dependencies in `requirements.txt` and execute `python verify.py` with Python 3. A successful run reports 96 finite diagnostics across four combinations of dimension and weight parameters. No finite computation is claimed to verify the asymptotic statements for every degree or parameter. The exact source text of the 2016 general weighted-Toeplitz study was unavailable, creating a residual historical-priority uncertainty; this is not a mathematical proof limitation.
