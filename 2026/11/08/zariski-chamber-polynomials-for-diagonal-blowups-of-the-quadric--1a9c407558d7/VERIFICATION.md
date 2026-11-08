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

The mathematical proof appears in `RESULT.md`. Run `python verify.py` using Python 3's standard library; no network access or nonstandard dependency is needed. The exact-arithmetic program reconstructs all \(3n+1\) intersection classes and all candidate supports for \(n=3,4,5,6\). It tests negative definiteness by rational \(LDL^\mathsf T\) decomposition after a valid two-by-two pruning and compares the resulting full support-size vectors with an independently expanded closed formula.

The actual run output is embedded as `verification_output.txt` and terminates with `ALL_CHECKS_PASSED`. Specifically, the vector for \(n=5\) is \((1,16,90,245,345,223,37)\); for \(n=6\) it is \((1,19,129,441,855,948,529,90)\). The computation covers only these four finite instances: the all-\(n\ge5\) conclusion follows from the published geometric chamber-support correspondence, adjunction, the intersection calculation and the counting proof. No complete enumeration for infinite \(n\) or independent scientific audit is claimed.
