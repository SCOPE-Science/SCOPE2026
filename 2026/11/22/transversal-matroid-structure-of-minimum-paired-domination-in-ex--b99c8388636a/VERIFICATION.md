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

The proof's finite classification enumerates all 28 four-element occupancy vectors over the five graph classes, subject to at most one vertex from each singleton class. Exactly thirteen have both graph domination and an induced perfect matching. The same thirteen admit a matching to the four auxiliary roles \(\{1,2,3,4\}\), so their identification is exact for all positive clique sizes. The proof of matroid basis exchange is the standard all-order transversal-matroid theorem, not a finite computational inference.

## Independent computational checks

Run `python3 verify_patterns.py`. It checks the 28 occupancy patterns; all 50,832 distinct four-subsets across \(1\le a,b\le8\) against independently computed graph and role tests; the exact counting polynomial; and the \(C_7\) non-matroid counterexample. Observed: all assertions passed.

Run `g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct && ./verify_direct`. It independently checks 94,941 four-subsets over \(1\le a,b\le9\), using direct graph domination and matching predicates versus a separate four-role permutation assignment; it checks the exact counting formula and all ordered basis exchanges for \(a=b=5\). Observed: all assertions passed.

The two programs and this documentation are supplied in the same package. Both checks were executed on the actual source files before packaging. No unbounded exhaustive computation or external mathematical certification is claimed.

## Verification limits

The no-two-set lower bound, four-role equivalence, all-order counting and diameter have explicit mathematical proofs in RESULT.md. Code only corroborates them. Historical priority remains subject to a full inspection of the closest original publisher PDF and inaccessible or unindexed literature. Independent scholarly audit has not been performed.
