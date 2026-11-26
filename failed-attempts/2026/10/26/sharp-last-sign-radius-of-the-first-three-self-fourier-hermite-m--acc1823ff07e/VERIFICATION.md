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

Independently expanded the physicists' Hermite polynomials in u=2πx²: stripping the Gaussian gives every packet member as P(u)=c+u[A(u−3)+Bp(u)] with p(u)=u³−14u²+105u/2−105/2 and c=f(0)≤0. Coefficient matching gives p+α(u−3)=(u−η)(u−z)² with η=14−2z, α=−3z²+28z−105/2 exactly when W(z)=0. W has critical points 3 and 14/3, both of negative value, and opposite signs at 11/2 and 6, so 2<η<3<z. As a direct certificate including negative origin values, weight P(η)/η by z−3 and P(z)/z by 3−η. The terms in A−Bα cancel and the resulting weighted sum is c[(z−3)/η+(3−η)/z]≤0. Nonnegativity at both contacts forces c=0 and A=Bα. Otherwise negativity at one contact, by continuity, forces a strictly larger last-sign radius. In the equality case eventual nonnegativity and nontriviality force B>0; the exhibited polynomial is negative below η and nonnegative from η on, giving the claimed radius and multiplicities. This also handles degree-degenerate cases. Read the SymPy checker and archived log, including R≈0.6009643878548390; no frozen code was executed.

## originality

FAIL

The distinct indexed 0c4edba5f7b1 record's headline is a different optimization, but its exact root-geometry result on the same affine cubic family directly supplies the radius optimizer and its full exclusion certificate. This is corollary coverage in the inspected evidence, not a claim about historical precedence (the compared entry bears a later catalogue date). The general Fourier literature by itself does not settle the finite packet.

## value

FAIL

An exact small-packet sign-radius benchmark is mathematically motivated, but for this finding the matched collision and parameter direction already force the same benchmark and equality using evaluation at the two given zeros. No separately useful, nonmechanical advance beyond the covered calculation is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
