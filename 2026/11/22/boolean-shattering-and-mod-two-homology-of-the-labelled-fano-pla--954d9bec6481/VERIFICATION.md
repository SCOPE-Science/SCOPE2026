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

Run `python3 check_fano.py` and `c++ -O2 -std=c++17 check_fano.cpp -o check_fano && ./check_fano` in the directory containing these files. Each script builds the 35 triple queries and all 30 labelled Fano-plane concepts; the enumerators use different mathematical constructions (full relabelling orbit versus exact covering of 21 point pairs). Both inspect all support sets of sizes zero through four and check every pattern, yielding the face counts \((1,35,315,840,0)\). Both build the triangle boundary matrix over \(\mathbb F_2\) and obtain rank 281, yielding the nonzero reduced Betti number 559 in dimension two. The geometric proof excludes every support of size at least four; thus not enumerating the much larger size-five-and-up families does not limit the claim. No infinite statement is inferred from the enumerations.

The displayed ranks and counts were reproduced by running both programs. These are reproducible checks accompanied by source code, not an independent external audit. No claims about integral homology or wider Steiner orders are certified.
