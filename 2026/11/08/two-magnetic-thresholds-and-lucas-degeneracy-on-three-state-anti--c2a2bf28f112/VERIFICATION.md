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

Execute `python verify.py` with Python 3 standard library from the extracted artifact directory. It enumerates the full three-color configuration space for wheel rims of 5 through 10 sites and evaluates nine exact rational positive fields each, comparing ground energy, multiplicity and (where unique) favored-color occupancy with the asserted formulas. All 54 checks and the Lucas asymptotic consistency check passed during construction. These are finite tests only; the all-size result follows from the written binary-cycle adjacency and hub comparison proof, not from finite enumeration.

At the critical field the verifier separately checks the precise favored-occupation support; at the second threshold it checks three competing states. Numerical entropy consistency is not a proof of the entropy limit (which follows from the exact Lucas identity). Independent validation has not been performed.
