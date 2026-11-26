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

Rank standardization gives exactly the set of distinct outputs for a deletion; inserting the erased rank into the standardized survivor word is the inverse relation. Thus pairwise disjoint decks are exactly cliques in the compatibility graph. Inspection of checker.py confirms its pivot recursion visits every maximal clique: an unreported maximal extension must contain a candidate outside the pivot's neighborhood or it could be enlarged by the pivot, and an already used pivot excludes rather than duplicates that extension. The separate JavaScript replay rebuilt the 61-source, 480-conflict graph by both deletion and insertion and obtained all 33,202 maximal cliques (777, 10498, 16495, 5033, 393, 6 at sizes 6 through 11). In a finite graph every clique extends to a maximal one. The six largest cliques exactly match the six codebooks; their seven-word intersection also matches. For even source length the reversal-complement map preserves the up-down signature and commutes with deletion up to the analogous length-five reversal-complement, so its four fixed codebooks and swapped pair really give five orbits. Replay notes: /workspace/branches/ba6a0dcd-e510-409c-bbaa-fbdeaa3352ed/record5_replay.md. Supplied checker inspected, not executed.

## originality

PASS

Best of knowledge, the supported distinct contribution is a matching finite upper bound and a complete equality classification for the one fixed alternating source signature, not the existence of an 11-word code. Crediting the earlier construction is conservative and agrees with an independent syndrome calculation: for inverse ascent bits, the six syndrome class sizes modulo 6 are 10,10,10,11,10,10 and the residue-3 class is exactly the listed third codebook.

## value

PASS

Alternation is a natural complete fixed-signature class in the rank-deletion construction, not a selected handful of favorable permutations. Even when a standard syndrome already supplies eleven words, it does not tell a researcher whether that size is maximal, how much freedom an optimal design has, or which words are unavoidable. The exhaustive classification answers all three for the 61-word instance and supplies an exact benchmark for alternative constructions. No extension to other lengths or to other channels is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
