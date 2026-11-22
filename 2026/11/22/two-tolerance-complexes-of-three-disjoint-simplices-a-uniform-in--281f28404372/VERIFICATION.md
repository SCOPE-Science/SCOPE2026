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

# Verification instructions

Run `python3 CHECK.py` from the directory containing this file. The program requires only the Python standard library and exhaustively enumerates all faces for six finite parameter triples, constructs oriented boundary matrices, computes ranks modulo two, three and five where indicated, and checks the complete Betti vector and Euler characteristic against the formulas. Compare to `CHECK_OUTPUT.txt`.

`INTEGRAL_CHECK.txt` records an additional exact integral Smith-form calculation for the two smallest mixed-dimensional examples. Reproduce it using `python3 INTEGRAL_CHECK.py` after installing SymPy 1.12 or later; compare the result with `INTEGRAL_CHECK_OUTPUT.txt`. This is a second, finite test. The mathematical proof for **all** block sizes is the explicit three-piece intersection calculation and integral Mayer–Vietoris spectral-sequence argument in `RESULT.md`. In particular the key noncomputational invariant is the *primitive* inclusion of the triple-intersection second homology into each pair intersection, and the key low-degree map is a signed permutation isomorphism. The homotopy upgrade also requires the four-dimensional homotopy-colimit model and the Whitehead/Hurewicz argument.

Every finite check can pass while an all-size proof is wrong. Do not treat the checker, these instructions or this self-review as independent mathematical certification.
