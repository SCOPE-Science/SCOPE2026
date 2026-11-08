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

# Reproduction

Compile and run `check_partition_kneser.cpp` as C++17 and run `check_partition_gp.py` as Python 3. Both use only standard libraries. The first completely enumerates all four-part minimum resolving partitions using the Kneser model and checks every connected-component distance with BFS; the second reconstructs graph distances in an independently built generalized Petersen model and separately enumerates all optimal partitions and legal transfers.

The exact reported checks are: zero valid three-block partitions, 7040 four-block partitions, 34500 unoriented transfers, one connected component, 6300 configurations of eccentricity seven, 740 of eccentricity eight. Both representations produce the same degree histogram and block-size distribution. The unordered pair-distance distribution sums to the exact number of unordered state pairs. All sources and executable artifacts are embedded alongside this file.

# Scope of verification

A full all-pairs breadth-first computation is provided by the C++ checker. The Python verifier independently confirms the graph-state and move counts and connectedness, plus distances from six selected states, rather than independently repeating the complete all-pairs search. These finite checks do not establish novelty or conclusions for larger graphs. No independent human audit is claimed.
