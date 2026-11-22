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

# Reproduction and verification

Run `python3 direct_check.py` and `python3 structural_check.py` using Python 3's standard library. Both were run from the packaged file contents. The direct verifier enumerates actual distinct one-symbol-deletion outcomes, tests every pair of palindromes in the stated finite parameter ranges, and independently derives their two-read conflict graphs. It compares those graphs against canonical alternating edges, checks forest components, center-flip matchings, all odd capacities, and even-length absence of conflict. The structural verifier starts from alternating-interval generators without any deletion-deck calculations, checks forest acyclicity through a disjoint-set construction, the component-size formula, the central-flip perfect matching on the nonisolated vertices, and an explicit maximum independent set for six larger parameter pairs.

The scripts' final success lines were `PASS: direct deck comparisons, all cases` and `PASS: canonical edge forest census, sharp matching bound and optimal codes`. Their parameter lists and assertions are inspectable in the scripts. These computations are finite corroborations; the infinite statements rest on the six mathematical lemmas in `RESULT.md`. There is no external or independent certification.
