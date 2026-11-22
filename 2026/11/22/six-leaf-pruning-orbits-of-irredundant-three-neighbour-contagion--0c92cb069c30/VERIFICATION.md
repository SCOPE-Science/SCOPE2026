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

The standalone `check_a.py` enumerates all \(65,536\) initial seed masks using set-based infection updates; `check_b.cpp` independently uses bitwise-neighborhood updates. Each tests all single-seed deletions of successful configurations and partitions the resulting minimal seeds under all \(384\) cube automorphisms. The independent `check_forest.py` enumerates maximal induced forests instead of simulating infection and obtains infection times from maximum component diameters. All three completed successfully when executed against their attached source files.

Each program asserts \(8\) size-six two-round minima, \(160\) size-seven three-round minima, \(768\) size-seven four-round minima, and a total of \(936\). The first two additionally assert the six orbit sizes \(8,64,96,192,192,384\), disjointness, and complete coverage; the third checks residual component orders and diameters. The time follows from the proven leaf-peeling equivalence, not from an unbounded numerical simulation.

Limits: the certificate covers \(Q_4\) with threshold three only; no external human review or independent audit is claimed. The literature comparison cannot exclude overlapping computations in inaccessible older appendices.
