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

# Reproduction

Run from the directory containing the two scripts using Python 3 and no external packages:

```sh
python verify_affine_involutions.py
python verify_exterior_automorphisms.py
```

The first script constructs finite-field multiplication explicitly and enumerates actual invertible affine transformations in characteristic two. It checks involutions by direct multiplication, then tests commutation of every ordered involution pair and separately counts points in both predicted components and their intersection. Tested field sizes are \(2,4,8\).

The second script separately builds the algebra multiplication table for \(1,x,y,xy\), evaluates all six-parameter algebra automorphisms over \(\mathbb F_2\) and \(\mathbb F_4\), and enumerates commuting square-one pairs by composing maps. It verifies that this algebraic calculation yields the affine-side numbers. This is an independent implementation, not a replay of precomputed result dictionaries.

The tests establish correctness of the finite enumerations only for those fields; they cannot certify algebraic-geometric component statements or all finite fields. Those assertions use the complete symbolic proof in RESULT.md. The comparison with earlier literature is provisional historical-priority assessment, not external certification.
