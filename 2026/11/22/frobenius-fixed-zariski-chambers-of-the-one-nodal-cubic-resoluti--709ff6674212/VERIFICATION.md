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

The code requires only Python 3 and the standard library. Run `python nodal_cubic_chambers.py`, then `python nodal_cubic_independent.py` in the directory containing the embedded files. The first program writes `nodal_cubic_chambers_results.json` with the eleven full chamber cycle profiles and the \(39\) abstract symmetry-orbit sizes. The two output text files record exact runs. Both final success markers must appear; a failed assertion or missing input is a verification failure, not negative mathematical evidence.

Direct finite checks include all \(1898\) negative-definite support Gram matrices by Sylvester signs, all \(720\) label permutations, the Burnside sum, direct breadth-first chamber orbit partition, and independently enumerated invariant vertex/edge orbit blocks. The geometric completeness of the twenty-two negative curves, the passage from Frobenius-invariant geometric supports to arithmetic chambers, and the realization of all cycle types are proved mathematically in `RESULT.md`, not delegated to the finite checks. No independent mathematical audit has been performed.
