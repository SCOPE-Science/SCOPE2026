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

`python3 verify.py` executes a fully self-contained direct enumeration using ordinary integer arithmetic. In its tested range of odd moduli \(3\le q\le139\), the checker computes inversion numbers by comparing every ordered pair of positions in the multiplication permutation, and checks both \(I(a,2q)\equiv2I(a,q)\pmod4\) and \(i^{I(a,2q)}=\left(\frac aq\right)\). It separately accumulates the exact fourth-root sum and compares it with the square/nonsquare evaluation. It tests 3,994 multipliers in 69 odd moduli. The proof in RESULT.md is unrestricted; finite testing does not establish the infinite case.

No independent audit or external certification has been performed.
