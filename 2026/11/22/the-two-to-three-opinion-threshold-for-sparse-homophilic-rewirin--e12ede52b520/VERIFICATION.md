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

Reconstructed the microscopic generator under uniform sampling of a discordant edge, fair retention, and weighted sampling from prior nonneighbors excluding self. The total target weight is at least w_min (N−1−K_N), so each specified vertex's arrivals are dominated by a fixed-rate Poisson process and the maximum degree stays o_P(N) over bounded times. Removing the unavailable neighbors and self perturbs the normalized class weights by O((1+max degree)/N) plus the class-proportion error. Thus the unordered-type drift is the displayed average of target-class moves with old type probability x_ab/d and endpoint probability 1/2; the bounded jumps give coordinate martingale variance O(1/N). On any compact interval before d=0 the vector field is Lipschitz on a neighborhood of the deterministic path bounded away from d=0, and a stopped Doob–Gronwall comparison also excludes premature exit from this neighborhood with high probability. For two classes, the concordant count has the same constant limiting normalized compensator rate v on the entire pre-absorption interval, independently of d>0. In particular C_N(t)=C_N(0)+v(t∧τ_N)+o_P(1) uniformly on bounded intervals. Before τ_N cap the approximation at one; after τ_N use the approximation at τ_N to obtain the same uniform error for min(1,C(0)+vt), including C(0)=1. For the matching comparison, endpoint normalizers in units of 1/5 are 9n−8 and 11n−8 for 01, and 9n−6 at either endpoint for 02; each concordant target numerator in those units is 5(n−1). The strict ordering follows since the numerator over the common denominator of 2/(9n−6)−1/(9n−8)−1/(11n−8) is 18n²−56n+32=(n−3)(18n−2)+26. Multiplying the limiting event probabilities 50/99 and 5/9 by N/K_N=3 gives 50/33 and 5/3. Their positive continuous local derivatives even exclude a common law applied only at positive times: both traverse the same short C-interval, where a single drift would have to tend to both limits as C descends to zero. One class is trivial. This is a proof check and exact algebra, not execution of the supplied script or a simulation-based fluid limit.

## originality

PASS

Credit the fixed-opinion stochastic rule, the scalar graphon approximation, and its formal asymptotically linear very-sparse behavior to Nagel et al. The distinct claim supported here is exact sparse convergence on typed edges for the stated class populations and initial sequences, including the universal two-class stopped law and the minimal three-class obstruction. Neither the graphon approximation nor the different stationary active-link model studied in the closest fixed-state lead entails that combined claim.

## value

PASS

The initiating work motivates concordance as a practical coarse coordinate. The theorem identifies precisely the first allowable class count at which that variable ceases to suffice uniformly, while supplying a concrete sufficient typed state and an order-one, fixed-density drift separation on two graph sequences with identical C(0). This is a test of the limits of the approximation's interpretation, not just a numerical comparison or a proposed replacement for its empirical fits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
