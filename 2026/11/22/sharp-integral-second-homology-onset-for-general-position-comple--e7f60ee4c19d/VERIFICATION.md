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

Execute `python3 verify.py` in a standard Python 3 environment; no third-party modules are needed. The program verifies the face criterion against metric betweenness and confirms the dimension bound through order 40, performs actual free-face removals for orders \(3,4,5,6,7,8,10\), and constructs all eight octahedral faces with signed integral boundary zero for eligible orders through 100. Compare standard output byte-for-byte to `verification_expected.txt`.

The zero cases are covered by the published proof's exhaustive seven-row gap classification, not by extrapolation from the finite script. The infinitely many positive cases are covered by balanced gaps, signed join cycles and the proof that \(C_3=0\). A finite verifier cannot independently certify the universal family or originality; a further independent mathematical audit has not been conducted.
