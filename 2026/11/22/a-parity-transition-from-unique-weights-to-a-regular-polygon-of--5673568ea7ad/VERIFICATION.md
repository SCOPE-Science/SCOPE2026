---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification

The result is proved analytically; the unitary equality criterion remains valid for zero probability coordinates, and the centered Fourier difference counts cover all dimensions. With the stated shift `(Px)[j] = x[(j-1) % n]`, the second vector evaluates the first harmonic at `j+1/2`, not `j-1/2`.

Run `python3 verify.py` with NumPy. A successful run reports `CYCLE_SCHUR_CHECKS_PASS dimensions=38 boundary_vertices=836`. It checks the scalar formula in dimensions 3 through 40, representative uniform and nonuniform weights, all polygon vertices in the even dimensions in that range, and a sign-sensitive dimension-four example. The check is numerical and bounded; it is not an exhaustive probability optimization or a formal proof certificate.
