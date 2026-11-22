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

# Reproducible checks

`python3 scripts/verify_census.py` uses only the standard library. It enumerates every code in increasing lexicographic index, imposes Hamming distance at least three, and tests every ordered splicing pair and all three offsets, including repeated codewords. Its expected outputs include 72 admissible singleton words, 1530 Hamming-compatible pairs, size histogram `{1:72, 2:1410, 3:7398, 4:9042, 5:1548}`, no larger code, 1548 optima and 129 symmetry classes of size 12.

An independently written implementation, `scripts/verify_census.cpp`, may be compiled by `g++ -O2 -std=c++17 scripts/verify_census.cpp -o /tmp/cf4_verify` and executed with `/tmp/cf4_verify`. It reports the same histogram and orbit count. The finite enumerations are exhaustive for the specified ternary model because each codeword must be primitive, each distinct pair must satisfy the Hamming filter, and every valid set has a unique increasing-index representation; the recursive deletion of nonadmissible extensions is justified by hereditary validity.

The proof of the \(q\)-ary projection bound is mathematical and requires no machine enumeration. No externally audited proof or formal infinite-case certification is claimed. All files required to reproduce the finite claims are included.
