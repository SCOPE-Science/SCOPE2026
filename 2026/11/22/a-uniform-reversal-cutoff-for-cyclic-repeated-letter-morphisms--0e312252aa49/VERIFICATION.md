---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The increment-first-letter boundary rule gives all ordered pairs, so for n <= 9 the length-nine second-substitution blocks over those pairs supply the whole language. Independently, the adjacent differences in the two-block window are D, wildcard, D with D=(0,1,-1,0,1,0,0,1); the wildcard is arbitrary because both block letters range freely. Reversal negates and reverses the differences. Comparing templates for n=3,...,9 uses only the distinguishable constants -1,0,1 modulo q>=3; there are 54,27,15,7,3,1,0 matches respectively, every match fixes every difference, and their integrated normalized signatures reproduce the stated table. The distinct signatures remain distinct modulo every q>=3. Directly reversing them gives 2,1,1,1,1,1,0 palindromic types. Lengths 1 and 2 are elementary; above length 9 any reversible factor would give one at length 9, and the length-eight palindrome makes the barrier sharp. Replay paths: /workspace/branches/audit-2-differences.py (difference-template reconstruction, also independently evaluated) and the exact weighted-disjoint-set enumeration /workspace/branches/7d5b45f9-3fe3-47f9-81d0-ea2796f3c76d/audit_certificate.py (executed and independently corroborated at q=3,4,5). The frozen graph and direct-prefix scripts and captured outputs were inspected, not executed; finite-prefix sampling is not used to establish the universal claim. The result does not cover q=2.

## originality

PASS

The q=3 substitution and its pair completeness are known, as are related substitution families and sharp barriers for other words. The evidence does not establish prior equivalent coverage of this family’s ordinary reversal/palindrome spectrum and sharp common cutoff. The distinct same-day same-family record concerns a different property and no priority is inferred from dates.

## value

PASS

This fixed point is a recognized automatic construction. The exact transition from a sharp length-eight palindrome to absence of every reversible factor at length nine is a strong directional property, beyond just nonclosure under reversal or a finite experimental cutoff. The table distinguishes palindromes from reversible nonpalindromes and its modulus-independent certificate makes it useful across the whole family, not merely at a single small alphabet.

The dated certificate retains the supplied scientific assessment, sources and limitations.
