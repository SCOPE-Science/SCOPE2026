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

# Verification procedure

Execute `python verify.py` (Python 3 standard library only). All calculations use exact rational fractions, not floating-point tolerances. The checker computes factorial moments, recovers the entire residual-component distribution by inversion, and tests positivity, normalization and factorial-moment reconstruction at every size \(3\le n\le13\). For \(3\le n\le6\) it **independently** enumerates every simple-edge state reachable in the uniform-new-edge graph process and compares both the residual distribution and full expected label-recovery count against the formulas. Repeated pair draws are explicitly included in the direct expected-time first-step equation, with geometric waiting until a new edge. The recorded run passed 79 assertions.

Selected exact outputs: at \(n=3\), \(\mathbb E Q_n=5/2\); at \(n=4\), \(\Pr(Y_n=2)=1/5\) and \(\mathbb E Q_n=41/10\); at \(n=5\), \(\Pr(Y_n=1)=11/42\) and \(\mathbb E(Q_n-T_n)=55/126\); at \(n=6\), \(\mathbb E(Q_n-T_n)=3425/8008\).

**Scope:** This is exact finite verification for the displayed test sizes; there is no infinite-size computational certification. The mathematical proof in `RESULT.md` verifies the quantifiers and general formulas for every integer \(n\ge3\). The code does not download external material or require any unpublished data.
