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

# Finite verification and proof limits

Execute `python check.py` with Python 3 and `mpmath` installed. The checked standalone file reports 77 phase-interval ordinal-pattern tests (orders 2 through 12) and 703 gap/entropy cases; it separately checks exact short-gap counts and quantitative lower bounds at partial quotients 73, 100, 1000 and 10000, as well as 699 bounded-type gap-entropy cases. Its arithmetic uses 85 decimal digits for irrational orbit coordinates; logarithmic inequality checks allow a small numerical tolerance.

The convergent-grid gap bound, the disjoint-cluster condition and the conditional Shannon inequality are proved in `RESULT.md`, not extrapolated from the checker. In particular, numerical tests at a finite selection of irrational frequencies do not certify the equivalence or the asymptotic for every irrational rotation. The source, period, partial-quotient and observation assumptions are fixed in the main statement. No independent scientific audit or separate external certification has been carried out.
