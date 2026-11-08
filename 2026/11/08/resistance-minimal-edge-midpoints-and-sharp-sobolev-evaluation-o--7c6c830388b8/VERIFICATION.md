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

The theorem is established by the proof in `RESULT.md`. The supplied `verify.py` is a standalone Python standard-library exact-rational checker, not an infinite proof or an external certificate. It builds the continuous Poisson representer by inserting an observation point, solving a grounded graph Laplacian with exact arclength source, integrating the exact quadratic correction, and comparing to independently computed discrete effective resistance and Kirchhoff index.

Executed checks:

- `DIRECT_CONTINUUM_POISSON_VS_SPECTRAL_FORMULA_PASSED 565` on eight graph families, including two circulants with distinct edge orbits and multiple hypercubes.
- `HYPERCUBE_EXACT_MAXIMUM_AND_MONOTONICITY_PASSED` for exact sample values and algebraic recurrence tests.

The all-dimension monotonicity and all-graph identity follow from explicit analytical arguments and are not inferred from this finite run. To reproduce: `python3 verify.py` with only Python 3 standard-library modules.

Source claims and scope were checked against the identified primary mathematical papers and related published mathematical claims. External independent audit has not been performed.
