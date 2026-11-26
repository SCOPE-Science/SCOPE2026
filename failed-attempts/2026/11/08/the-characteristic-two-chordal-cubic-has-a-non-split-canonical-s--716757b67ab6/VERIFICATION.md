---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In characteristic two the determinant has gradient (q0,0,q2,0,q4) and its equation is in the gradient ideal by Euler. The charts x0=1 and x4=1 cover the support, and elimination gives k[t,u]/(u^2) and k[s,v]/(v^2). After dehomogenizing on the overlap, s=t^(-1)+t^(-4)u and v=t^(-6)u, so the square-zero ideal is O_P1(-6). A retraction would force t^2+g(t^(-1))=t^4 f(t) for polynomials f and g, which is impossible at the coefficient of t^2. Codimension three makes the three quadrics a regular sequence; adjunction, the nilradical exact sequence and the Koszul resolution give O_J(1)=omega_J, Hilbert polynomial 8n-4, and h^0(omega_J)=5. The secant interpretation is characteristic-independent here: the two supporting geometric sequences on a generic secant satisfy a common order-two recurrence. Conversely the leading 2-by-2 minor on the determinant hypersurface generically gives such a recurrence with two distinct roots. This verifies the stated model without a characteristic-zero transfer. The frozen verification/verify.py and verification/output.txt are supporting evidence only; the check above is by algebra and was not a run of the uploaded verifier.

## originality

FAIL

A distinct earlier Resultary record states and proves the same scheme-theoretic result for this characteristic-two Hankel cubic. The match includes the nonsplitting, not just the reduced support or the genus. The Hilbert polynomial and complete canonical linear system follow directly from the same complete-intersection description. No distinct surviving theorem was identified in the frozen claim.

## value

PASS

As mathematics, the exact non-split scheme structure is a useful characteristic-two boundary case for the natural secant cubic: it distinguishes the intrinsic Jacobian scheme from the reduced rational normal curve and from a split ribbon with the same local equations. That intrinsic value does not make this duplicate contribution original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
