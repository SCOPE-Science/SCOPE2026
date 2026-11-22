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

# Verification of the new theorem

The proof in `RESULT.md` identifies both join pieces and their exact disconnected overlap; it applies the homotopy-pushout property of CW subcomplexes and the suspension splitting, followed by the full injective-word derangement theorem. No unproved computational lemma is used to establish the theorem for all sizes.

`block_reverse_checker.py` contains all data construction and finite-field row-reduction steps. Running `python block_reverse_checker.py` from the package directory, with no third-party dependencies, prints:

```
PASS all 9 nonempty pairs on 2+2 letters
PASS all 189 nonempty pairs on 2+3 letters
PASS 36 representative pairs on 3+3 letters
PASS 234 total exact GF(2)/GF(101) homology comparisons
full-block case 2 2 faces (4, 12, 16, 8) Betti [1, 1, 2, 2]
full-block case 2 3 faces (5, 20, 42, 48, 24) Betti [1, 1, 1, 2, 4]
full-block case 3 3 faces (6, 30, 84, 144, 144, 72) Betti [1, 1, 0, 4, 0, 8]
```

Field checks do not establish integral torsion-freeness in arbitrary finite cases, and neither the printed logs nor finite samples establish the full homotopy equivalence. That equivalence is supplied by the written argument. An independent mathematical audit has not been performed.
