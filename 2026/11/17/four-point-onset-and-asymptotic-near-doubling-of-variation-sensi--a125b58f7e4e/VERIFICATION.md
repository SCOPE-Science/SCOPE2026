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
# Verification and reproducibility

Run `python3 verify_convex_bv.py` from the package directory with a standard Python 3 interpreter. No external libraries, datasets or network access are required.

The checker enumerates every one of the 511 second-difference active faces over dimensions 2 through 10, computing exact rational least-squares projection matrices implicitly by Gram-system elimination, then evaluates every one-step BV probe. It compares against the nine stated rational sharp coefficients and verifies explicit strictly feasible finite two-input KKT certificates for their maximizing faces. It also evaluates balanced step witnesses at free-endpoint/affine-interior faces for all dimensions 6 through 100.

The analytical proof supplies the unrestricted all-dimensional lower bounds, the exact reduction to faces, and finite attainment. The finite computations alone do not prove an infinite-dimensional limit, nor do they give an exact large-dimension coefficient. The data and code used for exact certificates are embedded as supplied; no independent mathematical audit has been carried out.
