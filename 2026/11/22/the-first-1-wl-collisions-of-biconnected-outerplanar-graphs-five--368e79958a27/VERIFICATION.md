---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the finite 1-WL census

Run `python3 verify.py` with the ordinary Python 3 standard library. The script constructs the complete chord families, canonical representatives under dihedral automorphisms, exact common 1-WL classes and all five nonisomorphic witness pairs. It requires no data downloads, external packages, random seeds or external solver.

The actual replay of the included checker returned:

```text
ORDER_3 RAW_1 ISOMORPHISM_TYPES_1 CR_CLASSES_1 COLLISION_PAIRS_0 PASS
ORDER_4 RAW_3 ISOMORPHISM_TYPES_2 CR_CLASSES_2 COLLISION_PAIRS_0 PASS
ORDER_5 RAW_11 ISOMORPHISM_TYPES_3 CR_CLASSES_3 COLLISION_PAIRS_0 PASS
ORDER_6 RAW_45 ISOMORPHISM_TYPES_9 CR_CLASSES_9 COLLISION_PAIRS_0 PASS
ORDER_7 RAW_197 ISOMORPHISM_TYPES_20 CR_CLASSES_20 COLLISION_PAIRS_0 PASS
ORDER_8 RAW_903 ISOMORPHISM_TYPES_75 CR_CLASSES_75 COLLISION_PAIRS_0 PASS
ORDER_9 RAW_4279 ISOMORPHISM_TYPES_262 CR_CLASSES_262 COLLISION_PAIRS_0 PASS
ORDER_10 RAW_20793 ISOMORPHISM_TYPES_1117 CR_CLASSES_1112 COLLISION_PAIRS_5 PASS
PAIR_1 0x8020 0x100040 CHORDS [[0, 7], [2, 5]] | [[0, 8], [3, 5]] PASS
PAIR_2 0x8028 0x100048 CHORDS [[0, 5], [0, 7], [2, 5]] | [[0, 5], [0, 8], [3, 5]] PASS
PAIR_3 0x108060 0x20100041 CHORDS [[0, 7], [0, 8], [2, 5], [3, 5]] | [[0, 2], [0, 8], [3, 5], [5, 7]] PASS
PAIR_4 0x108068 0x20100049 CHORDS [[0, 5], [0, 7], [0, 8], [2, 5], [3, 5]] | [[0, 2], [0, 5], [0, 8], [3, 5], [5, 7]] PASS
PAIR_5 0x128060 0x20120041 CHORDS [[0, 7], [0, 8], [2, 5], [2, 7], [3, 5]] | [[0, 2], [0, 8], [2, 7], [3, 5], [5, 7]] PASS
EXACT_ENUMERATION_AND_FIVE_PAIR_CLASSIFICATION_PASS
VERIFY_OK
```

Each chord is decided exactly once by a recursive inclusion/exclusion branch; including an intersecting chord is forbidden. The canonical graph masks are the least over all dihedral images. The uniform-start 1-WL computation uses sorted full neighbor-color tuples rather than probabilistic graph hashes. The pair replay checks equal color multisets at every round as well as distinct canonical masks.

An auxiliary independent NetworkX WL-hash census agreed on zero collision pairs for orders 4 through 9 and five for order 10; it is corroboration and is not the proof since hashed signatures in general could collide.

**Limits.** Exhaustiveness stops at ten vertices; the source code plus finite execution constitute a transparent computational certificate, not a formally verified implementation or a proof of any unbounded statement. Independent mathematical audit has not been performed.
