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

The chain rule for conditional probabilities gives the specified product under the stated reset model. The Poisson derivative is Q'_m=e^(−u)u^(m−1)/(m−1)!; dividing by the positive tail gives h_m as in the theorem. Its denominator increases strictly from 1 to infinity, so h_m decreases from m to zero. Consequently each log-success derivative is −λ_i h_(m_i)(a_i e^(−λ_i d_i)), strictly decreasing in d_i. Strict concavity on the compact simplex yields a unique optimizer; at L=0 the simplex is a singleton. The positive marginal loss must equal t on positive gaps and be at least t at zero, by transfer of length between coordinates, with sufficiency by concavity. The resulting inverse lengths are continuous and their sum increases strictly from zero to infinity for t in (min c_i,b): a stage with b_i=b has c_i<b and diverges at b. This verifies the unique multiplier, activation ordering, and the permanent zero when c_i≥b, including equality. At L→∞ the nonminimum stages have the stated finite limits. For i∈M the small-u tail expansion gives b−t=K_i u_i(1+O(u_i)), so the diverging lengths sum to W−H log(b−t)+o(1). Inserting the complementary length D gives the multiplier and all additive offsets in (2). Multiplying the tails, the diverging factors share decay exponent b and joint length L−D+o(1); the other tails tend to positive finite values. This gives the coefficient with e^(bD), not its reciprocal. The three-stage transition equations reduce to the displayed formulas; positive length in stage 2 occurs strictly above the equality threshold. Independently computed example thresholds are 1.0334405869187265338 and 0.5145647539971824762, and 65-digit regularized-gamma/KKT calculations verified tied-stage offsets, multiplier and scaled probability at L=25 and 50. Lower bounds on gaps reduce by a shift of coordinates exactly as stated.

## originality

PASS

Standard separable concave allocation gives the optimality conditions, not a new general optimization principle. The supported distinct result is the evaluated heterogeneous Poisson-tail specialization, in particular the active-set cutoff and explicit tied minimum-product asymptotics with the sharp leading coefficient. The strongest inspected analogues change either the objective, the gap-dependent success law or the asymptotic regime. No inspected source was found to mechanically supply the whole Poisson-quorum theorem. One cited article and an adjacent reliability candidate were not accessible as primary full text; their access limitations are not negative evidence.

## value

PASS

The ideally reset chain is a natural product model in which heterogeneity changes the design in a precise way: some constraints never enter, others saturate, and tied slow exponential losses split the unbounded distance according to the inverse attenuation rates. The exact coefficient and additive offsets let a reader distinguish cases with the same leading decay rate. The entire finite-length optimizer and terminal law are a useful exact benchmark, not a claim that generic multiplier optimization is new or an empirical placement recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
