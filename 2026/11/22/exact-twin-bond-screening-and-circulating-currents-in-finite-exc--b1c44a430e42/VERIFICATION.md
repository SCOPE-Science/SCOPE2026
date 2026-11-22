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

# Computational verification

Execute `python verify_master.py` and `python verify_independent.py` using Python 3 and its standard library.

The first implementation constructs all \(k\)-particle subsets in five connected weighted graphs (total 61 configurations), evaluates the claimed stationary density using exact fractions, and verifies all entries of the master equation, every edge current and all joint outside-site marginals. The second independently constructs the full generator and obtains its unique stationary density by rational Gaussian elimination on ten separate graph/filling instances, comparing both twin and deliberately non-twin geometries. Both returned PASS on execution.

The computations check illustrative finite systems only. The universal claim for all finite graphs and positive real rates is proved algebraically in RESULT.md. No external or independent scientific audit has been performed.
