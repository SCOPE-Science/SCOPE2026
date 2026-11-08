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
# Exact reproducibility
Run `python3 verify.py` with Python 3 and its standard library. This rebuilds the 16-vertex Cayley graph and the antipodal quotient of the 32-vertex five-cube, checks they agree, and exhaustively constructs every independent simplex by two methods.

The verifier rebuilds the 191 matched pairs from the stated sixteen pivot choices, orients and checks all 1200 nonempty-face Hasse incidences, and removes all 392 faces using Kahn topological sorting. It confirms critical dimensions 0 (one) and 3 (nine). The exact integral homotopy conclusion follows from this certified acyclic matching and the absence of possible attaching maps to positive-dimensional lower cells.

Additional exhaustive mod-two boundary elimination gives ranks 15, 65, 95, 16 and mod-two Betti numbers 1, 0, 0, 9, 0. This is corroboration, not a replacement for the Morse homotopy proof. See `verification_output.txt` for exact recorded program output. No classification of larger folded hypercubes or independent external audit is supplied.
