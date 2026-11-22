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

The proof uses the exact subgradient optimality system, finite signed-block affine formulas, and the mass-coordinate chord inequality. Its converse consists of an explicit strictly increasing-data expanding-jump construction and a positive-length fusion-then-unfusion construction. The three-site rational witness has transitions at \(1/6\), \(1/2\), \(100/7\), and \(98/3\), with continuous solutions and valid KKT signs and bounds on each interval.

`check.py` is a standalone finite consistency checker. It enumerates signed partitions rather than assuming the claimed concavity law, checks every reconstructed candidate against the complete KKT equations, and tests 3,864 gap comparisons for sampled mass-concave profiles, nine exact rational example points including transition endpoints, and a nonconcave growing-gap example. It ran successfully and reported PASS. These computations provide independent finite checks of the formulas, not an exhaustive theorem over all data, masses, weights and dimensions. The analytical proof supplies the universal quantifiers.

The founding 2004 source was only partially accessible; a possible unindexed equivalent remains a historical-priority limitation. No external expert, independent mathematical audit, or formal certification was performed.
