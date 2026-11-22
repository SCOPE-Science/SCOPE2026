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
The full program is in `verification/verify.py`, with its successful exact output in `verification/expected_output.txt`. Run with Python 3.9+ using `python3 verification/verify.py`.

For each even alphabet size \(n\in\{2,4,6,8\}\), the script exhaustively enumerates \((n-1)!!\) fixed-point-free involutions and every one of their ordered subsequences. It computes the exact augmented cellular boundary matrices over \(\mathbb F_2\), with no numerical rounding; checks that \(\partial^2=0\) by direct two-deletion calculation; checks that high-pivot and low-pivot Gaussian elimination yield the same ranks; computes all Betti numbers by rank-nullity; and verifies the Euler identities and complete expected arrays.

Limits: a finite exhaustive computation proves the finite statement, not an assertion for larger \(n\). It does not compute integral Smith forms or certify integral torsion. Independent mathematical audit was not performed.
