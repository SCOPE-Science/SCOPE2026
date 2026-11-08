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

# Verification of the all-degree one-spoke theorem

The checked formula is the completed Gauss step \(F(hL)\), where \(F(z)=(z^2-6z+12)/(z^2+6z+12)\), for a star with at least four leaves and one exceptional conductance ratio. The proof in RESULT.md is universal in the number of leaves and in the real time-step and conductance parameters. No finite enumeration is used to justify these quantifiers.

The reproducible file `verify.py` constructs the exact equitable quotient in symbolic variables, checks the four polynomial adjugate off-diagonal identities, checks the difference formula for two ordinary leaves and the quotient characteristic polynomial. It then evaluates 80 strictly positive and stochastic full-matrix examples using exact rationals, and 10 excluded-ratio full-matrix negative witnesses. Running `python verify.py` with Python 3 and SymPy produces `VERIFY_OK 96`.

The library-paper comparison includes a prior complete inverse-M characterization whose conductance ratios coincide with the large-step necessary conditions, but whose group-inverse property is not a certificate for the Gauss matrix at every finite time. An older 1998 paper's full text remained inaccessible, and publication-priority review is not independent.
