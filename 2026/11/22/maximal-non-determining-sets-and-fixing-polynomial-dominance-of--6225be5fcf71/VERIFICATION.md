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

# Verification details

The proof reduces a non-determining vertex subset to inclusion in the fixed-point set of a nonidentity automorphism. Group-completeness lemmas use a six-cycle rooted neighborhood for the Shrikhande graph and maximal four-cliques for the rook graph; neither relies on a heuristic group guess.

Two separately written and executed Python 3 checks accompany this document. `verification/check_affine.py` enumerates all connection-set-preserving matrices and all row/column automorphisms, confirms exact maximal fixed-point families (28 cosets; 12 slabs and 24 transversals), and checks **every** one of the 65,536 vertex subsets on each graph. It confirms:

- Non-determining coefficients for Shrikhande: `[1,16,120,112,28,0,0,0,0,0,0,0,0,0,0,0,0]`.
- Non-determining coefficients for rook: `[1,16,120,560,812,672,336,96,12,0,0,0,0,0,0,0,0]`.

`verification/check_graph.py` constructs the two edge sets from scratch and uses generic NetworkX graph isomorphism to obtain all automorphisms (192 and 1,152), then checks every vertex subset against the complete list. It reproduces the entire determining-coefficient sequence, independently of affine or row/column formulas. Reproduce with `python3 verification/check_affine.py` and `python3 verification/check_graph.py`. The latter requires NetworkX version 2.8 or newer.

Both checks were executed successfully against the exact embedded source text. The scripts exhaust a finite problem only. The proof is structural; the tests are supporting reproducibility, not infinite certification or independent scholarly review. The original mathematical objects and the previously published Cartesian-product criterion retain the limitations stated in `RESULT.md`.
