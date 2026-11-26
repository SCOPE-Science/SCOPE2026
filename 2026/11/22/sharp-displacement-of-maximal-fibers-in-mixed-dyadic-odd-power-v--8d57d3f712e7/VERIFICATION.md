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

Odd exponentiation is bijective on dyadic units (the group has 2-power order), and reduction to the needed precision after taking out a power of two is surjective. This gives precisely the exponent-multiple valuation shells plus zero. At target valuation v, two lower equal shells give exactly one complementary partner per element, and an unequal-shell pair must have minimum valuation v; zero summands and the zero target give the stated extra terms. Squaring and summing by shell gives the energy. The |B_k| cap is attained at zero for k≤d and throughout shell d for k>d: subtraction of an odd b leaves an odd value; subtraction of an even b or zero preserves valuation d. Zero attains the cap exactly when B_k⊆A_k, equivalently k≤e or d divides e. Odd targets have exactly the sum of the two even-part sizes, bounded above by 2+2^k/7, strictly below the common odd-plus-odd contribution 2^(k−1) for even targets when k≥3. All odd targets already come from an odd and zero; every even target for k≥1 comes from two odd values. k=0 is the singleton case. Independent bounded enumeration corroborated all fibers, energy and extremal statements on seven exponent pairs and depths through 10; local replay: python3 /workspace/branches/review_replay.py 3. The frozen checker was inspected, not executed. Its 14,637 marker increments for two conditional assertions even when skipped, so it is an accounting marker, not a literal assertion count; the general proof does not use it.

## originality

PASS

Known unit-shell structure and general convolution/character methods are not new. The supported distinct result concerns mixed unweighted ordered values and the sharp maximizing-fiber displacement with depth, particularly attainment of the cardinality cap when the two images are not nested.

## value

PASS

Ordered convolution of the two natural dyadic power-value images measures concentration beyond mere coverage. The sharp cap being attained even without nesting, and the exact transition at which zero permanently loses optimality, are structural facts useful for diagnosing the concentration of these arithmetic sets. The shell formula provides depth-based computation of an arbitrary fiber and energy without residue enumeration; the value is not in a finite checker or reformulating energy alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
