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

## Reproducible checks

Run `python verify_exhaustive.py` to enumerate direct temporal updates in the bounded chip box for sizes 3 through 6; actual output is in `exhaustive_output.txt`. Run `python verify_phases.py` to independently intersect firing/waiting inequalities, assemble coefficient polynomials and test band support and endpoint formulas through size 8; actual output is in `phase_output.txt`.

The first program exhausts exactly \((2n-2)^n\) nonnegative vectors for each tested size and checks least period four. The box contains all possible nontrivial-period configurations by the external bound and by the phase derivation; this finite check is not an infinite proof. The second checks integer coefficients against direct phase-word inequality solutions and verifies the full connected support at each tested size. The all-size proof is the constructive argument in `RESULT.md`, invoking the published nonclumpy-pattern theorem for one critical exclusion.

All file contents and recorded outputs were compared after packaging; no independent audit has been performed.
