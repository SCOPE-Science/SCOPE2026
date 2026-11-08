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

# Reproduction and limits
Run `python3 verify.py` using the Python standard library, with no network access or external dependencies. The verifier reconstructs the twelve graph vertices and eighteen edges, independently enumerates all 4096 masks using two criteria, and asserts the 72 independent triples and 3674 faces. Two full staged Morse matchings (ascending and descending pivots) each produce 1834 pairs, six remaining six-dimensional simplices, and acyclicity after orienting all 20940 Hasse covering incidences. Each topological sort visits all 3674 augmented faces. Omitting the empty-face pair produces a critical vertex and six six-cells in the ordinary matching.

The same script calculates the signed reduced Lefschetz number for each of the 24 symmetries, checks that traces are constant on each conjugacy class, and decomposes the rational character against five irreducible characters. Exact expected results are in `verification_output.txt`. The final-package verifier was replayed and matched that output byte-for-byte.

These computations prove the finite statements through complete enumeration plus the standard discrete Morse and Lefschetz/character theorems. No general result about larger truncated polytopes, equivariant homotopy equivalences, or integral representation splittings is asserted. Independent external audit has not been performed.
