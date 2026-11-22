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

The included standalone script `verify_low_degree.py` requires Python 3.9 or newer and no external packages or network access. Run `python verify_low_degree.py` from the extracted directory.

It checks exact characteristic sums using independently generated maximal independent sets on cycles of lengths 3 through 17, and integer Walsh--Hadamard transforms for their frequency bands of degree 0, 1 and 2. Additional integer checks cover the recurrence identities and all pair distances through length 600. Rational arithmetic certifies the isolating interval for the plastic constant, three base bounds and the strict comparison needed by the all-length proof. The observed result is `PASSED: 92597 exact assertions`.

Finite checks are not an infinite proof: that is furnished by the recurrence-sign certificates and the uniform positive-root inequalities in RESULT.md. This verification does not examine Fourier degrees three and higher, or a weighted/greedy maximal-independent-set law.
