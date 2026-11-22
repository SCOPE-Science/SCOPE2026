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

The accompanying standalone `checker.py` uses only Python's standard-library exact rational arithmetic. Executing `python3 checker.py` from a directory containing the extracted file reproduced 94 exact checks, testing a direct Fourier-moment recurrence against both displayed rational formulas and the factored cumulant across 30 positive rational parameter pairs. It also checked the strict coefficient signs for four further rational angular diffusivities. The stationary existence proof, uniqueness for all real positive parameters and both singular-limit laws rely on exact analysis in RESULT.md; the finite test grid is not claimed as a computer proof of these infinite assertions. Independent review has not been conducted.
