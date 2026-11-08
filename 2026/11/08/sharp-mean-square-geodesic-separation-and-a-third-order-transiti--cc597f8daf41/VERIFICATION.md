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

# Reproducibility and verification

Run `python3 check_conical_distance.py` with the Python 3 standard library. The program independently computes the two stationary roots by sign-bracketed bisection, compares the exact squared-distance law to direct area-uniform surface sampling at seven cone angles, checks the phase levels and sampled monotonic intervals, and checks the cubic leading branch mismatch at the flat-angle threshold. For the recorded run it printed `CONE_AREA_DISTANCE_PHASE_AND_MC_OK`.

The geometry is sampled directly: independent radii are drawn as \(R\sqrt U\), independent angles are uniform modulo the full cone angle, and distance is obtained from the metric-cone law with angular truncation at \(\pi\). Monte Carlo comparisons use a six-standard-error plus absolute tolerance; the random seeds and sample count are fixed by the executable. This supplements the explicit analytic proof in `RESULT.md`.

The numerical root intervals verified with 60-decimal trigonometric evaluation are \(0.92537<x_-<0.92538\) and \(2.92216<x_+<2.92218\). The analytic root-count theorem uses signs and monotonicity of the stationary equation, not these numerical brackets. Symbolic differentiation confirmed agreement of the two moment branches through order two at \(x=\pi\), with third-order jump \(-8/(9\pi^2)\).

Independent verification and historical-priority assessment have not been performed.
