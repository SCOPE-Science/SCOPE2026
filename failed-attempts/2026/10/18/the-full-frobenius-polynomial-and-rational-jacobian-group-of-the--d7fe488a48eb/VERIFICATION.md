---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Smoothness and genus three follow from the stated gradient; on Y=0 the sole point is [0:0:1]. Independently computed the exact counts for all six admissible η using F₃[t] mod t²+1, t⁴+2t+2 and t⁶+2t+2, checking irreducibility and summing the multiplicities of z³+z at −η−x⁴. Every η gave (1,109,892). The corresponding power sums are (9,−27,−162); Newton's identities and the genus-three functional equation give (1−3T+9T²)³. There is also a direct all-η check: take b³+b=η, so b⁹=b+η³−η and b^(9³)=b. The substitution Z→Z+bY identifies the equation with the Hermitian quartic over F_{9³}. That Hermitian quartic has 28 F₉-points (nine affine x choices and three z choices per x, plus infinity), so its six F₉ eigenvalues are −3; over F_{9³} the eigenvalues are −27. The F₉ eigenvalues of C therefore lie in {−3,3e^(±iπ/3)}. The unique F₉ point makes the trace 9; conjugacy and degree six force the conjugate pair to have multiplicity three each, with no −3. Frobenius semisimplicity and the faithful Tate-module action give f(π)=0 for f(U)=U²−3U+9. On J(F₉), π=1 so f(1)=7 annihilates the group. Its order is L(1)=343, proving the displayed rank and exponent, without any inference from order alone. The eigenvalues give the cosine count formula. An elliptic class with trace 3 exists (e.g. y²=x³−x+1 over F₉ has seven points), so Tate gives the isogeny statement.

## originality

FAIL

A distinct same-day indexed result 2398b9ff888b states the general exact zeta theorem on this very family. Its specialization gives the entire frozen zeta polynomial and every extension count. It does not state the abstract rational Jacobian group, but its full polynomial gives that group by the direct standard semisimplicity deduction f(π)=0 and f(1)=7, not by cardinality alone. The resulting demonstrated mathematical coverage is separate from priority; the available date does not resolve which finding came first. There is no scientifically distinct nonmechanical remainder in the frozen statement.

## value

FAIL

The one-point class is naturally motivated, and its rational group is a meaningful invariant. Here the zeta computations recover a covered specialization; the asserted rank-three group follows directly from that polynomial's f(1)=7 and order 7³, using standard Frobenius semisimplicity. Re-enumerating the complete fixed-field table and spelling out this mechanical consequence supplies no independently new exact datum meeting the value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
