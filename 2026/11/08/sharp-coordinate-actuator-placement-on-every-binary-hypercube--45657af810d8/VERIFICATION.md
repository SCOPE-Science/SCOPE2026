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

Original mathematical assertions check out: degree j Walsh characters have eigenvalue 2j and form a binomial-dimensional eigenspace, so PBH applies to coordinate-row restriction. For n=2k+1, incidence up/down commutation gives a direct harmonic decomposition. Substituting the lifts reduces the action to a function of t=|x∩R| for each ℓ-set R; repeated lowering and Newton expansion cancel all terms below order ℓ. The surviving difference gives (−2)^ℓ[z^(j−ℓ)](1−z²)^(k−ℓ)(1+z), which yields the stated nonzero signed binomial. Column complementation handles j>k. The original even product placement follows by taking row sums and differences over the last bit; an even middle shell has proportional antipodal rows in degree k. For the repaired spectrum claim, separately checked the commutator recurrence for the unnormalized iterated up-lifts F_r: D_r F_r=(r−ℓ)(n−r−ℓ+1)F_(r−1). This gives ||E_(r,ℓ)h||²=binom(n−2ℓ,r−ℓ)||h||² and orthogonality of distinct sectors by induction (D_r U_(r−1) is scalar on each source sector). Thus the singular values use the square root of the target/source norm factors, with sector dimensions binom(n,ℓ)−binom(n,ℓ−1), including the ℓ=0 case. The supplied integer and modular checks were inspected, not replayed; full rank mod the prime suffices for full real rank but is not a general upper-bound certificate for real rank. The original upper bound for the middle shell comes from exact row proportionality, not modular evidence; the repaired spectral normalization is proved rather than inferred from those tests.

## originality

PASS

The frozen optimal-count claim and odd-layer placement have exact prior coverage, and they are not passed. The completed replacement claims only the closed harmonic-sector action of the fixed-degree Walsh sampling map and its counting-norm spectrum. The earlier controlling shell proof contains neither those coefficients nor the implied exact conditioning; its vanishing propagation can show nonzero action but cannot give its size. The two elementary parity observations of the original record are not used as a stand-alone novelty claim.

## value

PASS

For the known optimal odd sampling shell, recovering coefficients from node values benefits from knowing how each input mode is amplified, rather than merely knowing recoverability. The closed action and singular spectrum give that quantitative answer uniformly for all Walsh degrees, including multiplicities and inverse stability via the least singular value. This is a substantive exact invariant of a motivated sampling matrix, not a rederivation of the known actuator count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
