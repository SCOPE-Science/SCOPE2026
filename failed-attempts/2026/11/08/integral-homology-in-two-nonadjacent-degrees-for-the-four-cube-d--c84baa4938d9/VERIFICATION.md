---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Verified the exact closed-neighborhood/complimentary-domination face definition on all 65536 masks in an independently written and compiled C++17 program. Reconstructed the entire nonempty face poset (45706 faces), every one of 329552 cover incidences, the 22847 disjoint greedy pivot matching pairs and the 12 critical cells {0:1,7:10,9:1}. A fresh Kahn sort visits all 45706 faces after reversing precisely the matched incidences, proving acyclicity. The independently implemented reverse pivot order also gives the same critical cells and complete acyclicity. The facet vector {7:10,10:80,11:40} and reduced Euler characteristic -11 agree. Lower-dimensional checks give (d=1) {0:2}, (d=2) {0:1,1:3}, (d=3) {0:1,3:7}. Forman discrete Morse theory then supplies one 0-cell, ten 7-cells and one 9-cell: every cellular differential is zero due to absence of adjacent-dimensional cells, proving torsion-free integral H7=Z^10,H9=Z and six-connectivity. No assertion about the nontriviality of the 9-cell attaching map or all hypercubes is made. The initially mistyped Euler-sign comparison in the auditor’s checker was corrected by direct complement parity; only the corrected complete check is cited.

## originality

FAIL

The exact graph/complex/homology theorem is explicitly proved in the earlier SCOPE 2026-11-01 source and corresponding published Resultary record. That primary source was first committed on 2026-11-01T20:50:45Z, seven days before the assigned source at 2026-11-08T17:30:12Z. It gives identical homology and the same Morse counts, plus full hyperoctahedral character and five-cube corollary. Exact mathematical implication, not mere title similarity, is decisive. The later public mirror had a 2026-11-08 commit, but the underlying actual source was already recorded on November 1. No novel remainder can be inferred from the assigned package.

## value

FAIL

The topology of the four-cube dominance complex is a natural and significant exact finite invariant, so finite scope by itself would not defeat value. However the whole claimed invariant—torsion-free Z^10 in degree seven and Z in degree nine, plus six-connectivity and complete acyclic Morse witness—is already fully calculated in the prior stronger 2026-11-01 theorem. The assigned source contributes no new homotopy attaching map, new equivariant invariant, new structural lemma, or distinct natural classification. As a later recomputation of a known exact result it lacks independent mathematical value under the shared bar, despite being correct and reproducible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
