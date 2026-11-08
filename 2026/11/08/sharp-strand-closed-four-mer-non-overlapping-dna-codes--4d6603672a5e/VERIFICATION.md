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

The asserted optimum and classification are finite and reproducible. Run `python3 verify.py` to regenerate the reverse-complement orbits, compatibility masks, complete maximum-weight enumeration, and 32-codebook symmetry classification, while cross-checking `certificate.json`. Run `c++ -O2 -std=c++17 crosscheck.cpp -o crosscheck` followed by `./crosscheck` to enumerate every subset of the independently generated 20-vertex graph. The two implementations use different search methods: recursive branching with pruning, versus full subset dynamic programming.

Observed results after extracting the package: `VERIFY_OK small=7/2 large=17/8 global=32 classes=4x8` and `A1 6 7 2`, `A2 20 17 8`, `CROSSCHECK_OK`. The hand-readable clique partition in `RESULT.md` proves the 17-word upper bound independently of an optimization solver. The eight equality tuples then prove the codebook count by 162 finite pairwise tests.

No assertion is made about error correction, physical DNA performance, other word lengths, or independent audit.
