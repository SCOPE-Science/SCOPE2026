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

# Reproducibility and boundaries

Execute `python3 edge_check.py` from this directory with only Python's standard library. The checker derives both parity-neighborhood complexes directly from their graph neighborhoods after deleting the graph edge from binary words zero to one. For each integer dimension from three through eight, it counts every face by dimension, computes the mod-two ranks of the first three simplicial boundary maps, checks the predicted reduced two-dimensional Betti ranks, and checks that coordinate-bit toggling swaps the two sheets simplicially. Its recorded output is `edge_check.out` and the final line is `PASS: 12 parity components, 77718 nonempty faces, direct mod-2 boundary computations`.

These are finite binary-chain checks; they do not verify integral torsion-freeness, simple connectivity or the all-dimensional statement. Those follow from the explicit elementary collapse, triangular-relator replacement, cellular Euler argument and relative integral homology proof in `RESULT.md`. The integral inclusion-cokernel identification is a mathematical proof, not a computer certification. No independent mathematical audit has occurred.
