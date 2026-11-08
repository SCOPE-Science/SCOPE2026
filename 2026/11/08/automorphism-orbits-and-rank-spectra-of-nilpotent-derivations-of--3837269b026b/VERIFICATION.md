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
# Reproducibility checks

From the package root, run `python3 artifacts/check_p_derivations.py` with Python 3. No third-party packages, network access, or downloaded datasets are needed. The expected final output line is `ALL_DIRECT_MULTIPLICATION_AND_AUTOMORPHISM_ORBITS_OK`.

For each specified finite-field configuration, the checker constructs the original path-algebra multiplication, enumerates every matrix \(T\) with \(T^p=0\) and every vector \(w\) with \(T^{p-1}w=0\), and separately tests the Leibniz rule on all basis pairs, the original \(p\)-fold composition and the rank of the full derivation. It compares the results to a partition-based count using invertible centralizers. For four smaller configurations it independently enumerates actual algebra-automorphism orbits by all admissible arrow-basis changes and vertex shears. The extension field of order four uses binary-polynomial multiplication modulo \(u^2+u+1\).

The embedded `artifacts/check_output.txt` records all five successful field/dimension comparisons. A separate check verifies the rational orbit-generating-series coefficient identity for primes \(2,3,5\) through dimension \(16\). These finite checks are not an infinite proof, and no external mathematical audit has been performed.
