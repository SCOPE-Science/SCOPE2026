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

# Verification of the centroid-capture formula

Analytical verification uses an affine reduction to a reference triangle, the exhaustive partition into three edge-occupancy patterns, and exact one-variable integrations. The two-one and one-one-one conditional probabilities are computed symbolically by the standalone `verify.py` script. The nonattained lower bound follows directly from the strict triangle inequalities; the upper equality requires equal normalized side lengths. Majorization uses a strict pair-product increase under averaging.

Executed check: `python verify.py` (Python 3, NumPy and SymPy), producing:

`VERIFY_OK conditional_integrals=4 equilateral_and_degenerate_limits=2 independent_samples=1120000`

The code also generates independent boundary samples on five explicit Euclidean triangles and on three prescribed edge-weight laws, checking agreement with exact probabilities to five binomial standard errors. This numerical consistency check is **not** substituted for a proof for all shapes. No random search or finite enumeration can establish the universal majorization statement. The result does not establish statistical confidence intervals for recovered shape parameters; it determines exact population probabilities.
