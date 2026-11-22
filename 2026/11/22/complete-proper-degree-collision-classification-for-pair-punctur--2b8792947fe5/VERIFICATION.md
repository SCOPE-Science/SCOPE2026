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

# Reproducible verification

From a directory containing `verify.py`, execute `python3 verify.py` (Python 3.10+ standard library). The corresponding exact stdout is included in `verify_output.txt`; the final line is `VERIFY_OK`.

The verifier independently generates Fano and affine-9 Steiner triple systems and a cyclic 13-point system; it validates all Steiner pair-covering conditions and compares every two-puncture leave-graph matching polynomial with the cycle-factor product. It also computes a formal power-series inversion of each complete cycle polynomial as a separate check.

For the explicit 15-point witness, every one of its 105 old pairs is checked to lie in exactly one of the displayed 35 triples. For all 105 choices of deleted pair, the leave edges are reconstructed from scratch, every cycle checked to be even of length at least four, the entire polynomial independently enumerated by edge-inclusion recursion, and the recovered cycle partition cross-checked. The punctures \(\{1,2\}\) and \(\{3,13\}\) give the predicted coefficient vectors, differing by two only at the maximum degree. A separate combinatorial enumeration of all even-cycle partitions on \(N=4,6,\ldots,32\) checks that the sole proper-degree collisions have the proposed shape.

These finite tests do not independently certify the theorem for arbitrary size. That universal step follows from the formal logarithmic triangular-recovery lemma, the short-cycle deletion argument, and the algebraic identity in `RESULT.md`. All outputs concern finite relational one-point diagrams, not complete model-theoretic types or computational certification of historical novelty.
