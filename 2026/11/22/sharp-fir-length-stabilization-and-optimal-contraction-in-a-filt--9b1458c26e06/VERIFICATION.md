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

At a constant state p the equation is G²p²+(1−β)p−α=0, with one root of each sign. The first delay-Jacobian row is −2Gp c_j+β·1_{j=1}, with unit subdiagonal; thus P_p(1)=1−β+2G²p=±√Δ. On the positive branch, the product of distances from 1 to the multipliers is at most (1+ρ)^n. When √Δ>1, equality at ρ=√Δ^(1/n)−1>0 means every root equals −ρ, by equality in each triangle inequality and radius bound. The monic coefficients determine the taps injectively. The coefficients of (z+ρ)^n, with the β compensation at tap 1, are strictly positive and sum before division to (1+ρ)^n−1+β=2G²p_+. For √Δ≤1 the delayed selector gives z^(n−2)(z²+√Δ−1), with radius strictly below one; a sufficiently small interior perturbation of the normalized taps preserves Schur stability. This includes n=2 and √Δ=1. The closed-disk attainment at √Δ=2^n is unique; above this threshold the universal bound forces a multiplier outside. Finally, P_−(1)<0 and the monic polynomial tends to +∞ on the positive real axis, giving a real multiplier >1 on the negative branch.

## originality

PASS

The map, stationary branches, gain dependence, and Jacobian precedent are known, as is the elementary root-product argument in its general mathematical form. The inspected closest work analyzes selected filter families rather than optimizing all taps. The distinct result supported here is the attaining positive design, sharp all-length gain frontier and rigidity under the fixed-sum constraint, not the companion linearization or root-product bound by itself.

## value

PASS

Optimizing the local spectral radius at fixed feedback gain answers a concrete design question left open by stability diagrams for prescribed filters. The result gives a realizable positive design, rules out improvements even with signed coefficients, and quantifies a substantial length effect: the gain frontier grows exponentially in length and the best radius at fixed high feedback falls on the order of 1/n. The simple polynomial argument supplies a sharp structural boundary rather than merely renaming the known fixed-point equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
