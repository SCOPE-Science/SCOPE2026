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

The standard identification of the noncrossing-diagonal complex with the polar boundary of the polygon secondary polytope, and the orbit-space fundamental-group theorem, are literature premises. They are used in the proof and are not computer-certified. The finite checker `verify_even_associahedron.py` verifies the following conditions without external dependencies:

- For every even polygon length from 6 to 100, each subgroup's invariant dimension determined independently by vertex-permutation orbits agrees with the dimension determined by the real harmonic decomposition.
- Every individual reflection has a nonempty fixed sphere; the checker does **not** conflate this with the fixed-point space of the whole dihedral subgroup.
- The gcd of the exponents of all nontrivial rotations with nonempty fixed space is two precisely for polygon lengths that are powers of two, and one otherwise.

Run `python3 verify_even_associahedron.py`. Observed output begins with `All even polygon sizes 6..100 passed; fixed-subspace comparisons: 5508` and lists the predicted fundamental-group orders at sizes 6, 8, 10, 12, 16, 18, 24, 32, and 64. The finite test does not prove the theorem beyond this range. The proof supplies an independent symbolic argument valid for every even size at least six. The supplied files have received a self-review only; independent scientific audit has not been performed.
