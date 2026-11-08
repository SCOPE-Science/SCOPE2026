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

The exact finite checker `check_spectrum.py` (Python standard library only) was executed on the complete program source. It printed `HARMONIC_BERGMAN_MONOMIAL_FINITE_OK 23205`, with all 23,205 assertions passing. Tests compare two independently computed rational formulas for each projected monomial weight, verify signed coefficient reflection and positivity for representative indices, and check finite trace-norm and extremum identities for \(1\leq m\leq30\).

The infinite-dimensional theorem is proved symbolically in `RESULT.md`. Finite checks do not certify all degrees, infinite summation, publication originality or independent audit. Signed eigenvalue multiplicities, convergence, endpoint definitions and the unweighted area normalization are explicit there.
