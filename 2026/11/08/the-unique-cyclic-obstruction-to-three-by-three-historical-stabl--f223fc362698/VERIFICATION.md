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

# Finite verification

The proof's universal claim is confined to exactly three agents on each side with complete strict lists. `reachability_verify.py` and `reachability_census.cpp` enumerate the full space of \(6^6\) profiles using distinct code paths. Each independently produces the table \((1,1):34080\), \((2,2):11484\), \((3,2):12\), \((3,3):1080\). The Python checker also generates the 12 distinct independent-relabeling images of the cyclic profile and verifies set equality with all deficient profiles. Both codes explicitly test blocking pairs and stable proposal-chain outcomes. No statistical sampling or inference to larger markets is used.

To reproduce, run `python3 reachability_verify.py` and then compile and run the C++ file with any C++17 compiler. No external packages or network access are needed.

Limits: exhaustive computation is the certificate for the finite orbit exclusion; the codimension-one reduction of arbitrarily long histories is a separate mathematical argument. Independent third-party audit has not been performed.
