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

Insertion-deletion distance equals combined interval length minus twice LCS; hence strict synchronization iff R(w)<epsilon. Squarefree pruning is exhaustive below ratio one and restricted-growth words uniquely represent alphabet-permutation orbits. I independently wrote, compiled and ran a C++17 canonical square-free enumerator using bit-parallel LCS, distinct from the source C++ DP and Python bit-vector implementations. It reproduced every layer, the exact 27 count 2581/minimum 20/23/one orbit and 28 count 3370/minimum 8/9/thirteen orbits. The 28-prefix hereditary obstruction correctly extends strict epsilon<=8/9 to all longer words; at epsilon=20/23 the 26 length optimum 6/7 remains valid.

## originality

PASS

The October 18 published theorem already proves the length-27 unique extremizer and exact gap 3/23 and forbids 28 symbols for epsilon=7/8. These facts are NOT new and are explicitly excluded from the novelty claim. The present work determines the strictly stronger exact n=28 minimax value 8/9, thirteen canonical minimizers and the full first-28 spectrum, extending the strict length-27 cutoff from epsilon=7/8 up to epsilon=8/9. No inspected earlier source implies the new threshold; substantial previous overlap is a major qualification.

## value

PASS

The exact 28-length LCS minimax and all 13 normalized extremizers constitute a natural complete finite extremal classification. It strengthens an established strict length cutoff over the entire nonempty interval 7/8<epsilon<=8/9, even though the 27-word optimizer was previously known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
