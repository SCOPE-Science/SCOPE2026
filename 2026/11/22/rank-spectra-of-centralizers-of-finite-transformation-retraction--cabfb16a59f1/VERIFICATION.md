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

The finite formulas follow from a unique block/root decomposition and two explicit fiber counts (surjective image occupancy and idempotent fixed-image choices). The rank-one and rank-two boundary coefficients follow from the two disjoint types of image sets, with the empty-part/zero-prefactor convention spelled out in the result.

The bundled `CHECK.py` runs independent direct enumeration for 22 finite-block configurations on at most six points. It compares all coefficients of ordinary and idempotent centralizer-rank polynomials; extra formulas for rank one and rank two are tested across all integer partitions of sizes one through eight with at most five blocks. Run `python3 CHECK.py` with the Python standard library; all assertions must pass.

These checks are exhaustive *only in their stated finite ranges*. They do not certify historical uniqueness, establish a theorem outside the proven assumptions, or constitute an independent expert audit. A source with potentially relevant earlier implicit formulas was not completely available for inspection.
