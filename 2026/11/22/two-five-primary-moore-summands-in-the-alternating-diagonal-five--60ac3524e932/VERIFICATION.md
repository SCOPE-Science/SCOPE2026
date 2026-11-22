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

Run `python3 verify.py` using the Python 3 standard library.

The script enumerates the 1545 nonempty chessboard faces and 60 even permutations, forms the orbit CW complex from flags in the barycentric subdivision, and checks signed boundaries square to zero. It constructs the unique-free-coface collapses from highest to lowest dimension, removing 240 four/three and 404 three/two cell pairs; no lower-dimensional pair removals occur. It then performs exact unimodular integral reductions, obtaining 44, 264, and 74 unit boundary pivots respectively, with a remaining diagonal block having two entries of absolute value five in the top boundary. This proves the integral homology.

The separately stated global steps use the 1994 chessboard connectivity theorem, Armstrong's 1965 orbit-space fundamental-group theorem, Hurewicz and homological Whitehead. Finite chain computations do not purport to reprove these general theorems. No independent validation was performed.
