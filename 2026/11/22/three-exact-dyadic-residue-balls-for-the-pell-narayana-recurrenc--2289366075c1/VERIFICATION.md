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

# Reproducible mathematical verification

Run `python3 VERIFY.py` with Python 3; no third-party packages are required.

The checker evaluates exact matrix powers and differences for the four isometry branches, confirms the first two Mahler coefficient valuations and the all-level divisibility cutoffs, and verifies the four finite coefficients of the exceptional branch. It then constructs the recurrence modulo \(2^k\) for \(1\le k\le13\), checking the image against the claimed three-disk criterion, the cardinality, and the standard period bound \(3\cdot2^{k-1}\). It prints the tested exponents and reports 98,292 finite recurrence/containment check instances.

The program is finite evidence for explicitly calculated coefficients, not a substitute for the theorem's infinite isometry and binomial-difference argument. No independent audit has been performed.
