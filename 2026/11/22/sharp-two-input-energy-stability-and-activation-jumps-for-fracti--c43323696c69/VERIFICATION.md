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

## Reproducible numerical and exact checks

Run `python3 CHECKER.py` in a directory containing the attached checker and this result. The checker uses only Python's standard library and evaluates 214 exact rational branch-energy Gram identities and their rank-one decompositions for dimensions 2 through 14, confirms strictly positive interior cells and sharp local perturbation witnesses, executes 14,400 deterministic real-input direct pair tests over dimensions 2 through 11 and 1,500 genuinely complex-input pairs, and verifies the two-site activation jump for all dimensions 3 through 20. The exact branch identities and all sampled perturbation bounds passed. Strictly positive local witnesses achieve each applicable branch singular norm to numerical tolerance; the jump was checked in 18 dimensions.

The checks establish arithmetic consistency for the sampled parameters. They do not replace the finite-dimensional spectral derivation, the proof that every possible activation mask is covered, or the segment argument valid for all input pairs. They do not establish originality by themselves. The exact graph-ball normalization and the complex absolute-value reduction are stated in `RESULT.md`.
