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

The bundled `verify.py` uses exact integer and finite-field arithmetic with the Python standard library. Its run output is in `verification.log`; the last line is `CHECK_OK`.

Checks actually performed: cubic restriction identity in the quotient ring by the quadratic polynomial; Plücker ratio recovering the quadratic generator; exactly twelve generic permutation lines collapsing in pairs to six special lines; six reduced intersection points of the tangent conic and residual cubic; exactly fifteen explicit matching lines, disjoint from the six node lines; and independent enumeration of all \(806\) \(\mathbb F_5\)-rational ambient lines, of which exactly \(21\) lie on the special cubic.

These computations do not by themselves establish the absence of geometric lines over extension fields or the absence of nonreduced local Hilbert structure. The geometric projection classification and the finite-flat rank-and-surjection proof in `RESULT.md` supply those infinite/scheme-theoretic conclusions. No independent audit has been performed.
