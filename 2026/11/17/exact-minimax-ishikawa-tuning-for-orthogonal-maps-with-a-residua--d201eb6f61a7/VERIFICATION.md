---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The fixed space and its orthogonal complement reduce the surjective linear isometry. On the complement the residual bound is equivalent to the upper bound h=1-1/(2kappa²) on the selfadjoint real part of its complexified unitary. The spectrum therefore lies on the unit-circle arc Re(z)<=h, and each point's modulus is witnessed on a real plane by its conjugate-pair rotation (or by -I at the real endpoint). The Ishikawa step is p(U) for the probability triple a=1-alpha, b=alpha(1-beta), c=alpha beta; every triple is feasible. Dividing p(z) by z gives squared modulus [b+(1-b)u]²+(a-c)²(1-u²) with u=Re(z). At u=-1 and u=h this proves a lower bound max(|1-2b|,|h+(1-h)b|). It is strictly larger than (1+h)/(3-h) for b below or above (1-h)/(3-h), respectively. At that b equality at h forces a=c since 1-h²>0. For a=c=1/(3-h) the modulus is the absolute value of an affine function of u and is bounded by that same value, with both ends attained. Converting back gives the stated tuning and positive sharp contraction; the unique triple lies away from the alpha=0 parametrization degeneracy. Normality gives ||p(U)^n||=||p(U)||^n on the complement, so minimizing the worst-case factor for any positive fixed horizon n gives the same optimizer and sharp factor q^n. The endpoint kappa=1/2 is rightly excluded; there only u=-1 remains and b=1/2 leaves a,c nonunique. Replay: spectral reduction and two-endpoint identity in RESULT.md; inspected the frozen verification notes and checker without executing them.

## originality

PASS

The surviving claim is the exact, attained and uniquely parameterized worst-case constant over the stated residual-bounded orthogonal class. The journal article supplies exact fixed-parameter rates for individual rotations as well as a broader nonsharp subregularity rate. Chebyshev alternation supplies the affine interval extremal after symmetrization. Neither establishes the full operator-class minimax and the equality condition ruling out nonsymmetric triples; the strongest distinct indexed degree-two result uses a different spectral problem.

## value

PASS

The residual-bound constant is a natural specification available without knowing a particular spectrum. A class-wide unique tuning and an exactly attained contraction give a usable benchmark for the named two-evaluation scheme beyond general subregularity estimates or a single rotation. Indeed its factor (1+h)/(3-h) is strictly smaller than (1+h)/2, the sharp worst factor of two successive optimally tuned Mann steps with the same evaluation budget, for h<1. The strength is in the class-wide certificate and equality classification, not novelty of interval minimax or finite-horizon exponentiation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
