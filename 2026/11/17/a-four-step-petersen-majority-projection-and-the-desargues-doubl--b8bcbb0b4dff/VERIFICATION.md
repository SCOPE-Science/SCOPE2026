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

# Verification record

The machine-independent definition is disjointness on the ten two-subsets of a five-element set. The Python checker `check_petersen.py` enumerates all 1,024 shore states, all 120 permutations, and the 34 resulting unlabeled graph classes; it checks the exact six-iterate identity, 124 recurrent symbols, their 14 fixed states and 55 two-cycles, all three inverse-fiber multiplicities, and an explicit edge-by-edge graph isomorphism to `GP(10,3)`.

The independently coded C++ verifier `check_desargues.cpp` constructs `GP(10,3)` directly, visits all 1,048,576 labelled states, and classifies every orbit and its basin using indegree pruning. It checks the sharp four-update entry cutoff, exact entry-time/period populations, and nine orbit-basin multiplicities. Neither program samples states or relies on numerical floating-point approximations. Run `python3 check_petersen.py` and `g++ -std=c++17 -O2 -Wall -Wextra check_desargues.cpp -o check_desargues && ./check_desargues`; their recorded outputs are `check_petersen_output.txt` and `check_desargues_output.txt`.

The finite certificates prove only the specified two finite graphs. The general period-two property is classical; absolute historical originality and independent external mathematical validation have not been established.
