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

`verify.py` uses only the standard Python library. For each alphabet size from two through six, it builds the complete directed overlap graph of admissible triples, computes the exact directed matrix-tree determinant by Bareiss elimination, and compares it with the closed formula. At alphabet sizes two and three, it additionally exhaustively counts all edge-distinct closed Eulerian tours normalized to start with `000`. The resulting success marker is `VERIFY_OK`.

`crosscheck.cpp` is a separately written C++17 edge-by-edge tour enumerator. With `c++ -O2 -std=c++17 crosscheck.cpp -o crosscheck && ./crosscheck`, it confirms exactly two and 288 normalized tours at the binary and ternary alphabet sizes and prints `CROSSCHECK_OK`.

The exact determinant checks do not prove the general determinant identity by themselves. The proof in `RESULT.md` establishes the full-parameter block inversion, Schur complement, and fixed-edge BEST normalization. These mathematical steps, rather than finite outputs, support the assertion for all alphabet sizes. Independent scientific or historical-priority review has not been performed.
