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

## How to reproduce

Run `python3 checker.py` with standard Python 3. The program enumerates legal length-\(k\) multiset permutations and compares their distinct descendants against the independent local endpoint-count formula. It exhaustively checks 24,337 source/window/alphabet instances: \(q\in\{2,3,4\}\), \(2\le n\le7\) for \(q\le3\), \(2\le n\le5\) for \(q=4\), and \(2\le k\le n\). It checks attainment counts and strict alphabet thresholds in those cases. It also verifies the binary length-three maximum and number of maximizers at every \(3\le n\le16\), and independently matches the transfer-matrix polynomial against full source enumeration through length 12, including exact mean and variance. The command returned `PASS` during preparation.

The unbounded assertions rely on the mathematical proof, not finite testing. Historical priority is not independently certified, and complete access to the closest 2026 preprint was unavailable.
