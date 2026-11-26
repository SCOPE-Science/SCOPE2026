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

I reconstructed the identity with the specified measures. Character orthogonality supplies q³ against q^(−6), and Newton identities determine a multiset of three roots from three power sums since 2 and 3 are invertible, also over nonprime fields. Each surviving second triple is a rearrangement of the first and all coefficient phases cancel. The multiplicity classes have probabilities S₃, 3(S₂−S₃), and 1−3S₂+2S₃, and respective rearrangement counts 1, 3, 6, giving F₃=6−9S₂+4S₃. For unordered pairs, I recover Σ(θ_s−θ_t)²=qS₂−1 and Σ(θ_s−θ_t)²(θ_s+θ_t)=qS₃−S₂ by counting each θ_i square or cube q−1 times and expanding the mixed terms. The difference reproduces (1) on the probability simplex and is termwise nonnegative. The variance in (2) equals qN²||θ−ν||₂². A nonuniform zero remainder requires an unequal pair summing to one; a third, zero coordinate then forces at most one positive mass. Uniform law and point masses indeed saturate, and a point mass has nonzero variance and forces sharpness. The cubic expansion yields 9−12/q as the local quadratic coefficient (not the Hessian eigenvalue, which is twice that). The zero function is covered separately by (2).

## originality

FAIL

The claimed sharp invariant, its equality alternatives and its local/global comparison are mechanically implied by accessible prior results, even without an earlier source restating the exact coefficient in extension notation. The known cubic rearrangement formula gives D=(9−12/q)r²−4∑h_t³, where h=θ−ν and r=||h||₂. Wilkins's classical sharp finite-sample skewness bound gives ∑h_t³≤[(q−2)/√(q(q−1))]r³. The simplex bound r≤√(1−1/q) gives D≥(5−4/q)r² immediately. Every nonuniform equality case must attain the simplex radius, so is a point mass, where direct substitution attains the coefficient. The earlier local result supplies the local comparison, also immediate from the cubic. The explicit pairwise square display was not identified in an earlier inspected source; its left-over cubic polynomial is already determined by the known moment and sharp estimate, and its symmetrization supplies a different proof, not a separate new sharp invariant. The later exact catalogue match is noted as overlap, not used as earlier priority.

## value

FAIL

A sharp stability estimate with sparse equality would have substantive value if it were not already a short consequence of known sharp sample-moment control and the cubic collision functional. The pairwise certificate is a clean proof and can be pedagogically useful, but here it symmetrizes the residual already fixed by subtraction and gives no additional quantitative bound, classification, or distinct motivated invariant beyond the mechanically implied result. This fails the value threshold for the submitted purported new exact finding, not the mathematical validity or general interest of stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
