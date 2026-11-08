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

# Reproduction and boundaries

The exact proof consists of the root-of-unity orthogonality calculation, two real Nyquist equations with determinant \(-\sin(d\alpha)\), and rational scaling rigidity after recovery of full-circle squared magnitudes. The proof does not depend on numerical enumeration.

Run `python check_sampling.py` with a Python standard-library installation. The fixed-seed program checks direct Fourier coefficients, inversion of the top coefficient, four off-grid intensity evaluations per orbit, and explicit resonant pairs for each degree from \(1\) through \(13\). Expected output: `BALANCED_POLYGON_PHASE_CHECKS_PASS 5148`.

These finite tests are diagnostics only; they do not prove the universal theorem or historical priority. The result requires distinct positive radii and a nonresonant relative angle; no numerical condition number for polynomial-coefficient reconstruction is asserted.
