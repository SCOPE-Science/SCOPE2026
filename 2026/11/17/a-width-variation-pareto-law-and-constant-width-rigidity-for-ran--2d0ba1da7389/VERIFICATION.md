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
# Reproducible mathematical verification
The exact normal-line intersection equation is derived in `RESULT.md`, equation (1). The only nonremovable singularity is antipodal and its numerator is \(w'(\theta)\). For \(q=Rs\), the conditional densities are supported in a fixed bounded angular strip and converge to the displayed limiting density, whose integral is exactly one. Scheffé's lemma provides the asserted total-variation statement. These are analytical checks, not computational substitutions.

The companion `normal_intersection_checks.py` uses 4,000,000 uniformly sampled normal-angle pairs for the strictly convex Fourier support \(h=1+0.2\cos(2\theta)\), which has curvature radius at least 0.4. Ratios of empirical \(R\Pr(\|Z\|>R)\) to the exact coefficient at thresholds 20, 40, 80, 160 are 0.99991, 1.00405, 1.00818, 0.98795. It separately tests \(h=1+0.1\cos(3\theta)\) with curvature radius at least 0.2, a noncircular constant-width example, and reports a bounded sampled maximum. Output ends in `NORMAL_INTERSECTION_CHECKS_OK`.

Run with Python 3 and NumPy: `python normal_intersection_checks.py`. Finite sampling does not prove uniform boundedness or exact asymptotics; these follow from the support-function proof. No independent audit or external mathematical validation has occurred. Historical priority is provisional.
