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

Run `python3 check_dyck_pressure.py` using Python 3 with its standard library. It exhaustively enumerates primitive positive excursions of semilength at most seven, tests Catalan totals and Narayana peak counts, and verifies cyclic pair-energy identities for three independent real parameter settings. It also computes exact-form finite-core pressure roots by scalar bisection for seven cutoffs and cross-checks the closed limiting and full Perron pressures. Finally, it maps all balanced binary words of lengths eight through sixteen into primitive excursions, verifies admissibility and tests the explicit rotation preimage bound. The observed result was `PASS exact enumeration / pressure / surgery checks: 18188`.

The finite diagnostics do not prove weak-star entropy density, infinite constrained-pressure equality, or all-parameter equality classification. The analytic proof in `RESULT.md` provides those claims, including the positive Markov approximation, counting and distortion bounds, variational duality, and exact two-symbol Markov optimization. The quantitative finite-core pressure asymptotic of a previously published record is treated only as a prior-work comparison, not a reproduced novelty claim.

No independent mathematical audit or certification has been performed.
