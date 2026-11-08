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

# Mathematical verification

`verify_relative.py` is a standalone Python 3 program using only the standard library. Run `python3 verify_relative.py`. Its expected exact output is in `verification_output.txt`.

The program enumerates all complete bipartite shore sizes between two and five, every possible pair of root-shore counts with at least two remaining vertices, and each valid \(r\). The program includes additional empty-root control cases; the theorem itself requires a nonempty root. For each instance it builds maximal faces from the graph connectivity predicate, constructs the proposed independent-set family, and compares the entire down-closed face sets. It computes the reduced Euler characteristic and compares the top-rank formula. For cases with at most eight unrooted vertices it constructs the mod-two boundary operators and checks vanishing outside the predicted top degree. For every case it computes signed fixed-face traces under a nontrivial shore-preserving involution and compares them with the exact exterior-power character formula.

Actual recorded output:

```
CASES_OK=916 HOMOLOGY_MOD2_OK=875 EQUIVARIANT_TRACES_OK=916
ALL_VERIFY_OK
```

The underlying theorem for arbitrary graph sizes follows from the written mathematical proof in `RESULT.md`; finite enumeration cannot establish an infinite-range statement. The representation exact sequence is established integrally, whereas explicit irreducible characters are interpreted over \(\mathbb Q\). No independent mathematical audit has been performed.
