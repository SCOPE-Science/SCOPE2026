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

# Reproducibility

Run `python3 verify.py` with Python 3 and compare stdout exactly with `verification_output.txt`. The script uses standard-library exact integer and rational arithmetic; the trigonometric enclosures are proved from alternating arctangent series and factorial Taylor remainders. It enumerates independent faces and verifies the integral chain, separation and regular-ray degree. In particular the unique intersection with the chosen positive target ray has algebraic contribution \(-1\).

The program does not itself certify the classical nonequivariant homotopy type \(\operatorname{Ind}(C_{11})\simeq S^3\), nor the topological Whitehead and free-quotient descent arguments. Those are established separately in RESULT.md. No independent mathematical audit was performed.
