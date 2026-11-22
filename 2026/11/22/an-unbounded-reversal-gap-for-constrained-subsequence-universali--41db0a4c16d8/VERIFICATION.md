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

# Verification checks

`python3 verify.py` checks two independent finite properties against the theorem:

1. Construct the reachable complete deterministic product automaton, then refine right-language partitions until stable for all integers \(2\le d\le13\), \(1\le k\le16\), and both forbidden patterns. Exactly 384 minimal-state counts agree with the claimed formulas.
2. For \(2\le d\le5\), \(1\le k\le3\), and binary words of lengths zero through twelve, directly check forbidden-factor avoidance and embedding of every binary length-\(k\) pattern; compare with automaton acceptance. All 196,584 comparisons agree.

A successful run prints three `PASS` lines. The proof of the infinite result is in `RESULT.md`; finite checks do not certify all parameters. No independent audit has been performed.
