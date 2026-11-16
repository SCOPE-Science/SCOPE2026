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

## Reproducibility
Run `python3 checker.py` in the same directory. It uses only Python standard-library modules and implements direct Fourier evaluation independently of the collision calculation.

## Actual checks
- Exhaustive grouping of the \(35\) three-multisets into \(25\) residue fibers, giving \(15\) singleton and \(10\) two-multiset fibers.
- Exact verification of each resonance monomial as one of the \(10\) pairwise quotients of the five cyclic phase ratios.
- Exact integer determinant \(5\) of the reduced phase-map matrix.
- Cyclotomic-ring equality of both sixth-moment expressions for \(625\) fifth-root phase inputs, fixing the common phase.
- Complete enumeration of the \(625\) normalized fifth-root inputs, matching the exactly \(100\) minimizers to the cubic-chirp parameterization.
- \(200\) independent continuous-phase direct Fourier evaluations and explicit endpoint evaluations.

These finite checks support the exact formula but do not themselves prove every continuous-phase case; Steps 1–5 in `RESULT.md` provide that argument, including torus surjectivity. No independent mathematical audit has been performed.
