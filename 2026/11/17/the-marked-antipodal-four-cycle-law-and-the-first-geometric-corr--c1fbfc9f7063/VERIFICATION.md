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
# Reproduction and verification

Install dependencies using `pip install -r requirements.txt`, then execute `python check_antipodal_cycle.py`. An invocation from the actual package directory returned `ANTIPODAL_CYCLE_SMALL_CAP_DIAGNOSTIC_OK`.

The planar lens integral evaluated numerically to a normalized coefficient \(0.45962035390753186\), agreeing with the exact expression \(1-16/(3\pi^2)\) to the displayed precision. Conditional four-cycle simulations at three angular thresholds used 800,000 configurations each and yielded coefficient estimates \(0.462264\), \(0.462837\), and \(0.463241\), with sampling uncertainties about \(0.0014\) each; the deviations are consistent with finite-angle geometric effects. Independent uniform-sphere simulations of 700,000 configurations per experiment found the sample-diameter event frequencies approximately \(0.0895457\), \(0.1142157\), and \(0.0974429\) for the three test pairs \((n,\delta)=(4,0.25),(5,0.22),(7,0.14)\), respectively. Their cubic asymptotic predictions were \(0.0896935\), \(0.1141577\), and \(0.0978523\).

The code is a diagnostic, not a proof. The continuum limit and remainder bound come from the bounded tangent-coordinate change of variables and inclusion–exclusion in `RESULT.md`. Conditional total-variation convergence is proved mathematically rather than inferred from simulation. Independent scientific validation has not been performed.
