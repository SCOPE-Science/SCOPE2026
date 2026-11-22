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

The executable `verify.py` is a standalone Python 3 program with no external dependencies. Running `python3 verify.py` checks the candidate formulas for \(N,C,I\) on the \(5\times5\) positive interpolation grid, along both axes and at the empty base, then on seven outside-grid cases. It separately constructs transitive closures of all two-new-point diagrams when each old chain has at most two elements, checking 2,367 feasibility decisions. The saved output ends in `VERIFICATION_OK`.

The infinite assertion uses a separate mathematical fact: each pair type over two chains is specified by four cut coordinates on each old chain; its status depends only on their weak order and boundary incidences. For each fixed order pattern with \(k\le4\) distinct interior cut values, there are \(\binom{m-1}{k}\) realisations on a positive-length chain. Consequently both pair-profile functions are polynomials of degree at most four in each positive chain length, and are similarly univariate polynomials on an axis. The finite grid uniquely determines those polynomials. Finite tests alone would not justify an all-size statement.

No independent mathematical validation, external formal certification or claim of historical uniqueness has been performed.
