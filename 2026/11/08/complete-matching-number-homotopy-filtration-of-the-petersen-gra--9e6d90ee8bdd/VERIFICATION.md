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

# Reproducibility and verification

The attached `verify_nonmatching.py` enumerates the exact fifteen-edge Petersen graph with integer masks, counts all forbidden matchings at each threshold, checks every directed Hasse cover for acyclicity, reconstructs signed Morse boundaries by gradient cancellation, checks primitive columns, and verifies a determinant-one minor for the intermediate boundary. Execute from this directory with `python3 verify_nonmatching.py`. The corresponding original output is `verify_nonmatching_output.txt` and ends with `INTEGRAL_MORSE_CHECKS_PASS`.

`verify_kneser.py` independently builds the graph as \(KG(5,2)\), verifies an explicit graph isomorphism with the other labeling, enumerates every simplex, and computes every simplicial boundary rank over \(\mathbb F_2\) by bitset Gaussian elimination. Execute with `python3 verify_kneser.py`. Its output is `verify_kneser_output.txt` and ends with `KNESER_INDEPENDENT_CHECKS_PASS`.

The integral homotopy proof specifically uses signed integer Morse differentials, primitive lattice images, the discrete Morse CW theorem, and the homological Whitehead theorem. The independent mod-two calculation does not by itself establish integral torsion-freeness or full homotopy type. Computations are exhaustive on this finite fifteen-coordinate complex only. No external homotopy certification or independent mathematical audit has been performed.
