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

The program `verify.py` requires only Python 3 standard-library modules. It enumerates all \(2^{15}-1\) nonempty simple edge subsets, selects the 12,067 faces with degree at most three, and verifies all independent four-sets in the corresponding Kneser graph. It constructs the lexicographic repeated-toggle discrete Morse matching with 6,021 pairs and 25 critical faces. A topological sort of the full directed incidence graph visits all 12,067 faces. Oriented boundary substitution reconstructs the \(20\)-by-\(1\) and \(3\)-by-\(20\) integral Morse matrices and a determinant-one four-column minor. Running `python3 verify.py` must terminate with `ALL_VERIFY_OK`; the complete observed standard output is in `verification_output.txt`.

Integral homology and homotopy follow from the matching plus the primitive boundary computation and standard Hurewicz/Whitehead implications. The finite certificate pertains only to the explicitly specified finite complex; no infinite-family homotopy conclusion is asserted. Independent validation is not performed.
