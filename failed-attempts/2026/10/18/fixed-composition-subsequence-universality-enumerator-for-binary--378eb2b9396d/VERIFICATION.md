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

The index equals the maximum number of ordered disjoint complete-alphabet blocks: choosing one requested letter from each block proves universality in one direction, while the greedy arch ends followed by a symbol missing from the rest exhibit a missing subsequence in the other. For a palindrome let ℓ be the end of the last of the r greedy arches of its left half, or zero when r=0. An ordered sequence of 2r+1 complete blocks must have its middle block after ℓ (earliest possible end of r complete blocks) and before n+1−ℓ (latest possible start of r complete blocks by reversal). Thus that block must fit in the rest, optional center and reversed rest. At most one block can meet the midpoint, so 2r+2 complete blocks are impossible. The 2r left/right blocks always exist, and one more exists exactly when the odd center is opposite to the nonempty constant rest. This proves the rule including empty or constant halves, rather than assuming the positive-index hypothesis of the cited proposition includes them. Each half-letter then marks two full letters; the two completed-arch types give H=u²y²x⁴[(1−x²)⁻¹+(1−y²x²)⁻¹]. The rest-and-center factors in the frozen proof count all possible centers once with their actual weight and apply u exactly when the midpoint adds a block. Multiplying by (1−H)⁻¹ and clearing the two geometric denominators gives the stated rational identity. I also generated all 1021 palindromes through length 16, encoded their distinct subsequences directly, and checked denominator times the census coefficientwise against the numerator through that length. The length-16 weight-8 example gave counts 2,16,36,16 at indices 2,4,6,8. This is finite corroboration, not the proof. The inspected supplied checker can be replayed with python3 VERIFY.py in the frozen package; it was not executed here.

## originality

FAIL

No inspected source directly prints this exact trivariate expression. However, the exact joint series is mechanically recoverable from the indexed composition-refined arch and rest functions together with the indexed palindrome enumeration's midpoint and completed-arch formulas; the latter uses the published palindrome center rule. This is demonstrable implication, not a priority verdict: the most closely matching indexed records are in later date directories. The unweighted palindrome marginal or the whole-word type-class marginal alone would not establish overlap for the full joint law.

## value

FAIL

The labeled fixed-composition palindrome inventory is natural and the weight-refined coefficients are useful, but in the inspected comparison the exact law is a mechanical substitution into an already letter-resolved arch series and a known palindrome completion decomposition. The explicit algebra and sample census add no separate surviving exact result beyond that implication. This judgment is not based on the finite size of the example or a demand for further downstream applications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
