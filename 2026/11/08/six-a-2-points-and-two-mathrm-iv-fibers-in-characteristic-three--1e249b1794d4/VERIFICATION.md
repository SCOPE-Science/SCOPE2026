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

# Verification of the characteristic-three degeneration

The proof in `RESULT.md` verifies the theorem for **every** algebraically closed field of characteristic \(3\) and every coefficient pair satisfying its explicit nonempty open hypotheses. The only nonstandard local coordinate change is justified by \(h'_r(x_0)\ne0\); it produces the exact completed local equation \(ts+u^3=0\). The triple-line fiber resolves to the affine \(E_6\) diagram, with central multiplicity \(3\) and three length-two arms with multiplicities \(2,1\). The other six singular residual cubics have explicit ordinary-node quadratic terms.

Run `python3 verify_char3.py`; compare to `verification_output.txt`. This is a standalone Python 3 script without external packages. It checks an exact coefficient witness over \(\mathbb F_9\), including the separability of both singular-point cubics, using arithmetic in \(\mathbb F_3[r]/(r^2+r-1)\). It also enumerates the \(820\) points of \(\mathbb P^3(\mathbb F_9)\) and tests the surface's exact gradient. The actual execution returned `CHAR3_DEGENERATION_EXACT_CHECKS_PASSED`.

The finite enumeration is **not** used as an infinite proof; it provides an explicit nonempty instance. In particular, the six geometric singularities need not be rational over \(\mathbb F_9\); none is \(\mathbb F_9\)-rational for the chosen witness. No claim of independent human review, formal theorem-prover certification, exhaustive literature coverage, or complete classification of all special coefficient choices is made.
