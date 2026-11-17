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

# Exact verification

`VERIFY.py` is self-contained Python 3 standard library code, reading no external scientific data and regenerating all noncrossing partial matchings for \(4\le n\le8\), their chain orbit complexes under rotations, and both cyclic and dihedral actions at eight vertices. `CHECK_OUTPUT.txt` contains its deterministic exact output and terminates with `VERIFY_OK`.

For the octagon, original nonempty simplex counts are \((28,140,140,14)\). Cyclic barycentric orbit cell ranks are \((45,169,168,42)\) and signed unit cancellations are \((44,124,42)\), leaving residual chain ranks \((1,1,2,0)\) and one degree-two boundary coefficient \(2\). Dihedral ranks are \((35,112,105,27)\), with \((34,78,27)\) cancellations leaving a single zero-cell. Every boundary composition is checked as zero before contraction.

The independent quotient two-skeleton computation uses a spanning tree and oriented triangle relators. The cyclic presentation has \(125\) initial generators, \(124\) verified Tietze eliminations, and only \(g^2=1\); the dihedral presentation has \(78\) initial generators eliminated completely. The nonzero cup square follows from the integral Bockstein sequence and universal coefficient theorem, not computational cup-product conjecture. No infinite generalization or independent audit is asserted.
