---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For a palindromic host H, any embedding of a palindromic scattered output has the termwise minima of each early embedded left-half symbol and the corresponding reflected late symbol as strictly increasing positions in the host left half A. Conversely any V subsequence in A completes by reflection to VV^R, and an allowed left-center Vd in A completes to VdV^R. In even AA^R, odd centers must lie in a half; for odd AcA^R the central c creates VcV^R for every V∈Sub(A), while off-center d≠c requires Vd∈Sub(A). The resulting disjoint language decompositions are injective by palindrome length and center, giving F_even=S_A(t²)+t^(-1)S_A(t²), F_odd=S_A(t²)+t(1+S_A(t²))+t^(-1)(S_A(t²)-E_{A,c}(t²)) for arbitrary finite alphabets and A including empty. Independent finite language enumeration corroborates exact languages but not the universal proof.

## originality

PASS

Best-of-knowledge originality after comparing statements, direct implications and inspected primary source material.

## value

PASS

Distinct palindromic scattered subsequences are a natural but nontrivial language invariant. This classifies the entire graded palindrome language of all symmetric hosts over arbitrary alphabets in terms of just their half-word distinct subsequences and one end-letter correction, simplifying a general palindrome automaton to an exact reusable closed form. The arbitrary repetitions/central letter adjustment are not merely the known distinct-letter binomial case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
