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

The self-overlap exclusion is exactly the unbordered-word condition; compatibility of two vertices requires absence of both orientations of overlap. Cliques therefore correspond exactly to codebooks. In verifying the source upper bound, each color class is independent in the compatibility graph, so the remaining color count bounds the largest extension. The recursive choice of the last available vertex followed by removal from the parent exhausts cliques not pruned by this valid bound. An independent finite reproduction used the length-one overlap to reduce every nonempty code at n>1 to common first bit 1 and last bit 0, up to reversal. It generated eligible words from the binary cube, formed conflicts by equal prefix/suffix buckets, and used degree order and first-fit coloring for an exact clique search. It matched all reported capacities, eligible-word counts, and witness sizes for n=1 through 16, and checked every published witness against the language and every proper overlap in both orientations. In particular M_15=30 and M_16=42, and none of the earlier entries reaches 32. For the reversed marker families, the gaps between consecutive ones must be 1 through k−1 zeros, with exactly k trailing zeros and at least two ones. The independent composition recurrence counts all families at n=16 and gives 24 at both k=4 and k=5. This is consistent with the finding's nonexclusive claim of attainment at k=5. Thus the unrestricted choice within the no-11 language yields five whole payload bits versus four for the specified marker families.

## originality

PASS

The prefix/suffix construction framework and its asymmetric run-limit extension are already covered at the method level, and the classical fixed-zero-marker family is known. The supported distinct finding is the exact optimization table in the one-sided no-11 language, the certified first 32-word length, and the corresponding numeric gap to the restricted marker construction. The closest inspected primary results give all maximal codes through a general construction or compute optima for other constraints, not this finite asymmetric optimum table.

## value

PASS

For a basic constrained binary language, precise capacity immediately answers the minimum fixed-length question for a concrete five-bit block payload. The table rules out all shorter lengths and certifies a feasible code, rather than illustrating only one construction at one length. The exact separation from the standard marker families crosses a whole-bit boundary and shows why choosing the common construction alone would miss feasible payload within this model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
