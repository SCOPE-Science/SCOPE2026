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

# Exact finite verification

Run, with Python 3 standard library only:

```sh
python3 verify_direct.py
python3 verify_forbidden.py
```

Both scripts build the two sixteen-vertex adjacency structures independently from coordinate rules. `verify_direct.py` visits all combinations of vertices and checks total domination and every closed-neighborhood identifying signature. `verify_forbidden.py` builds sixteen complements of open neighborhoods and 120 complements of closed-neighborhood symmetric differences; it marks all submasks of these caps. Their methods are equivalent by the explicit forbidden-cap lemma, but their implementations and traversal are distinct. The algorithms assert every coefficient and produce identical complete 65,536-byte membership bitmap hashes per graph.

Recorded values:

| Graph | Size-6 codes | Size-7 codes | Size-8 codes | Size-9 codes | Bitmap SHA-256 |
|---|---:|---:|---:|---:|---|
| Rook | 1056 | 5520 | 10170 | 10800 | `9d8d0ad3f0e7e26b8737e31617483ac657db0e4340475b25880a5e4cc845fcd7` |
| Shrikhande | 1040 | 5584 | 10206 | 10800 | `571438a8c5572fa534b1eb16e2cdc80cba596dcd92b1fc8fcb8b905f405fb912` |

Both programs assert the complete remaining coefficient vector. The direct program confirms degree six and exactly two common neighbors for any distinct vertex pair. The second program confirms the 64 ten-vertex forbidden caps are distinct, with pairwise intersection size at most eight; this also proves the binomial high-degree tail. Execution outputs are retained as separate text artifacts.

**Limits:** The exhaustive universe comprises exactly all vertex subsets of these two specified sixteen-vertex graphs. This is not a theorem about arbitrarily large strongly regular graphs. Replayability and self-review are not external independent auditing or publication-priority certification.
