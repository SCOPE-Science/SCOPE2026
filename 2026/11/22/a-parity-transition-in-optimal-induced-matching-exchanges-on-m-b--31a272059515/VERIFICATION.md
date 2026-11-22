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

# Reproduction and verification

Execute the standalone Python 3 scripts included with this result, with no nonstandard package dependencies:

```bash
python3 verify_rim.py 12
python3 check_twisted.py 12
```

Both commands executed successfully and produced identical optimum sizes, counts, degrees and exchange connectivity for all integers from 4 through 12. The rim verifier constructs the cycle-plus-chords graph and performs an exhaustive maximum independent-set search in its edge-conflict graph. The twisted-column verifier independently builds the rail/chord graph and checks every candidate induced matching of the theorem's optimal cardinality using endpoint adjacency; it does not use the first verifier's conflict graph, enumerator or construction.

The expected checked records are:

| n | size | number of optima | exchange structure |
|---:|---:|---:|---|
| 4 | 2 | 2 | isolated |
| 5 | 2 | 25 | connected, 10 of degree 4, 10 of degree 5, 5 of degree 6 |
| 6 | 3 | 6 | isolated |
| 7 | 3 | 49 | connected, 28/14/7 at degrees 4/5/6 |
| 8 | 4 | 2 | isolated |
| 9 | 4 | 81 | connected, 54/18/9 at degrees 4/5/6 |
| 10 | 5 | 6 | isolated |
| 11 | 5 | 121 | connected, 88/22/11 at degrees 4/5/6 |
| 12 | 6 | 2 | isolated |

All-order correctness derives from the accompanying combinatorial proof of column separation, the complete gap-two transitions, twisted-seam closure, and the classification of every legal one-edge exchange. Finite checker success does not prove the statements for every \(n\), nor does it exclude unindexed earlier literature. The same-object 1998 enumerative paper was not available in full through the open repository, so its precise coverage remains uncertain. No independent scholarly validation was performed.
