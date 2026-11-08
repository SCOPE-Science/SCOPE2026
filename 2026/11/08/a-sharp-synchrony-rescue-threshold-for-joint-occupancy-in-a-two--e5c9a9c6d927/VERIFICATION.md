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

The exact model, states, normalization, and proof of the sign inequalities are in `RESULT.md`. `verify.py` uses only the Python standard library and builds the unreduced four-state generator independently of the aggregate formula. It solves the invariant system by exact `fractions.Fraction` Gaussian elimination and checks the derived closed form for all five catastrophe synchronization fractions in a five-by-five-by-five-by-five grid of positive rates. It additionally checks the exact endpoint inequality/equality cases for regional occurrence, expected occupancy, and joint occupancy.

Command: `python3 verify.py`

Observed result from the included file: `PASS 5000 exact rational assertions; 4-state independent generator.`

The grid covers 3,125 distinct model parameter/synchrony combinations and 1,875 exact endpoint assertions. This is neither an exhaustive check over real parameters nor independent review. Symbolic derivative identities and denominator positivity are proved in `RESULT.md`; no unproved numerical extrapolation is required for the theorem. No external validation or expert certification has been performed.
