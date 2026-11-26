---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With p_t the loss probability in the transition from the collection after t rounds to that after t+1, conditional on K_t=k the pre-loss size is k+1 with probability (n−k)/n and otherwise k. Independent post-loss survival yields the displayed x_t=p_t+(1−p_t)z recurrence including loss of the newly drawn label. The polar-derivative root argument is valid: for a PGF F of degree k the transformed polynomial P(y)=y^n F(1+1/y) has all zeros in [−1,0]. Its derivative is y^(n−1)[nF+(1−x)F'] at x=1+1/y. By Rolle, every finite zero of the bracket arises from a nonzero zero of P' in [−1,0), so is real nonpositive; P' is not identically zero. Multiplication by x and the affine thinning for p_t<1 keep the roots real nonpositive; p_t=1 gives F_{t+1}=1. This covers repeated zeros, n=1, time zero and both endpoint losses. Normalizing the factors gives a Poisson-binomial count, not independent coupon indicators. Permutation invariance and polarization give the full strongly Rayleigh law. Constant 0<p<1 makes the finite subset chain irreducible (it can clear and build any specified subset) and aperiodic (self-loop at empty); the normalized coefficientwise stationary limit is nonzero and remains real-rooted, hence strongly Rayleigh.

## originality

FAIL

The finite-time property is a direct corollary of a verified earlier, more general update lemma for arbitrary exchangeable input, not just an analogue for a different coupon model. Take complements: a uniform arrival intersects the current vacant set with an independent uniform (n−1)-subset. The earlier hypergeometric lemma covers that exact step. Independent thinning on the occupied side is just an affine PGF substitution, and reversal of a rank polynomial across complements preserves nonpositive real zeros (zero roots may become constant factors). Thus alternate the known update with affine thinning, starting from the empty collection, for every deterministic p_t. The fixed-loss conclusion then follows by closure for the already-known stationary chain. The recurrence itself also follows immediately from the earlier kernel in the single-label case plus recomplementing and thinning. This is demonstrable prior implication, not a claim that an earlier article used the same wording or that the theorem is false.

## value

FAIL

Strong Rayleigh is meaningful for the careless collector, and the analytic proof is readable. But the asserted theorem and recurrence specialize a known hypergeometric transition at removal of one vacant label, then apply an elementary affine substitution, a known polarization criterion and a routine stationary limit. The record does not identify a new stability-preserving operation, quantitative consequence, or independent exact invariant beyond that mechanically implied corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
