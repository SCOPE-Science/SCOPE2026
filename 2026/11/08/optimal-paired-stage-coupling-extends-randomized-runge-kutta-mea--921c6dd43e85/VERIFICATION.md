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

One step has multiplier R_z(u)=1−z+z²u. Independence across pairs makes H^k the even-index second-moment factor, and the first stage of the next pair adds the fixed finite factor g=E R_z² at odd indices. For the squared multipliers A,B, layer-cake integration of joint survival probabilities yields the lower bound using max(P(A>s)+P(B>t)−1,0) at every s,t. Opposite quantiles realize that bound simultaneously; continuous joint survival functions and the nonnegative integrand of the difference also justify the stated uniqueness at the magnitude level. For z≤1 the multiplier is monotone and nonnegative, so complementary stages minimize. For z>1, the distance |U−a| has density 2 below a and 1 above a; at paired distance w≤a the two branches a±w must be chosen equally, while only the plus branch is used for w>a. This recovers uniform V and reaches the optimal joint magnitudes. Integration on [0,2a], [2a,1−2a] and [1−2a,1] gives the polynomial, with a≤1/4 and a vanishing middle interval at z=2. The iid bound g²<1 covers 0<z≤4/3 by the strictly increasing cubic for (g−1)/z. Above 4/3 the lower quantile branch has derivative zt>0 for t>0 and the upper branch derivative is at least 3−4/z; continuity at the moving branch boundary gives strict increase in z for each interior t. The quantile grows as order z² on an interior t band as z→∞, so H diverges. H(2)=4/5 proves the unique crossing is beyond 2; H=1 does not imply decay for nonzero initial data. Both quoted decimals and z=2 comparisons were checked exactly to the stated precision.

## originality

PASS

The independent stage threshold, complementary-stage stability improvement and countermonotone rearrangement are already known in their respective scopes. The distinct result is the exact optimization for the given scheme on the entire negative real axis, including the folded-magnitude uniform-stage construction, explicit piecewise value and sharp strictly larger stability interval extending past z=2. The inspected scopes do not cover this frontier.

## value

PASS

The scalar test equation is the usual benchmark for negative-axis stability. Two-step dependence at unchanged one-step marginals gives mean-square decay in a regime not attained even by raw antithetic pairing or deterministic midpoint, with a realizable optimizer and an exact exclusion of all other iid-pair laws beyond the frontier. This is a structural regime change and a baseline for comparisons of couplings, not an isolated decimal refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
