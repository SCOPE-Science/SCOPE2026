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

# Verification procedure

Run `python3 verify_thermal_matching.py` in the directory containing that standalone script. The dependencies are Python 3, NumPy, SciPy and SymPy. A successful run prints `PASS 17202 finite checks`. The code constructs complete-graph weighted Laplacians from first principles, compares exact characteristic polynomials and budget identities, compares matrix-exponential heat traces with the two-eigenspace formula, checks the exact optimizer against other symmetric allocations, samples nonsymmetric feasible competitors, and checks the stated large-size limit numerically.

The analytical proof in `RESULT.md` establishes global strict convexity, exact symmetry, scalar optimality and the limiting law. The finite tests are deliberately not cited as proof of every graph order, all real prices or all times. There is no independent external validation.
