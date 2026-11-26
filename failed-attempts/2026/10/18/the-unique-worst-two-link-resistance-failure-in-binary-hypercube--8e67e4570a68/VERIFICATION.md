---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The cube has edge connectivity d, so the deletion leaves a positive definite Laplacian on the zero-mean space. The Woodbury trace correction for incidence columns B is N times the trace of (I−BᵀL⁺B)⁻¹ Bᵀ(L⁺)²B, yielding the stated fraction with c>|t|. In the Walsh expansion an incidence column is supported on characters containing its direction. For parallel pairs the signed summands from the j differing base coordinates expand (1−z)^j; for perpendicular pairs the two forced directions contribute one extra z after integration. Both mixed correlations have the same sign and their absolute values strictly decrease with j. Thus it suffices to compare incident edges and opposite parallel edges in a square. For k=0,1 the ratios of the z-weighted to the (1−z)-weighted integrals under the common density proportional to (−log z)^k(1+z)^(d−2) strictly increase with d, since tilting by 1+z increases E[z] by Var(z)/(1+E[z]). The first ratio exceeds one at d=3. The product of the ratios exceeds one at d=5 by the binomial integrals (t_T u_T−t_P u_P=241/491520) and thereafter. Hence for d≥5 both numerator and reciprocal denominator strictly favor incident edges; only c,s>0 is needed for the monotonicity, not the stronger c>s in the text. For d=3,4 an independent grounded inverse, summing electrical resistances, gave incident versus closest parallel values 154/5 versus 214/7, and 4004/51 versus 36296/465, respectively. The resulting gaps 8/35 and 1196/2635 equal the frozen per-vertex gaps multiplied by 2^d. The equality class and 2^d binom(d,2) count follow by strict comparison and the unique shared vertex. The intact trace baseline follows from eigenvalues 2k with multiplicities binom(d,k).

## originality

FAIL

Distinct published Resultary record 24ab48d1f4b0 contains the same all-d classification, optimizer count, exact maximum and d=3 gap under identical assumptions. The formulas are mathematically identical under the Green-correlation substitution, not simply numerically similar. This is duplicate coverage relative to the indexed corpus; the nominal record dates do not establish priority or lineage.

## value

FAIL

Identifying the uniquely worst failure shape would be a worthwhile robustness benchmark if distinct. Here the classification, optimizer count, exact value and reported gap already occur together in an indexed result. The present alternate proof threshold for the same comparison is not a new robustness regime or useful separate invariant, and no distinct valuable remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
