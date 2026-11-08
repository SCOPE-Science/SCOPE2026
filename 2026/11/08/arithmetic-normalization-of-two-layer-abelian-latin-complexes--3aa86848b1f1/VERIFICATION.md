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

## Mathematical and computational checks
The construction has \(3N\) vertices, \(3N^2\) edges, and \(2N^2\) triangles for any nonzero shift; the proof partitions it into \(d^2\) sheets indexed by ordered coset pairs. Each edge belongs to exactly one sheet; each sheet has \(3m\) vertices, \(3m^2\) edges, and \(2m^2\) triangles. Its links are single \(2m\)-cycles, and the alternating triangle orientation provides an integral fundamental class. The graph of sheet-vertex incidences has \(d^2+3N\) vertices and \(3Nd\) edges and is connected. Its cycle rank is \(3N(d-1)-d^2+1\). These exact steps imply the integral homotopy type; no Smith-normal-form guess or finite sampling is used as an infinite proof.

`verify.py` separately constructs the original full simplicial complex, checks the vertex-link cycle structure and the sheet and incidence counts, and calculates complete mod-two chain ranks for ten finite examples, including noncyclic groups. The recorded output is `verify_output.txt`; the final line must be `ALL_TWO_LEVEL_CHECKS_OK`. No external dependencies are required.

## Scope of verification
Computational ranks test only the supplied finite examples. The integral torsion-free conclusion and arbitrary finite-abelian-group classification follow from the sheet normalization and graph-of-spaces proof, not from mod-two ranks. The source comparisons inspect the current claim's implication relative to the flabby-inflation theorem, the Latin-array single-layer theorem, the published unit-difference homology theorem, and classical connected regular Latin biembeddings. Unindexed equivalent treatments of singular Latin bitrades remain a possible overlap risk. No independent audit has been performed.
