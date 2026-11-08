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

# Verification and scope

This finite result is checked by two standalone enumerators based on different search decompositions. `enumerate.cpp` processes lexicographically increasing six-subsets of all 64 words; its only pruning test is a capacity inequality based on at most three target pairs per remaining word. `verify.py` instead branches on an uncovered ordered pair, recursively chooses a word covering it, and deduplicates the resulting sets. Every valid codebook of six words is included by an inductive coverage argument. The two generated sorted catalogs match exactly, not only in cardinality.

Run `sh reproduce.sh` with Python 3 and a C++17 compiler, or run `python3 verify.py` to replay the second enumerator and check both embedded certificates using only Python's standard library. Verified output: `VERIFY_OK 644 codebooks 21 orbits 120 perfect`. The two TSV files list every minimum codebook and every canonical class representative, including shadow-excess and orbit-size data. The proof of the minimum size is mathematical and does not depend on a computation.

All arithmetic is exact integer and bitwise arithmetic. The enumeration is exhaustive only for the defined alphabet of size four and six distinct codewords of length three. It does not establish analogous classifications at larger parameters. The verification described here is an internal reproducibility check, not an independent scientific audit.
