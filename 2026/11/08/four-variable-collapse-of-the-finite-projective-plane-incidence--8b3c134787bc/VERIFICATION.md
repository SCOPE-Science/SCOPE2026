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

# Reproduction of finite checks

Run `python3 verify.py` with Python 3.9 or later in the directory containing that script. It requires only the standard library. Compare standard output byte-for-byte with `verify.out`.

The checker builds projective planes over the finite fields of orders 2, 3, 4 and 5, validates their sizes and incidence counts, forms atomic signatures augmented by collinearity/concurrence on every triple, and compares every extension catalogue from enhanced triples to enhanced quadruples. All triples are enumerated for the smaller orders 2 and 3; for orders 4 and 5, each enhanced triple type is covered and deterministic additional representatives are checked. It independently evaluates the explicit four-variable sentence in each computed model, with variables ranged over their explicitly guarded point/line sorts. The recorded output has 48 enhanced triple types in each field; 400 versus 410 enhanced four-types for order two versus orders at least three; and a common extension catalogue at orders 3, 4 and 5. The sentence is false at order two and true at 3, 4 and 5.

The checker is finite corroboration only, not an exhaustive test of all finite projective planes or proof of infinitary pebble-game equivalence. Those conclusions depend on the projective-plane axioms and the geometric extension case analysis in RESULT.md. No external independent check was carried out.
