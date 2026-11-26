---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The strict coefficient bounds control deviations of each edge factor from +1 or −1 over the entire edge, giving a counterclockwise boundary with no intervening equilibria. The corner rates follow from the diagonal entries −2xP and −2yQ at x,y=±1, where P,Q are the printed quadratic factors. Multiplying the four stable-to-unstable rates gives (1). Integrating the logarithmic rates in shrinking saddle boxes gives each saddle passage exponent; regular transitions from fixed sections to smaller boxes and along open edges have nonzero finite derivatives, hence exponent 1. Composition gives the logarithmic exponent, not an exact monomial return map. On the slice the denominator stays positive and the sign is the sign of 4h²(1+ε)²−8ε(1+ε²). The finding's iff phrasing is valid only off equality, as explicitly scoped by the repeated exclusion of ρ=1; it cannot establish nonattraction or nonrepulsion at equality. The focus has eigenvalues −ε±i and the formal second root is strictly below x=−1. The attracting collar excludes the focus basin closure from the boundary, so its interior basin boundary is a nonempty compact invariant set with no rest point. Poincaré–Bendixson gives an interior periodic orbit, without claiming uniqueness, hyperbolicity or stability. The witness gives ρ=32019867/26185967 and second root −10001/2525; no witness was inferred from the finite mesh, and the uploaded checker was inspected, not executed.

## originality

FAIL

Bastos–Buzzi–Santana's earlier Eq. (31) is exactly the four-corner product in a broader polynomial invariant-square class, and its preceding Cherkas criterion already gives the strict dynamical interpretation. An affine square change and direct corner substitution recover (1) for the frozen family, then direct substitution on the chosen slice gives the claimed h threshold. The logarithmic exponent is the classical product of saddle passage exponents. The remaining existence assertion is the standard planar trapping argument once the one focus and the stable square have been checked; no separately original theorem survives the exact broader comparison.

## value

FAIL

An explicit interior-cycle region would be useful if it required new analysis of this family. Here the exact product is already available for arbitrary polynomial corner factors; the proposed chamber and two-parameter slice just make its substitution simple, and the existence proof supplies a standard planar consequence of the resulting trappings. The package proves neither the neutral return behavior nor the type, count or other genuinely new precise feature of the interior orbit. A notation or scope correction would not produce a separately valuable surviving invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
