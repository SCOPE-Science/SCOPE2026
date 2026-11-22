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

# Reproducibility and boundaries

Run `python3 verify.py` (Python 3 standard library only). Every assertion must succeed, the listed 25 conjugacy classes must have total cardinality 51840, and the terminal marker must be `SCHLAFLI_WEYL_HOMOLOGY_CHARACTER_VERIFIED_OK`. The bundled `verification_output.txt` records the actual exact-integer output of a successful execution.

The verified finite objects are 27 Picard line classes, 2764 cliques including the empty simplex, six augmented mod-two boundary matrices, the six Weyl reflections, 51840 permutations, and 25 conjugacy classes with complete oriented-face Lefschetz traces. Mod-two ranks plus the dimension inequalities force the rational Betti numbers without any numerical approximation.

The proof uses the standard classification of 27 line divisor classes and the semisimplicity/character-uniqueness theorem for rational representations of a finite group. This does not certify integral equivariant homology, formal proof-assistant verification, or historical priority. Independent validation has not been performed.
