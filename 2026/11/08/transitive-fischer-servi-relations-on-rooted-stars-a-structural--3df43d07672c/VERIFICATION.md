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

# Verification

The unrestricted claim is proved by a unique structural decomposition in `RESULT.md`. Finite checks verify boundary conditions and the combinatorial count rather than supplying an infinite certificate.

* `checker.py` independently enumerates every relation and constructs every normal form on rooted stars of zero through three leaves, comparing **sets** of matrices. Its outputs report equal sets and no missing or extra matrices.
* `checker.cpp` independently exhausts each of the \(2^{(m+1)^2}\) matrices for every \(0\le m\le4\), using rowwise tests for confluence and transitivity. The counts are \(2,8,38,379,7182\) and it reports `ROOTED_STAR_TRANSITIVE_CONFLUENCE_OK`.
* `count_transitive5.cpp` exhaustively enumerates every five-point binary relation and counts the transitive ones, those with no empty row, and those with no empty row or column; it reports \((154303,47262,16762)\). Smaller auxiliary counts were independently calculated in the displayed proof table.

Reproduce with `python3 checker.py`, `c++ -std=c++17 -O3 checker.cpp -o checker && ./checker`, and `c++ -std=c++17 -O3 count_transitive5.cpp -o count5 && ./count5`. No third-party libraries are required. Counts concern labelled relations and optional loops. Checks do not establish historical priority; independent audit has not been performed.
