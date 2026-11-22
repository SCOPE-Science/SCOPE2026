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

# Verification notes

The analytical argument in RESULT.md proves the full arbitrary-law statement; neither finite grids nor symbolic checking can replace that proof. The accompanying `checker.py` is standalone and requires only Python 3 with its standard library.

Execution: `python3 checker.py`.
Observed: `PASS: 111355 deterministic assertions`.

Checks: the example with wash-off rates \(1/2\) and \(3/2\) and respective mass weights \(1/4\) and \(3/4\) has exact \(v_*=2/3\), \(c_*=\sqrt3/2\) and first/last-flush crossing at \(8/9\). A fixed-seed set of 110 finite mixtures checks unique optimizer values against dense grids, including threshold ties, upper cost boundary, and existence of a partial optimal branch.

Limits: the code checks finite mixtures only, uses floating-point tolerances, and cannot establish historical priority or field calibration. The proof supplies the strict minimizer, inequalities, uniqueness, and continuum endpoint assertions.
