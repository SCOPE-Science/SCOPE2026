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

# Reproducible checks

Run `python3 verify_gp3.py`. No external packages, randomness, network service or cached output are needed. The checker exhaustively enumerates all proper outer-cycle three-colour words on seven and eight positions, partitions those words by actual dihedral and palette symmetries, and generates every compatible inner word. It then checks all inner edges and all vertex neighbourhoods against a separately generated graph adjacency structure. It verifies exact orbit tables (three orbits totalling 126 words and eight totalling 258), all eleven constructive base cases, equality of the initial six column pairs of lengths 10 through 18, and spliced valid words at lengths 20 through 200. Recorded final output: `VERIFY_OK`.

There is no claim that the finite enumeration establishes existence for unbounded order. The unbounded result follows from the six-column transfer-state concatenation lemma and the exact length decomposition. The algorithm is a finite proof certificate for the two excluded orders, conditional only on the transparent exhaustive loops and conventional Python execution. Self-review do not constitute independent audit.
