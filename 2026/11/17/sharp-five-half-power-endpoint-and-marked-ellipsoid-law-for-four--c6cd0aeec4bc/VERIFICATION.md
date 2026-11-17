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
# Verification notes

Run `python CHECK.py` with NumPy and SymPy available. The standalone code reconstructs the exact inner-product derivatives rather than merely trusting printed matrix entries. It checks all 25 entries of the Hessian, every leading principal minor's positivity, the exact radical determinant and the closed coefficient. Reproducibly seeded ball samples (150,000 samples shared across two orientation branches at each threshold) gave normalized local-volume ratios about 1.006061 at deficit 0.002 and 1.005298 at deficit 0.0002. These are finite numerical diagnostics, not a proof of the infinitesimal probability or of total-variation convergence.

The analytical proof is in `RESULT.md`. It independently requires the exact rotational sampling density, equality characterization of the global maximum, Hessian positivity, uniform quadratic localization, the five-ball volume and dominated convergence. No formal theorem prover, independent referee, or external validation is claimed. Historical priority is provisional; Beck (1984) full text was not available.
