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

# Reproducible mathematical checks

Run `python3 verify.py` from this extracted directory. No network access or nonstandard Python libraries are required. The standalone verifier independently constructs the adjacency graph and calculates every induced-subset independence number by exact dynamic programming. It compares those values with the proved blockwise formula on every subset, enumerates all simplices, assembles all matching pairs, and performs a complete directed Hasse-incidence acyclicity test (not just an Euler-characteristic calculation).

The verifier tests 21 parameter pairs with widths ranging from 2 to 5 in several mixtures, with between one and five biclique blocks, and thresholds from 2 to 5. It checks the exact unmatched critical-face lists, including the contractible cases. A separate signed Lefschetz evaluation checks 24 automorphism-character instances, including local leaf transpositions, interchanges of equal-size blocks, and composites. The recorded executable output is in `verification_output.txt`; the final two markers are `ROBUST_BICLIQUE_BOUQUET_ALL_EXACT_TESTS_PASS` and `EQUIVARIANT_HOMOLOGY_CHARACTER_TESTS_PASS`.

These are finite checks. The unlimited parameter range, integral homotopy statement, and equivariant lattice decomposition follow from the symbolic matching and relative-chain proof in `RESULT.md`, not from extrapolating test values. No independent mathematical audit has been performed.
