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
# Verification of the parity-sharp toroidal contact coloring

The analytic proof is in RESULT.md. It uses a graph identification, a short odd-subset counting argument, and two precisely stated established theorems; it does not infer an infinite claim from finite calculation.

To reproduce the explicit 5-by-5 witness, from this directory run:

```sh
python3 verify_torus_coloring.py certificate_5x5.json
```

The checker reconstructs 25 lattice vertices, 75 edges, 50 equilateral faces, and 150 small triangular cells; checks all actual common-point contacts rather than just edge sharing; verifies each small cell has 21 distinct neighbors and that all 1,575 contact edges are properly colored; and counts exactly six color classes of size 11 and seven of size 12. It uses no external packages. The same checker verifies the 12-clique lower bound at all original vertices in the concrete witness.

The proof's universal density inequalities are exact: for odd induced sets of orders 3, 5, 7, 9, 11 and at least 13, the maximum bounds are respectively 6, 10, at most 34/3, 13, 64/5 and 13. Its odd full-vertex density is strictly greater than 12. The conditions for the cited even-order Cayley 1-factorization and general Goldberg–Seymour upper bound are checked directly in RESULT.md.

This is mathematical and programmatic self-review only. No independent audit has been performed.
