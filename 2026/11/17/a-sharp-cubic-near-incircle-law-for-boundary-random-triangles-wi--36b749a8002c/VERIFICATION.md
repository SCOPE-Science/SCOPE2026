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

The mathematical proof is contained in `RESULT.md` and relies on a global uniqueness lemma, six explicit first derivatives, finite-dimensional simplex volume convergence, an \(L^1\) density argument, and a sharp elementary symmetric-function inequality.

`check_inradius.py` ran successfully using Python 3 and NumPy. It calculated all six corner-direction derivative coefficients from independent finite-difference geometry, checked equivalent coefficient formulas, checked the extremal equilateral case, and performed importance-sampled numerical comparisons for equilateral, scalene and right triangle hosts. The three observed probability-to-leading-asymptotic ratios at relative deficit \(0.018\) were approximately \(0.985605\), \(0.969248\) and \(0.954450\), respectively. The terminal diagnostic was `INRADIUS_CORNER_CUBIC_DIAGNOSTICS_OK`.

The numerical checks are finite-resolution diagnostics and are not independent mathematical validation. The conditional total-variation law is proved analytically, not experimentally certified. Historical-priority uncertainty remains.
