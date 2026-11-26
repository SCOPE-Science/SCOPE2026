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

For P_{e,w}(1)=2, positivity, constant term one, and coefficientwise KL monotonicity give P_{x,w}=1 or 1+q^h for a common h≥1. If S_w records the ranks of the second class, palindromicity of P_w+q^h S_w gives d_k=[q^{k−h}]S_w−[q^{ℓ(w)−k−h}]S_w. For k<ℓ(w)/2 this is at most the full-flag coefficient at k−1, using rank unimodality when k−h≥0, and is at most zero otherwise. In D₅ the ranks (1,5,14,30,54) agree with the flag product with factor sizes 2,4,5,6,8. Independent exact replay via signed inversion length and transitive closure of decreasing reflections (not reduced subwords) lists all 1920 even signed permutations, longest length 20. At ℓ>6 with d₁≤1,d₂≤5, exactly nine have d₃=14 and none exceed it. At ℓ>8 with the additional d₃≤14, exactly 572 qualify, the largest d₄ is 27 and there are seven candidates. Direct KL right-descent recursion with μ corrections (not the bundled R recursion) gives P_{e,w}=1+q only for the given inverse pair among these candidates with evaluation 2; the remaining candidates all evaluate to 3 or 4. The length-16 vectors and d₀,…,d₇ agree entrywise, and direct inversion gives (−1,4,−2,−3,−5) from (−1,−3,−4,2,−5). The check is exhaustive for the equality sets because the filters are necessary, not a sample of KL classes. The supplied bar-identity implementation uses signed reversed R coefficients, equal to the ordinary R coefficients by R-polynomial reciprocity; this is consistent with its written description.

## originality

PASS

The general inequality in degrees three and four is prior. The supported new content is the exact degree-four gap and the equality classification for both restricted D₅ maxima. The cited type A/B sharpness statements and available KL tables do not compute this type D₅ optimum. An exact group algorithm without its evaluated classification is not an existing numerical bound or census.

## value

PASS

The opposite-degree Betti differences and the constraint P_{e,w}(1)=2 already arise in general Schubert asymmetry theorems, so this is a motivated extremal invariant on the full next simply-laced D rank, not an arbitrary slice of a lookup table. Knowing that the universal estimate is attained at degree three but loses three at degree four in the very same group, with the same unique inverse pair, gives concrete limits to the universal sharpness pattern. A researcher comparing types or investigating the sharpness mechanism can need precisely these exact values and witnesses; no infinite-rank implication is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
