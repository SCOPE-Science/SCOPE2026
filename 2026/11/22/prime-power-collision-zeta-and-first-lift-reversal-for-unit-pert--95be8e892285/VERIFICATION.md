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

The ordered collision congruence is (x−y)(x+y)(x²+y²+c)≡0. The conic has p−χ_p(−1) points: for a=−c≠0, factoring v²−u² as (v−u)(v+u) gives sum_x χ_p(x²−a)=−1. The lines meet at the origin off the conic, and each meets the conic in 1+η points. Inclusion–exclusion gives U=3p−3−ε−2η, with I=3+2η double crossings and no triple points. At a simple point, prescribe the coordinate complementary to a unit partial derivative and lift the other, giving p^(k−1) solutions. At a crossing the two vanishing factors form local coordinates: the Jacobian determinants are units, up to signs 2 and 4t with t≠0. Digit-by-digit inversion gives the same residue-disc bijection modulo every p^k. The third factor is a unit and the local equation is uv≡0 with u,v≡0 mod p. The u=0 term gives p^(k−1) choices, and each valuation i=1,…,k−1 contributes (p−1)p^(k−1), so E=p^(k−1)[U+(k−1)(p−1)I]. This includes p=3 and k=1, and only the residue class character of the unit c survives. Subtraction gives the advertised first-lift sign flip; summing the two geometric terms gives the pole and the factor-of-five change, and E/p^k−1 is the variance since mean fiber size is 1. The independent replay `/workspace/branches/7426aeda-fc46-47cd-9fcb-e98c8fce40d1/record2_replay.py` directly tested all 80 unit coefficient cases at p=3,5,7 and k=1,2 (114240 ordered comparisons). Class differences were −4 at k=1 and 12,60,140 respectively at k=2. The frozen nested `artifacts/verify.py` and its self-reported run are separate, and neither finite test replaces the lifting proof.

## originality

PASS

The supported distinction is the explicit all-precision ordered equal-value count for this quartic family and the reversal driven by the coefficient-dependent number of crossing disks. Normal-crossing lifting is standard; neither a new lifting theorem nor priority for mod-p quartic analysis is claimed. The same-map additive-energy results and finite-field intersection results do not supply the prime-power second fiber moment.

## value

PASS

For a natural low-degree family the result explains why finite-field collision ordering predicts the wrong ordering at every higher precision: additional transverse crossings contribute a growing valuation term. The explicit all-k formula, rational series and two variance slopes give usable quantitative information about unevenness of fibers, not just a numerical comparison at p² or a rephrasing of graph energy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
