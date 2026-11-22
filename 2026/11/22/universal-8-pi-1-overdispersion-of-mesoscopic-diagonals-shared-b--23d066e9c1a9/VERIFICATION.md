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

# Verification and limitations

The standalone standard-library program `check.py` was executed using `python check.py`. It independently enumerated all convex polygon triangulations with five through nine vertices and every ordered pair, checking the exact single and double common-diagonal moments against separately calculated Catalan cutting identities for admissible length bands; **106 exact assertions passed**.

The same execution checked a finite truncation of the Catalan-square series within its proved summable tail bound and printed independent numerical evaluations of the exact finite sums for polygon sizes 2000, 10000 and 40000. These are reproducibility diagnostics only. The infinite-family and limiting covariance claims are established by the Catalan decomposition, uniform Stirling estimates, Riemann sums, and a dominated-convergence argument in `RESULT.md`, not by finite computation.

No independent mathematical validation has been performed. Historical-priority comparisons do not establish absolute uniqueness, and the theorem does not prove full distributional convergence of the common-diagonal counting process.
