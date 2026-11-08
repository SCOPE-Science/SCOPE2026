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

# Reproduction and limitations

Execute `python VERIFY.py` with Python 3.10 or later. The program uses only the Python standard library. The expected stdout is `VERIFICATION_OUTPUT.txt`. It asserts every property below and exits nonzero on any failure.

- Perfect-matchings from graph recursion and independent vertex-subset dynamic programming: both 169.
- Every nonempty facet submask enumerated: 379056 faces including empty, with exact 12-term face vector.
- Complete acyclicity verification of both independently ordered matching choices: all 2550660 Hasse incidences each.
- Forward signed Morse boundaries of sizes 10 by 40 and 40 by 6: exact ranks 10, 5 and zero composite.
- Exact Bareiss unit minors: determinant +1 (10 by 10); determinant -1 (5 by 5).
- Reverse signed Morse boundaries with exact ranks 7, 8 and 1 and zero composites.
- Integral CW cancellation argument in dimensions 3-5 establishes full nonequivariant wedge homotopy, not only Betti numbers.

The source graph, face set, complete oriented Hasse graph and all integer Morse differentials are constructed in memory. The randomization-free certificate is a finite proof for this particular graph, not a theorem for larger permutahedra. Self-review has been completed; independent external audit has not been performed.
