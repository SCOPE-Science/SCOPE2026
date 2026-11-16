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

# Reproduction and proof checks

Run `python check_mixed_disk.py` with Python 3 and installed `mpmath` and `sympy`. In the reviewed run the script reported `All checks passed: 3081`. It numerically integrates the explicit first-Hermite spectrogram radial density independently of the closed eigenvalue formula for eight weighting parameters, twelve disk areas, and Hermite indices through ten. It also checks each corresponding adjacent eigenvalue gap, symbolic discriminants, tangency and reversal-interval boundaries, and index-cutoff cases. The finite checks corroborate formulas but do not prove the universal theorem. The proof in `RESULT.md` uses exact Hermite–Laguerre identities, a two-term incomplete-gamma recurrence, elementary sign analysis and an exact quadratic discriminant, all for arbitrary integer index and positive disk area. All quoted results concern the specified incoherent two-channel operator. No independent external audit has been performed.
