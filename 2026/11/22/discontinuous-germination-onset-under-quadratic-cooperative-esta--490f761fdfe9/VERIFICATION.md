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

For 0<R≤1 and each 0<g<1, 1−g+Rg²<1 and 1−g<1, so the dormant policy strictly beats every positive g. For R>1, t=−log(1−g) rewrites excess log growth exactly as −t+p h_R(t). Since h_R'' has the sign of (1−2R)cosh(t)+2R, it changes from positive to negative once. H=t h_R'−h_R starts at zero, increases then decreases, and tends to −log R since h_R=t+log R+O(e^(−t)), h_R'=1+O(e^(−t)). Thus the first positive zero t_c is unique, and t/h_R has its unique minimum there. Its limits at zero and infinity are infinity and 1, respectively, with t/h_R<1 eventually, yielding 0<p_c<1. The sign of −t+p h_R gives the strict dormant optimum below p_c and exactly the stated tie at p_c. Above p_c, the derivative at t_c is p/p_c−1>0, and −1+p h_R' decreases strictly from there to p−1<0. This produces the unique positive global maximizer on the falling branch (any earlier derivative root is a local minimum); at zero the derivative is always −1. This root tends to t_c as p decreases to p_c, so the positive onset is a jump. The objective tends to −infinity as t→infinity for p<1, also excluding g=1. In x=√R t the optimized ratio h_R(x/√R)/x converges locally uniformly to log(1+x²)/x. Near zero it is O(x); when t is small and x is large it is bounded by log(1+C x²)/x; away from small t use h_R(t)≤t+log(1+R). These estimates confine maximizers to a compact positive x-interval. The limiting maximizer is unique because log u−2(1−1/u) decreases on (1,2), increases thereafter and changes from negative to positive after 2. This gives the two constants. For the linear payoff, strict concavity and the derivative at zero give the claimed reciprocal threshold and clipped interior optimizer.

## originality

PASS

The supported distinct contribution is the exact global optimizer jump and its strong-cooperation constants for the specified quadratic good-season return. Log growth, seed banking, facilitation and the analogous smooth linear comparison are established or contextual ingredients and are not claimed as independent novel results. The available exact and abstract-level comparisons give no demonstrated prior implication for the quadratic threshold; the strongest inaccessible work is a priority risk.

## value

PASS

For the natural comparison between first-order and cooperative returns in this stylized seed-bank model, the exact optimizer analysis distinguishes a global policy jump with a persistent local dormant maximum from linear continuous onset. The inverse-square-root thresholds with identified constants quantify the change in regime beyond the observation that the payoff is nonlinear. This is useful as a mathematical benchmark for other fraction-based return models, without making an empirical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
