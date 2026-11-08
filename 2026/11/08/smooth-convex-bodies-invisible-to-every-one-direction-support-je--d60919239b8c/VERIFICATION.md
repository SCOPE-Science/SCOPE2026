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

# Reproducibility and limitations

Run `python3 verify_jet_width.py` from the directory containing the accompanying file, using Python 3 and only its standard library. The deterministic program samples 120000 normal angles for each of two strictly convex support functions, compares discrete histograms of support values, first derivatives and curvature radii; evaluates the prescribed perimeter/area integrals; and separates the covariance at shift \(\pi/3\). Its successful first output line is:

`VERIFY_OK shapes=2 normal_samples_per_shape=120000 jet_orders=0,1,2 perimeter_area_identities=4 distinct_two_angle_correlations=1 minimum_radius_greater_than=0.968`

In the assessed execution, the second output line gave area approximately 3.14159270863078, perimeter approximately 6.28318536224597, positive first covariance approximately \(1.29637980606\cdot10^{-15}\), and zero second covariance. Because the parameter \(\varepsilon\) is very small, differences in the strict two-angle statistic are correspondingly small; the sign conclusion rests on exact support separation, not floating-point arithmetic. Sampling cannot verify infinitely many derivatives, continuum parameter values or exact distribution equality. Those assertions are proved by the disjoint-support and curvature-radius arguments in `RESULT.md`. No independent validation is asserted.
