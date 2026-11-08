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
# Verification scope

The universal result is derived in `RESULT.md` by a three-cone reduction, exact affine spectral comparisons, and a scalar two-step return. For a universal statement, symbolic derivative checks and numerical orbit samples alone are insufficient; all parameter and orbit quantifiers rely on the written argument.

The standalone `verify.py` uses SymPy and standard-library rational arithmetic. It reconstructs the two expanding branch characteristic polynomials, exact finite orbit coordinates, rank-one two-step spectra, rational scalar-return identities, 1,844 negative-cone rational samples, 1,000 rational return cases, and 5,000 typical orbit simulations. Its successful output was:

`VERIFY_OK symbolic_matrices=3 exact_2cycles=4 invariant_cone_grid=1844 diagonal_returns=1000 numerical_escape_samples={1: 1000, 1.5: 1000, 2: 1000, 2.5: 1000, 3: 1000}`

The simulation cannot certify that every orbit escapes; the proof establishes the exception set, including exact periodic orbits and their preimages. This material has had a self-review, not an independent audit.
