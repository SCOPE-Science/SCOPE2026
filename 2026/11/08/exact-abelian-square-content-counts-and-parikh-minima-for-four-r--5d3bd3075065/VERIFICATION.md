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

# Verification details

The symbolic proof is in `RESULT.md`. The exact classification enumerates all admissible factor contents, including the single possible intersection of the two four-run families. The fixed-Parikh lower bound is based on explicit mixed squares compensating for at most two trivial-count deficits. No finite program proves the assertion for unbounded integers.

Run `python3 verify_four_run.py` using Python 3 with only the standard library. The replay tests every tuple of four positive run lengths at most nine: 6,561 cases, comparing three separately defined representations (direct substring collection, structural-family set, and closed numerical formula). It also compares exact minima for all 361 pairs of letter counts in the interval from four through 22, inclusive. The boundary check confirms the formula remains valid where the separate minimum theorem cannot be extended.

A further local consistency check compared the formula against reversal-plus-complement symmetry for 10,000 tuples with runs at most ten. These reproducible finite checks identify no discrepancy. They do not exclude an error beyond the tested parameters, nor do they resolve historical priority or independently certify the proof.
