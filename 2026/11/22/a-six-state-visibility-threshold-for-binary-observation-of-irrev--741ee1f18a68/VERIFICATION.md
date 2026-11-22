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

The accompanying `check.py` was executed using Python with NumPy, SciPy and SymPy and reported `PASS 458 assertions`. Its symbolic calculation forms the exact six-by-six generator, verifies uniform stationarity and the identity
\[
f^\mathsf TQD_fQ^2f-f^\mathsf TQ^2D_fQf=(a-b)(a^2+ab+b^2).
\]
Its finite enumeration checks all binary colorings on rings of size three, four and five. Direct matrix exponentials test stationarity, binary two-time reversal, equal-spaced three-time reversal and the sign and leading asymptotic of the unequal-lag three-time statistic for representative positive rates. The finite tests do not establish arbitrary rate or infinite-time claims: these follow from reflection conjugacy, analytic matrix Taylor expansion, and stationary marginal identities in `RESULT.md`.

The proof does not certify robustness to observation noise, a prescribed finite sampling lag, or heterogeneity in hopping rates. No independent mathematical audit is included.
