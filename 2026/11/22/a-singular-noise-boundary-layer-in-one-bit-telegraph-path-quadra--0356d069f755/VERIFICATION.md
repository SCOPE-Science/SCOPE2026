---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independent Poisson increments give the covariance kernel e^(−a|s−u|)−e^(−a(s+u)) in normalized time. Integrating it once gives D(z)/a and twice gives (2a−3+4p−p²)/a². An independent flip scales covariances by c; because the bit has two values, its conditional mean estimator is exactly affine, so the variance reduction is c²D²/[a²(1−c²z²)], not a linear-estimator bound. At c=0 it vanishes; at c=1,z=1 the deterministic bit gives the prior variance, also the continuous limit since D vanishes linearly at z=1. In the informative interior D>0. The derivative numerator for D²/(1−c²z²) has sign S=p/z²−(2−p)+2c²(z−p). S''=6p/z⁴>0, S(p)=(1−p)²/p>0, and S(1)=−2(1−p)(1−c²). For c<1 these give one crossing with strictly negative slope. When c=1, z²S=(z−1)(2z²−pz−p), and the positive quadratic root is interior with the same derivative sign. The implicit root increases with c², hence the optimal normalized time decreases with reliability. For rare switches, with δ=1−c², the uniform expansion has leading terms −2aδ(1−u)+a²[3u²−2u−δ(u²−1)] and remainder O(a³). At fixed δ>0 this gives 1−u∼a/(2δ); with δ/a→κ<∞ the limiting equation is 3u²−2u=2κ(1−u), and the perfect-bit lower bound u→2/3 excludes the zero root at κ=0. With δ/a→∞ the same expansion forces u→1. For fast switching, the uniform bracket √p/2<z_*<√p gives p/z_*²=2+O(√p) by the exact equation and hence the stated uniform log-time expansion. Replay: RESULT.md §§1–5; VERIFICATION.md, requirements.txt and verify.py were inspected, not executed. This is an exact known-start, known-rate, one-predetermined-bit result; the numerical grids and simulation are supplemental.

## originality

PASS

The distinct scope is the exact globally unique design time and singular noisy-channel rare-switching law for estimating a signed occupation integral from one corrupted state bit. The telegraph integral, parity covariance, and binary conditional-mean identity are prior ingredients. Inspected nearby results concern different stochastic processes, different encoding classes, or a different direction of inference and do not imply the optimizer and crossover here. No exclusive priority claim is made.

## value

PASS

Timing a single constrained observation to estimate an accumulated duration is a natural design problem. In the rare-switching regime, the physical randomness in the observed state is of order a while the independent flip contributes variance of order 1−c²; their competition creates an explicit nonuniform crossover. The move from limiting time 2/3 to the endpoint and the quantitative layer between them are structural effects, not a numerical adjustment to a single design point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
