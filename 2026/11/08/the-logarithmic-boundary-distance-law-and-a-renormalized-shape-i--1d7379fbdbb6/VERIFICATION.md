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

# Verification record

The analytic proof above checks: the cusp upper-half-plane area form, the exact integration threshold \(y=w/(2\sinh s)\), the \(\cosh t\) Fermi area element, cancellation of horoball diameters, Möbius chord-product invariance, Ptolemy's inequality and equality class, and the exact ideal-triangle change-of-variables Jacobian. The ideal triangle's support endpoint is \(\rho=\frac12\log3\). The proof separates exact finite statements from the nonuniform \(s\downarrow0\) limit; it makes no uniformity claim for degenerating polygon families.

The accompanying extracted checker numerically compared the ideal-triangle survival integral with the explicit CDF for seven thresholds, with maximum discrepancy less than \(2\times10^{-13}\). For ideal quadrilaterals \(0,1,t,\infty\) with \(t=2,3,5\), it sampled \(524288\) area-uniform interior points per shape and compared the nearest-side distance CDF with the asymptotic expression at distances \(0.007,0.012,0.02\). In the completed tests the largest absolute discrepancy was approximately \(1.215\times10^{-5}\), as expected for a small-threshold finite-sample check. The program prints `IDEAL_HYPERBOLIC_POLYGON_BOUNDARY_LAW_OK` after completing its deterministic tests.

To reproduce, install the requirements from `requirements.txt` and execute `python checks/ideal_polygon_checks.py` after extracting both files from the same package. This finite test does not establish the universal asymptotic or novelty; those are addressed separately in the proof and source comparison. Independent auditing has not been conducted.
