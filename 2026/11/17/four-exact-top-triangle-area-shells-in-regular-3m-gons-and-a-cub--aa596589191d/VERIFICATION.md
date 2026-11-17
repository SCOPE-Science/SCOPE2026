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

# Verification instructions and limits

With a Python 3 standard-library interpreter, run `python3 check_triangle_shells.py`. Its passing summary is `REGULAR_TRIANGLE_FOUR_SHELL_CHECKS_PASSED orders=26 triples=707434 range=9..84`.

The checker enumerates all \(\binom N3\) unordered vertex triples for every \(N\in\{9,12,\dots,84\}\), computes each area from an independent Cartesian shoelace determinant, and compares the four greatest distinct numerical area groups with the analytically predicted cyclic gap shapes, multiplicities, and area separations. It uses round-to-ten-decimal grouping and tolerance \(1.1\cdot10^{-10}\) for numerical comparisons, not a symbolic decision algorithm for arbitrary order. The infinite result follows from strict Schur concavity and the exact trigonometric identities in the proof, not from the bounded enumeration.

The historical source comparison includes the inspected 2020 and 2021 primary articles and the complete public OEIS record A400213. The linked primary Zenodo manuscript was inaccessible, so historical priority is provisional. Independent audit has not been performed.
