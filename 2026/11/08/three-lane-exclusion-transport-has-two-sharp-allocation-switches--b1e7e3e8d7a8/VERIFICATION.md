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

Run `python check.py` from this package directory with Python 3 and SymPy. The embedded code is standalone and uses no files outside this package. It checks the flux reduction, Schur equality factor, coexistence candidate values, two local-stability thresholds, exclusion of nonsymmetric interior local maxima, and a two-lane fixed-density comparison. It also performs exact rational exhaustive grid checks and direct canonical-current and stationary-generator checks on short periodic lattices; all passed at package preparation.

The analytic global theorem is established by the proof in `RESULT.md`, not by finite enumeration. Short-lattice calculations do not certify every lattice length, and finite rational grids do not establish a continuum optimum. The equivalence between the microscopic rates and the cited current law is independently shown by the stationary-balance argument in the proof.

No external independent audit has been performed.
