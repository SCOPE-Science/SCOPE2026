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

The mathematical argument in `RESULT.md` proves the arbitrary-peak existence theorem using an explicit Poisson concentration bound and a finite-witness local-maximum argument. This is not a computer-assisted proof of the infinite statement.

Run `python3 check.py` with a standard Python 3 installation. For the exact cutoff of \(0.1\%\), \(K=1000\), and \(\gamma=1/4\), the script checks fourteen strict interval inequalities at rational effort levels. It constructs Poisson cumulative probabilities through positive recursions, uses directed decimal rounding and conservative exponential brackets, and includes an analytic upper bound on all omitted positive Poisson-tail contributions. The packaged checker completed all fourteen strict comparisons successfully.

This verifies at least seven distinct strict local maxima, not their exact positions or the absence of further extrema. No field dataset or external independent scientific audit has been used. Numerical samples and printed decimal approximations are illustrative; the acceptance comparisons use outward-rounded interval endpoints.
