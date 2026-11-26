---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In the stationary causal convolution, the orientational dot kernel is C(u)=exp(-d|u|)cos(wu), and the independent translational noise has zero mixed covariance. The difference divided by v is the integral of exp(-ks)[C(t-s)-C(t+s)] over s>=0. Splitting at s=t and integrating exponentials gives the stated a and b, with A'(0+)>0. For k<d and w>0 both coefficients are positive; after arranging the zero equation as exp(-(d-k)t)cos(wt+phi)=cos(phi), the initial positive lobe decreases from the level and contributes no positive root. The j-th later positive lobe has its unique maximum at (2πj-delta-phi)/w, with negative second derivative there. Its height exceeds the root level iff j<z and equals it iff j=z, giving the stated rounding rule including quadratic contact and exclusion of t=0. At fixed d,w>0 the logarithm in z is smooth as k tends up to d, so the coefficient of 1/(d-k) and O(1) remainder follow. At k=d>0 with w>0 the two cosine solutions per period are distinct and simple. For k>d and w>0 the oscillatory term dominates after factoring exp(-dt); both the residual and its derivative decay in that normalization, giving infinitely many eventual simple sign changes. At w=0 the scalar difference has positive sign for k≠d and extends to vt exp(-dt) at k=d. Independent replay: python3 /workspace/checks/frozen_replay.py 3; four covariance quadratures including matched and achiral limits, and sampled sign counts 0,2,14 for w=1,3,10 at k=1/2,d=1. Sampling corroborates but does not prove the counts or certify tangencies.

## originality

PASS

The supported distinct contribution is the exact integer staircase, tangencies and regime classification for the stationary mixed heading–position dot statistic in the planar chiral harmonic model. Exponential kernels and lobe counting are standard; related equal-time, velocity–heading and positional memory results are not the same classification.

## value

PASS

For a measurable stationary lag statistic, the exact finite count, its tangencies and its growth at rate matching are stronger than detecting some oscillation. The formula separates robust sign reversals from touches and isolates the roles of trap, orientational noise and chirality, with thermal positional noise and the positive swimming amplitude irrelevant to the zeros. This is a benchmark for the ideal harmonic model, not a finite-sample detection or generic irreversibility theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
