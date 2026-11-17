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

# Verification and reproducibility

Execute with Python 3 (standard library only) in a directory containing the complete embedded package:

```sh
python3 verify_full.py
python3 character.py
python3 direct_fixed_check.py
```

`verify_full.py` independently derives the \(508\) maximal cliques, all \(830101\) augmented faces, \(414848\) matched pairs, and \(405\) unmatched tetrahedra, then performs a topological sort over the full matched Hasse directed graph. The output marker is `PREMISE_Q4_WEDGE_405_VERIFIED`. This independently checks the essential homological premise, although that nonequivariant classification was previously known.

`character.py` reconstructs the \(64\) translations and their admissible orbit quotient graphs, evaluates each exact independence polynomial at \(-1\), groups the ten coordinate-cycle types, and performs all \(64\) exact Gaussian-integer Fourier inversions. It asserts the complete claimed types, total \(405\), nine full-group invariants and seventy-one half-turn subgroup invariants, then writes `translation_character.csv`. The output marker is `QUATERNARY_TRANSLATION_CHARACTER_PASS`.

`direct_fixed_check.py` independently builds every simplex from the complete maximal-face taxonomy (coordinate planes, Hamming balls, and parity tetrahedra), and for one representative of each of the ten automorphism types directly sums the signed simplicial action over **every** fixed simplex, including the empty-face reduced correction. Its output marker is `DIRECT_FACE_LEFSCHETZ_PASS`.

Recorded execution output is included as `verification_output.txt`, and the full sixty-four-row table is included as `translation_character.csv`. The calculations prove the finite claims through exact integer recurrence and exhaustive enumerations; they do not prove an arbitrary-alphabet extension. The proof of the invariant-subcomplex relation and of rational orbit-space homology is mathematical and not a separate computer test. Independent external mathematical audit has not been performed.
