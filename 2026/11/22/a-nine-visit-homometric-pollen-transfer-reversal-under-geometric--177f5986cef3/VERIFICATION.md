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

The standalone `verify.py` was executed with Python 3. It computes the full aperiodic conspecific-pair lag spectra, checks species counts and all nontrivial symmetry transformations, expands the exact independent-pollination product into integer polynomials, checks the exact difference and positive-root Descartes transform, verifies strict rational inequalities on both sides of the transition, and exhaustively enumerates all binary visit histories of lengths one through nine. Its checks are exact; the approximate root is a display aid only. The general uniqueness conclusion is supported by Descartes' rule and continuity, not numerical root enumeration. The benchmark is conditional on independent transfer attempts and does not validate a real pollination process.
