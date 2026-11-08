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

# Mathematical verification

The standalone `checker.py` (Python 3, standard library) evaluates all displayed rational formulas and the exact relationship between the root polynomial and the optimized two-step mean-square factor. It compares a separate discretized quantile integral to the symbolic formula at nine rational stepsizes; the discrete checks confirm implementation only, not an infinite proof. Exact rational bisection verifies the quoted scalar threshold and its enclosure. The full analytical proof, including all real parameters and the construction of an admissible optimal coupling, is in `RESULT.md`.

To repeat the checks, run `python3 checker.py` from a directory containing the package files. Expected standard output is preserved as `checker_output.txt`.

Reproduction tests cannot establish uniqueness against literature or independent mathematical certification. Both remain outside this verification.
