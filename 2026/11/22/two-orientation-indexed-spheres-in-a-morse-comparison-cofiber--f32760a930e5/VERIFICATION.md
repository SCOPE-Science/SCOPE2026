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
# Verification scope

Run `python3 verify_relative.py` in the same directory; the Python script uses only the standard library. Expected output is captured in `verification_output.txt`.

For every integer \(3\le n\le10\), the test constructs the full generalized incidence complex of the cycle with one- or two-edge pendant path, identifies both forbidden oriented-cycle simplices, verifies exhaustion and disjointness of their coface blocks, and builds the signed relative boundary matrices directly. For the two-edge path, each orientation contributes exactly one \((n-1)\)-face, three \(n\)-faces and one \((n+1)\)-face. Both integral differentials are primitive, giving the verified homology pattern. The independent unbounded proof consists of the three-tail-incidence link calculation and quotient decomposition in RESULT.md; finite outputs do not themselves prove the infinite theorem.

Status: self-reviewed. Independent audit not performed.
