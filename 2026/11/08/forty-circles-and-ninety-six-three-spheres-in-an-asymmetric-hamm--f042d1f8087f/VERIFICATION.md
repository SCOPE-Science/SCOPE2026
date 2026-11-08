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

# Reproduction instructions

Requires only Python 3 and the accompanying files in the same directory. Execute:

```
python3 verify_morse.py verify morse_certificate.json
python3 verify.py verify certificate.json
```

The first script independently generates 30,991 nonempty faces from the 36-point Hamming metric and checks a deterministic, total discrete-Morse matching with 15,447 pairs and one critical vertex plus 96 critical tetrahedra. It validates the complete orientation of 178,668 face-poset cover incidences and a strict topological order of all 30,991 faces. Therefore the matching is acyclic and the 96-sphere integral homotopy type follows from Forman's theorem.

The second script independently enumerates maximal cliques and verifies 14,227 sequential simplicial collapses, leaving face vector (36,387,1185,929). It checks a 35-edge spanning tree, 352 triangle homotopy relations eliminating every other edge-path generator, exact integral column reductions of the degree-three boundary with 833 unit pivots, and the independent mod-two boundary rank of 833. The residual complex has trivial fundamental group, vanishing second homology and 96 free third-homology generators, consistently with the first proof.

`morse_verification_output.txt` and `verification_output.txt` preserve the exact successful replay messages. Neither certificate substitutes a finite sample for an infinite claim: the subject is one fixed, completely enumerated complex. The first certificate proves the claimed homotopy type directly; the second is a separate validation route. The results were checked by the same mathematical review process; an independent external mathematical audit has not been performed.
