---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The two symmetric bidegree-(3,3) polynomials are genuinely uniform integral models. Integer elimination shows nested resultants R_A=982087492035469593396623616 and R_B=5838078345771419602547015726577988403024765030400 with gcd 338688=2^8*3^3*7^2, so at least one affine smooth divisor for p outside {2,3,7}. In those three primes the claimed selected Jacobian ideals (f,f_u,f_v) have Groebner basis [1], using B for p=2,3 and A for p=7. The u/v infinity charts have nonzero derivative in v when p!=3, and in t for B when p=3; the corner is absent. Smooth (3,3) ample divisors have genus four, canonical O(1,1), a unique smooth containing quadric. Frobenius factor-swap descends the symmetric divisor to the nonsplit quadric and fixes (0,0); it permutes the two geometric trigonal pencils, while Riemann–Roch on the rational point gives a degree <=4 pencil. Hence every prime-power field admits the asserted genus-four gonality-four example. Source certificates and elimination identities were independently inspected, with actual exact resultant values checked.

## originality

FAIL

A previous PUBLIC theorem dated October 18, 2026, “Four-gonal genus-four curves over every finite field”, proves the exact existential conclusion for every finite field, including characteristic 2, characteristic 3, odd q and rational point, on nonsplit canonical quadrics with explicit smooth cubic sections. The entire prior RESULT.md was read, including three characteristic-specific equations and geometric proof. The new two-polynomial symmetric integral/resultant presentation supplies a different explicit witness/certificate but does NOT establish a new main theorem, parameter domain, moduli invariant or mathematical property absent from the existing result. The general existence claim is decisively covered, even though the precise coefficients of its witness differ. Other October 26 results separately cover odd and even fields. This is a scientific originality rejection, not an access failure.

## value

FAIL

The final finding is the universal existence of pointed genus-four k-gonality-four curves, which was resolved explicitly in the prior October 18 2026 result with the same canonical nonsplit-quadric mechanism. The new alternate two-equation choice and resultant smoothness certificate are reproducible and correct but are not established as an independently motivated optimality, classification, deformation or new geometric invariant. Therefore the substantive final theorem no longer fills an open mathematical gap; correctness and a distinct proof certificate alone do not establish incremental V. No disclaimer or certificate can rescue the unchanged covered claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
