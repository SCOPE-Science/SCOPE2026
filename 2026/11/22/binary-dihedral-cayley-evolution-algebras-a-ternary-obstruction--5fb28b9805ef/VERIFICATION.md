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

# Verification scope
The reproducible script `verify.py` computes binary structure-matrix rank by exact row reduction, independently checks divisibility of the ternary polynomial via the polynomial Euclidean algorithm, and reconstructs the intrinsic rotation/reflection edge distinction. It runs for all integers \(3\le n\le60\). An independent directed-graph isomorphism enumeration tests all graph automorphisms for \(3\le n\le6\). Run `python3 verify.py` in a Python environment with NetworkX available.

The complete script executed successfully. Expected final line: `BINARY_DIHEDRAL_EVOLUTION_VERIFIED n=3..60; graph_aut=2n; corank=2*indicator(3|n)`.

The source proof, not enumeration, establishes all \(n\) and arbitrary field extensions. Matrix rank over \(\mathbb F_2\) plus an exact polynomial-gcd proof establishes rank over extensions; no characteristic-zero-to-two rank shortcut is used. The published complex three-term convolution theorem covers an analogous preliminary calculation and is credited. The self-review is not independent validation.
