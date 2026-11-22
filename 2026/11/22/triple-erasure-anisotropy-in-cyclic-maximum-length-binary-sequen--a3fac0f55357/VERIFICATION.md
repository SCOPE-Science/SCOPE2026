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

# Verification and limits

The field-based checker `check_erasure.py` constructs the trace sequence in polynomial quotient fields of degrees two through five and enumerates every coordinate support of the relevant sizes for representative empty, one-, two-, and three-phase deletion sets. It checks the arbitrary-set top formula and the dependent-triple next-to-top correction.

The independent recurrence checker `check_erasure_independent.py` uses a linear recurrence directly, not the finite-field multiplication or trace routine. For degrees three and four it exhaustively checks both leading coefficients for every three-phase deletion set (35 and 455 choices respectively); for degree five it checks six further samples. Both were replayed successfully, and their predicted outputs agree. The only shared mathematical information is the expected theorem formula and the primitive polynomials.

These finite comparisons are not an all-degree proof. The all-degree proof uses trace-map fiber cardinalities, the exact pairing in the one-dimensional kernel and basis counts. The result does not assert general lower-degree shattering coefficients after four or more phase deletions, nor exact minimum saturating-set sizes. Historical priority is conditional on the scope of the read sources and accessible index; independent external mathematical validation remains unperformed.
