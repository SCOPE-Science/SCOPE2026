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

Compile and execute the complete finite census by running `python3 replay.py` in this directory, with Python 3 and `g++` supporting C++17. Each implementation enumerates exactly 14,348,907 distinct ternary initial states separately for each threshold one through four and computes the complete deterministic successor relation. The first uses indegree elimination; the second uses direct path tracing and a disjoint-pairs construction of the Petersen graph with bit-plane state encoding.

The replayed stdout is checked against both captured implementations' output and exact expected counts. Every primitive cycle count, individual basin-size histogram, full first-entry/period table and global population total is compared. Both implementations agree for all thresholds. The observed sharp maximal transient lengths are 12, 6, 3, and 3. The threshold-two starting state 66495 in the primary encoding reaches zero for the first time on update six; 930 labelled states take the maximum time. The threshold-one witness 94238 first reaches periodicity on update twelve.

Proof scope: this is complete enumeration of an explicitly defined finite graph and the four stated contact thresholds. It does not verify any arbitrary graph, produce a closed-form all-size formula, or constitute third-party independent audit.
